# Study 002 — Exact-First Screening of Compact Games

## Status

**Active. Exact candidate cycle 4 of at most 6 is complete.**

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
- [`EXACT_SCREEN_ANALYSIS.md`](EXACT_SCREEN_ANALYSIS.md) — candidate results, reproducibility correction, and procedural audit
- [`data/exact_screen_v1.json`](data/exact_screen_v1.json) — complete compact exact result
- [`manifest/README.md`](manifest/README.md) — frozen 18-entry overview
- [`manifest/index.json`](manifest/index.json) — machine-readable manifest index

Implementation:

- `src/templex_zero/exact_first/schema.py`
- `src/templex_zero/exact_first/manifest.py`
- `src/templex_zero/exact_first/solver.py`
- `src/templex_zero/exact_first/bruteforce.py`
- `experiments/run_study_002_exact_screen.py`
- `experiments/compare_study_002_exact_runs.py`

## Frozen sample

The manifest contains exactly 18 candidates:

- 9 on 3×3 boards and 9 on 4×4 boards;
- exactly three in every board-size × mechanism-family cell;
- no manual ranking, replacement, or result-dependent editing.

The compact full-entry list SHA-256 is:

`cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

## Exact-instrument gate

The no-reduction memoized solver and an independently written queue-built retrograde oracle agreed on all twelve reachable states of the four frozen fixtures, including every action value and the two retained color-role symmetry claims.

The correctness gate passed before candidate outcomes existed.

## Exact candidate result

The formal experiment was committed before candidate outcomes were inspected at commit `9a453ccc2a2e1f30691d23028b12b3296ebb4f13`.

| Measure | Result |
|---|---:|
| Candidates | 18 |
| Exactly solved | 15 |
| Time-capped | 3 |
| 3×3 solved | 9 / 9 |
| 4×4 solved | 6 / 9 |
| First-participant exact wins | 9 |
| First-participant exact losses | 6 |
| Exact draws | 0 |
| Solved within 2 optimal plies | 4 / 15 |
| Solved within 8 optimal plies | 14 / 15 |
| Zero non-losing openings | 6 / 15 |

The continuation threshold of twelve exact solutions passed. The degenerate-majority failure condition did not trigger.

The three time-capped candidates were `S2-4-CE-02`, `S2-4-LB-01`, and `S2-4-LB-03`.

## Reproducibility

Two configured runs agreed on every exact value, opening value, solved state count, solved/unsolved classification, and cap reason.

The original report projection incorrectly treated the number of states expanded before a wall-clock cap as deterministic. A separate committed comparator isolated that defect without changing any experiment condition. After excluding only timing-dependent fields, both runs produced:

`9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`

## Procedural limitation

The frozen proposal required a declarative-feature shallow-search heuristic to be generated **before exact results were inspected**. No heuristic was frozen in cycles 1–3, although the activation sequence placed exact solving before approximate screens.

Exact results have now been inspected. A new heuristic could not honestly satisfy the frozen requirement. Therefore:

- the formal depth-1/2/3 shallow screen is cancelled;
- no post-result heuristic will be represented as precommitted evidence;
- H2 will remain unresolved;
- Study 002 cannot receive a fully successful methodological disposition.

The preconfigured random screen remains valid because it requires no heuristic.

## Verification limitations

- Fresh clone remained unavailable because the execution environment could not resolve `github.com`.
- The exact execution used a functionally reconstructed local copy whose manifest hash and four fixture outputs matched live GitHub.
- Byte-identical identity of every reconstructed source file is not claimed.
- The repository has no recorded GitHub Actions workflow.

## Next bounded cycle

Commit and run the frozen random screen only: 2,000 fixed-seed games for each of all 18 candidates, recording participant results, duration, terminal reason, opening distribution, and branching. Repeat deterministic aggregates. Do not create or run a shallow heuristic. Reserve cycle 6 for exact-versus-random synthesis and closure as partial/incomplete.
