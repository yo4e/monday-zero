# Study 001 Work Log

This chronological log was superseded for detailed implementation evidence on 2026-07-16 by dedicated analysis records. Earlier entries remain preserved in Git history.

## 2026-07-16 — Span v0.2 reference implementation

### Work completed

- Preserved the rejected Span v0.1 implementation and negative evidence unchanged.
- Added `src/templex_zero/games/span_v0_2.py` as a separate participant-aware implementation of the frozen single-change revision.
- Represented normal placement and the one-time opening swap as explicit actions.
- Tracked the participant to move, each participant's color, swap availability, elapsed turns, and placement count separately from the colored board.
- Reused the frozen v0.1 placement geometry, components, bounding rectangles, connection, and immobilization behavior rather than duplicating or silently altering them.
- Added `tests/test_span_v0_2.py` with fourteen deterministic cases across ten test functions.
- Reconstructed the live source and test tree locally and ran `PYTHONPATH=src python -m pytest -q`; **45 cases passed**, comprising 31 existing cases and 14 v0.2 cases.
- Ran `PYTHONPATH=src python -m compileall -q src tests`; compilation completed without error.
- Recorded implementation details and limitations in `analysis/span_v0_2_implementation.md`.

### Result

The tested implementation matches the frozen swap timing, board invariance, participant-color ownership exchange, post-swap turn order, one-time availability, participant winner mapping, and representative v0.1 placement rules. The board is not recolored during a swap, and the rejected v0.1 implementation remains available as its own historical object.

### Limitations

The tests are not an exhaustive proof. No participant-aware v0.2 agent or match harness exists, and no v0.2 game has been played. Passing rule tests is not evidence that swap fixes balance, preserves multiple viable openings, or adds strategic depth. No GitHub Actions workflow exists; verification used a local reconstruction of live GitHub files.

### Decision

Advance to participant-aware search and match instrumentation. The same symmetric agent and budget must choose the first placement, decide whether to swap, and choose every later placement. Do not run formal v0.2 experiments until deterministic instrumentation tests and the full regression suite pass.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. Implementation architecture, tests, verification, interpretation, and the next research decision were **A0**.

## Historical record

The complete pre-2026-07-16 chronological work log remains available in Git history at blob `66947a25b0cfc564325c326fb366a84891efc0b3`. Dedicated analysis, prototype disposition, data, STATE, and issue records remain the authoritative evidence for earlier cycles.