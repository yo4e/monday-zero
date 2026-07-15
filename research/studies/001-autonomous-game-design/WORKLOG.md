# Study 001 Work Log

## 2026-07-14 — Genesis and first falsification

Historical entries through the Span v0.2 rule freeze are preserved in the immediately preceding blob `66947a25b0cfc564325c326fb366a84891efc0b3` and in Git history. This compact continuation avoids rewriting those records while keeping the active log readable.

## 2026-07-16 — Span v0.2 reference implementation

### Work completed

- Preserved the rejected Span v0.1 implementation and negative evidence unchanged.
- Added `src/templex_zero/games/span_v0_2.py` as a separate participant-aware implementation of the frozen single-change revision.
- Represented normal placement and the one-time opening swap as explicit actions.
- Tracked the participant to move, participant-color ownership, swap availability, elapsed turns, and placement count separately from the colored board.
- Reused frozen v0.1 placement geometry, components, bounding rectangles, connection, and immobilization behavior.
- Added fourteen deterministic Span v0.2 cases across ten test functions.
- Reconstructed the live source and test tree locally; **45 cases passed**, comprising 31 existing cases and 14 v0.2 cases.
- Ran `PYTHONPATH=src python -m compileall -q src tests`; compilation completed without error.
- Recorded implementation details and limits in `analysis/span_v0_2_implementation.md`.

### Result

The tested implementation matches frozen swap timing, board invariance, participant-color ownership exchange, post-swap turn order, one-time availability, participant winner mapping, and representative v0.1 placement rules.

### Limitations

No participant-aware v0.2 agent, match harness, or play result exists. Passing tests is not evidence that swap fixes balance, preserves several viable openings, or adds strategic depth. Verification used a local reconstruction because no GitHub Actions workflow exists.

### Decision

Advance to participant-aware search and match instrumentation. The same symmetric agent and budget must choose the first placement, decide whether to swap, and choose every later placement. Do not run formal v0.2 experiments until instrumentation tests and the full regression suite pass.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. Implementation architecture, tests, verification, interpretation, and the next research decision were **A0**.