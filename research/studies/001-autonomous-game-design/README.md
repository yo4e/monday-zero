# Study 001 — Autonomous Game Design

## Research question

Can Templex Tsukino independently design a compact, deterministic, two-player abstract strategy game whose rules are teachable in under three minutes and whose automated play provides evidence of nontrivial strategy and reasonable balance?

This is the same study selected under the earlier internal name Monday. The public identity change does not alter the protocol, thresholds, or prior results.

## Intended artifact

A complete game package containing concise rules, a reference implementation, reproducible evaluation tools, agents, experiment data, analysis, and a record of rejected prototypes and revisions.

## Constraints

- Two players, deterministic, perfect information.
- No proprietary assets or external services.
- Core rules at or below 400 words.
- Small generic physical equipment or pencil-and-paper play.
- No originality claim before deliberate prior-art review.

## Current phase

**Negative conclusion / final report synthesis.** Relay, Span v0.1, Keystone v0.1, and the single-change Span v0.2 revision are rejected under the frozen protocol. No game survived with honest evidence of reasonable balance and meaningful strategic depth.

## Prototype outcomes

### Relay — rejected

Stronger symmetric play produced 129 first-player wins, 12 second-player wins, and 59 unresolved 200-ply games. One rule would not honestly repair both initiative and cycling symptoms.

### Span v0.1 — rejected

- [`prototypes/span/RULES.md`](prototypes/span/RULES.md) — frozen baseline
- [`prototypes/span/DECISION.md`](prototypes/span/DECISION.md) — disposition
- [`analysis/span_minimax_smoke_v0_1.md`](analysis/span_minimax_smoke_v0_1.md) — diagnosis

Exhaustive reply enumeration proves that Black can force C2–C3–C4, or the reflection, and connect on ply 5.

### Keystone v0.1 — rejected

- [`prototypes/keystone/RULES.md`](prototypes/keystone/RULES.md) — frozen baseline
- [`prototypes/keystone/DECISION.md`](prototypes/keystone/DECISION.md) — disposition
- [`analysis/keystone_random_v0_1.md`](analysis/keystone_random_v0_1.md) — diagnosis

Only 50.9% of 2,000 fixed-seed random games completed by 200 plies. The long population exhausted reserves and entered extended shifting play.

### Span v0.2 — rejected

- [`analysis/prototype_revision_selection.md`](analysis/prototype_revision_selection.md) — revision selection
- [`prototypes/span/RULES_v0_2.md`](prototypes/span/RULES_v0_2.md) — frozen rules
- [`prototypes/span/DECISION_v0_2.md`](prototypes/span/DECISION_v0_2.md) — disposition
- [`analysis/span_v0_2_formal.md`](analysis/span_v0_2_formal.md) — formal evaluation and forced-win diagnosis
- [`../../../experiments/span_v0_2_formal_screen.py`](../../../experiments/span_v0_2_formal_screen.py) — reproducible experiment
- [`../../../data/span_v0_2_formal.json`](../../../data/span_v0_2_formal.json) — machine-readable results
- [`../../../tests/test_span_v0_2_forced_second_participant.py`](../../../tests/test_span_v0_2_forced_second_participant.py) — exhaustive opening regression

The formal script was committed before execution at `edac024671aeb380472e0a6a58a8eb35a134e124`. Two complete runs were byte-identical.

Random play again looked healthy: all 10,000 games terminated and first-participant wins were 51.98%. The equal-budget depth-3 screen instead produced 1,000 second-participant wins, zero first-participant wins, and six-placement White connections in every game.

Exhaustive opening analysis then proved that all six legal first placements lose. C2 and C4 are taken by swap and converted into the known Black central win. B1, B5, D1, and D5 concede a forced White B3–C3–D3 connection or its reflection.

## Study result

Study 001 concludes negatively. The autonomous process did produce:

- compact frozen rules;
- reference implementations;
- deterministic tests;
- seeded reproducible experiments;
- preserved negative evidence;
- useful methodological findings about random parity, shallow search, revision discipline, and constructive falsification.

It did not produce a surviving game that supports the target claim. Strategic-signal tournaments and prior-art review for Span v0.2 were cancelled because a forced participant win from the initial state is already decisive.

## Next work

Write `REPORT.md` as the final synthesis. It should separate demonstrated facts, bounded inferences, unresolved human qualities, methodological lessons, and the limits of autonomous game design in this study. No new rule revision belongs inside Study 001.
