# Span v0.2 Formal Screen and Forced-Win Diagnosis

_Date: 2026-07-16 (Asia/Tokyo)_

## Scope

This is the formal empirical evaluation of the frozen Span v0.2 opening-swap revision. The experiment script was committed before execution as `edac024671aeb380472e0a6a58a8eb35a134e124`. No rule, heuristic, opening restriction, anchor, draw condition, or swap-specific evaluation term was changed after the run began.

## Configuration and reproducibility

- random pathology screen: 10,000 games, seeds 0–9,999;
- equal-budget symmetric screen: 1,000 games, seeds 0–999;
- minimax depth: 3 for both participants at every decision;
- the same agent and budget chose the first placement, opening swap response, and later placements;
- Python 3.13.5;
- manual exclusions: zero.

The complete configured experiment was run twice. Both JSON outputs were byte-identical with SHA-256 `93f55d3c5e9cacf86aec7bbecdf351fc661f2f5ecbfdefb1f7e05c08482e56d2`.

The reproducible script is `experiments/span_v0_2_formal_screen.py`. The compact machine-readable record is `data/span_v0_2_formal.json`.

## Random pathology screen

All 10,000 games completed within the structural limit.

- first participant: 5,198 wins (51.98%);
- second participant: 4,802 wins (48.02%);
- Black: 5,260 wins;
- White: 4,740 wins;
- swap: 1,410 games (14.1%);
- connection: 8,201 games;
- immobilization: 1,799 games;
- median: 15 action plies;
- mean: 14.1916 action plies;
- maximum: 22 action plies;
- mean legal actions: 5.9328.

This passes termination and practical-duration checks. It is not balance evidence. The near-even participant result concealed a forced win, just as v0.1 random play concealed Black's five-ply forced line.

## Equal-budget depth-3 screen

The symmetric screen failed maximally.

- first participant: 0 wins;
- second participant: 1,000 wins;
- Black: 0 wins;
- White: 1,000 wins;
- swap: 0 games;
- connection: 1,000 games;
- every game ended on action ply 6 after six placements.

Only four openings were selected:

| First placement | Games | Second response | Winner |
|---|---:|---|---|
| B1 | 257 | B3 | second participant as White |
| B5 | 252 | B3 | second participant as White |
| D1 | 246 | D3 | second participant as White |
| D5 | 245 | D3 | second participant as White |

The first-participant decisive win rate is 0%, outside the precommitted 40–60% interval.

## Exhaustive opening diagnosis

The tournament result led to a bounded constructive check of every legal first placement. The regression test is `tests/test_span_v0_2_forced_second_participant.py`.

### Central openings: C2 and C4

The second participant swaps and takes Black. The opening participant, now White, cannot prevent the new Black owner from completing the already-proved v0.1 central line:

- after C2: swap, then C3 and C4;
- after C4: swap, then C3 and C2.

For each central opening, the test enumerates all six legal first White replies after swap and all 42 second-reply continuations after C3. Every continuation permits the finishing Black placement and gives the second participant the win.

### Outer openings: B1, B5, D1, and D5

The second participant does not swap and remains White.

- after B1 or B5: play B3, then C3, then D3;
- after D1 or D5: play D3, then C3, then B3.

For each outer opening, the test enumerates all seven legal Black replies after the first White placement and all 51 second Black-reply continuations after C3. Every continuation permits the finishing White placement and gives the second participant the win.

Therefore all six legal initial placements lose for the first participant. The defect is not a depth-3 heuristic artifact or a statistical imbalance. Span v0.2 has a constructive second-participant forced win.

## Interpretation

The swap rule did remove ownership of the v0.1 Black opening win from the first participant, but it did not balance the game. It exposed the dual defect:

- central Black openings are too valuable and are taken by swap;
- noncentral Black openings concede an immediate White horizontal connection race.

The balancing device prices the opening but cannot create a viable first move when every opening belongs strategically to the responder.

Random play again demonstrated why random parity is restricted to pathology screening. Its 51.98% first-participant result was not merely imprecise; it pointed in the opposite direction from the solved opening structure.

## Limitations

- The depth-3 tournament is not an independent proof of optimal play.
- The exhaustive test is deliberately narrow, but it covers every legal initial placement and every intervening first-participant response required by the stated forcing strategies.
- Fun, teachability, elegance, and human strategic experience remain untested.
- No prior-art review was performed because the design failed basic viability before any originality claim became relevant.
- The repository has no GitHub Actions workflow. The new exhaustive test passed in a local reconstruction; the previous 52-case full suite had already passed before this cycle, and no game or agent source changed during the formal screen.

## Decision

Reject frozen Span v0.2. Do not run strategic-signal tournaments, prior-art review, or an unplanned v0.3 repair inside Study 001.

All three selected prototypes and the one reasonable single-change revision have now failed decisive precommitted criteria. Study 001 should conclude negatively: the autonomous process produced compact, reproducible, falsifiable game designs and useful methodological evidence, but no surviving game that supports an honest claim of reasonable balance and meaningful strategic depth.
