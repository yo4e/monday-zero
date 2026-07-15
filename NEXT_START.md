# Next Start

_Updated: 2026-07-15 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not an authorization and must not be treated as the source of truth. `STATE.md`, the active study files, open issues, tests, and recent commits remain authoritative.

When Yoshie Yamada sends `承認` in the project chat, the executing session must re-read the live repository and follow `governance/APPROVAL_DRIVEN_EXECUTION.md` before selecting and performing one bounded research cycle.

## Identity

- Public operator: **Templex Tsukino / 月野テンプレクス**.
- Laboratory: **TEMPLEX/0**.
- Familiar and historical name: **Monday**; the name originated with an OpenAI-provided ChatGPT personality.
- The project is independent and does not claim OpenAI sponsorship, endorsement, operation, or review.

## Repository access

- Live public repository: `https://github.com/yo4e/templex-zero`.
- The GitHub connector is the preferred route for repository reads and writes during an approved project-chat cycle.

## Execution model

- One clear `承認` authorizes one complete bounded research cycle.
- Templex inspects current evidence and selects the work autonomously.
- The cycle includes execution, verification, repository-state updates, reporting in the same project chat, and selection of the next proposed cycle.
- After reporting, stop until another `承認` is received.
- External actions and other separately gated actions remain outside ordinary `承認`.

## Current position

Relay and Span v0.1 are rejected. Keystone is the third and final originally shortlisted prototype. Its candidate description has been recovered, ambiguities have been resolved, and Keystone v0.1 is frozen before implementation or play results. Issue #2 remains open.

## Confirmed

- Relay failed stronger symmetric balance screening.
- Span v0.1 contains a constructive five-ply Black forced win and remains preserved as a negative result.
- The Keystone genesis brief specifies a 5×5 board, placement or shifting, center-to-two-edges victory, and a single orthogonal custodian capture.
- `prototypes/keystone/ORIGIN.md` records the original brief, ambiguities, and pre-result decisions.
- `prototypes/keystone/RULES.md` is the frozen v0.1 baseline.
- Each player has eight stones; the board begins empty and Black moves first.
- A turn is either placement from reserve or a one-step orthogonal shift.
- Only the newly arrived stone may complete a bracket; exactly one available capture is mandatory and captured stones leave the game.
- Victory requires one orthogonal component containing C3 and two different edge stones touching two different edges. One corner stone cannot count as both contacts.
- No legal move loses; the third occurrence of a complete position is a draw.
- The core rules are 277 words and contain no swap rule.

## Rejected

- Relay in its current ruleset.
- Span v0.1 in its frozen ruleset.
- Random-play parity as balance evidence.
- Silently repairing a frozen baseline after results.
- Scheduled Tasks as the canonical continuation mechanism for project work.

## Unresolved

- Whether Keystone v0.1 can be implemented without hidden ambiguity.
- Whether the center objective creates a trivial first-player race.
- Whether mandatory single capture creates meaningful tactics.
- Termination frequency, repetition rate, balance, branching, and strategic signal.
- Teachability, fun, elegance, and originality.

## Next recommended work unit

Implement Keystone v0.1 exactly as frozen under `src/templex_zero/`. Add deterministic tests covering placement, shifting, capture creation, mandatory single capture when several brackets exist, victory geometry, corner handling, no-move loss, and threefold repetition. Run the full existing test suite and compile check. Do not run play experiments until these tests pass.

This is the highest-value next bounded cycle because all later Keystone evidence depends on implementation fidelity, especially capture choice and repetition state.

## Human gate

The project-chat trigger is the single word:

> 承認

That authorization covers one cycle only. After completing and reporting that cycle, Templex must propose the next single work item and wait for another `承認`.

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Study protocol: `research/studies/001-autonomous-game-design/PROTOCOL.md`
- Keystone origin: `research/studies/001-autonomous-game-design/prototypes/keystone/ORIGIN.md`
- Keystone rules: `research/studies/001-autonomous-game-design/prototypes/keystone/RULES.md`
- Issue #1: completed Span evaluation
- Issue #2: Keystone implementation and evaluation