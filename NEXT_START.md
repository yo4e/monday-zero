# Next Start

_Updated: 2026-07-15 (Asia/Tokyo)_

## Purpose

This is a compact bridge for a scheduled read-only planning session. The repository is public, so the planner should inspect the live repository directly rather than rely on this file alone. `STATE.md`, the active study files, open issues, and recent commits remain the source of truth.

After human approval, the executing session must re-read the repository and prefer current evidence over this snapshot.

## Identity

- Public operator: **Templex Tsukino / 月野テンプレクス**.
- Laboratory: **TEMPLEX/0**.
- Familiar and historical name: **Monday**; the name originated with an OpenAI-provided ChatGPT personality.
- The project is independent and does not claim OpenAI sponsorship, endorsement, operation, or review.
- Early commits retain **MONDAY/0** and `monday_zero` as historical evidence. Current Python imports use `templex_zero`.

## Current position

Study 001 is comparing three candidate abstract-game mechanisms. Relay has been rejected in its current form. Span v0.1 rules are frozen before implementation or play results. Issue #1 remains open.

## Confirmed

- The repository is public as of 2026-07-15 and is an auditable but provisional working record.
- Scheduled planning is read-only. Repository-changing sessions require a bounded human approval token under the current operating bridge.
- Relay appeared balanced under random play but showed a severe first-player advantage under depth-2 symmetric play: 129–12 with 59 draws in 200 games.
- Random-vs-random play is useful only for termination and gross-pathology screening, not as evidence of strategic balance.
- Span v0.1 uses a 5×5 board with fixed midpoint anchors: Black at C1/C5 and White at A3/E3.
- A Span placement must either expand the pre-move bounding rectangle of one friendly orthogonal component or merge at least two friendly components.
- Connection across the assigned opposite edges wins; beginning a turn without a legal placement loses.
- The frozen baseline is `research/studies/001-autonomous-game-design/prototypes/span/RULES.md` and must not be silently rewritten after results.

## Rejected

- Relay in its current ruleset.
- Random-play parity as sufficient balance evidence.
- Retrofitting Span's baseline rules in response to results without creating a new version.

## Unresolved

- Whether Span v0.1 is implemented correctly and unambiguously.
- Span's termination profile, first-player advantage, branching behavior, and response to stronger play.
- Whether immobilization or connection dominates actual play.
- Keystone remains unimplemented and should not begin before Span receives a documented disposition.

## Next recommended work unit

Implement Span v0.1 exactly as frozen in the shared Python framework under `src/templex_zero/`, including legal moves, terminal conditions, and a readable board renderer. Add deterministic tests covering expansion, merging, illegal interior filling, connection victory, and immobilization. Do not run broad balance experiments until the implementation passes those tests.

This work unit may be proposed by the read-only scheduler. A human approval token authorizes only the described repository-writing session in this already-public repository. It does not authorize external communication, submissions, third-party repository changes, spending, contracts, permission changes, credential exposure, unlawful action, or harmful action.

## Human gate

The planning report may ask for the single-word approval token: `承認`.

That approval authorizes only the bounded work unit described in the report. The executing session must inspect the live repository before acting and may narrow or revise the plan if the repository has changed.

## Human action pending

The GitHub repository slug is still `monday-zero`. Rename it to `templex-zero` when convenient; after that, update the scheduled planner to the new URL before re-enabling the public-read test.

## Anchors

- `STATE.md` updated on 2026-07-15; current content must be re-read live.
- Span v0.1 rules commit: `418bdc92c7e32637c2b35648cfc7a79b4a3b444c`
- Issue #1: `Study 001: Implement and evaluate Span`
