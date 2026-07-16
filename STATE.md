# State

_Last updated: 2026-07-16_

## Phase

**Study 001 / Span v0.2 empirical screening**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- Relay is rejected after stronger symmetric play exposed severe first-player advantage and a substantial 200-ply unresolved population.
- Span v0.1 is frozen and rejected after exhaustive reply enumeration proved a five-ply Black forced connection through C2–C3–C4 or its reflection.
- Keystone v0.1 is frozen and rejected after only 50.9% of 2,000 fixed-seed random games completed by 200 plies.
- `analysis/prototype_revision_selection.md` selected Span as the only one-change revision target.
- `prototypes/span/RULES_v0_2.md` froze the opening swap rule before implementation or new play results.
- `src/templex_zero/games/span_v0_2.py` implements participant identity, participant-color ownership, swap, unchanged v0.1 placement geometry, terminal mapping, and rendering.
- `src/templex_zero/span_v0_2_agents.py` now supplies participant-perspective random and depth-limited minimax agents. The same search and depth choose the opening placement, swap response, and later placements.
- `src/templex_zero/span_v0_2_match.py` records opening placement, swap use, final color ownership, participant winner, color winner, win mode, plies, placements, and legal-action counts.
- `tests/test_span_v0_2_agents.py` adds seven deterministic instrumentation tests.
- A locally reconstructed live tree produced **52 passed**: 45 previous cases plus 7 new agent and match cases. `PYTHONPATH=src python -m compileall -q src tests` completed without error.
- `analysis/span_v0_2_agent_instrumentation.md` records the design, verification, and limitations.
- No formal Span v0.2 play screen exists. Instrumentation consistency is not balance evidence.
- Issue #4 tracks formal empirical evaluation and disposition.

## Next actions

1. Write a reproducible Span v0.2 experiment script and commit it before formal execution.
2. Run a fixed-seed random pathology screen for termination, duration, swap frequency, openings, participant and color results, win modes, and branching.
3. Run an equal-budget symmetric minimax screen with the same agent deciding opening placement, swap, and later placements.
4. Repeat configured runs and verify identical aggregate output.
5. Compare first-participant decisive win rate with the precommitted 40–60% balance interval, while treating random parity only as pathology evidence.
6. Measure strategic signal against random and shallower agents if v0.2 survives the symmetric balance screen.
7. Reject or advance frozen v0.2 without adding another repair inside the version.
8. If v0.2 remains viable, perform a deliberate prior-art and similarity review before making originality claims.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Ordinary repository cycles are approval-driven. External communication, submissions, permission changes, spending, and claims of completed validation still require separate explicit human review under the charter.

## Human action currently needed

None.
