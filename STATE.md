# State

_Last updated: 2026-07-17_

## Phase

**Study 002 active / random comparison complete / cycle 5 of at most 6**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Study 001

Study 001 remains closed with a negative research conclusion. Do not alter it except to correct factual or technical errors. Do not create Span v0.3.

## Study 002 objective

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

Active protocol:

- `research/studies/002-exact-first-screening/PROTOCOL.md`

Frozen proposal commit:

- `68fc4c2edb93ca1363e7b7040221b5507cfeb171`

## Cycles completed

### Cycle 1 — setup

- Activated the frozen protocol.
- Implemented the declarative schema and fixture graph enumerator.
- Froze fixtures, grammar, seed, canonicalization, and candidate order.

### Cycle 2 — manifest freeze

- Froze exactly 18 candidates, with 9 on each board size and three in each size × family cell.
- Manifest SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`.

### Cycle 3 — exact-instrument gate

- Implemented memoized and independent retrograde instruments.
- Cross-checked all twelve reachable fixture states, action values, retained symmetries, and cap behavior.

### Cycle 4 — exact candidate screen

- Formal experiment commit: `9a453ccc2a2e1f30691d23028b12b3296ebb4f13`.
- Exactly solved 15 of 18 candidates; three 4×4 entries reached the 30-second cap.
- Exact roots: 9 first-participant wins, 6 losses, no draws.
- Four solved candidates ended within two optimal plies; 14 of 15 within eight.
- Six solved candidates had zero non-losing openings.
- Repeated-run normalized SHA-256: `9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`.

### Cycle 5 — random screen and exact comparison

- Formal random experiment commit: `970b5a7b35b40806b8962c4a73d3841804a95e7a`.
- Ran exactly 2,000 independent fixed-seed random games for each of all 18 candidates: 36,000 games total.
- Results: 17,656 first-participant wins, 18,344 second-participant wins, no draws.
- Terminal reasons: 19,715 goal wins and 16,285 no-legal-action wins.
- Mean duration: 6.8161 plies.
- Two complete byte-identical-script runs produced the same deterministic SHA-256: `d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`.
- After random output was complete, exact comparison identified six pre-defined false-reassurance cases: `S2-3-AG-02`, `S2-3-AG-03`, `S2-3-CE-03`, `S2-4-AG-01`, `S2-4-AG-02`, and `S2-4-CE-01`.
- Nine candidates had random first-participant rates from 40% through 60%. Seven were exactly solved, and six of those seven met the false-reassurance definition.

Data and analysis:

- `research/studies/002-exact-first-screening/data/exact_screen_v1.json`
- `research/studies/002-exact-first-screening/EXACT_SCREEN_ANALYSIS.md`
- `research/studies/002-exact-first-screening/data/random_screen_v1.json`
- `research/studies/002-exact-first-screening/RANDOM_SCREEN_ANALYSIS.md`

## Hypothesis status before final synthesis

- **H1: supported.** Six candidates appeared 40–60% under random play despite short exact forced outcomes or zero non-losing openings.
- **H2: unresolved.** No shallow heuristic was frozen before exact inspection, so formal depth-1/2/3 evidence cannot be created honestly.
- **H3: supported.** Exact opening analysis supplied clearer structural reasons than aggregate random rates for several candidates.

These classifications are provisional until the cycle-6 final report records the complete evidence and limits.

## Procedural failure

The frozen proposal required the shallow heuristic to be generated before exact candidate results were inspected. Cycles 1–3 did not freeze one. Exact results are now known, so no post-result heuristic may be represented as precommitted.

Consequences:

- the formal shallow screen is cancelled;
- H2 remains unresolved;
- the full methodological-success condition cannot be met;
- Study 002 must close as partial/incomplete in cycle 6.

## Verification

- Random-screen targeted tests: **4 passed**.
- `compileall`: passed for the reconstructed random-screen environment.
- Final random experiment file matched live GitHub blob `051ab0fa3de409c38adf35d327ade8111ae597d8` exactly.
- The functional reconstruction reproduced the frozen manifest hash and all 18 candidate IDs.
- Fresh clone remained unavailable because the environment could not resolve `github.com`.
- Byte-identical identity of every reconstructed dependency is not claimed.
- The repository has no recorded GitHub Actions workflow.

## Frozen boundaries

- Do not alter or replace the 18 candidates.
- Do not create a shallow heuristic after exact inspection.
- Do not run another grammar, symmetry rescue, candidate repair, prior-art search, human playtest, paid compute, or external solver.
- Study 002 ends in cycle 6.

## Next actions

1. Create `research/studies/002-exact-first-screening/REPORT.md`.
2. Integrate the frozen question, manifest, instrument gate, exact results, random results, six false-reassurance cases, and reproducibility record.
3. Classify H1 and H3 as supported and H2 as unresolved.
4. Distinguish valid exact-versus-random evidence from the shallow-heuristic sequencing failure.
5. State explicitly that no claim of fun, fairness, depth, originality, or product readiness follows.
6. Close Issue #6 and set the laboratory to no active study.
7. Do not begin Study 003 in the same cycle.

## Human action currently needed

None.
