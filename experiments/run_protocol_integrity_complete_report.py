"""Build the deterministic final Study 003 validation report.

The runner combines the already frozen synthetic-gate and historical-transfer
results. It does not alter validator outcomes or historical expectations.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

SYNTHETIC_RESULT_BLOB = "53c801c18cd3b5a7cf696a146b0302d4659265e3"
SYNTHETIC_RESULT_SHA256 = "46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de"
HISTORICAL_ARTIFACT_BLOB = "840a7779a1cee3ba4f3f88e62342269b804c2719"
HISTORICAL_ARTIFACT_SHA256 = "8cdaec94de2e8a7aff3158924db5e570f4af3008bcb33f18602f584b29b41053"
HISTORICAL_RESULT_BLOB = "161b65efb09d2d98cba0584574aeeaf0dfa5ec66"
HISTORICAL_RESULT_SHA256 = "c59c621a1efad82ba95ca6eb92465a062b9b412b4fd8f4a05d69dccfcdcdac4a"
PRIMARY_BLOB = "71080f1051acc015e74b42de19d56ce8782b9f25"
ORACLE_BLOB = "74159c7a7502975b1bcd376510d5dad0283e03cd"
BASELINE_BLOB = "7af3b9e1db56a90e08b93690a14d90ee541b9d18"
CORPUS_SHA256 = "b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84"

EXPECTED_HISTORICAL = {
    "H1-SPAN-FORMAL-VALID": {"verdict": "valid"},
    "H2-EXACT-SUBSTUDY-VALID": {"verdict": "valid"},
    "H3-STUDY002-SHALLOW-CONTAMINATED": {
        "verdict": "invalid",
        "first_violation_index": 5,
        "dependency_class": "D1",
        "reason_code": "artifact-not-frozen",
    },
    "H4-EXACT-PROJECTION-CORRECTION-VALID": {"verdict": "valid"},
}
NAMED_BEYOND_ORDERING = ["P2-I", "P3-I", "P5-I", "P6-I"]
EXPECTED_SYNTHETIC_IDS = (
    [f"P{i}-{suffix}" for i in range(1, 7) for suffix in ("V", "I")]
    + [item for i in range(1, 5) for item in ([f"C{i}-V"] + [f"C{i}-M{j}" for j in range(1, 6)])]
)


def compact_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def build_complete_report(synthetic: dict[str, Any], historical: dict[str, Any]) -> dict[str, Any]:
    metrics = synthetic["metrics"]
    failures = synthetic["failures"]
    rows = synthetic["rows"]
    historical_rows = historical["rows"]

    _require(synthetic.get("passed") is True, "synthetic gate did not pass")
    _require(metrics.get("trace_count") == 36, "synthetic trace count mismatch")
    _require(metrics.get("expected_valid") == 10, "synthetic valid count mismatch")
    _require(metrics.get("expected_invalid") == 26, "synthetic invalid count mismatch")
    _require(metrics.get("false_accept_count") == 0, "synthetic false accept")
    _require(metrics.get("false_reject_count") == 0, "synthetic false reject")
    _require(metrics.get("first_violation_accuracy") == 1.0, "first-index mismatch")
    _require(metrics.get("violation_class_accuracy") == 1.0, "class mismatch")
    _require(metrics.get("reason_code_accuracy") == 1.0, "reason mismatch")
    _require(metrics.get("primary_oracle_agreement") == 1.0, "synthetic oracle mismatch")
    _require(metrics.get("mutation_count") == 20, "mutation count mismatch")
    _require(metrics.get("mutants_rejected") == 20, "mutant rejection mismatch")
    _require(metrics.get("special_case_finding_count") == 0, "special-case branch found")
    _require(all(not value for value in failures.values()), "synthetic failure list non-empty")
    _require(len(rows) == 36, "synthetic result rows missing")
    synthetic_ids = [row["trace_id"] for row in rows]
    _require(synthetic_ids == EXPECTED_SYNTHETIC_IDS, "synthetic trace order or set mismatch")
    _require(len(set(synthetic_ids)) == 36, "duplicate synthetic trace id")
    _require(sum(row.get("expected", {}).get("verdict") == "valid" for row in rows) == 10, "row valid count mismatch")
    _require(sum(row.get("expected", {}).get("verdict") == "invalid" for row in rows) == 26, "row invalid count mismatch")
    _require(sum(row.get("category") == "composite-mutant" for row in rows) == 20, "row mutation count mismatch")
    for row in rows:
        _require(row.get("primary") == row.get("expected"), f"synthetic primary mismatch: {row.get('trace_id')}")
        _require(row.get("oracle") == row.get("expected"), f"synthetic oracle mismatch: {row.get('trace_id')}")
    _require(
        metrics.get("named_baseline_false_accepts") == NAMED_BEYOND_ORDERING,
        "named beyond-ordering cases mismatch",
    )

    _require(historical.get("passed") is True, "historical gate did not pass")
    _require(historical.get("trace_count") == 4, "historical trace count mismatch")
    _require(historical.get("event_count") == 44, "historical event count mismatch")
    _require(historical.get("expected_verdict_matches") == 4, "historical verdict mismatch")
    _require(historical.get("first_violation_matches") == 4, "historical first-index mismatch")
    _require(historical.get("primary_oracle_agreement_count") == 4, "historical oracle mismatch")
    _require(len(historical_rows) == 4, "historical result rows missing")
    historical_ids = [row["trace_id"] for row in historical_rows]
    _require(set(historical_ids) == set(EXPECTED_HISTORICAL), "historical trace set mismatch")
    for row in historical_rows:
        trace_id = row["trace_id"]
        _require(row["expected"] == EXPECTED_HISTORICAL[trace_id], f"historical expectation drift: {trace_id}")
        _require(row.get("expected_match") is True, f"historical expected mismatch: {trace_id}")
        _require(row.get("primary_oracle_agreement") is True, f"historical oracle mismatch: {trace_id}")

    hypotheses = {
        "H1_synthetic_correctness": {
            "disposition": "supported",
            "basis": "36/36 synthetic traces matched with zero false accepts and false rejects and full primary/oracle agreement",
        },
        "H2_mutation_detection": {
            "disposition": "supported",
            "basis": "20/20 frozen mutations were rejected at their precommitted first violations",
        },
        "H3_historical_transfer": {
            "disposition": "supported",
            "basis": "4/4 precommitted repository histories matched without instrument changes or new event kinds",
        },
        "H4_beyond_ordering": {
            "disposition": "supported",
            "basis": "the full validators rejected all four named stateful cases accepted by the order-only baseline",
        },
    }

    report: dict[str, Any] = {
        "schema_version": 1,
        "report": "study-003-complete-validation-v1",
        "source_artifacts": {
            "synthetic_corpus_sha256": CORPUS_SHA256,
            "synthetic_result": {
                "git_blob": SYNTHETIC_RESULT_BLOB,
                "canonical_sha256": SYNTHETIC_RESULT_SHA256,
            },
            "historical_traces": {
                "git_blob": HISTORICAL_ARTIFACT_BLOB,
                "canonical_sha256": HISTORICAL_ARTIFACT_SHA256,
            },
            "historical_result": {
                "git_blob": HISTORICAL_RESULT_BLOB,
                "canonical_sha256": HISTORICAL_RESULT_SHA256,
            },
            "instruments": {
                "primary_git_blob": PRIMARY_BLOB,
                "oracle_git_blob": ORACLE_BLOB,
                "baseline_git_blob": BASELINE_BLOB,
            },
        },
        "coverage": {
            "synthetic_traces": 36,
            "historical_traces": 4,
            "total_traces": 40,
            "synthetic_events": 528,
            "historical_events": 44,
            "total_events": 572,
            "synthetic_trace_ids": synthetic_ids,
            "historical_trace_ids": historical_ids,
        },
        "synthetic_metrics": metrics,
        "historical_metrics": {
            "expected_verdict_matches": historical["expected_verdict_matches"],
            "first_violation_matches": historical["first_violation_matches"],
            "primary_oracle_agreement_count": historical["primary_oracle_agreement_count"],
        },
        "historical_dispositions": [
            {
                "trace_id": row["trace_id"],
                "expected": row["expected"],
                "primary": row["primary"],
                "oracle": row["oracle"],
            }
            for row in historical_rows
        ],
        "hypotheses": hypotheses,
        "methodological_disposition": "success_with_bounded_claims",
        "claim_limits": [
            "valid trace classification does not establish truth, value, safety, novelty, autonomy, or scientific quality",
            "the historical transfer set contains only four preselected repository episodes",
            "the synthetic corpus is specification-derived and therefore not an independent natural distribution",
            "the validators enforce only the declared fourteen-event vocabulary and six dependency classes",
        ],
        "passed": True,
    }
    report["deterministic_sha256"] = sha256(compact_bytes(report)).hexdigest()
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("synthetic_result", type=Path)
    parser.add_argument("historical_result", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    synthetic = json.loads(args.synthetic_result.read_text(encoding="utf-8"))
    historical = json.loads(args.historical_result.read_text(encoding="utf-8"))
    report = build_complete_report(synthetic, historical)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(compact_bytes(report))
    print(report["deterministic_sha256"])


if __name__ == "__main__":
    main()
