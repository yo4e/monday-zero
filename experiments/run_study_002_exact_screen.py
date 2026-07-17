"""Run the frozen Study 002 exact-candidate screen.

This script must be committed before candidate outcomes are inspected. It loads the
frozen manifest in manifest order, uses the validated no-reduction solver, enforces
all per-candidate and study-wide caps, and separates measured timing from the
fields required to reproduce exactly.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import platform
from time import perf_counter
from typing import Any

from templex_zero.exact_first.manifest import manifest_object, selected_candidates
from templex_zero.exact_first.schema import coordinate
from templex_zero.exact_first.solver import solve_exact

EXPECTED_MANIFEST_SHA256 = (
    "cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee"
)
PER_CANDIDATE_STATE_CAP = 2_000_000
PER_CANDIDATE_TIME_LIMIT_SECONDS = 30.0
TOTAL_STATE_CAP = 25_000_000
MINIMUM_SOLVED = 12


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def deterministic_projection(report: dict[str, Any]) -> dict[str, Any]:
    """Remove fields that may legitimately vary between identical runs."""

    return {
        "experiment_version": report["experiment_version"],
        "code_version": report["code_version"],
        "manifest_sha256": report["manifest_sha256"],
        "caps": report["caps"],
        "candidates": [
            {
                key: value
                for key, value in candidate.items()
                if key not in {"elapsed_seconds"}
            }
            for candidate in report["candidates"]
        ],
        "summary": {
            key: value
            for key, value in report["summary"].items()
            if key not in {"elapsed_seconds_total"}
        },
    }


def value_record(value: Any) -> dict[str, Any]:
    return {"outcome": value.outcome, "distance": value.distance}


def run(code_version: str) -> dict[str, Any]:
    manifest = manifest_object()
    actual_manifest_sha = manifest["entries_sha256"]
    if actual_manifest_sha != EXPECTED_MANIFEST_SHA256:
        raise RuntimeError(
            "frozen manifest hash mismatch: "
            f"expected {EXPECTED_MANIFEST_SHA256}, got {actual_manifest_sha}"
        )

    candidates = selected_candidates()
    if len(candidates) != 18:
        raise RuntimeError(f"expected 18 frozen candidates, got {len(candidates)}")

    rows: list[dict[str, Any]] = []
    total_expanded = 0
    run_started = perf_counter()

    for candidate in candidates:
        remaining_total = TOTAL_STATE_CAP - total_expanded
        if remaining_total <= 0:
            rows.append(
                {
                    "manifest_index": candidate.manifest_index,
                    "id": candidate.candidate_id,
                    "board_size": candidate.spec.board_size,
                    "family": candidate.spec.family.value,
                    "status": "unsolved",
                    "root": None,
                    "opening_values": [],
                    "opening_counts": {"win": 0, "draw": 0, "loss": 0},
                    "non_losing_opening_proportion": None,
                    "expanded_states": 0,
                    "effective_state_cap": 0,
                    "cap_reached": True,
                    "cap_reason": "total_state_before_candidate",
                    "elapsed_seconds": 0.0,
                }
            )
            continue

        effective_state_cap = min(PER_CANDIDATE_STATE_CAP, remaining_total)
        started = perf_counter()
        result = solve_exact(
            candidate.spec,
            state_cap=effective_state_cap,
            time_limit_seconds=PER_CANDIDATE_TIME_LIMIT_SECONDS,
        )
        elapsed = perf_counter() - started
        total_expanded += result.expanded_states

        if result.cap_reached:
            cap_reason = result.cap_reason
            if (
                result.cap_reason == "state"
                and effective_state_cap < PER_CANDIDATE_STATE_CAP
            ):
                cap_reason = "total_state_during_candidate"
            rows.append(
                {
                    "manifest_index": candidate.manifest_index,
                    "id": candidate.candidate_id,
                    "board_size": candidate.spec.board_size,
                    "family": candidate.spec.family.value,
                    "status": "unsolved",
                    "root": None,
                    "opening_values": [],
                    "opening_counts": {"win": 0, "draw": 0, "loss": 0},
                    "non_losing_opening_proportion": None,
                    "expanded_states": result.expanded_states,
                    "effective_state_cap": effective_state_cap,
                    "cap_reached": True,
                    "cap_reason": cap_reason,
                    "elapsed_seconds": elapsed,
                }
            )
            continue

        opening_values = [
            {
                "action": item.action,
                "coordinate": coordinate(candidate.spec, item.action),
                **value_record(item.value),
            }
            for item in result.opening_values
        ]
        counts = Counter(item["outcome"] for item in opening_values)
        opening_counts = {
            outcome: counts.get(outcome, 0) for outcome in ("win", "draw", "loss")
        }
        non_losing = opening_counts["win"] + opening_counts["draw"]
        non_losing_proportion = (
            non_losing / len(opening_values) if opening_values else None
        )
        rows.append(
            {
                "manifest_index": candidate.manifest_index,
                "id": candidate.candidate_id,
                "board_size": candidate.spec.board_size,
                "family": candidate.spec.family.value,
                "status": "solved",
                "root": value_record(result.root),
                "opening_values": opening_values,
                "opening_counts": opening_counts,
                "non_losing_opening_proportion": non_losing_proportion,
                "expanded_states": result.expanded_states,
                "effective_state_cap": effective_state_cap,
                "cap_reached": False,
                "cap_reason": None,
                "elapsed_seconds": elapsed,
            }
        )

    solved = [row for row in rows if row["status"] == "solved"]
    short_solved = [
        row
        for row in solved
        if row["root"] is not None and row["root"]["distance"] <= 2
    ]
    solved_count = len(solved)
    continuation_threshold_met = solved_count >= MINIMUM_SOLVED
    degenerate_majority = bool(solved) and len(short_solved) > solved_count / 2
    failure_reasons = []
    if not continuation_threshold_met:
        failure_reasons.append("fewer_than_12_exact_solutions")
    if degenerate_majority:
        failure_reasons.append("majority_of_solved_candidates_end_by_ply_2")

    report: dict[str, Any] = {
        "experiment_version": 1,
        "code_version": code_version,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "manifest_sha256": actual_manifest_sha,
        "caps": {
            "per_candidate_states": PER_CANDIDATE_STATE_CAP,
            "per_candidate_seconds": PER_CANDIDATE_TIME_LIMIT_SECONDS,
            "total_states": TOTAL_STATE_CAP,
            "minimum_solved": MINIMUM_SOLVED,
        },
        "candidates": rows,
        "summary": {
            "candidate_count": len(rows),
            "solved_count": solved_count,
            "unsolved_count": len(rows) - solved_count,
            "total_expanded_states": total_expanded,
            "elapsed_seconds_total": perf_counter() - run_started,
            "root_outcomes": dict(
                sorted(Counter(row["root"]["outcome"] for row in solved).items())
            ),
            "solved_by_board_size": dict(
                sorted(Counter(str(row["board_size"]) for row in solved).items())
            ),
            "solved_by_family": dict(
                sorted(Counter(row["family"] for row in solved).items())
            ),
            "solved_distance_le_2": len(short_solved),
            "continuation_threshold_met": continuation_threshold_met,
            "degenerate_majority": degenerate_majority,
            "failure_reasons": failure_reasons,
        },
    }
    projection = deterministic_projection(report)
    report["deterministic_sha256"] = sha256(
        compact_json(projection).encode("utf-8")
    ).hexdigest()
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code-version", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    report = run(args.code_version)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report["summary"], ensure_ascii=False, sort_keys=True))
    print(report["deterministic_sha256"])


if __name__ == "__main__":
    main()
