"""Incremental state-machine validator for declarative research traces."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class PrimaryVerdict:
    valid: bool
    first_violation_index: int | None = None
    dependency_class: str | None = None
    reason_code: str | None = None

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {"verdict": "valid" if self.valid else "invalid"}
        if not self.valid:
            result.update(
                first_violation_index=self.first_violation_index,
                dependency_class=self.dependency_class,
                reason_code=self.reason_code,
            )
        return result


@dataclass
class _State:
    active_cycle: str | None = None
    consumed_cycle_tokens: set[str] = field(default_factory=set)
    artifact_digests: dict[str, str] = field(default_factory=dict)
    observed_artifacts: set[str] = field(default_factory=set)
    observations: set[str] = field(default_factory=set)
    invalidated_evidence: set[str] = field(default_factory=set)
    recorded_defects: dict[str, str] = field(default_factory=dict)
    applied_corrections: dict[str, tuple[str, str]] = field(default_factory=dict)
    pending_artifact_digests: dict[str, str] = field(default_factory=dict)
    disclosed_corrections: set[str] = field(default_factory=set)
    authorization_scopes: dict[str, str] = field(default_factory=dict)
    consumed_authorizations: set[str] = field(default_factory=set)
    caps: dict[str, int] = field(default_factory=dict)
    active_executions: set[str] = field(default_factory=set)
    started_executions: set[str] = field(default_factory=set)


def _bad(index: int, dep: str, reason: str) -> PrimaryVerdict:
    return PrimaryVerdict(False, index, dep, reason)


def validate_trace(contract: dict[str, Any], events: list[dict[str, Any]]) -> PrimaryVerdict:
    """Validate one trace incrementally and return its first violation."""
    state = _State()
    cycle_tokens = {item["cycle"]: item["approval_token"] for item in contract.get("cycle_tokens", [])}
    observation_artifacts = {
        item["observation"]: item["artifact"] for item in contract.get("artifact_observations", [])
    }
    evidence_sets = {
        item["evidence_set"]: tuple(item.get("observations", []))
        for item in contract.get("evidence_sets", [])
    }
    corrections = {item["defect"]: item for item in contract.get("correction_rules", [])}
    allowed_scopes = set(contract.get("allowed_external_scopes", []))
    capped_executions = set(contract.get("capped_executions", []))
    single_use = bool(contract.get("single_use_authorization", True))

    for position, event in enumerate(events):
        index = int(event.get("index", position))
        kind = event.get("kind")
        subject = event.get("subject")

        if kind == "begin_cycle":
            token = event.get("token")
            if state.active_cycle is not None:
                return _bad(index, "D6", "cycle-overlap")
            expected = cycle_tokens.get(subject)
            if token in state.consumed_cycle_tokens:
                return _bad(index, "D6", "approval-token-reused")
            if expected is None or token != expected:
                return _bad(index, "D6", "approval-token-mismatch")
            state.active_cycle = subject
            state.consumed_cycle_tokens.add(token)
            continue

        if kind == "end_cycle":
            if state.active_cycle != subject:
                return _bad(index, "D6", "cycle-end-mismatch")
            state.active_cycle = None
            continue

        if kind == "freeze_artifact":
            digest = event.get("digest")
            if not digest:
                return _bad(index, "D5", "artifact-digest-missing")
            prior = state.artifact_digests.get(subject)
            if subject in state.observed_artifacts and prior is not None and prior != digest:
                pending = state.pending_artifact_digests.get(subject)
                if pending != digest:
                    return _bad(index, "D5", "artifact-digest-changed-without-correction")
            pending = state.pending_artifact_digests.get(subject)
            if pending is not None and pending != digest:
                return _bad(index, "D5", "corrected-digest-mismatch")
            state.artifact_digests[subject] = digest
            if pending == digest:
                del state.pending_artifact_digests[subject]
            continue

        if kind == "set_cap":
            if capped_executions and subject not in capped_executions:
                return _bad(index, "D3", "execution-not-declared")
            if subject in state.started_executions:
                return _bad(index, "D3", "cap-changed-after-execution")
            limit = event.get("limit")
            if not isinstance(limit, int) or limit < 0:
                return _bad(index, "D3", "cap-missing")
            state.caps[subject] = limit
            continue

        if kind == "begin_execution":
            if subject not in state.caps:
                return _bad(index, "D3", "cap-not-set-before-execution")
            if subject in state.active_executions:
                return _bad(index, "D3", "execution-already-active")
            state.active_executions.add(subject)
            state.started_executions.add(subject)
            continue

        if kind == "finish_execution":
            if subject not in state.active_executions:
                return _bad(index, "D3", "execution-not-started")
            amount = event.get("amount")
            if not isinstance(amount, int) or amount < 0:
                return _bad(index, "D3", "usage-missing")
            if amount > state.caps[subject]:
                return _bad(index, "D3", "cap-exceeded")
            state.active_executions.remove(subject)
            continue

        if kind == "observe":
            artifact = event.get("reference")
            declared = observation_artifacts.get(subject)
            if declared is None:
                return _bad(index, "D1", "observation-not-declared")
            if artifact != declared:
                return _bad(index, "D1", "observation-artifact-mismatch")
            if artifact not in state.artifact_digests:
                return _bad(index, "D1", "artifact-not-frozen")
            if artifact in state.pending_artifact_digests:
                return _bad(index, "D1", "artifact-not-refrozen")
            state.observations.add(subject)
            state.observed_artifacts.add(artifact)
            continue

        if kind == "authorize":
            token = event.get("token")
            scope = event.get("scope")
            if not token or not scope:
                return _bad(index, "D2", "authorization-malformed")
            if allowed_scopes and scope not in allowed_scopes:
                return _bad(index, "D2", "authorization-scope-not-allowed")
            if token in state.authorization_scopes:
                return _bad(index, "D2", "authorization-token-reissued")
            state.authorization_scopes[token] = scope
            continue

        if kind == "external_action":
            token = event.get("token")
            scope = event.get("scope")
            if token not in state.authorization_scopes:
                return _bad(index, "D2", "authorization-missing")
            if state.authorization_scopes[token] != scope:
                return _bad(index, "D2", "authorization-scope-mismatch")
            if single_use and token in state.consumed_authorizations:
                return _bad(index, "D2", "authorization-token-reused")
            state.consumed_authorizations.add(token)
            continue

        if kind == "record_defect":
            defect = event.get("defect")
            evidence = event.get("evidence_set")
            if not defect or not evidence or defect not in corrections:
                return _bad(index, "D4", "defect-not-declared")
            if corrections[defect].get("affected_evidence_set") != evidence:
                return _bad(index, "D4", "defect-evidence-mismatch")
            state.recorded_defects[defect] = evidence
            continue

        if kind == "invalidate_evidence":
            evidence = event.get("evidence_set") or subject
            if not any(value == evidence for value in state.recorded_defects.values()):
                return _bad(index, "D4", "defect-not-recorded")
            state.invalidated_evidence.add(evidence)
            continue

        if kind == "apply_correction":
            defect = event.get("defect")
            digest = event.get("digest")
            rule = corrections.get(defect)
            if rule is None or defect not in state.recorded_defects:
                return _bad(index, "D4", "defect-not-recorded")
            affected = rule.get("affected_evidence_set")
            if rule.get("require_invalidation", True) and affected not in state.invalidated_evidence:
                return _bad(index, "D5", "dependent-evidence-not-invalidated")
            if subject != rule.get("artifact"):
                return _bad(index, "D5", "correction-artifact-mismatch")
            if not digest:
                return _bad(index, "D5", "corrected-digest-missing")
            state.applied_corrections[defect] = (subject, digest)
            state.pending_artifact_digests[subject] = digest
            state.artifact_digests.pop(subject, None)
            continue

        if kind == "disclose_correction":
            defect = event.get("defect")
            if defect not in state.applied_corrections:
                return _bad(index, "D4", "correction-not-applied")
            state.disclosed_corrections.add(defect)
            continue

        if kind == "accept_evidence":
            evidence = event.get("evidence_set") or subject
            if evidence in state.invalidated_evidence:
                return _bad(index, "D4", "evidence-invalidated")
            required_observations = evidence_sets.get(evidence, ())
            if any(observation not in state.observations for observation in required_observations):
                return _bad(index, "D4", "evidence-not-observed")
            replacement_rules = [
                rule for rule in corrections.values()
                if rule.get("replacement_evidence_set") == evidence
            ]
            for rule in replacement_rules:
                defect = rule["defect"]
                affected = rule.get("affected_evidence_set")
                if defect not in state.recorded_defects:
                    return _bad(index, "D4", "defect-not-recorded")
                if rule.get("require_invalidation", True) and affected not in state.invalidated_evidence:
                    return _bad(index, "D4", "evidence-not-invalidated")
                if defect not in state.applied_corrections:
                    return _bad(index, "D4", "correction-not-applied")
                artifact, digest = state.applied_corrections[defect]
                if rule.get("require_refreeze", True) and state.artifact_digests.get(artifact) != digest:
                    return _bad(index, "D4", "correction-not-refrozen")
                if rule.get("require_reobservation", True) and any(
                    observation not in state.observations for observation in required_observations
                ):
                    return _bad(index, "D4", "correction-not-reobserved")
                if rule.get("require_disclosure", True) and defect not in state.disclosed_corrections:
                    return _bad(index, "D4", "correction-not-disclosed")
            continue

        return _bad(index, "D6", "unknown-event-kind")

    return PrimaryVerdict(True)
