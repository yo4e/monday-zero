import importlib.util
from pathlib import Path

MODULE = Path(__file__).parents[1] / "experiments" / "run_protocol_integrity_complete_report.py"
spec = importlib.util.spec_from_file_location("complete_report", MODULE)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def synthetic_fixture():
    rows = []
    for trace_id in module.EXPECTED_SYNTHETIC_IDS:
        is_invalid = trace_id.endswith("-I") or "-M" in trace_id
        expected = {"verdict": "invalid" if is_invalid else "valid"}
        category = "composite-mutant" if "-M" in trace_id else "fixture"
        rows.append({
            "trace_id": trace_id,
            "category": category,
            "expected": expected,
            "primary": expected,
            "oracle": expected,
        })
    return {
        "passed": True,
        "metrics": {
            "trace_count": 36,
            "expected_valid": 10,
            "expected_invalid": 26,
            "false_accept_count": 0,
            "false_reject_count": 0,
            "first_violation_accuracy": 1.0,
            "violation_class_accuracy": 1.0,
            "reason_code_accuracy": 1.0,
            "primary_oracle_agreement": 1.0,
            "mutation_count": 20,
            "mutants_rejected": 20,
            "special_case_finding_count": 0,
            "baseline_false_accept_count": 12,
            "named_baseline_false_accepts": ["P2-I", "P3-I", "P5-I", "P6-I"],
        },
        "failures": {
            "false_accepts": [], "false_rejects": [], "first_violation_errors": [],
            "violation_class_errors": [], "reason_code_errors": [],
            "primary_oracle_disagreements": [], "special_case_findings": [],
        },
        "rows": rows,
    }


def historical_fixture():
    rows = []
    for trace_id, expected in module.EXPECTED_HISTORICAL.items():
        rows.append({
            "trace_id": trace_id,
            "expected": expected,
            "primary": expected,
            "oracle": expected,
            "expected_match": True,
            "primary_oracle_agreement": True,
        })
    return {
        "passed": True,
        "trace_count": 4,
        "event_count": 44,
        "expected_verdict_matches": 4,
        "first_violation_matches": 4,
        "primary_oracle_agreement_count": 4,
        "rows": rows,
    }


def test_complete_report_is_deterministic():
    one = module.build_complete_report(synthetic_fixture(), historical_fixture())
    two = module.build_complete_report(synthetic_fixture(), historical_fixture())
    assert module.compact_bytes(one) == module.compact_bytes(two)
    assert one["coverage"]["total_traces"] == 40
    assert one["coverage"]["total_events"] == 572
    assert one["passed"] is True
    assert {x["disposition"] for x in one["hypotheses"].values()} == {"supported"}


def test_rejects_historical_drift():
    historical = historical_fixture()
    historical["rows"][2]["expected"] = {"verdict": "valid"}
    try:
        module.build_complete_report(synthetic_fixture(), historical)
    except ValueError as error:
        assert "historical expectation drift" in str(error)
    else:
        raise AssertionError("expected historical drift rejection")
