# Study 002 — Exact-First Screening of Compact Games

## Status

**Active. Manifest cycle 2 of at most 6 is complete.**

Study 002 was activated on 2026-07-16 from the frozen proposal at commit `68fc4c2edb93ca1363e7b7040221b5507cfeb171`.

## Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

This is a methodological study, not a renewed attempt to rescue Span or to produce a publication-ready game.

## Frozen artifacts

- [`PROTOCOL.md`](PROTOCOL.md) — active commitments and stopping rules
- [`GRAMMAR.md`](GRAMMAR.md) — candidate grammar, seed, canonicalization, and enumeration order
- [`FIXTURES.md`](FIXTURES.md) — four hand-audited reachable state graphs
- [`MANIFEST_AUDIT.md`](MANIFEST_AUDIT.md) — static generation and verification record
- [`manifest/README.md`](manifest/README.md) — frozen 18-entry overview
- [`manifest/index.json`](manifest/index.json) — machine-readable manifest index
- `manifest/<candidate-id>.json` — complete canonical tuples, rule text, word counts, ranks, and validation records
- `src/templex_zero/exact_first/schema.py` — declarative game schema and deterministic state transitions
- `src/templex_zero/exact_first/fixtures.py` — machine-readable fixture specifications and graphs
- `src/templex_zero/exact_first/grammar.py` — frozen grammar constants
- `src/templex_zero/exact_first/manifest.py` — deterministic static manifest generator
- `experiments/generate_study_002_manifest.py` — regeneration entrypoint
- `tests/test_exact_first_schema.py`
- `tests/test_exact_first_fixtures.py`
- `tests/test_exact_first_manifest.py`

## Current result

The frozen grammar generated exactly 18 candidates without alteration or manual replacement:

- 9 on 3×3 boards and 9 on 4×4 boards;
- exactly three in every board-size × mechanism-family cell;
- unique canonical tuples selected solely by the frozen seeded SHA-256 order;
- generated rule texts between 83 and 142 words;
- all selected entries passed the frozen schema, full-board, symmetry, and 250-word boundaries.

The compact full-entry list has SHA-256:

`cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

The final manifest generator produced byte-identical files across repeated runs. The targeted manifest suite reported **7 passed**, `compileall` succeeded, and the Git blob SHA of every generated manifest file and implementation artifact matched the locally verified version.

No exact solver exists yet. No random, shallow, or exact candidate result has been observed. The manifest is a static experimental sample, not a quality ranking.

## Verification limitation

A fresh clone failed because the execution environment could not resolve `github.com`. A combined rerun with the previous setup suite was not accepted because that local reconstruction did not contain the complete live schema. The current cycle therefore claims only the seven final manifest tests, successful compilation, and exact remote-blob identity. The repository has no recorded GitHub Actions workflow.

## Next bounded cycle

Implement the generic memoized exact solver and a separately written brute-force fixture enumerator. Cross-check root outcome, distance, and every opening-action value on all four frozen fixtures, and verify the two claimed fixture symmetries. Do not solve any of the eighteen candidates until that correctness gate passes.
