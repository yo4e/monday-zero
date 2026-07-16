# State

_Last updated: 2026-07-17_

## Phase

**Study 002 active / exact instrument validated / cycle 3 of at most 6**

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

- Generated and froze exactly 18 candidates: 9 on 3×3, 9 on 4×4, exactly three per board-size × family cell.
- Full compact entry-list SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`.
- No candidate result was inspected.

### Cycle 3 — exact-instrument correctness gate

- Implemented a generic no-reduction memoized full-width solver.
- Implemented an independent queue-built, retrograde brute-force fixture oracle.
- Fixed the value convention: player-to-move perspective; win shortest, loss longest, draw shortest among outcome-preserving actions.
- Cross-checked outcome, distance, and every legal action value on all twelve reachable states of the four frozen fixtures.
- Verified the retained color-role symmetry claims on Fixtures 1 and 2 only.
- Added deterministic state-cap and controlled-clock time-cap tests.
- Did **not** solve, enumerate, play, or assign an outcome to any frozen candidate.

## Correctness-gate result

Fixture roots:

- immediate component win: win in 1; 2 states;
- single-cell draw: draw in 1; 2 states;
- branching pattern: win in 1; 4 states; A1 wins in 1 and B1 loses in 2;
- adjacency chain: win in 3; 4 states.

The memoized and retrograde instruments agreed on all twelve states and all action values. The instrument-disagreement failure condition did not trigger.

Audit:

- `research/studies/002-exact-first-screening/EXACT_INSTRUMENT_AUDIT.md`

## Verification

- Final solver suite: **8 passed**.
- Setup, fixture, and solver tests together: **18 passed**.
- `python -m compileall -q src tests`: no errors.
- Git blob SHAs for the solver, brute-force oracle, package export, and final test matched the locally executed files.
- The prior manifest suite remains separately recorded at 7 passed; it was not rerun in this reconstruction because the twenty-one manifest files were not recreated locally.
- Fresh clone failed because the execution environment could not resolve `github.com`.
- The repository has no recorded GitHub Actions workflow.

## Frozen study boundaries

- The 18-entry manifest is immutable except for factual or technical correction.
- Placement only; no movement, capture, swap, chance, scoring, repetition, or pass.
- Exact caps remain 2,000,000 expanded states and 30 seconds per candidate; 25,000,000 states total in manifest order.
- At least 12 exact solutions are required.
- Random screen remains 2,000 games per candidate.
- Shallow screen remains 200 equal-agent games at depths 1, 2, and 3 per candidate.
- Maximum six approval-driven cycles including final synthesis.
- No symmetry reduction is required; no second grammar, candidate replacement, polishing, prior-art search, human playtest, paid compute, or external solver.

## Next actions

1. Commit a deterministic exact-candidate experiment before inspecting results.
2. Load candidates strictly from the frozen manifest in manifest order.
3. Solve with the validated no-reduction solver under 2,000,000 states and 30 seconds per candidate and 25,000,000 states total.
4. Record root outcome, distance, all opening values, value counts, non-losing opening proportion, state count, elapsed time, and cap reason.
5. Record all later entries as unsolved if the total state cap is reached.
6. Repeat the configured run and compare deterministic fields; treat measured timing separately.
7. Do not change candidates, caps, or value conventions.
8. Do not run random or shallow screens in that cycle.

## Human action currently needed

None.
