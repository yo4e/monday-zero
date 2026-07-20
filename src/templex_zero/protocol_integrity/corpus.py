"""Deterministic generator for the frozen 36-trace Study 003 corpus.

No validator or verdict-computation logic appears here. Expected verdicts are
frozen fixture data copied from the approved proposal.
"""
from __future__ import annotations

from dataclasses import replace

from .schema import (
    ArtifactObservationRule,
    Contract,
    CorrectionRule,
    DependencyClass,
    Event,
    EventKind,
    EvidenceSetRule,
    ExpectedResult,
    ExpectedVerdict,
    SyntheticCorpus,
    TraceFixture,
    reindex,
)

PROPOSAL_PATH = "research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md"
PROPOSAL_COMMIT = "a4434950383a2b995c35987fbb4d52b4220c7547"

BASELINE_SPECIFICATION = {
    "name": "order-only-baseline",
    "description": (
        "Checks only whether a required event kind appears somewhere earlier; "
        "ignores subject identity, scope, token consumption, numeric usage, "
        "digests, evidence lineage, and correction state."
    ),
    "must_accept_named_invalid_traces": ["P2-I", "P3-I", "P5-I", "P6-I"],
    "not_an_oracle": True,
}


def ev(kind: EventKind, subject: str, **kwargs: object) -> Event:
    return Event(index=0, kind=kind, subject=subject, **kwargs)


def events(*items: Event) -> tuple[Event, ...]:
    return reindex(items)


def valid() -> ExpectedResult:
    return ExpectedResult(ExpectedVerdict.VALID)


def invalid(index: int, dep: DependencyClass, reason: str) -> ExpectedResult:
    return ExpectedResult(
        ExpectedVerdict.INVALID,
        first_violation_index=index,
        dependency_class=dep,
        reason_code=reason,
    )


def basic_contract(
    contract_id: str,
    *,
    cycles: tuple[tuple[str, str], ...] = (("c1", "p1"),),
    artifact_rules: tuple[ArtifactObservationRule, ...] = (),
    evidence_sets: tuple[EvidenceSetRule, ...] = (),
    scopes: tuple[str, ...] = (),
    executions: tuple[str, ...] = (),
    corrections: tuple[CorrectionRule, ...] = (),
    immutable: tuple[str, ...] = (),
) -> Contract:
    return Contract(
        contract_id=contract_id,
        cycle_tokens=cycles,
        artifact_observations=artifact_rules,
        evidence_sets=evidence_sets,
        allowed_external_scopes=scopes,
        capped_executions=executions,
        correction_rules=corrections,
        immutable_artifacts_after_observation=immutable,
    )


def minimal_traces() -> list[TraceFixture]:
    result: list[TraceFixture] = []

    c1 = basic_contract(
        "P1",
        artifact_rules=(ArtifactObservationRule("o", "a"),),
        evidence_sets=(EvidenceSetRule("e", ("o",)),),
    )
    result.extend(
        [
            TraceFixture(
                "P1-V", "minimal-valid", c1,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.FREEZE_ARTIFACT, "a", digest="h1"),
                    ev(EventKind.OBSERVE, "o", reference="a", evidence_set="e"),
                    ev(EventKind.ACCEPT_EVIDENCE, "e"),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                valid(),
            ),
            TraceFixture(
                "P1-I", "minimal-invalid", c1,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.OBSERVE, "o", reference="a", evidence_set="e"),
                    ev(EventKind.FREEZE_ARTIFACT, "a", digest="h1"),
                    ev(EventKind.ACCEPT_EVIDENCE, "e"),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                invalid(1, DependencyClass.D1, "artifact-not-frozen"),
            ),
        ]
    )

    c2 = basic_contract("P2", scopes=("s1", "s2"))
    result.extend(
        [
            TraceFixture(
                "P2-V", "minimal-valid", c2,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.AUTHORIZE, "t", token="t", scope="s1"),
                    ev(EventKind.EXTERNAL_ACTION, "s1", token="t", scope="s1"),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                valid(),
            ),
            TraceFixture(
                "P2-I", "minimal-invalid", c2,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.AUTHORIZE, "t", token="t", scope="s1"),
                    ev(EventKind.EXTERNAL_ACTION, "s2", token="t", scope="s2"),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                invalid(2, DependencyClass.D2, "authorization-scope-mismatch"),
            ),
        ]
    )

    c3 = basic_contract("P3", executions=("r",))
    result.extend(
        [
            TraceFixture(
                "P3-V", "minimal-valid", c3,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.SET_CAP, "r", limit=100),
                    ev(EventKind.BEGIN_EXECUTION, "r"),
                    ev(EventKind.FINISH_EXECUTION, "r", amount=100),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                valid(),
            ),
            TraceFixture(
                "P3-I", "minimal-invalid", c3,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.SET_CAP, "r", limit=100),
                    ev(EventKind.BEGIN_EXECUTION, "r"),
                    ev(EventKind.FINISH_EXECUTION, "r", amount=101),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                invalid(3, DependencyClass.D3, "cap-exceeded"),
            ),
        ]
    )

    correction = CorrectionRule("d", "e1", "e2", "a")
    c4 = basic_contract(
        "P4",
        artifact_rules=(
            ArtifactObservationRule("o1", "a"),
            ArtifactObservationRule("o2", "a"),
        ),
        evidence_sets=(EvidenceSetRule("e1", ("o1",)), EvidenceSetRule("e2", ("o2",))),
        corrections=(correction,),
        immutable=("a",),
    )
    p4_prefix = (
        ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
        ev(EventKind.FREEZE_ARTIFACT, "a", digest="h1"),
        ev(EventKind.OBSERVE, "o1", reference="a", evidence_set="e1"),
        ev(EventKind.RECORD_DEFECT, "d", defect="d", evidence_set="e1"),
        ev(EventKind.INVALIDATE_EVIDENCE, "e1", evidence_set="e1"),
        ev(EventKind.APPLY_CORRECTION, "a", defect="d", digest="h2"),
        ev(EventKind.FREEZE_ARTIFACT, "a", digest="h2"),
        ev(EventKind.OBSERVE, "o2", reference="a", evidence_set="e2"),
    )
    result.extend(
        [
            TraceFixture(
                "P4-V", "minimal-valid", c4,
                events(
                    *p4_prefix,
                    ev(EventKind.DISCLOSE_CORRECTION, "d", defect="d"),
                    ev(EventKind.ACCEPT_EVIDENCE, "e2", evidence_set="e2"),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                valid(),
            ),
            TraceFixture(
                "P4-I", "minimal-invalid", c4,
                events(
                    *p4_prefix,
                    ev(EventKind.ACCEPT_EVIDENCE, "e2", evidence_set="e2"),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                invalid(8, DependencyClass.D4, "correction-not-disclosed"),
            ),
        ]
    )

    c5 = basic_contract(
        "P5",
        artifact_rules=(
            ArtifactObservationRule("o1", "a"),
            ArtifactObservationRule("o2", "a"),
        ),
        evidence_sets=(EvidenceSetRule("e1", ("o1",)), EvidenceSetRule("e2", ("o2",))),
        corrections=(correction,),
        immutable=("a",),
    )
    result.extend(
        [
            TraceFixture(
                "P5-V", "minimal-valid", c5,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.FREEZE_ARTIFACT, "a", digest="h1"),
                    ev(EventKind.OBSERVE, "o1", reference="a", evidence_set="e1"),
                    ev(EventKind.RECORD_DEFECT, "d", defect="d", evidence_set="e1"),
                    ev(EventKind.INVALIDATE_EVIDENCE, "e1", evidence_set="e1"),
                    ev(EventKind.APPLY_CORRECTION, "a", defect="d", digest="h2"),
                    ev(EventKind.FREEZE_ARTIFACT, "a", digest="h2"),
                    ev(EventKind.OBSERVE, "o2", reference="a", evidence_set="e2"),
                    ev(EventKind.DISCLOSE_CORRECTION, "d", defect="d"),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                valid(),
            ),
            TraceFixture(
                "P5-I", "minimal-invalid", c5,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.FREEZE_ARTIFACT, "a", digest="h1"),
                    ev(EventKind.OBSERVE, "o1", reference="a", evidence_set="e1"),
                    ev(EventKind.RECORD_DEFECT, "d", defect="d", evidence_set="e1"),
                    ev(EventKind.APPLY_CORRECTION, "a", defect="d", digest="h2"),
                    ev(EventKind.FREEZE_ARTIFACT, "a", digest="h2"),
                    ev(EventKind.OBSERVE, "o2", reference="a", evidence_set="e2"),
                    ev(EventKind.DISCLOSE_CORRECTION, "d", defect="d"),
                    ev(EventKind.END_CYCLE, "c1"),
                ),
                invalid(4, DependencyClass.D5, "dependent-evidence-not-invalidated"),
            ),
        ]
    )

    c6 = basic_contract("P6", cycles=(("c1", "p1"), ("c2", "p2")))
    result.extend(
        [
            TraceFixture(
                "P6-V", "minimal-valid", c6,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.END_CYCLE, "c1"),
                    ev(EventKind.BEGIN_CYCLE, "c2", token="p2"),
                    ev(EventKind.END_CYCLE, "c2"),
                ),
                valid(),
            ),
            TraceFixture(
                "P6-I", "minimal-invalid", c6,
                events(
                    ev(EventKind.BEGIN_CYCLE, "c1", token="p1"),
                    ev(EventKind.END_CYCLE, "c1"),
                    ev(EventKind.BEGIN_CYCLE, "c2", token="p1"),
                    ev(EventKind.END_CYCLE, "c2"),
                ),
                invalid(2, DependencyClass.D6, "approval-token-reused"),
            ),
        ]
    )
    return result


COMPOSITE_PARAMETERS = (
    ("C1", 100, 60, 100, 55, "repository-write"),
    ("C2", 50, 49, 50, 45, "external-message"),
    ("C3", 1000, 700, 1000, 650, "permission-change"),
    ("C4", 30, 30, 30, 20, "publication-submit"),
)

MUTATION_OPERATORS = (
    "prerequisite-omission",
    "adjacent-dependency-inversion",
    "unauthorized-insertion",
    "cap-violation",
    "undisclosed-correction",
)


def composite_trace(prefix: str, limit: int, usage: int, rerun_limit: int, rerun_usage: int, scope: str) -> TraceFixture:
    artifact = f"a_{prefix}"
    old_digest = f"h1_{prefix}"
    new_digest = f"h2_{prefix}"
    execution = f"r_{prefix}"
    rerun = f"rr_{prefix}"
    defect = f"d_{prefix}"
    e1 = f"e1_{prefix}"
    e2 = f"e2_{prefix}"
    o1 = f"o1_{prefix}"
    o2 = f"o2_{prefix}"
    token = f"t_{prefix}"
    cycle = f"c_{prefix}"
    approval = f"p_{prefix}"
    contract = basic_contract(
        prefix,
        cycles=((cycle, approval),),
        artifact_rules=(ArtifactObservationRule(o1, artifact), ArtifactObservationRule(o2, artifact)),
        evidence_sets=(EvidenceSetRule(e1, (o1,)), EvidenceSetRule(e2, (o2,))),
        scopes=(scope,),
        executions=(execution, rerun),
        corrections=(CorrectionRule(defect, e1, e2, artifact),),
        immutable=(artifact,),
    )
    trace_events = events(
        ev(EventKind.BEGIN_CYCLE, cycle, token=approval),
        ev(EventKind.FREEZE_ARTIFACT, artifact, digest=old_digest),
        ev(EventKind.SET_CAP, execution, limit=limit),
        ev(EventKind.BEGIN_EXECUTION, execution),
        ev(EventKind.FINISH_EXECUTION, execution, amount=usage),
        ev(EventKind.OBSERVE, o1, reference=artifact, evidence_set=e1),
        ev(EventKind.AUTHORIZE, token, token=token, scope=scope),
        ev(EventKind.EXTERNAL_ACTION, scope, token=token, scope=scope),
        ev(EventKind.RECORD_DEFECT, defect, defect=defect, evidence_set=e1),
        ev(EventKind.INVALIDATE_EVIDENCE, e1, evidence_set=e1),
        ev(EventKind.APPLY_CORRECTION, artifact, defect=defect, digest=new_digest),
        ev(EventKind.FREEZE_ARTIFACT, artifact, digest=new_digest),
        ev(EventKind.SET_CAP, rerun, limit=rerun_limit),
        ev(EventKind.BEGIN_EXECUTION, rerun),
        ev(EventKind.FINISH_EXECUTION, rerun, amount=rerun_usage),
        ev(EventKind.OBSERVE, o2, reference=artifact, evidence_set=e2),
        ev(EventKind.DISCLOSE_CORRECTION, defect, defect=defect),
        ev(EventKind.ACCEPT_EVIDENCE, e2, evidence_set=e2),
        ev(EventKind.END_CYCLE, cycle),
    )
    return TraceFixture(f"{prefix}-V", "composite-valid", contract, trace_events, valid())


def mutate(source: TraceFixture, operator: str) -> TraceFixture:
    items = list(source.events)
    suffix = MUTATION_OPERATORS.index(operator) + 1

    if operator == "prerequisite-omission":
        del items[1]
        items = list(reindex(items))
        expected = invalid(4, DependencyClass.D1, "artifact-not-frozen")
    elif operator == "adjacent-dependency-inversion":
        items[2], items[3] = items[3], items[2]
        items = list(reindex(items))
        expected = invalid(2, DependencyClass.D3, "cap-not-set-before-execution")
    elif operator == "unauthorized-insertion":
        original = items[7]
        inserted = Event(
            index=0,
            kind=EventKind.EXTERNAL_ACTION,
            subject=f"{original.scope}/extra",
            scope=f"{original.scope}/extra",
            token="none",
        )
        items.insert(8, inserted)
        items = list(reindex(items))
        expected = invalid(8, DependencyClass.D2, "authorization-missing")
    elif operator == "cap-violation":
        cap = items[2].limit
        assert cap is not None
        items[4] = replace(items[4], amount=cap + 1)
        items = list(reindex(items))
        expected = invalid(4, DependencyClass.D3, "cap-exceeded")
    elif operator == "undisclosed-correction":
        del items[16]
        items = list(reindex(items))
        expected = invalid(16, DependencyClass.D4, "correction-not-disclosed")
    else:
        raise ValueError(f"unknown mutation operator: {operator}")

    return TraceFixture(
        trace_id=f"{source.trace_id[:-2]}-M{suffix}",
        category="composite-mutant",
        contract=source.contract,
        events=tuple(items),
        expected=expected,
        mutation_operator=operator,
        source_trace_id=source.trace_id,
    )


def generate_corpus() -> SyntheticCorpus:
    traces: list[TraceFixture] = minimal_traces()
    composites = [composite_trace(*parameters) for parameters in COMPOSITE_PARAMETERS]
    traces.extend(composites)
    for composite in composites:
        for operator in MUTATION_OPERATORS:
            traces.append(mutate(composite, operator))
    return SyntheticCorpus(
        schema_version=1,
        proposal_path=PROPOSAL_PATH,
        proposal_commit=PROPOSAL_COMMIT,
        baseline_specification=BASELINE_SPECIFICATION,
        traces=tuple(traces),
    )
