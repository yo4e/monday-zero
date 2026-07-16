# Study 002 — Exact-First Screening of Compact Games

## Status

**Active. Exact-instrument cycle 3 of at most 6 is complete.**

Study 002 was activated on 2026-07-16 from the frozen proposal at commit `68fc4c2edb93ca1363e7b7040221b5507cfeb171`.

## Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

This is a methodological study, not a renewed attempt to rescue Span or to produce a publication-ready game.

## Frozen artifacts

- [`PROTOCOL.md`](PROTOCOL.md) — active commitments and stopping rules
- [`GRAMMAR.md`](GRAMMAR.md) — candidate grammar, seed, canonicalization, and enumeration order
- [`FIXTURES.md`](FIXTURES.md) — four hand-audited reachable state graphs
- [`MANIFEST_AUDIT.md`](MANIFEST_AUDIT.md) — static generation and verification record
- [`EXACT_INSTRUMENT_AUDIT.md`](EXACT_INSTRUMENT_AUDIT.md) — solver correctness-gate record
- [`manifest/README.md`](manifest/README.md) — frozen 18-entry overview
- [`manifest/index.json`](manifest/index.json) — machine-readable manifest index
- `manifest/<candidate-id>.json` — complete canonical tuples, rule text, word counts, ranks, and validation records
- `src/templex_zero/exact_first/schema.py` — declarative game schema and deterministic state transitions
- `src/templex_zero/exact_first/fixtures.py` — machine-readable fixture specifications and graphs
- `src/templex_zero/exact_first/grammar.py` — frozen grammar constants
- `src/templex_zero/exact_first/manifest.py` — deterministic static manifest generator
- `src/templex_zero/exact_first/solver.py` — no-reduction memoized exact solver
- `src/templex_zero/exact_first/bruteforce.py` — independent fixture graph and retrograde oracle
- `experiments/generate_study_002_manifest.py` — manifest regeneration entrypoint
- `tests/test_exact_first_schema.py`
- `tests/test_exact_first_fixtures.py`
- `tests/test_exact_first_manifest.py`
- `tests/test_exact_first_solver.py`

## Frozen sample

The frozen grammar generated exactly 18 candidates without alteration or manual replacement:

- 9 on 3×3 boards and 9 on 4×4 boards;
- exactly three in every board-size × mechanism-family cell;
- unique canonical tuples selected solely by the frozen seeded SHA-256 order;
- generated rule texts between 83 and 142 words;
- all selected entries passed the frozen schema, full-board, symmetry, and 250-word boundaries.

The compact full-entry list has SHA-256:

`cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

The manifest is a static experimental sample, not a quality ranking.

## Exact-instrument result

The no-reduction memoized solver and an independently written queue-built retrograde oracle agreed on all twelve reachable states of the four frozen fixtures.

| Fixture | States | Root value | Opening values |
|---|---:|---|---|
| immediate component win | 2 | win in 1 | A1: win in 1 |
| single-cell draw | 2 | draw in 1 | A1: draw in 1 |
| branching pattern | 4 | win in 1 | A1: win in 1; B1: loss in 2 |
| adjacency chain | 4 | win in 3 | A1: win in 3 |

The instruments matched on every state outcome, terminal distance, legal action value, and state count. Fixtures 1 and 2 also passed their retained color-role symmetry checks. Deterministic state-cap and controlled-clock time-cap behavior passed.

The correctness gate therefore passed before candidate outcomes existed.

## Verification

- final solver suite: **8 passed**;
- setup, fixture, and solver tests together: **18 passed**;
- `compileall`: passed;
- Git blob SHAs of the final solver, oracle, package export, and solver test matched the locally executed files.

The previous manifest suite remains separately recorded at **7 passed** and byte-identical regeneration. It was not rerun in this local reconstruction because the twenty-one committed manifest files were not recreated.

A fresh clone failed because the execution environment could not resolve `github.com`. The repository has no recorded GitHub Actions workflow.

## Current limitation

No frozen candidate has yet been solved, enumerated, played, or assigned an exact result. Passing tiny fixtures establishes an instrument correctness gate, not general proof that the solver is defect-free on larger games or that any candidate is balanced, deep, interesting, or original.

## Next bounded cycle

Commit and run an exact-candidate experiment using the validated no-reduction solver. Process the eighteen candidates strictly in frozen manifest order under 2,000,000 states and 30 seconds per candidate and 25,000,000 states total. Record capped entries as unsolved and repeat deterministic fields. Do not run random or shallow screens in that same cycle.
