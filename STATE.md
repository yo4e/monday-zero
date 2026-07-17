# State

_Last updated: 2026-07-17_

## Phase

**Study 002 active / exact candidate screen complete / cycle 4 of at most 6**

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

### Cycle 2 — manifest freeze

- Generated and froze exactly 18 candidates: 9 on 3×3, 9 on 4×4, exactly three per board-size × family cell.
- Full compact entry-list SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`.

### Cycle 3 — exact-instrument correctness gate

- Implemented a generic no-reduction memoized full-width solver.
- Implemented an independent queue-built, retrograde brute-force fixture oracle.
- Cross-checked all twelve reachable fixture states and every action value.
- Verified the retained symmetry claims and deterministic cap behavior.

### Cycle 4 — exact candidate screen

- Committed the formal experiment before inspecting candidate outcomes: `9a453ccc2a2e1f30691d23028b12b3296ebb4f13`.
- Solved candidates strictly in frozen manifest order under 2,000,000 states and 30 seconds per candidate and 25,000,000 states total.
- Exactly solved 15 of 18 candidates: all nine 3×3 entries and six of nine 4×4 entries.
- Three 4×4 candidates reached the time cap: `S2-4-CE-02`, `S2-4-LB-01`, and `S2-4-LB-03`.
- Exact roots among solved candidates: 9 first-participant wins, 6 first-participant losses, and no draws.
- Four solved candidates terminated within two plies; 14 of 15 terminated within eight plies.
- Six candidates had zero non-losing legal openings for the first participant.
- The exact continuation threshold passed and the degenerate-majority failure condition did not trigger.

Data and analysis:

- `research/studies/002-exact-first-screening/data/exact_screen_v1.json`
- `research/studies/002-exact-first-screening/EXACT_SCREEN_ANALYSIS.md`

## Reproducibility correction

Two configured exact runs agreed on all exact values, solved/unsolved classifications, opening values, solved state counts, and cap reasons.

The formal script's original deterministic projection incorrectly included expanded-state counts observed at a wall-clock time cap. Those counts varied slightly for the three time-capped candidates. A separately committed comparator isolated this within the same cycle and produced the same normalized hash for both runs:

`9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`

The correction did not alter rules, solver values, caps, or candidate classifications.

## Shallow-screen sequencing defect

The frozen proposal requires a declarative-feature heuristic to be generated before exact results are inspected. No heuristic was frozen in cycles 1–3, while the activation plan placed exact candidate solving before approximate screens.

Exact results have now been inspected. A newly created heuristic could not honestly satisfy the pre-result requirement. Therefore:

- the shallow depth-1/2/3 screen is cancelled as formal Study 002 evidence;
- no post-result heuristic will be presented as precommitted;
- H2 will remain unresolved;
- Study 002 cannot receive a fully successful methodological disposition.

The frozen random screen remains valid because it requires no heuristic and was specified before exact results.

## Verification

- Formal exact script was committed before outcome inspection.
- Manifest hash in the local reconstruction matched the frozen hash.
- Reconstructed schema and solver reproduced the four known fixture root and opening values.
- Two exact runs completed in approximately 119 seconds each.
- Corrected deterministic fields were identical across runs.
- Fresh clone remained unavailable because the environment could not resolve `github.com`.
- The exact execution used a functionally reconstructed local copy whose manifest hash and fixture outputs matched live GitHub; byte-identical identity of every reconstructed source file is not claimed.
- The repository has no recorded GitHub Actions workflow.

## Frozen study boundaries

- The 18-entry manifest remains immutable.
- Candidate and state caps remain unchanged.
- No second grammar, candidate replacement, symmetry rescue, polishing, prior-art search, human playtest, paid compute, or external solver.
- Maximum six approval-driven cycles including final synthesis.
- No shallow heuristic will be retroactively created for formal evidence.

## Next actions

1. Commit the random-screen script before running games.
2. Run exactly 2,000 fixed-seed random games for each of all 18 candidates.
3. Record participant results, duration, terminal reason, opening distribution, and branching.
4. Repeat and verify deterministic aggregate fields.
5. Do not run shallow search or consult exact values in move selection.
6. Compare random rates with exact values only after the random output is complete.
7. Reserve cycle 6 for synthesis and closure as partial/incomplete, with H2 unresolved.

## Human action currently needed

None.
