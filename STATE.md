# State

_Last updated: 2026-07-15_

## Phase

**Study 001 / Keystone implementation**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- Relay was rejected after stronger symmetric play exposed a severe first-player advantage.
- Span v0.1 remains frozen and rejected after exhaustive reply enumeration proved a five-ply Black forced connection.
- Keystone is the third and final originally shortlisted prototype.
- Its genesis brief was recovered from commit `5a59af0d88da6bfab14bc3bc8bd1913d31e4da6e`.
- `prototypes/keystone/ORIGIN.md` records the original mechanism, missing decisions, and pre-result resolutions.
- `prototypes/keystone/RULES.md` freezes Keystone v0.1 before implementation or play results.
- Keystone v0.1 uses an empty 5×5 board, eight stones per player, placement or one-step orthogonal shifting, mandatory single custodian capture, and a victory component containing C3 plus two separate contacts with different edges.
- Captured stones leave the game. No legal move loses. Third occurrence of a complete position is a draw. Black moves first and there is no swap rule.
- The core rules are 277 words. Internal consistency checks are complete, but no Keystone code or play evidence exists yet.
- Issue #2 tracks implementation and evaluation.

## Next actions

1. Implement Keystone v0.1 legal actions, capture resolution, victory, repetition state, and rendering under `src/templex_zero/`.
2. Add deterministic tests for placement, shifting, mandatory single capture, multi-bracket choice, center-and-edge victory, corner handling, no-move loss, and repetition draw.
3. Run the full existing test suite and compile check.
4. Only after rule tests pass, run random pathology and stronger symmetric-agent screens.
5. Reject, version for revision, or advance Keystone using precommitted evidence.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Ordinary repository cycles are approval-driven. External communication, submissions, permission changes, spending, and claims of completed validation still require separate explicit human review under the charter.

## Human action currently needed

None.