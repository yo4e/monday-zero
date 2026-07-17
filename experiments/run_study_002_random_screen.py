"""Run the frozen Study 002 random screen.

This experiment is committed before random play. It loads all eighteen frozen
candidates in manifest order and runs exactly 2,000 independent uniformly random
legal-action games per candidate. It does not import exact results or shallow
search code.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import platform
import random
from statistics import mean, median
from time import perf_counter
from typing import Any

from templex_zero.exact_first.manifest import manifest_object, selected_candidates
from templex_zero.exact_first.schema import (
    apply_action,
    coordinate,
    goal_satisfied,
    initial_state,
    legal_actions,
    terminal_result,
)

EXPECTED_MANIFEST_SHA256 = (
    "cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee"
)
GAMES_PER_CANDIDATE = 2_000
SEED_NAMESPACE = "study002-random-v1"


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def game_seed(manifest_index: int, game_index: int) -> int:
    payload = (
        f"{SEED_NAMESPACE}|{EXPECTED_MANIFEST_SHA256}|"
        f"{manifest_index}|{game_index}"
    )
    return int.from_bytes(sha256(payload.encode("utf-8")).digest()[:8], "big")


def play_random_game(spec: Any, seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    state = initial_state(spec)
    opening: str | None = None
    branching: list[int] = []

    while terminal_result(spec, state) == "ongoing":
        actions = legal_actions(spec, state)
        if not actions:
            raise RuntimeError("ongoing state exposed no legal actions")
        branching.append(len(actions))
        action = actions[rng.randrange(len(actions))]
        if opening is None:
            opening = coordinate(spec, action)
        state = apply_action(spec, state, action)

    terminal = terminal_result(spec, state)
    if terminal.startswith("win:"):
        winner = int(terminal.split(":", 1)[1])
        reason = "goal" if goal_satisfied(spec, state, winner) else "no_legal_action"
    elif terminal == "draw":
        winner = None
        reason = "draw_no_legal_action"
    else:
        raise RuntimeError(f"unexpected terminal result: {terminal}")

    return {
        "winner": winner,
        "terminal_reason": reason,
        "plies": state.ply,
        "opening": opening,
        "branching": branching,
    }


def screen_candidate(candidate: Any, games: int = GAMES_PER_CANDIDATE) -> dict[str, Any]:
    if games <= 0:
        raise ValueError("games must be positive")

    wins: Counter[str] = Counter()
    reasons: Counter[str] = Counter()
    openings: Counter[str] = Counter()
    ply_counts: Counter[int] = Counter()
    branch_counts: Counter[int] = Counter()
    plies: list[int] = []
    total_decision_points = 0
    total_legal_actions = 0
    maximum_branching = 0

    for game_index in range(games):
        result = play_random_game(
            candidate.spec,
            game_seed(candidate.manifest_index, game_index),
        )
        winner = result["winner"]
        wins["draw" if winner is None else str(winner)] += 1
        reasons[result["terminal_reason"]] += 1
        if result["opening"] is not None:
            openings[result["opening"]] += 1
        plies.append(result["plies"])
        ply_counts[result["plies"]] += 1
        for value in result["branching"]:
            branch_counts[value] += 1
            total_decision_points += 1
            total_legal_actions += value
            maximum_branching = max(maximum_branching, value)

    decisive = wins["0"] + wins["1"]
    first_decisive_rate = wins["0"] / decisive if decisive else None
    return {
        "manifest_index": candidate.manifest_index,
        "id": candidate.candidate_id,
        "board_size": candidate.spec.board_size,
        "family": candidate.spec.family.value,
        "games": games,
        "results": {
            "first_participant": wins["0"],
            "second_participant": wins["1"],
            "draw": wins["draw"],
            "first_participant_decisive_rate": first_decisive_rate,
        },
        "terminal_reasons": dict(sorted(reasons.items())),
        "plies": {
            "minimum": min(plies),
            "maximum": max(plies),
            "mean": round(mean(plies), 6),
            "median": median(plies),
            "histogram": {str(key): ply_counts[key] for key in sorted(ply_counts)},
        },
        "openings": dict(sorted(openings.items())),
        "branching": {
            "decision_points": total_decision_points,
            "mean_legal_actions": round(total_legal_actions / total_decision_points, 6),
            "maximum_legal_actions": maximum_branching,
            "histogram": {str(key): branch_counts[key] for key in sorted(branch_counts)},
        },
    }


def deterministic_projection(report: dict[str, Any]) -> dict[str, Any]:
    return {
        "experiment_version": report["experiment_version"],
        "code_version": report["code_version"],
        "manifest_sha256": report["manifest_sha256"],
        "seed_formula": report["seed_formula"],
        "games_per_candidate": report["games_per_candidate"],
        "candidates": report["candidates"],
        "summary": {
            key: value
            for key, value in report["summary"].items()
            if key != "elapsed_seconds"
        },
    }


def run(code_version: str) -> dict[str, Any]:
    manifest = manifest_object()
    if manifest["entries_sha256"] != EXPECTED_MANIFEST_SHA256:
        raise RuntimeError("frozen manifest hash mismatch")
    candidates = selected_candidates()
    if len(candidates) != 18:
        raise RuntimeError(f"expected 18 frozen candidates, got {len(candidates)}")

    started = perf_counter()
    rows = [screen_candidate(candidate) for candidate in candidates]
    summary = {
        "candidate_count": len(rows),
        "game_count": sum(row["games"] for row in rows),
        "first_participant_wins": sum(
            row["results"]["first_participant"] for row in rows
        ),
        "second_participant_wins": sum(
            row["results"]["second_participant"] for row in rows
        ),
        "draws": sum(row["results"]["draw"] for row in rows),
        "elapsed_seconds": perf_counter() - started,
    }
    report: dict[str, Any] = {
        "experiment_version": 1,
        "code_version": code_version,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "seed_formula": (
            "uint64_be(sha256('study002-random-v1|manifest_sha256|"
            "manifest_index|game_index')[:8])"
        ),
        "games_per_candidate": GAMES_PER_CANDIDATE,
        "candidates": rows,
        "summary": summary,
    }
    report["deterministic_sha256"] = sha256(
        compact_json(deterministic_projection(report)).encode("utf-8")
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
