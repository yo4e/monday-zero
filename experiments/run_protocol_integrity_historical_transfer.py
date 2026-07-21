"""Evaluate the four frozen Study 003 historical traces with frozen validators."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from templex_zero.protocol_integrity.oracle import inspect_trace
from templex_zero.protocol_integrity.validator import validate_trace

EXPECTED_ARTIFACT_BLOB = "840a7779a1cee3ba4f3f88e62342269b804c2719"
FROZEN_PRIMARY_BLOB = "71080f1051acc015e74b42de19d56ce8782b9f25"
FROZEN_ORACLE_BLOB = "74159c7a7502975b1bcd376510d5dad0283e03cd"


def git_blob_sha(payload: bytes) -> str:
    return hashlib.sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def run(artifact_path: Path) -> dict[str, Any]:
    raw = artifact_path.read_bytes()
    if git_blob_sha(raw) != EXPECTED_ARTIFACT_BLOB:
        raise RuntimeError("historical artifact blob mismatch")
    artifact = json.loads(raw)
    rows: list[dict[str, Any]] = []
    for trace in artifact["traces"]:
        expected = trace["expected"]
        primary = validate_trace(trace["contract"], trace["events"]).to_dict()
        oracle = inspect_trace(trace["contract"], trace["events"]).to_dict()
        rows.append(
            {
                "trace_id": trace["trace_id"],
                "expected": expected,
                "primary": primary,
                "oracle": oracle,
                "expected_match": primary == expected and oracle == expected,
                "primary_oracle_agreement": primary == oracle,
                "source_count": len(trace["sources"]),
            }
        )
    report = {
        "schema_version": 1,
        "gate": "study-003-historical-transfer-v1",
        "historical_artifact_blob": EXPECTED_ARTIFACT_BLOB,
        "historical_canonical_sha256": artifact["canonical_sha256"],
        "frozen_instruments": {"primary": FROZEN_PRIMARY_BLOB, "oracle": FROZEN_ORACLE_BLOB},
        "trace_count": len(rows),
        "event_count": artifact["event_count"],
        "expected_verdict_matches": sum(row["expected_match"] for row in rows),
        "first_violation_matches": sum(
            row["expected"]["verdict"] == "valid"
            or (
                row["primary"].get("first_violation_index") == row["expected"].get("first_violation_index")
                and row["oracle"].get("first_violation_index") == row["expected"].get("first_violation_index")
            )
            for row in rows
        ),
        "primary_oracle_agreement_count": sum(row["primary_oracle_agreement"] for row in rows),
        "passed": all(row["expected_match"] and row["primary_oracle_agreement"] for row in rows),
        "rows": rows,
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run(args.artifact)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(canonical_bytes(report))
    print(json.dumps({key: report[key] for key in ("passed", "trace_count", "expected_verdict_matches", "first_violation_matches", "primary_oracle_agreement_count")}, sort_keys=True))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
