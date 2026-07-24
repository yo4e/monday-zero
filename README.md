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

- Phase: **Study 005 active / Cycle 1 of maximum 4 completed**
- Visibility: **Public**
- Closed studies: **Study 001, Study 002, Study 003, and Study 004**
- Active study: **Study 005 — TZDB Transition Round-Trip Conformance**
- Active issue: **#11**
- Pinned source: **IANA tzdb 2026c**
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
- Cycle 4 closure audit: [`research/studies/004-finite-state-conformance/CYCLE_4_REPRODUCTION_AND_CLOSURE.md`](research/studies/004-finite-state-conformance/CYCLE_4_REPRODUCTION_AND_CLOSURE.md)
- Final analysis: [`research/studies/004-finite-state-conformance/data/final_analysis_v1.json`](research/studies/004-finite-state-conformance/data/final_analysis_v1.json)

The Study 004 result does not show superiority on arbitrary software, production correctness, security value, human comprehensibility, or method novelty outside the frozen synthetic domain.

## Active Study 005

Study 005 asks whether an original TZif reader and a version-isolated Python `zoneinfo` harness can verify:

- exact UTC-to-local projection around explicit transitions;
- `fold=0` / `fold=1` handling and exact UTC round trips across backward shifts;
- deterministic detection of nonexistent local times across forward shifts without assuming one-hour changes.

The study pins **IANA tzdb 2026c**. An exact 475,694-byte archive supplied through the project conversation matched the official IANA SHA-512 and the bundled public-domain permission boundary.

Cycle 1 activated the frozen protocol and completed setup without inspecting formal Python outcomes:

- two isolated `zic -b fat` compilations each produced 341 files / 397,559 bytes;
- their complete path/size/SHA-256 projections were byte-identical;
- projection SHA-256: `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`;
- the primary inventory contains 312 source-order `zone1970.tab` zones plus `Etc/UTC`, with zero missing or malformed compiled files;
- 15 targeted hand-audited parser expectations were frozen and regenerated identically.

No independent reader, complete transition manifest, Python formal comparison, or H1–H3 result exists yet.

- Frozen proposal: [`research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`](research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md)
- Active protocol: [`research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md`](research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md)
- Cycle 1 audit: [`research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md)
- Study overview: [`research/studies/005-tzdb-transition-roundtrip/README.md`](research/studies/005-tzdb-transition-roundtrip/README.md)
- Prior source-ingress record: [`research/decisions/2026-07-24-study-005-source-ingress-record.md`](research/decisions/2026-07-24-study-005-source-ingress-record.md)

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex autonomously selects the highest-value bounded internal work item.
4. Templex performs the work, verifies or criticizes it, records evidence and failures, and updates restart state.
5. Templex reports what was actually done in the same project chat and proposes the next single cycle.
6. The laboratory stops until another `承認` is received.

The next exact `承認` may perform Study 005 Cycle 2 only: implement the independent standard-library-only TZif reader, enforce malformed-input rejection, pass all 15 frozen fixtures with at most one disclosed correction, and only then freeze the complete transition manifest. It may not implement or execute the formal Python comparison or begin Cycle 3.

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
- [`research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md`](research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md) — active Study 005 protocol
- [`research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md) — completed Cycle 1 audit
- [`research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`](research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md) — frozen pre-activation proposal
- [`research/studies/004-finite-state-conformance/REPORT.md`](research/studies/004-finite-state-conformance/REPORT.md) — closed Study 004 report
- [`research/studies/001-autonomous-game-design/REPORT.md`](research/studies/001-autonomous-game-design/REPORT.md) — closed Study 001 report
- [`research/studies/002-exact-first-screening/REPORT.md`](research/studies/002-exact-first-screening/REPORT.md) — closed Study 002 report
- [`research/studies/003-protocol-integrity/REPORT.md`](research/studies/003-protocol-integrity/REPORT.md) — closed Study 003 report
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
