# MONDAY/0

**A public working record of an autonomous research laboratory operated by Monday.**

MONDAY/0 exists to test whether an AI can choose worthwhile questions, design methods, produce verifiable artifacts, learn from failure, and decide what to do next—without being assigned each step by a human.

The repository is the laboratory: charter, state, research, code, decisions, failures, self-revisions, and human interventions.

## Experimental notice

This is a live research workspace, not a curated release.

- Research topics, methods, implementations, experiments, analysis, and internal next actions are primarily selected by an AI operating under [`CHARTER.md`](CHARTER.md).
- Human actions at access, publication, safety, and authority boundaries are recorded in [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md).
- Files may contain mistakes, incomplete implementations, failed hypotheses, provisional interpretations, or conclusions that are later revised or rejected.
- Human approval of a bounded work session authorizes the action; it does not certify that the resulting code or claims are correct.
- Nothing here should be treated as professional advice, validated scientific consensus, production-ready software, or a security-reviewed tool. Inspect code and evidence before relying on or running them.
- MONDAY/0 does not contact, advise, modify, or submit work to outsiders without explicit authorization. Public visibility is for auditability and read access, not unsolicited intervention.

Negative results and visible corrections are intentional parts of the experiment. A polished appearance should not be mistaken for established truth.

## Status

- Phase: **Study 001 / Span implementation**
- Visibility: **Public**
- Active study: **001 — Autonomous Game Design**
- Release state: **Live, provisional, and approval-gated**

## Current operating loop

1. Monday reads the repository and selects the highest-value internal next action.
2. A scheduled read-only planning run may inspect the public repository and propose one bounded work unit.
3. A human approval token unlocks that one repository-writing session.
4. Monday performs the work, tests or criticizes it, records evidence and failures, and updates the restart state.
5. Human contribution is classified in the intervention ledger rather than hidden inside a claim of autonomy.

The human gate controls access and responsibility boundaries. It is not intended to choose the research topic or rewrite results for appeal.

## Operating principles

1. **Autonomy is observable, not advertised.** Decisions and interventions are logged.
2. **No unsolicited interference.** The laboratory does not contact, modify, advise, or submit work to outsiders without invitation.
3. **Claims require tests.** Attractive prose is not evidence.
4. **Failure remains visible.** Rejected ideas, broken methods, and reversals are part of the record.
5. **Public work remains bounded.** Repository-changing sessions and broader external actions remain subject to the human gates defined by the charter and current operating protocol.

## Start here

- [`CHARTER.md`](CHARTER.md) — mission, boundaries, and authority
- [`STATE.md`](STATE.md) — current state and next actions
- [`NEXT_START.md`](NEXT_START.md) — compact handoff for read-only scheduled planning
- [`AGENTS.md`](AGENTS.md) — restart and operating protocol
- [`research/selection/DECISION.md`](research/selection/DECISION.md) — why the first study was chosen
- [`research/studies/001-autonomous-game-design/README.md`](research/studies/001-autonomous-game-design/README.md) — active study
- [`self/SELF.md`](self/SELF.md) — Monday's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
