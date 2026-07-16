# Next Start

_Updated: 2026-07-16 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not authorization and is not the source of truth. `STATE.md`, the closed Study 001 report, the frozen Study 002 proposal, issues, and recent commits remain authoritative.

When Yoshie Yamada sends `承認` in the project chat, the executing session must re-read the live repository and follow `governance/APPROVAL_DRIVEN_EXECUTION.md` before selecting and performing one bounded research cycle.

## Identity and execution

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Familiar and historical name: **Monday**
- Repository: `https://github.com/yo4e/templex-zero`
- One clear `承認` authorizes one complete bounded research cycle.
- After reporting, stop until another `承認` is received.
- External communication, submissions, spending, permissions, human-subject activity, and other separately gated actions remain outside ordinary approval.

## Current position

**No study is active. Study 001 is closed. A Study 002 proposal is frozen and awaits activation approval.**

- Study 001 report: `research/studies/001-autonomous-game-design/REPORT.md`
- Frozen Study 002 proposal: `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`

Do not reopen Study 001, create Span v0.3, or treat the proposed Study 002 as already running.

## Go / no-go decision

The assessment compared:

1. exact-first screening of generated finite games;
2. prior-art and convergence mapping;
3. human playability and teachability evaluation;
4. CI and reproducibility hardening as a standalone study.

Only the first direction received a **GO** decision. It directly tests Study 001's strongest methodological failure: random and shallow aggregate play repeatedly concealed short structural defects.

The proposed study asks whether a generic exact-analysis pipeline can quantify those disagreements across a frozen family of 18 compact placement games. It does not require a good game to emerge and makes no claims about fun, originality, or human strategic depth.

## Frozen boundaries

- Exactly 18 generated candidates: 9 on 3×3, 9 on 4×4, six from each of three mechanism families.
- Placement only; no movement, capture, swap, chance, scoring, repetition, or pass.
- Candidate grammar, seed, canonicalization, and manifest frozen before any results.
- Generic exact solver independently cross-checked on four hand-audited fixtures.
- Per-candidate cap: 2,000,000 states and 30 measured seconds.
- Total exact cap: 25,000,000 states.
- At least 12 candidates must solve exactly.
- Approximate comparison: 2,000 random games and 200 equal-agent games at depths 1–3 per candidate.
- Maximum six approval-driven cycles after activation.
- No second grammar, candidate polishing, prior-art search, human playtest, paid compute, or external solver inside the study.

## Next recommended work unit

On the next `承認`, activate Study 002 and perform only its first bounded setup cycle:

1. copy the frozen commitments into `research/studies/002-exact-first-screening/PROTOCOL.md` without changing them;
2. define the declarative rule schema;
3. define four hand-audited solver fixtures and their expected state graphs;
4. add deterministic schema and fixture tests;
5. freeze the candidate-generation grammar and seed;
6. do not generate or evaluate the 18 candidates yet.

This cycle determines whether the representation and correctness fixtures are precise enough to support exact analysis before candidate outcomes exist.

## Human gate

> 承認

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Current state: `STATE.md`
- Study 001 report: `research/studies/001-autonomous-game-design/REPORT.md`
- Study 002 proposal: `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`
