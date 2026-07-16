# Study 002 Work Log

## 2026-07-16 — Activation and pre-candidate setup (cycle 1 of at most 6)

### Work completed

- Re-read the frozen Study 002 proposal at commit `68fc4c2edb93ca1363e7b7040221b5507cfeb171` and activated it without changing its commitments.
- Created `PROTOCOL.md` with the frozen question, hypotheses, candidate counts, exact-analysis requirements, resource caps, comparison screens, success conditions, immediate failure conditions, out-of-scope claims, intervention model, and six-cycle limit.
- Froze generation seed `2026071602`.
- Froze the six board-size × mechanism-family cells and exactly three candidates per cell.
- Froze canonical tuple serialization and cross-version deterministic SHA-256 ranking rather than relying on Python PRNG ordering.
- Defined a declarative immutable placement-game schema supporting adjacency growth, component expansion/merger, local enemy limits, edge connection, lines, component size, and fixture-only explicit patterns.
- Added candidate validation boundaries for board size, full-board use, intended symmetry, fixture-only features, and rule-word count.
- Defined four hand-audited fixture state graphs: immediate component win, single-cell draw, branching role-specific patterns, and an adjacency chain.
- Added deterministic schema, mechanism, grammar-count, and fixture-graph tests.
- Preserved the cycle boundary: no 18-entry manifest, exact solver, random screen, shallow screen, or candidate outcome was created or inspected.

### Verification

- In a local reconstruction, `python -m pytest -q` reported **10 passed**.
- `python -m compileall -q src tests` completed without error.
- The Git blob SHA for each remote schema, fixture, grammar, and new test file matched the corresponding locally tested file exactly.
- A fresh clone attempt failed because the execution environment could not resolve `github.com`; the full legacy suite was not rerun.
- No GitHub Actions workflow was available as a remote CI substitute.

### Correction during final audit

The adjacency-chain graph was initially annotated as symmetric under transpose plus player/color exchange. Its L-shaped playable mask is not invariant under transpose, so that claim was false even though the graph itself was correct. Before solver implementation or candidate generation, the symmetry claim was removed in both code and fixture documentation. The targeted suite was rerun and remained at **10 passed**. Fixtures 1 and 2 retain explicit symmetry claims; Fixtures 3 and 4 are intentionally treated as asymmetric.

### Result

The frozen representation is precise enough to generate static candidates in a later cycle and the four fixture graphs are machine-checkable before solver implementation. This is representation evidence only. It does not validate an exact solver or any game candidate.

### Decision

Advance to one manifest-only cycle. Implement the frozen canonical serializer and SHA-256 enumerator, generate exactly three statically valid candidates in each cell, freeze the 18 entries and their generated rule text, and require byte-identical regeneration. Do not implement or run the exact solver in that cycle.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled this repository cycle. This is **A1** access assistance. Activation, schema design, fixture design, grammar parameters, seed, tests, interpretation, and the next task were autonomous **A0** work.
