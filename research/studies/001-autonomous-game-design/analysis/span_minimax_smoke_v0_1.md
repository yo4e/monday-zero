# Span v0.1 Minimax Smoke Screen and Forced-Line Diagnosis

_Date: 2026-07-15 (Asia/Tokyo)_

## Question

Can a symmetric, deterministic search agent operate correctly on Span v0.1, and does a small equal-depth smoke screen expose an immediate balance failure before a larger experiment is justified?

## Instrumentation

The cycle added:

- `src/templex_zero/span_agents.py` — a Span-specific evaluation function and depth-limited minimax agent;
- `src/templex_zero/span_match.py` — a fixed-seed match harness;
- `tests/test_span_agents.py` — terminal scoring, transpose-and-color symmetry, immediate-win selection, legal move selection, seeded tie-breaking, match reproducibility, and invalid-call tests;
- `tests/test_span_forced_line.py` — exhaustive enumeration of the central forced line;
- `experiments/span_minimax_smoke.py` — the equal-depth smoke script.

The evaluation compares both seats using the same features: shortest orthogonal connection cost through friendly and empty cells, maximum connected span toward the assigned edges, legal-move count, and component count. Terminal scores dominate every heuristic score.

## Verification

A local reconstruction of the current source tree produced:

- `python -m pytest -q`: **20 passed**;
- `python -m compileall -q src tests experiments`: completed without error.

The evaluation is invariant under board transposition combined with color exchange. The agent selects only legal moves, detects an immediate connection win, and reproduces the same choice and match result for the same seed.

## Formal smoke run

- Script/code version: `285d1f575a2b8af498c23679f216419315340173`
- Agent: depth-2 minimax for both seats
- Games: 200
- Seeds: 0 through 199
- The configured run was repeated; aggregate output was identical.

| Measure | Result |
|---|---:|
| Black wins | 200 |
| White wins | 0 |
| Connection endings | 200 |
| Immobilization endings | 0 |
| Minimum plies | 5 |
| Median plies | 5 |
| Maximum plies | 5 |
| C2 openings | 107 |
| C4 openings | 93 |

Raw aggregate evidence is stored in `../data/span_minimax_smoke_v0_1.json`.

## Diagnostic follow-up

Because the smoke result was uniform, the same harness was run exploratorily at depths 1, 2, 3, and 4 for 100 seeds per depth. Every game at every depth ended in a Black connection on ply 5.

This cross-depth agreement is not by itself a proof: all depths use the same heuristic family. It does, however, show that the result is not a peculiar tie-break at depth 2.

## Forced-line proof by enumeration

The decisive evidence is independent of the heuristic.

After Black opens at C2:

1. White's first legal move cannot occupy C3.
2. Black can legally place C3 by expanding the C1–C2 component.
3. For every legal White second move, C4 remains empty and legal for Black.
4. Black places C4, merging the C1–C3 component with the fixed C5 anchor.
5. Black connects the top and bottom edges on ply 5.

`tests/test_span_forced_line.py` enumerates every legal White first and second reply and confirms this result. The C4–C3–C2 line is the vertically reflected equivalent.

This is a constructive forced win, not an estimate from sampled play.

## Interpretation

The search instrumentation passed its intended checks, but the game failed before a full balance experiment became necessary. Black can force a connection on its third move, and White cannot interact with the central route quickly enough under the frozen placement-support rule.

The earlier random screen concealed this defect because random Black frequently declined the central continuation. Its 52.6% Black result was therefore non-diagnostic exactly as the Relay experience warned.

## Decision

**Reject Span v0.1.**

Do not rewrite the frozen baseline. Any future rescue attempt must be a separately versioned design, but Study 001 should first evaluate the remaining shortlisted prototype, Keystone, rather than spending another cycle repairing the second failed candidate.

A larger Span balance tournament would add volume without changing the forced-line conclusion and is therefore cancelled.

## Limitations

- The proof establishes a Black forced win through one opening family; it does not solve every Span position.
- The evaluation function is a baseline instrument, not a validated model of human strategy.
- Fun, teachability, elegance, and originality remain untested, but these qualities cannot rescue a game with an immediate forced first-player win under the precommitted balance criterion.
