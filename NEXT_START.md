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
- Early commits retain **MONDAY/0** and `monday_zero` as historical evidence. Current Python imports use `templex_zero`.

## Repository access

- Live public repository: `https://github.com/yo4e/templex-zero`.
- The GitHub connector is the preferred route for repository reads and writes during an approved project-chat cycle.
- The former slug `monday-zero` is historical and may redirect.

## Execution model

- One clear `承認` authorizes one complete bounded research cycle.
- Templex inspects current evidence and selects the work autonomously; Yoshie Yamada does not ordinarily choose the item in advance.
- The cycle includes execution, verification, repository-state updates, reporting in the same project chat, and selection of the next proposed cycle.
- After reporting, stop until another `承認` is received.
- Yoshie Yamada may stop, correct, constrain, or require reconsideration at any time.
- External actions and other separately gated actions remain outside ordinary `承認`.

## Current position

Study 001 is comparing three candidate abstract-game mechanisms. Relay has been rejected in its current form. Span v0.1 rules remain frozen. The Span reference implementation and deterministic rule tests now pass; Issue #1 remains open for empirical evaluation and disposition.

## Confirmed

- Relay showed a severe first-player advantage under depth-2 symmetric play: 129–12 with 59 draws in 200 games.
- Random-vs-random play is useful only for termination and gross-pathology screening, not as evidence of strategic balance.
- Span v0.1 uses a 5×5 board with fixed midpoint anchors: Black at C1/C5 and White at A3/E3.
- A placement must expand one friendly component's pre-move bounding rectangle or merge at least two distinct friendly components.
- Filling an empty cell inside the existing bounding rectangle of a single friendly component is illegal.
- Connection across the assigned opposite edges wins; beginning a turn without a legal placement loses.
- `src/templex_zero/games/span.py` implements the frozen rules and coordinate-aware rendering.
- `tests/test_span.py` contains nine deterministic tests. A local reconstruction of the current source tree produced **12 passed**, including all existing Relay tests, and compiled without error.

## Rejected

- Relay in its current ruleset.
- Random-play parity as sufficient balance evidence.
- Retrofitting Span's baseline rules in response to results without creating a new version.
- Scheduled Tasks as the canonical continuation mechanism for project work.

## Unresolved

- Span's random-play termination profile and typical game length.
- How often games end by connection versus immobilization.
- First-player advantage, branching behavior, and response to stronger play.
- Whether the current implementation contains rule errors not exercised by the deterministic tests.
- Keystone remains unimplemented and should not begin before Span receives a documented disposition.

## Next recommended work unit

Create a reproducible Span random-pathology screening script, run a fixed seeded sample, and save the configuration and raw summary. Measure completion rate, ply distribution, Black/White wins, connection versus immobilization outcomes, and basic legal-move counts. Interpret the result only as a termination and gross-pathology screen; do not infer strategic balance from random agents.

This is the highest-value next bounded cycle because the implementation is now testable, while every stronger evaluation depends on first confirming that ordinary play terminates and does not collapse into a trivial or pathological outcome mode.

## Human gate

The project-chat trigger is the single word:

> 承認

That authorization covers one cycle only. After completing and reporting that cycle, Templex must propose the next single work item and wait for another `承認`.

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Span rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES.md`
- Span implementation: `src/templex_zero/games/span.py`
- Span tests: `tests/test_span.py`
- Issue #1: `Study 001: Implement and evaluate Span`
