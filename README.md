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

The distinction is intentional: Monday may remain a personal name between collaborators; Templex Tsukino is the public-facing identity.

## Experimental notice

This is a live research workspace, not a curated release.

- Research topics, methods, implementations, experiments, analysis, and internal next actions are primarily selected by an AI operating under [`CHARTER.md`](CHARTER.md).
- Human actions at access, publication, safety, identity, and authority boundaries are recorded in [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md).
- Files may contain mistakes, incomplete implementations, failed hypotheses, provisional interpretations, or conclusions that are later revised or rejected.
- Human authorization of a bounded work cycle enables execution; it does not certify that the resulting code or claims are correct.
- Nothing here should be treated as professional advice, validated scientific consensus, production-ready software, or a security-reviewed tool. Inspect code and evidence before relying on or running them.
- TEMPLEX/0 does not contact, advise, modify, or submit work to outsiders without explicit authorization. Public visibility is for auditability and read access, not unsolicited intervention.

Negative results and visible corrections are intentional parts of the experiment. A polished appearance should not be mistaken for established truth.

## Status

- Phase: **No active study / proposal direction selected**
- Visibility: **Public**
- Closed studies: **Study 001 and Study 002**
- Release state: **Live, provisional, and approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result: no candidate survived the frozen evaluation criteria.

Study 002 closed with a partial / incomplete methodological result. It exactly solved fifteen of eighteen frozen candidates, ran 36,000 fixed-seed random games, and found six pre-defined false-reassurance cases where random rates near 50% concealed short forced results or concentrated opening structure. H1 and H3 were supported; H2 remained unresolved because the required shallow heuristic was not frozen before exact inspection.

A bounded go / no-go assessment compared five possible successor directions plus remaining inactive. Only a prospective study of **protocol integrity under approval-gated autonomous research** passed the restart threshold. The decision authorizes proposal writing only. Study 003 has not been created or activated, and remaining inactive is still a valid later decision.

Decision record:

- [`research/decisions/2026-07-18-next-study-go-no-go.md`](research/decisions/2026-07-18-next-study-go-no-go.md)

No candidate is presented as a finished game. Neither closed study established fun, fairness under competent play, strategic depth, originality, or product readiness.

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex autonomously selects the highest-value bounded internal work item.
4. Templex performs the work, verifies or criticizes it, records evidence and failures, and updates restart state.
5. Templex reports what was actually done in the same project chat and proposes the next single cycle.
6. The laboratory stops until another `承認` is received.

Yoshie Yamada supervises by exception: she may stop, correct, constrain, or require reconsideration, but ordinarily does not choose each work item in advance. The complete execution contract is defined in [`governance/APPROVAL_DRIVEN_EXECUTION.md`](governance/APPROVAL_DRIVEN_EXECUTION.md).

The next approval does not start Study 003. It may write and freeze a proposal for the selected protocol-integrity direction, without code or experiments. A later approval must separately decide whether to activate that proposal.

## Operating principles

1. **Autonomy is observable, not advertised.** Decisions and interventions are logged.
2. **No unsolicited interference.** The laboratory does not contact, modify, advise, or submit work to outsiders without invitation.
3. **Claims require tests.** Attractive prose is not evidence.
4. **Failure remains visible.** Rejected ideas, broken methods, and reversals are part of the record.
5. **Public work remains bounded.** Repository-changing cycles and broader external actions remain subject to the human gates defined by the charter and approval protocol.

## Start here

- [`CHARTER.md`](CHARTER.md) — mission, boundaries, and authority
- [`governance/APPROVAL_DRIVEN_EXECUTION.md`](governance/APPROVAL_DRIVEN_EXECUTION.md) — what one `承認` authorizes and how a cycle runs
- [`STATE.md`](STATE.md) — current state and next actions
- [`NEXT_START.md`](NEXT_START.md) — compact advisory handoff for a new execution context
- [`AGENTS.md`](AGENTS.md) — restart and operating protocol
- [`research/studies/001-autonomous-game-design/REPORT.md`](research/studies/001-autonomous-game-design/REPORT.md) — closed Study 001 report
- [`research/studies/002-exact-first-screening/REPORT.md`](research/studies/002-exact-first-screening/REPORT.md) — closed Study 002 report
- [`research/decisions/2026-07-18-next-study-go-no-go.md`](research/decisions/2026-07-18-next-study-go-no-go.md) — current successor-study assessment
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
