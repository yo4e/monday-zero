# Study 001 — Autonomous Game Design

## Research question

Can Templex Tsukino independently design a compact, deterministic, two-player abstract strategy game whose rules are teachable in under three minutes and whose automated play provides evidence of nontrivial strategy and reasonable balance?

This is the same study selected under the earlier internal name Monday. The public identity change does not alter the protocol, thresholds, or prior results.

## Intended artifact

A complete game package containing:

- concise rules;
- a reference implementation;
- command-line play;
- reproducible simulation and evaluation tools;
- baseline agents of differing strength;
- experiment data and analysis;
- a record of rejected prototypes and revisions;
- later, if justified, a small browser interface.

## Constraints

- Two players.
- Deterministic and perfect information.
- No dependence on proprietary assets or external services.
- Core rules should fit within 400 words.
- A physical version should require at most a small board and a modest set of generic pieces, or be playable with pencil and paper.
- The design must not knowingly duplicate an existing game; claims will remain qualified until a deliberate similarity search occurs.

## Current phase

**Prototype comparison / Keystone implementation.** Relay and Span v0.1 have both been rejected in their tested forms. Keystone v0.1 was recovered, ambiguity-resolved, and frozen before implementation or play results on 2026-07-15.

## Prototype outcomes

### Relay — rejected

Stronger symmetric play exposed a severe first-player advantage: 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 depth-2 games.

### Span v0.1 — rejected

- [`prototypes/span/RULES.md`](prototypes/span/RULES.md) — frozen baseline
- [`prototypes/span/DECISION.md`](prototypes/span/DECISION.md) — disposition
- [`../../../src/templex_zero/games/span.py`](../../../src/templex_zero/games/span.py) — reference implementation
- [`../../../tests/test_span_forced_line.py`](../../../tests/test_span_forced_line.py) — exhaustive five-ply forced-line evidence
- [`analysis/span_minimax_smoke_v0_1.md`](analysis/span_minimax_smoke_v0_1.md) — diagnosis and limitations

Black can force C2–C3–C4, or the reflected C4–C3–C2 line, to connect the fixed C1 and C5 anchors on ply 5. The frozen rules remain preserved rather than repaired after the result.

### Keystone v0.1 — active

- [`prototypes/keystone/ORIGIN.md`](prototypes/keystone/ORIGIN.md) — recovered candidate, ambiguities, and pre-result decisions
- [`prototypes/keystone/RULES.md`](prototypes/keystone/RULES.md) — frozen v0.1 baseline
- Issue #2 — implementation and evaluation work

The baseline uses an empty 5×5 board, eight stones per player, placement or one-step orthogonal shifting, mandatory single custodian capture, and a victory component containing C3 plus separate contacts with two different edges. Threefold repetition is a draw. The baseline has no swap rule.

## Planned study files

- `PROTOCOL.md` — evaluation plan and thresholds
- `candidates/` — candidate mechanisms and rejection notes
- `prototypes/` — versioned rules for implemented candidates
- `src/templex_zero/` — game and agent implementations
- `experiments/` — reproducible runs and data
- `analysis/` — interpretation and critique
- `RULES.md` — rules of the surviving design
- `REPORT.md` — final research report