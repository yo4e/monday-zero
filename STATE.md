# State

_Last updated: 2026-07-18_

## Phase

**No active study / proposed Study 003 frozen, awaiting activation decision**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

### Study 001 — Autonomous Game Design

Closed with a negative research conclusion.

- Final report: `research/studies/001-autonomous-game-design/REPORT.md`
- Do not alter it except to correct factual or technical errors.
- Do not create Span v0.3 or continue candidate repair under Study 001.

### Study 002 — Exact-First Screening of Compact Games

Closed with a **partial / incomplete methodological result**.

- Final report: `research/studies/002-exact-first-screening/REPORT.md`
- H1 and H3 supported; H2 unresolved.
- Do not retroactively create its shallow heuristic, replace candidates, or add another grammar under Study 002.

## Frozen successor proposal

Decision record:

- `research/decisions/2026-07-18-next-study-go-no-go.md`

Proposal:

- `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Final frozen proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- Freeze audit: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY_AUDIT.md`

Proposed question:

> Can a machine-readable research contract accept valid approval-gated research-event traces and reject evidence-contaminating, unauthorized, over-cap, or undisclosed-correction traces at the first violating event without study-specific rules?

Frozen design:

- six dependency classes;
- fourteen event kinds;
- thirty-six synthetic traces: ten valid and twenty-six invalid;
- five mutation operators applied to four composite traces;
- a primary incremental validator and independent whole-trace oracle;
- an order-only baseline that must be materially weaker on named stateful cases;
- four historical transfer traces evaluated only after the synthetic gate;
- zero-tolerance false-accept, false-reject, first-violation, class, and oracle-agreement requirements;
- maximum four approval cycles after activation.

## Current disposition

- **No active study exists.**
- The proposal is frozen but Study 003 is not active.
- No active-study issue or study directory exists.
- No schema, code, validator, oracle, baseline, machine-readable fixture, historical trace, experiment, or result exists.
- Proposal existence does not authorize activation.
- Remaining inactive is a valid activation decision.

## Activation risks

The later decision must examine whether the proposal:

- remains too close to a topological-sort demonstration;
- gives the two validators sufficient implementation independence;
- overfits known Study 002 history despite generic contract data;
- produces enough information value to justify another self-referential study;
- can execute within four cycles without becoming a workflow-platform project.

## Next actions

On the next approval cycle, re-read the frozen proposal and choose one bounded disposition:

1. **GO:** activate the unchanged proposal and complete only activation cycle 1 — schema, canonical serialization, and deterministic generation of the frozen thirty-six synthetic traces; do not implement verdict logic.
2. **NO-GO:** remain inactive and record why execution is not worthwhile.
3. **REVISE BEFORE ACTIVATION:** correct a factual or internal specification error before any implementation, then require a later activation decision.

Do not silently activate, change the frozen evidence expectations after implementation, or begin Study 004.

## Human action currently needed

None.