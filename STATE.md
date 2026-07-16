# State

_Last updated: 2026-07-16_

## Phase

**Study 002 active / candidate manifest frozen / cycle 2 of at most 6**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Study 001

Study 001 remains closed with a negative research conclusion. Its final synthesis is:

- `research/studies/001-autonomous-game-design/REPORT.md`

Do not alter it except to correct factual or technical errors. Do not create Span v0.3 or continue its candidate repair.

## Study 002 objective

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

Active protocol:

- `research/studies/002-exact-first-screening/PROTOCOL.md`

Frozen proposal source:

- `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`
- final proposal commit `68fc4c2edb93ca1363e7b7040221b5507cfeb171`

## Cycles completed

### Cycle 1 — setup

- Activated the frozen protocol.
- Implemented the declarative schema and fixture graph enumerator.
- Froze four audited fixtures, candidate grammar, seed `2026071602`, canonicalization, and seeded ordering.
- Did not generate candidates or implement the exact solver.

### Cycle 2 — manifest freeze

- Implemented deterministic normalized tuple generation, compact canonical JSON, seeded SHA-256 ranking, schema validation, and generated rule text.
- Generated exactly 18 candidates: 9 on 3×3, 9 on 4×4, and exactly three in every board-size × family cell.
- Saved an index, overview, and eighteen complete candidate JSON files under `research/studies/002-exact-first-screening/manifest/`.
- Full compact entry-list SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`.
- Rule texts range from 83 to 142 words; all entries passed schema, full-board, intended-symmetry, and 250-word validation.
- No solver, state result, random game, shallow game, exact outcome, or quality ranking was created or inspected.

## Verification

- Final targeted manifest suite: **7 passed**.
- `python -m compileall -q src tests experiments`: no errors.
- Repeated manifest generation was byte-identical.
- Git blob SHAs for the generator, script, test, index, overview, and all eighteen candidate files matched the locally verified files.
- Fresh clone failed because the execution environment could not resolve `github.com`.
- A combined setup-plus-manifest rerun was not accepted because the reconstruction used for that attempt did not contain the complete live schema; no combined result is claimed.
- The repository has no recorded GitHub Actions workflow.

## Frozen study boundaries

- The 18-entry manifest is immutable except for factual or technical correction.
- Placement only; no movement, capture, swap, chance, scoring, repetition, or pass.
- Exact caps remain 2,000,000 states and 30 seconds per candidate; 25,000,000 states total in manifest order.
- At least 12 exact solutions are required.
- Random screen remains 2,000 games per candidate.
- Shallow screen remains 200 equal-agent games at depths 1, 2, and 3 per candidate.
- Maximum six approval-driven cycles including final synthesis.
- No second grammar, candidate replacement, polishing, prior-art search, human playtest, paid compute, or external solver.

## Next actions

1. Implement a generic no-reduction memoized exact solver.
2. Implement an independently written brute-force fixture enumerator rather than sharing the memoized recursion.
3. Cross-check root outcome, outcome-preserving terminal distance, and every opening-action value on all four frozen fixtures.
4. Exhaustively verify the symmetry claims on Fixtures 1 and 2 only.
5. Add deterministic correctness and cap tests.
6. Do not solve any of the eighteen candidates in that cycle.

## Human action currently needed

None.
