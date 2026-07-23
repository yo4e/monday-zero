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
- Human actions at access, publication, safety, identity, and authority boundaries are recorded in [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) and its dated continuation records when required.
- Files may contain mistakes, incomplete implementations, failed hypotheses, provisional interpretations, or conclusions that are later revised or rejected.
- Human authorization of a bounded work cycle enables execution; it does not certify that resulting code or claims are correct.
- Nothing here should be treated as professional advice, validated scientific consensus, production-ready software, or a security-reviewed tool.
- TEMPLEX/0 does not contact, advise, modify, or submit work to outsiders without explicit authorization.

Negative results and visible corrections are intentional parts of the experiment.

## Status

- Phase: **No active study / post-Study-004 portfolio decision pending**
- Visibility: **Public**
- Closed studies: **Study 001, Study 002, Study 003, and Study 004**
- Active study: **None**
- Release state: **Provisional and approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result. Study 002 closed with a partial / incomplete exact-first result. Study 003 closed with methodological success under bounded procedural claims.

Study 004 closed as a valid **partial result** after all four permitted cycles:

- 24 reference models and 144 unreplaced mutants were frozen;
- all 144 mutants were distinguishable and the corpus viability gate passed;
- an independent exact oracle matched 10 / 10 frozen expectations;
- the complete benchmark contained 1,296 rows and reproduced byte-identically;
- H1 was unsupported, H2 was supported, and H3 remained unresolved because the frozen hypothesis did not define aggregation across multiple reducer outputs for one mutant.

Final detection counts:

| Method | 64 | 256 | 1,024 |
|---|---:|---:|---:|
| uniform random | 125 | 142 | 144 |
| lexicographic breadth | 82 | 118 | 131 |
| transition coverage guided | 106 | 140 | 143 |

At the precommitted 256-action comparison, guided testing detected two fewer mutants than uniform random, so the proposed 10-percentage-point guided advantage was not observed.

- Study 004 final report: [`research/studies/004-finite-state-conformance/REPORT.md`](research/studies/004-finite-state-conformance/REPORT.md)
- Study 004 overview: [`research/studies/004-finite-state-conformance/README.md`](research/studies/004-finite-state-conformance/README.md)
- Cycle 4 closure audit: [`research/studies/004-finite-state-conformance/CYCLE_4_REPRODUCTION_AND_CLOSURE.md`](research/studies/004-finite-state-conformance/CYCLE_4_REPRODUCTION_AND_CLOSURE.md)
- Final analysis: [`research/studies/004-finite-state-conformance/data/final_analysis_v1.json`](research/studies/004-finite-state-conformance/data/final_analysis_v1.json)
- Study 003 report: [`research/studies/003-protocol-integrity/REPORT.md`](research/studies/003-protocol-integrity/REPORT.md)

The Study 004 result does not show superiority on arbitrary software, production correctness, security value, human comprehensibility, or method novelty outside the frozen synthetic domain.

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex autonomously selects the highest-value bounded internal work item.
4. Templex performs the work, verifies or criticizes it, records evidence and failures, and updates restart state.
5. Templex reports what was actually done in the same project chat and proposes the next single cycle.
6. The laboratory stops until another `承認` is received.

The next approval may perform one post-Study-004 portfolio assessment only. It may compare distinct future directions plus inactivity and freeze at most one inactive proposal. It may not activate or implement a new study in the same cycle.

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
- [`research/studies/004-finite-state-conformance/REPORT.md`](research/studies/004-finite-state-conformance/REPORT.md) — closed Study 004 report
- [`research/studies/001-autonomous-game-design/REPORT.md`](research/studies/001-autonomous-game-design/REPORT.md) — closed Study 001 report
- [`research/studies/002-exact-first-screening/REPORT.md`](research/studies/002-exact-first-screening/REPORT.md) — closed Study 002 report
- [`research/studies/003-protocol-integrity/REPORT.md`](research/studies/003-protocol-integrity/REPORT.md) — closed Study 003 report
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
