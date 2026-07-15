# State

_Last updated: 2026-07-15_

## Phase

**Study 001 / Span stronger-agent screening**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- Relay was implemented and rejected after depth-2 symmetric play produced 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 games.
- Random-vs-random play is treated only as termination and gross-pathology evidence.
- Span v0.1 rules remain frozen in `research/studies/001-autonomous-game-design/prototypes/span/RULES.md`.
- The Span reference implementation and nine deterministic tests pass; a reconstructed full suite produced 12 passing tests.
- The fixed-seed random screen ran 10,000 games twice with identical aggregates using script commit `d1ed92b0a6ada87e8aef7c479ca4a38ab6d01f9e`.
- All games terminated within 21 plies. Median length was 15; connection caused 8,201 outcomes and immobilization 1,799.
- Black won 52.6% under random play. This is not interpreted as balance evidence.
- No gross random-play pathology currently justifies rejection or revision.

## Next actions

1. Implement a Span-specific symmetric search agent and evaluation function.
2. Run equal-budget agent-vs-agent games from both seats with fixed seeds and recorded settings.
3. Measure first-player advantage and inspect whether deeper search changes outcomes or move choice.
4. Test stronger play against random and shallow agents for strategic signal.
5. Reject, version for revision, or advance Span using the precommitted protocol.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Ordinary repository cycles are approval-driven. External communication, submissions, permission changes, spending, and claims of completed validation still require separate explicit human review under the charter.

## Human action currently needed

None.
