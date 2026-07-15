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

**Span v0.2 participant-aware agent instrumentation.** Relay, Span v0.1, and Keystone v0.1 are rejected in their tested forms. Span v0.2 is the only selected revision and now has a reference implementation plus deterministic swap tests. No v0.2 play experiment has been run.

## Prototype outcomes

### Relay — rejected

Stronger symmetric play exposed a severe first-player advantage: 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 depth-2 games. Random parity had concealed the defect. A swap rule would not also address the unresolved long-game population, so Relay was not selected for a one-change revision.

### Span v0.1 — rejected

- [`prototypes/span/RULES.md`](prototypes/span/RULES.md) — frozen baseline
- [`prototypes/span/DECISION.md`](prototypes/span/DECISION.md) — disposition
- [`analysis/span_minimax_smoke_v0_1.md`](analysis/span_minimax_smoke_v0_1.md) — diagnosis

Black can force C2–C3–C4, or the reflected line, and connect its fixed anchors on ply 5. Exhaustive reply enumeration makes a larger v0.1 tournament unnecessary.

### Keystone v0.1 — rejected

- [`prototypes/keystone/ORIGIN.md`](prototypes/keystone/ORIGIN.md) — recovered candidate and ambiguity decisions
- [`prototypes/keystone/RULES.md`](prototypes/keystone/RULES.md) — frozen baseline
- [`prototypes/keystone/DECISION.md`](prototypes/keystone/DECISION.md) — disposition
- [`analysis/keystone_random_v0_1.md`](analysis/keystone_random_v0_1.md) — diagnosis and limitations

In 2,000 fixed-seed random games, only 50.9% completed by 200 plies; 49.1% hit the observation limit. Shifts were 88.13% of observed actions. Restricting movement or adding a new progress score would alter the reversible-control mechanism or add substantial bookkeeping, so Keystone was not selected for a one-change revision.

## Selected revision

### Span v0.2 — implemented, not yet empirically evaluated

- [`analysis/prototype_revision_selection.md`](analysis/prototype_revision_selection.md) — cross-prototype comparison and decision
- [`prototypes/span/RULES_v0_2.md`](prototypes/span/RULES_v0_2.md) — frozen v0.2 rules
- [`../../../src/templex_zero/games/span_v0_2.py`](../../../src/templex_zero/games/span_v0_2.py) — participant-aware reference implementation
- [`../../../tests/test_span_v0_2.py`](../../../tests/test_span_v0_2.py) — deterministic swap and regression tests
- [`analysis/span_v0_2_implementation.md`](analysis/span_v0_2_implementation.md) — implementation verification and limits

Span v0.2 changes exactly one rule: after the first Black placement, the second participant may either place White normally or swap sides. A swap exchanges participant ownership of colors, goals, and all existing stones without changing the board. It consumes the second participant's turn, after which the opening participant moves as White.

The revision preserves fixed anchors, expansion and merge legality, connection goals, immobilization loss, and finite placement. The v0.1 module and negative evidence remain unchanged. The reconstructed full suite produced **45 passed**: 31 existing cases plus 14 v0.2 cases. `compileall` completed without error.

This establishes implementation fidelity only. Balance, strategic signal, swap frequency, viable openings, and participant advantage remain unresolved.

## Next work

Adapt symmetric search and match instrumentation to participant identity. The same agent and computation budget must choose the first placement, the second participant's swap decision, and all later placements. Add deterministic agent and match tests before running the formal v0.2 screens.

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