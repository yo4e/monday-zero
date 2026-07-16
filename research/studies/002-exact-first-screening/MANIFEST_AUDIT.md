# Study 002 Manifest Freeze Audit

_Date: 2026-07-16 (Asia/Tokyo)_  
_Status: **Static manifest frozen before solver implementation or candidate play**_

## Scope

This audit records only deterministic candidate generation and static validation. It contains no state enumeration, exact result, heuristic result, play trace, win rate, candidate ranking by quality, or manual replacement.

## Frozen generator

- Seed: `2026071602`
- Board sizes: 3×3 and 4×4
- Families: adjacency growth, component expansion/merger, local blocking/pattern
- Cell order: 3×3 AG, 3×3 CE, 3×3 LB, 4×4 AG, 4×4 CE, 4×4 LB
- Selection per cell: first three distinct statically valid canonical tuples in ascending `(seeded SHA-256 rank, canonical JSON)` order
- Canonical encoding: compact UTF-8 JSON with frozen insertion order
- Manual ranking or replacement: none

Implementation:

- `src/templex_zero/exact_first/manifest.py`
- `experiments/generate_study_002_manifest.py`

## Static generation counts

| Board | Family | Raw | Canonical unique | Statically valid | Selected |
|---:|---|---:|---:|---:|---:|
| 3×3 | adjacency growth | 24 | 24 | 24 | 3 |
| 3×3 | component expansion | 24 | 24 | 24 | 3 |
| 3×3 | local blocking/pattern | 16 | 16 | 16 | 3 |
| 4×4 | adjacency growth | 24 | 24 | 24 | 3 |
| 4×4 | component expansion | 24 | 24 | 24 | 3 |
| 4×4 | local blocking/pattern | 16 | 16 | 16 | 3 |

The frozen grammar therefore passed its static failure condition: every cell produced at least three distinct valid candidates without changing the grammar or seed.

## Frozen output

The complete manifest is stored in:

- `research/studies/002-exact-first-screening/manifest/index.json`
- `research/studies/002-exact-first-screening/manifest/README.md`
- eighteen files named `<candidate-id>.json`

The compact full-entry list has SHA-256:

`cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

Candidate identifiers run from `S2-3-AG-01` through `S2-4-LB-03`, with exactly three entries in each frozen board-size × family cell.

Generated core-rule texts range from 83 to 142 whitespace-delimited words. Every selected entry:

- validates as a 3×3 or 4×4 full-board `GameSpec`;
- states intended symmetry;
- contains no fixture-only explicit opening or winning pattern;
- uses placement only;
- remains below the 250-word limit.

## Verification

The final locally reconstructed generator was run twice. The generated JSON, Markdown overview, index, and eighteen candidate files were byte-identical across runs.

The targeted manifest suite reported:

- `7 passed`

It checks:

- sufficient distinct tuples in every cell;
- exact seeded-rank formula;
- eighteen unique IDs and canonical tuples;
- exact three-per-cell distribution;
- schema, full-board, symmetry, and word-count boundaries;
- manifest self-hash consistency;
- byte-for-byte equality between committed files and regeneration;
- absence of outcome and play-result fields.

`python -m compileall -q src tests experiments` completed without error.

All 21 committed manifest files, the generator module, the regeneration script, and the final manifest test file were compared by Git blob SHA with the locally verified versions and matched exactly.

A fresh clone could not be obtained because the execution environment could not resolve `github.com`. An attempted combined rerun with earlier setup tests was discarded because the local reconstruction contained a reduced schema snapshot rather than the full live schema. Therefore this cycle claims only the seven final manifest tests, successful compilation, and remote-blob identity—not a fresh full-repository regression.

The repository has no recorded GitHub Actions workflow.

## Interpretation

The candidate family is now fixed independently of play results. This does not show that any candidate terminates well, is balanced, is interesting, or can be solved within the resource caps. It shows only that the frozen grammar can produce the required eighteen static, reproducible candidate descriptions without adaptive replacement.

## Next gate

The next cycle may implement the generic exact solver and an independently written brute-force fixture enumerator, then compare outcomes, distances, and opening-action values on the four frozen fixtures. It must not solve the eighteen candidates until that correctness gate passes.
