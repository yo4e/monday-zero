"""Deterministic synthetic correctness gate for protocol-integrity validators."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from typing import Any

from .baseline import inspect_order
from .oracle import inspect_trace
from .validator import validate_trace


FORBIDDEN_BRANCH_PATTERN = re.compile(
    r"(?:P[1-6]-(?:V|I)|C[1-4]-(?:V|M[1-5])|S2-|Study\s*00[123]|research/studies/)"
)


def canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def load_bundle(data_dir: Path) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    index = json.loads((data_dir / "index.json").read_text(encoding="utf-8"))
    if index["trace_count"] != 36:
        raise ValueError("frozen bundle must contain 36 traces")
    loaded: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for file_info in index["files"]:
        path = data_dir / file_info["path"]
        payload = path.read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        if digest != file_info["sha256"]:
            raise ValueError(f"bundle digest mismatch: {path.name}")
        group = json.loads(payload)
        contracts = {item["contract_id"]: item for item in group["contracts"]}
        for trace in group["traces"]:
            loaded.append((contracts[trace["contract_id"]], trace))
    if len(loaded) != 36:
        raise ValueError("bundle trace count mismatch")
    return loaded


def scan_special_cases(source_paths: list[Path]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in source_paths:
        text = path.read_text(encoding="utf-8")
        for match in FORBIDDEN_BRANCH_PATTERN.finditer(text):
            findings.append({"path": str(path), "match": match.group(0)})
    return findings


def run_gate(data_dir: Path, source_paths: list[Path]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    false_accepts: list[str] = []
    false_rejects: list[str] = []
    index_errors: list[str] = []
    class_errors: list[str] = []
    reason_errors: list[str] = []
    oracle_disagreements: list[str] = []
    rejected_mutants: list[str] = []
    baseline_accepted_invalid: list[str] = []

    for contract, trace in load_bundle(data_dir):
        expected = trace["expected"]
        primary = validate_trace(contract, trace["events"]).to_dict()
        oracle = inspect_trace(contract, trace["events"]).to_dict()
        baseline = inspect_order(trace["events"]).to_dict()
        trace_id = trace["trace_id"]

        expected_valid = expected["verdict"] == "valid"
        primary_valid = primary["verdict"] == "valid"
        if expected_valid and not primary_valid:
            false_rejects.append(trace_id)
        if not expected_valid and primary_valid:
            false_accepts.append(trace_id)
        if not expected_valid and not primary_valid:
            if primary.get("first_violation_index") != expected.get("first_violation_index"):
                index_errors.append(trace_id)
            if primary.get("dependency_class") != expected.get("dependency_class"):
                class_errors.append(trace_id)
            if primary.get("reason_code") != expected.get("reason_code"):
                reason_errors.append(trace_id)
        if (
            primary.get("verdict"),
            primary.get("first_violation_index"),
            primary.get("dependency_class"),
            primary.get("reason_code"),
        ) != (
            oracle.get("verdict"),
            oracle.get("first_violation_index"),
            oracle.get("dependency_class"),
            oracle.get("reason_code"),
        ):
            oracle_disagreements.append(trace_id)
        if trace.get("mutation_operator") and primary.get("verdict") == "invalid":
            rejected_mutants.append(trace_id)
        if expected["verdict"] == "invalid" and baseline["verdict"] == "valid":
            baseline_accepted_invalid.append(trace_id)

        rows.append(
            {
                "trace_id": trace_id,
                "category": trace["category"],
                "mutation_operator": trace.get("mutation_operator"),
                "expected": expected,
                "primary": primary,
                "oracle": oracle,
                "baseline": baseline,
            }
        )

    named = ["P2-I", "P3-I", "P5-I", "P6-I"]
    special_cases = scan_special_cases(source_paths)
    metrics = {
        "trace_count": len(rows),
        "expected_valid": sum(row["expected"]["verdict"] == "valid" for row in rows),
        "expected_invalid": sum(row["expected"]["verdict"] == "invalid" for row in rows),
        "false_accept_count": len(false_accepts),
        "false_reject_count": len(false_rejects),
        "first_violation_accuracy": (26 - len(index_errors)) / 26,
        "violation_class_accuracy": (26 - len(class_errors)) / 26,
        "reason_code_accuracy": (26 - len(reason_errors)) / 26,
        "primary_oracle_agreement": (36 - len(oracle_disagreements)) / 36,
        "mutants_rejected": len(rejected_mutants),
        "mutation_count": sum(row["mutation_operator"] is not None for row in rows),
        "named_baseline_false_accepts": [item for item in named if item in baseline_accepted_invalid],
        "baseline_false_accept_count": len(baseline_accepted_invalid),
        "special_case_finding_count": len(special_cases),
    }
    passed = (
        metrics["trace_count"] == 36
        and metrics["expected_valid"] == 10
        and metrics["expected_invalid"] == 26
        and not false_accepts
        and not false_rejects
        and not index_errors
        and not class_errors
        and not oracle_disagreements
        and metrics["mutants_rejected"] == 20
        and metrics["mutation_count"] == 20
        and metrics["named_baseline_false_accepts"] == named
        and not special_cases
    )
    return {
        "schema_version": 1,
        "gate": "study-003-synthetic-correctness-v1",
        "passed": passed,
        "metrics": metrics,
        "failures": {
            "false_accepts": false_accepts,
            "false_rejects": false_rejects,
            "first_violation_errors": index_errors,
            "violation_class_errors": class_errors,
            "reason_code_errors": reason_errors,
            "primary_oracle_disagreements": oracle_disagreements,
            "special_case_findings": special_cases,
        },
        "baseline_accepted_invalid": baseline_accepted_invalid,
        "rows": rows,
    }
