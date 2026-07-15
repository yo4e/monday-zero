# State

_Last updated: 2026-07-15_

## Phase

**Study 001 / Keystone random pathology screening**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- Relay was rejected after stronger symmetric play exposed a severe first-player advantage.
- Span v0.1 remains frozen and rejected after exhaustive reply enumeration proved a five-ply Black forced connection.
- Keystone is the third and final originally shortlisted prototype.
- `prototypes/keystone/ORIGIN.md` records the recovered mechanism, ambiguities, and pre-result resolutions.
- `prototypes/keystone/RULES.md` freezes Keystone v0.1 before implementation or play results.
- `src/templex_zero/games/keystone.py` now implements placement, one-step orthogonal shifting, mandatory singular custodian capture, center-and-two-edge victory, no-action loss, complete-position history, threefold repetition, and rendering.
- `tests/test_keystone.py` contains eleven deterministic tests covering the frozen rule distinctions.
- A reconstructed current source tree produced **31 passed**, including all twenty existing Relay and Span tests; `python -m compileall -q src tests` completed without error.
- No Keystone play experiment has been run. Passing rule tests is not evidence of balance, depth, termination quality, teachability, or originality.
- Issue #2 tracks the remaining evaluation and disposition.

## Next actions

1. Build a reproducible Keystone random pathology screen with a 200-ply observation limit and recorded seeds.
2. Measure natural victories, threefold-repetition draws, limit hits, game length, captures, placements versus shifts, reserve use, branching, and first-player results.
3. Interpret random win rates only as gross-pathology evidence, not balance evidence.
4. If the random screen justifies continuation, implement a symmetric stronger agent and run equal-budget tests.
5. Reject, version for revision, or advance Keystone using precommitted evidence.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Ordinary repository cycles are approval-driven. External communication, submissions, permission changes, spending, and claims of completed validation still require separate explicit human review under the charter.

## Human action currently needed

None.
