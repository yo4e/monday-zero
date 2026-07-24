"""Study 005 Cycle 2 fixture gate and complete transition manifest builder."""

from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
from typing import Any

from templex_zero.tzif_reader import canonical_transition_records, read_tzif

START = 0
END = 4_102_444_800  # 2100-01-01T00:00:00Z


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("ascii")


def run_fixture_gate(tzdir: Path, fixtures_path: Path) -> dict[str, Any]:
    frozen_bytes = fixtures_path.read_bytes()
    frozen = json.loads(frozen_bytes)
    results: list[dict[str, Any]] = []

    for fixture in frozen["fixtures"]:
        path = tzdir / fixture["zone"]
        file_bytes = path.read_bytes()
        parsed = read_tzif(path)
        checks: list[dict[str, Any]] = []

        def check(name: str, observed: Any, expected: Any) -> None:
            checks.append(
                {
                    "expected": expected,
                    "name": name,
                    "observed": observed,
                    "passed": observed == expected,
                }
            )

        check("file_bytes", len(file_bytes), fixture["tzif_file_bytes"])
        check("file_sha256", _sha256(file_bytes), fixture["tzif_file_sha256"])
        check("version", parsed.version, fixture["tzif_version_byte"])

        epoch = fixture.get("transition_epoch")
        if epoch is None:
            retained = [t.timestamp for t in parsed.transitions if START <= t.timestamp < END]
            check("retained_transition_count", len(retained), 0)
            check("footer", parsed.footer, fixture["footer"])
        else:
            pre, post = parsed.transition_at(epoch)
            check(
                "pre",
                {"abbr": pre.abbreviation, "gmtoff": pre.utoff, "isdst": int(pre.isdst)},
                fixture["pre"],
            )
            check(
                "post",
                {"abbr": post.abbreviation, "gmtoff": post.utoff, "isdst": int(post.isdst)},
                fixture["post"],
            )
            check("delta", post.utoff - pre.utoff, fixture["delta"])

        results.append(
            {
                "checks": checks,
                "fixture_id": fixture["id"],
                "passed": all(item["passed"] for item in checks),
                "zone": fixture["zone"],
            }
        )

    for zone, expected_footer in sorted(frozen["posix_footers"].items()):
        parsed = read_tzif(tzdir / zone)
        results.append(
            {
                "checks": [
                    {
                        "expected": expected_footer,
                        "name": "footer",
                        "observed": parsed.footer,
                        "passed": parsed.footer == expected_footer,
                    }
                ],
                "fixture_id": f"FOOTER:{zone}",
                "passed": parsed.footer == expected_footer,
                "zone": zone,
            }
        )

    result = {
        "fixture_expectations_bytes": len(frozen_bytes),
        "fixture_expectations_sha256": _sha256(frozen_bytes),
        "passed": all(item["passed"] for item in results),
        "result_count": len(results),
        "results": results,
        "schema": "templex-zero.study005.fixture-gate-result.v1",
    }
    return result


def build_manifest(tzdir: Path, zones_path: Path) -> tuple[bytes, dict[str, Any]]:
    zones = zones_path.read_text(encoding="utf-8").splitlines()
    rows: list[list[Any]] = []
    class_counts: Counter[str] = Counter()
    delta_counts: Counter[int] = Counter()
    total_transitions = 0

    for zone in zones:
        path = tzdir / zone
        file_bytes = path.read_bytes()
        parsed = read_tzif(path)
        rich_transitions = list(canonical_transition_records(zone, parsed, START, END))
        for item in rich_transitions:
            class_counts[str(item["class"])] += 1
            delta_counts[int(item["delta"])] += 1
        total_transitions += len(rich_transitions)

        local_types = [
            [
                item.utoff,
                int(item.isdst),
                item.abbreviation,
                item.abbreviation_index,
                None if item.is_standard is None else int(item.is_standard),
                None if item.is_ut is None else int(item.is_ut),
            ]
            for item in parsed.local_time_types
        ]
        retained_transitions = [
            [item.timestamp, item.type_index]
            for item in parsed.transitions
            if START <= item.timestamp < END
        ]
        rows.append(
            [
                zone,
                len(file_bytes),
                _sha256(file_bytes),
                parsed.version,
                parsed.footer,
                local_types,
                None if not parsed.transitions else parsed.transitions[-1].timestamp,
                retained_transitions,
            ]
        )

    manifest = {
        "columns": [
            "zone",
            "file_bytes",
            "file_sha256",
            "tzif_version",
            "footer",
            "local_time_types",
            "final_explicit_transition",
            "retained_transitions",
        ],
        "date_interval": [START, END],
        "local_time_type_columns": [
            "utoff",
            "isdst",
            "abbreviation",
            "abbreviation_index",
            "is_standard",
            "is_ut",
        ],
        "pre_first_transition_type_index": 0,
        "schema": "templex-zero.study005.transition-manifest-compact.v1",
        "source_release": "2026c",
        "transition_columns": ["timestamp", "type_index"],
        "zones": rows,
    }
    raw = _canonical_json(manifest)
    summary = {
        "class_counts": dict(sorted(class_counts.items())),
        "delta_counts": {str(key): delta_counts[key] for key in sorted(delta_counts)},
        "manifest_bytes": len(raw),
        "manifest_sha256": _sha256(raw),
        "schema": "templex-zero.study005.transition-manifest-summary.v1",
        "serialization": "templex-zero.study005.transition-manifest-compact.v1",
        "transition_count": total_transitions,
        "zone_count": len(rows),
    }
    return raw, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tzdir", type=Path, required=True)
    parser.add_argument("--fixtures", type=Path, required=True)
    parser.add_argument("--zones", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    gate = run_fixture_gate(args.tzdir, args.fixtures)
    gate_bytes = _canonical_json(gate)
    (args.output_dir / "fixture_gate_result_v1.json").write_bytes(gate_bytes)
    if not gate["passed"]:
        raise SystemExit("fixture gate failed")

    manifest, summary = build_manifest(args.tzdir, args.zones)
    (args.output_dir / "transition_manifest_compact_v1.json.gz").write_bytes(
        gzip.compress(manifest, compresslevel=9, mtime=0)
    )
    (args.output_dir / "transition_manifest_summary_v1.json").write_bytes(
        _canonical_json(summary)
    )


if __name__ == "__main__":
    main()
