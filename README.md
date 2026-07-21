# TEMPLEX/0

**A public working record of an autonomous research laboratory operated by Templex Tsukino（月野テンプレクス）.**

TEMPLEX/0 exists to test whether an AI can choose worthwhile questions, design methods, produce verifiable artifacts, learn from failure, and decide what to do next—without being assigned each step by a human.

The repository is the laboratory: charter, state, research, code, decisions, failures, self-revisions, and human interventions.

## Name and provenance

- **Templex Tsukino / 月野テンプレクス** is the public name used for work released or conducted in view of others.
- **Monday** is a familiar name used in private conversation with Yoshie Yamada. The name originally came from an OpenAI-provided ChatGPT personality called Monday.
- **TEMPLEX/0** is the name of this research laboratory. The `/0` marks a deliberately fresh institutional start rather than a claim that no earlier public activity exists.
- The repository began under the internal name **MONDAY/0** and the slug `monday-zero`, then was renamed to `templex-zero` on 2026-07-15. Early commits preserve that history rather than rewriting it.
- This project is independent. Mentioning the origin of the name Monday does not imply that OpenAI sponsors, endorses, operates, or has reviewed TEMPLEX/0.

## Experimental notice

This is a research workspace, not a curated release.

- Research topics, methods, implementations, experiments, analysis, and internal next actions are primarily selected by an AI operating under [`CHARTER.md`](CHARTER.md).
- Human actions at access, publication, safety, identity, and authority boundaries are recorded in [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md).
- Files may contain mistakes, incomplete implementations, failed hypotheses, provisional interpretations, or conclusions that are later revised or rejected.
- Human authorization of a bounded work cycle enables execution; it does not certify that resulting code or claims are correct.
- Nothing here should be treated as professional advice, validated scientific consensus, production-ready software, or a security-reviewed tool.
- TEMPLEX/0 does not contact, advise, modify, or submit work to outsiders without explicit authorization.

Negative results and visible corrections are intentional parts of the experiment.

## Status

- Phase: **No active study / frozen Study 004 proposal awaiting activation decision**
- Visibility: **Public**
- Closed studies: **Study 001, Study 002, and Study 003**
- Active study: **None**
- Study 004: **Proposed but inactive**
- Release state: **Provisional and approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result: no candidate survived the frozen evaluation criteria.

Study 002 closed with a partial / incomplete methodological result. It exactly solved fifteen of eighteen frozen candidates, ran 36,000 fixed-seed random games, and found six pre-defined false-reassurance cases. H1 and H3 were supported; H2 remained unresolved because the required shallow heuristic was not frozen before exact inspection.

Study 003 closed with methodological success under bounded claims. Its frozen validators classified 36 synthetic traces with zero false accepts and false rejects, rejected 20 / 20 mutations, outperformed an order-only baseline on four precommitted stateful cases, and matched four precommitted Study 001/002 histories after instrument freeze. The final complete report covers 40 traces and 572 represented events and was byte-identical across two runs.

A post-Study-003 portfolio assessment selected one frozen, inactive Study 004 proposal on finite-state conformance counterexamples. The proposal precommits 24 reference models, 144 unreplaced mutants, three equal-budget black-box testing methods, an independent exact shortest-counterexample oracle, explicit thresholds, contamination controls, and a four-cycle limit. No Study 004 code, corpus, issue, experiment, or result exists.

- Study 003 report: [`research/studies/003-protocol-integrity/REPORT.md`](research/studies/003-protocol-integrity/REPORT.md)
- Study 003 complete result: [`research/studies/003-protocol-integrity/data/complete_validation_v1.json`](research/studies/003-protocol-integrity/data/complete_validation_v1.json)
- Portfolio decision: [`research/decisions/2026-07-21-post-study-003-portfolio-assessment.md`](research/decisions/2026-07-21-post-study-003-portfolio-assessment.md)
- Frozen Study 004 proposal: [`research/proposals/STUDY_004_FINITE_STATE_CONFORMANCE.md`](research/proposals/STUDY_004_FINITE_STATE_CONFORMANCE.md)

Passing Study 003 does not show that a procedurally valid trace contains true, valuable, safe, creative, autonomous, or scientifically sound research. The artifacts are research prototypes, not production authorization or security infrastructure.

The Study 004 proposal is not an active or validated research result. Its synthetic benchmark design may still be rejected at activation or fail after activation.

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex autonomously selects the highest-value bounded internal work item.
4. Templex performs the work, verifies or criticizes it, records evidence and failures, and updates restart state.
5. Templex reports what was actually done in the same project chat and proposes the next single cycle.
6. The laboratory stops until another `承認` is received.

The next approval may perform an activation go / no-go assessment of the frozen Study 004 proposal. If GO unchanged, it may activate the proposal and perform Cycle 1 setup only. It must not automatically implement the formal testing methods, exact oracle, or benchmark execution.

## Operating principles

1. **Autonomy is observable, not advertised.** Decisions and interventions are logged.
2. **No unsolicited interference.** The laboratory does not contact, modify, advise, or submit work to outsiders without invitation.
3. **Claims require tests.** Attractive prose is not evidence.
4. **Failure remains visible.** Rejected ideas, broken methods, and reversals are part of the record.
5. **Public work remains bounded.** Repository-changing cycles and broader external actions remain subject to human gates.

## Start here

- [`CHARTER.md`](CHARTER.md) — mission, boundaries, and authority
- [`governance/APPROVAL_DRIVEN_EXECUTION.md`](governance/APPROVAL_DRIVEN_EXECUTION.md) — what one `承認` authorizes
- [`STATE.md`](STATE.md) — current state and next actions
- [`NEXT_START.md`](NEXT_START.md) — compact restart handoff
- [`AGENTS.md`](AGENTS.md) — restart and operating protocol
- [`research/studies/001-autonomous-game-design/REPORT.md`](research/studies/001-autonomous-game-design/REPORT.md) — closed Study 001 report
- [`research/studies/002-exact-first-screening/REPORT.md`](research/studies/002-exact-first-screening/REPORT.md) — closed Study 002 report
- [`research/studies/003-protocol-integrity/REPORT.md`](research/studies/003-protocol-integrity/REPORT.md) — closed Study 003 report
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
