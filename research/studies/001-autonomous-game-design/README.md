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
- The design must not knowingly duplicate an existing game; claims remain qualified until a deliberate similarity search occurs.

## Current phase

**Initial prototype comparison / revision decision.** Relay, Span v0.1, and Keystone v0.1 have each received a first documented disposition and are rejected in their tested forms. Issue #3 compares the evidence and repair costs before any v0.2 rules are frozen.

## Prototype outcomes

### Relay — rejected

Stronger symmetric play exposed a severe first-player advantage: 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 depth-2 games. Random parity had concealed the defect.

### Span v0.1 — rejected

- [`prototypes/span/RULES.md`](prototypes/span/RULES.md) — frozen baseline
- [`prototypes/span/DECISION.md`](prototypes/span/DECISION.md) — disposition
- [`analysis/span_minimax_smoke_v0_1.md`](analysis/span_minimax_smoke_v0_1.md) — diagnosis

Black can force C2–C3–C4, or the reflected line, and connect its fixed anchors on ply 5. Exhaustive reply enumeration makes a larger tournament unnecessary.

### Keystone v0.1 — rejected

- [`prototypes/keystone/ORIGIN.md`](prototypes/keystone/ORIGIN.md) — recovered candidate and ambiguity decisions
- [`prototypes/keystone/RULES.md`](prototypes/keystone/RULES.md) — frozen baseline
- [`prototypes/keystone/DECISION.md`](prototypes/keystone/DECISION.md) — disposition
- [`../../../src/templex_zero/games/keystone.py`](../../../src/templex_zero/games/keystone.py) — reference implementation
- [`../../../tests/test_keystone.py`](../../../tests/test_keystone.py) — deterministic rule tests
- [`../../../experiments/keystone_random_screen.py`](../../../experiments/keystone_random_screen.py) — reproducible screen
- [`data/keystone_random_v0_1.json`](data/keystone_random_v0_1.json) — formal aggregate data
- [`analysis/keystone_random_v0_1.md`](analysis/keystone_random_v0_1.md) — diagnosis and limitations

The reconstructed full suite produced **31 passed** and compiled without error. In 2,000 fixed-seed random games, only 50.9% completed by 200 plies; 49.1% hit the observation limit. Shifts were 88.13% of observed actions. Keystone v0.1 therefore fails the precommitted termination threshold, and its stronger-agent screen is cancelled.

## Next decision

Issue #3 must compare the three failures using one table, estimate the smallest honest repair for each, and select at most one versioned revision—or conclude Study 001 negatively. No v0.1 baseline may be rewritten after results.

## Planned study files

- `PROTOCOL.md` — evaluation plan and thresholds
- `candidates/` — candidate mechanisms and rejection notes
- `prototypes/` — versioned rules and dispositions
- `src/templex_zero/` — game and agent implementations
- `experiments/` — reproducible runs
- `data/` — machine-readable results
- `analysis/` — interpretation and critique
- `RULES.md` — rules of a surviving design, if any
- `REPORT.md` — final research report
