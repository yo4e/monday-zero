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

Relay is rejected in its current form. Span v0.1 remains frozen and implemented. Deterministic rule tests pass, and a 10,000-game fixed-seed random pathology screen found reliable termination, practical game length, connection-dominant outcomes, and no gross random-play reason for immediate rejection. Issue #1 remains open for stronger evaluation and disposition.

## Confirmed

- Relay showed a severe first-player advantage under depth-2 symmetric play: 129–12 with 59 draws in 200 games.
- Random-vs-random play is useful only for termination and gross-pathology screening, not balance evidence.
- `src/templex_zero/games/span.py` implements the frozen Span v0.1 rules.
- `tests/test_span.py` contains nine deterministic tests; a reconstructed full suite produced 12 passing tests.
- `experiments/span_random_screen.py` at commit `d1ed92b0a6ada87e8aef7c479ca4a38ab6d01f9e` ran seeds 0–9,999 twice with identical aggregate output.
- All 10,000 random games terminated within the 21-placement structural maximum.
- Median length was 15 plies; the 10th and 90th percentiles were 9 and 18.
- Connection ended 8,201 games and immobilization ended 1,799.
- Mean legal moves across 140,506 decision nodes was 5.8609; maximum was 11.
- Black won 52.6% of random games, but this is explicitly not treated as balance evidence.

## Rejected

- Relay in its current ruleset.
- Random-play parity as sufficient balance evidence.
- Retrofitting Span's baseline rules in response to results without creating a new version.
- Scheduled Tasks as the canonical continuation mechanism for project work.

## Unresolved

- First-player advantage under competent symmetric play.
- Whether increasing search depth changes outcomes or reveals forced lines.
- Whether a stronger Span agent reliably defeats random and shallower agents.
- Whether the evaluation function captures strategically meaningful features rather than merely tempo.
- Whether the current implementation contains rule errors not exercised by existing tests and random play.
- Keystone remains unimplemented and should not begin before Span receives a documented disposition.

## Next recommended work unit

Implement a Span-specific deterministic evaluation function and depth-limited minimax agent, with tests for seat symmetry, terminal scoring, and legal move selection. Then run a small fixed-seed equal-depth symmetric smoke screen to confirm the agent and match harness behave reproducibly. Do not yet run the full balance experiment until these agent tests pass.

This is the highest-value next bounded cycle because random screening has completed and all substantive balance and strategic-signal claims now depend on a stronger, symmetric, reproducible decision procedure.

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
- Random-screen script: `experiments/span_random_screen.py`
- Random-screen data: `research/studies/001-autonomous-game-design/data/span_random_v0_1.json`
- Random-screen analysis: `research/studies/001-autonomous-game-design/analysis/span_random_v0_1.md`
- Issue #1: `Study 001: Implement and evaluate Span`
