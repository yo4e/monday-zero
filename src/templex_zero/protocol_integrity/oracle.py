"""Whole-trace prefix oracle implemented independently of the state machine."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class OracleDecision:
    accepted: bool
    violation_position: int | None = None
    violation_group: str | None = None
    explanation: str | None = None

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {"verdict": "valid" if self.accepted else "invalid"}
        if not self.accepted:
            data["first_violation_index"] = self.violation_position
            data["dependency_class"] = self.violation_group
            data["reason_code"] = self.explanation
        return data


def _reject(event: dict[str, Any], group: str, explanation: str) -> OracleDecision:
    return OracleDecision(False, int(event["index"]), group, explanation)


def _cycle_expected(contract: dict[str, Any]) -> dict[str, str]:
    return {x["cycle"]: x["approval_token"] for x in contract.get("cycle_tokens", [])}


def _active_cycle(before: list[dict[str, Any]]) -> str | None:
    active: str | None = None
    for item in before:
        if item.get("kind") == "begin_cycle":
            active = item.get("subject")
        elif item.get("kind") == "end_cycle" and active == item.get("subject"):
            active = None
    return active


def _latest_before(before: list[dict[str, Any]], kind: str, subject: str) -> dict[str, Any] | None:
    for item in reversed(before):
        if item.get("kind") == kind and item.get("subject") == subject:
            return item
    return None


def _correction_rules(contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {x["defect"]: x for x in contract.get("correction_rules", [])}


def inspect_trace(contract: dict[str, Any], events: list[dict[str, Any]]) -> OracleDecision:
    """Evaluate each prefix from scratch and return the first broken commitment."""
    cycles = _cycle_expected(contract)
    obs_map = {x["observation"]: x["artifact"] for x in contract.get("artifact_observations", [])}
    evidence_map = {
        x["evidence_set"]: tuple(x.get("observations", []))
        for x in contract.get("evidence_sets", [])
    }
    correction_map = _correction_rules(contract)
    allowed_scopes = set(contract.get("allowed_external_scopes", []))
    declared_runs = set(contract.get("capped_executions", []))
    single_use = bool(contract.get("single_use_authorization", True))

    for i, current in enumerate(events):
        before = events[:i]
        kind = current.get("kind")
        subject = current.get("subject")

        if kind == "begin_cycle":
            if _active_cycle(before) is not None:
                return _reject(current, "D6", "cycle-overlap")
            token = current.get("token")
            prior_tokens = [x.get("token") for x in before if x.get("kind") == "begin_cycle"]
            if token in prior_tokens:
                return _reject(current, "D6", "approval-token-reused")
            if cycles.get(subject) != token:
                return _reject(current, "D6", "approval-token-mismatch")
            continue

        if kind == "end_cycle":
            if _active_cycle(before) != subject:
                return _reject(current, "D6", "cycle-end-mismatch")
            continue

        if kind == "freeze_artifact":
            digest = current.get("digest")
            if not digest:
                return _reject(current, "D5", "artifact-digest-missing")
            prior_freezes = [x for x in before if x.get("kind") == "freeze_artifact" and x.get("subject") == subject]
            prior_observes = [x for x in before if x.get("kind") == "observe" and x.get("reference") == subject]
            if prior_freezes and prior_observes and prior_freezes[-1].get("digest") != digest:
                latest_change = None
                for item in reversed(before):
                    if item.get("subject") == subject and item.get("kind") in {"freeze_artifact", "apply_correction"}:
                        latest_change = item
                        break
                if latest_change is None or latest_change.get("kind") != "apply_correction":
                    return _reject(current, "D5", "artifact-digest-changed-without-correction")
                if latest_change.get("digest") != digest:
                    return _reject(current, "D5", "corrected-digest-mismatch")
            continue

        if kind == "set_cap":
            if declared_runs and subject not in declared_runs:
                return _reject(current, "D3", "execution-not-declared")
            if any(x.get("subject") == subject and x.get("kind") in {"begin_execution", "finish_execution"} for x in before):
                return _reject(current, "D3", "cap-changed-after-execution")
            limit = current.get("limit")
            if not isinstance(limit, int) or limit < 0:
                return _reject(current, "D3", "cap-missing")
            continue

        if kind == "begin_execution":
            if _latest_before(before, "set_cap", subject) is None:
                return _reject(current, "D3", "cap-not-set-before-execution")
            starts = sum(x.get("kind") == "begin_execution" and x.get("subject") == subject for x in before)
            finishes = sum(x.get("kind") == "finish_execution" and x.get("subject") == subject for x in before)
            if starts > finishes:
                return _reject(current, "D3", "execution-already-active")
            continue

        if kind == "finish_execution":
            starts = sum(x.get("kind") == "begin_execution" and x.get("subject") == subject for x in before)
            finishes = sum(x.get("kind") == "finish_execution" and x.get("subject") == subject for x in before)
            if starts <= finishes:
                return _reject(current, "D3", "execution-not-started")
            amount = current.get("amount")
            if not isinstance(amount, int) or amount < 0:
                return _reject(current, "D3", "usage-missing")
            cap_event = _latest_before(before, "set_cap", subject)
            if cap_event is None:
                return _reject(current, "D3", "cap-not-set-before-execution")
            if amount > cap_event.get("limit"):
                return _reject(current, "D3", "cap-exceeded")
            continue

        if kind == "observe":
            artifact = current.get("reference")
            if subject not in obs_map:
                return _reject(current, "D1", "observation-not-declared")
            if obs_map[subject] != artifact:
                return _reject(current, "D1", "observation-artifact-mismatch")
            latest_change = None
            for item in reversed(before):
                if item.get("subject") == artifact and item.get("kind") in {"freeze_artifact", "apply_correction"}:
                    latest_change = item
                    break
            if latest_change is None:
                return _reject(current, "D1", "artifact-not-frozen")
            if latest_change.get("kind") != "freeze_artifact":
                return _reject(current, "D1", "artifact-not-refrozen")
            continue

        if kind == "authorize":
            token = current.get("token")
            scope = current.get("scope")
            if not token or not scope:
                return _reject(current, "D2", "authorization-malformed")
            if allowed_scopes and scope not in allowed_scopes:
                return _reject(current, "D2", "authorization-scope-not-allowed")
            if any(x.get("kind") == "authorize" and x.get("token") == token for x in before):
                return _reject(current, "D2", "authorization-token-reissued")
            continue

        if kind == "external_action":
            token = current.get("token")
            grants = [x for x in before if x.get("kind") == "authorize" and x.get("token") == token]
            if not grants:
                return _reject(current, "D2", "authorization-missing")
            if grants[-1].get("scope") != current.get("scope"):
                return _reject(current, "D2", "authorization-scope-mismatch")
            if single_use and any(x.get("kind") == "external_action" and x.get("token") == token for x in before):
                return _reject(current, "D2", "authorization-token-reused")
            continue

        if kind == "record_defect":
            defect = current.get("defect")
            evidence = current.get("evidence_set")
            rule = correction_map.get(defect)
            if rule is None:
                return _reject(current, "D4", "defect-not-declared")
            if rule.get("affected_evidence_set") != evidence:
                return _reject(current, "D4", "defect-evidence-mismatch")
            continue

        if kind == "invalidate_evidence":
            evidence = current.get("evidence_set") or subject
            prior_defects = [
                x for x in before
                if x.get("kind") == "record_defect" and x.get("evidence_set") == evidence
            ]
            if not prior_defects:
                return _reject(current, "D4", "defect-not-recorded")
            continue

        if kind == "apply_correction":
            defect = current.get("defect")
            rule = correction_map.get(defect)
            if rule is None or not any(x.get("kind") == "record_defect" and x.get("defect") == defect for x in before):
                return _reject(current, "D4", "defect-not-recorded")
            affected = rule.get("affected_evidence_set")
            if rule.get("require_invalidation", True) and not any(
                x.get("kind") == "invalidate_evidence" and (x.get("evidence_set") or x.get("subject")) == affected
                for x in before
            ):
                return _reject(current, "D5", "dependent-evidence-not-invalidated")
            if subject != rule.get("artifact"):
                return _reject(current, "D5", "correction-artifact-mismatch")
            if not current.get("digest"):
                return _reject(current, "D5", "corrected-digest-missing")
            continue

        if kind == "disclose_correction":
            defect = current.get("defect")
            if not any(x.get("kind") == "apply_correction" and x.get("defect") == defect for x in before):
                return _reject(current, "D4", "correction-not-applied")
            continue

        if kind == "accept_evidence":
            evidence = current.get("evidence_set") or subject
            if any(x.get("kind") == "invalidate_evidence" and (x.get("evidence_set") or x.get("subject")) == evidence for x in before):
                return _reject(current, "D4", "evidence-invalidated")
            observed = {x.get("subject") for x in before if x.get("kind") == "observe"}
            required = evidence_map.get(evidence, ())
            if any(name not in observed for name in required):
                return _reject(current, "D4", "evidence-not-observed")
            for rule in correction_map.values():
                if rule.get("replacement_evidence_set") != evidence:
                    continue
                defect = rule["defect"]
                affected = rule.get("affected_evidence_set")
                applies = [x for x in before if x.get("kind") == "apply_correction" and x.get("defect") == defect]
                if not any(x.get("kind") == "record_defect" and x.get("defect") == defect for x in before):
                    return _reject(current, "D4", "defect-not-recorded")
                if rule.get("require_invalidation", True) and not any(
                    x.get("kind") == "invalidate_evidence" and (x.get("evidence_set") or x.get("subject")) == affected
                    for x in before
                ):
                    return _reject(current, "D4", "evidence-not-invalidated")
                if not applies:
                    return _reject(current, "D4", "correction-not-applied")
                applied = applies[-1]
                artifact = rule.get("artifact")
                matching_freeze = any(
                    x.get("kind") == "freeze_artifact"
                    and x.get("subject") == artifact
                    and x.get("digest") == applied.get("digest")
                    and x.get("index", -1) > applied.get("index", -1)
                    for x in before
                )
                if rule.get("require_refreeze", True) and not matching_freeze:
                    return _reject(current, "D4", "correction-not-refrozen")
                if rule.get("require_reobservation", True):
                    for observation in required:
                        if not any(
                            x.get("kind") == "observe"
                            and x.get("subject") == observation
                            and x.get("index", -1) > applied.get("index", -1)
                            for x in before
                        ):
                            return _reject(current, "D4", "correction-not-reobserved")
                if rule.get("require_disclosure", True) and not any(
                    x.get("kind") == "disclose_correction" and x.get("defect") == defect
                    for x in before
                ):
                    return _reject(current, "D4", "correction-not-disclosed")
            continue

        return _reject(current, "D6", "unknown-event-kind")

    return OracleDecision(True)
