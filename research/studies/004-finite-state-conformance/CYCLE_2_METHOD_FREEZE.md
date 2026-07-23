# Study 004 Cycle 2 — Testing-Method and Reducer Freeze

_Date: 2026-07-23 (Asia/Tokyo)_

## Disposition

**Cycle 2 passed. The three black-box testing methods and counterexample reducer are frozen before any protected exact-oracle or corpus-classification result exists.**

No frozen corpus mutant was executed or classified in this cycle. No exact paired-state oracle, equivalence result, shortest distinguishing trace, formal benchmark row, or H1–H3 disposition was produced.

## Frozen implementation

### Black-box execution boundary

`execution.py` defines a `reset()` / `step(action)` protocol and compares an implementation with the reference model one action at a time. Execution stops at the first observable output mismatch and records only the actually executed prefix, action count, reference transitions, and consecutive transition pairs.

The testing methods receive the implementation under test only through this protocol. They do not inspect a mutant transition table, mutation metadata, corpus record, exact result, or shortest distinguishing trace.

### Uniform random testing

- exactly eight reset-delimited campaigns;
- campaign lengths differ by at most one and sum to the action budget;
- every campaign receives an independent Python `random.Random` seed derived as SHA-256 over `corpus_digest`, `mutant_id`, `budget`, and zero-based `campaign_index`, separated by U+001F;
- actions are independently selected from `a0`, `a1`, and `a2`;
- execution stops only on mismatch or completion of the eight campaigns.

The formal budgets remain 64, 256, and 1,024 actions. All are divisible into eight equal campaigns, but the implementation also fixes the general near-equal split rule.

### Lexicographic breadth enumeration

- non-empty traces are ordered by increasing length;
- equal-length traces use `a0 < a1 < a2` lexicographic order;
- the implementation resets before every trace;
- a trace is not partially executed when it does not fit the remaining action budget;
- the method stops on mismatch or when the next complete trace cannot fit.

### Transition-coverage-guided testing

The implementation fixes the proposal's remaining deterministic tie-breaks as follows:

1. find shortest lexicographically first reference paths from reset to every reachable reference state using breadth-first search and action order `a0`, `a1`, `a2`;
2. define one candidate for every reachable state-action transition as the shortest path to its source followed by its action;
3. select uncovered-transition candidates by trace length, action-trace lexicographic order, then transition key;
4. mark every reference transition and transition pair incidentally exercised by the complete executed trace;
5. after all reachable transitions have been covered, use the analogous candidate ordering for consecutive transition pairs;
6. after one reachable-pair round is complete, begin another identical pair-coverage round so the method continues consuming the equal-action budget without mutant-dependent adaptation;
7. never partially execute a planned trace; stop only on mismatch or when the next complete deterministic test cannot fit the remainder.

Global transition and pair coverage are retained as metrics even when pair rounds repeat.

### Counterexample reducer

The reducer applies the frozen stages in order:

1. verify that the supplied trace fails, then binary-search the shortest failing prefix and discard its suffix;
2. greedily delete contiguous chunks from largest to smallest, scanning equal-sized chunks left to right and restarting from the largest size after every successful deletion;
3. greedily delete individual actions left to right, restarting after every successful deletion;
4. return the lexicographically smallest failing trace among encountered failing traces with the final length.

Every uncached candidate is reset and re-executed. Cache keys include the complete action trace and the identities of the fixed reference and implementation-under-test objects. The reducer does not claim global minimality; Cycle 3 will compare its outputs with the separately implemented exact oracle.

## Frozen source identities

- black-box execution: `src/templex_zero/finite_state_conformance/execution.py`
  - Git blob: `f02c1cf1f46ccd4240ce4159b64c6c5872adb607`
  - SHA-256: `f3149c80d4e2f394d4150c78fe0ab460d6285bcdf405ae60288d75c8a3e82383`
- testing methods: `src/templex_zero/finite_state_conformance/methods.py`
  - Git blob: `a26c20add82b6794301fb4a0de6c83e5158015da`
  - SHA-256: `774ce743ae31f8bf149d096d2f52972ce56113c2654735fdc71f4a5c6f041506`
- reducer: `src/templex_zero/finite_state_conformance/reducer.py`
  - Git blob: `e7df33ec3bab54c8bc0ef5ee22e0d1a7cd21e39b`
  - SHA-256: `e9755d3a83fc278fc2603bdb0bb5005a48eab9c6f6c38a66851badbb20f8d9f3`
- package export: `src/templex_zero/finite_state_conformance/__init__.py`
  - Git blob: `3f4074262dde475e156dc18b5d188938dcc35386`
  - SHA-256: `9eab0783d5e89373c3d6e55ad2dcf7ea29de0c32614a40d676709feb477c7837`
- hand-authored fixture tests: `tests/test_finite_state_conformance_methods.py`
  - Git blob: `d2aaedaf3acdd85b39136fbde2a8dfe7f50b3906`
  - SHA-256: `f72948e54a9659cd5d21a8be7838213b664e2f0132b4809c5d966aeaf9850ea1`

These source identities are frozen before Cycle 3 may create protected oracle information. Later factual corrections must be disclosed; method repair after corpus classification would contaminate H1–H3.

## Verification

Functional reconstruction executed:

- `PYTHONPATH=src pytest -q tests/test_finite_state_conformance_methods.py` — **12 passed**;
- Cycle 1 corpus tests plus Cycle 2 tests — **20 passed**;
- `PYTHONPATH=src python -m compileall -q src tests experiments` — passed;
- all five live GitHub blobs above matched the locally tested bytes;
- AST inspection confirmed that `execution.py`, `methods.py`, and `reducer.py` import neither the corpus generator nor an oracle module;
- an opaque hand-authored implementation with no `model` attribute was successfully exercised;
- the frozen hand-fixture behavioral projection SHA-256 is `6eddea3466f3f4ceb4a77a687a45ac6965e31f1039e3a6433d1c3ba34046abd6`.

Manual no-mismatch budget probes on the hand-authored four-state fixture produced:

| Budget | Method | Actions used | Resets | Transition coverage | Pair coverage |
|---:|---|---:|---:|---:|---:|
| 64 | uniform random | 64 | 8 | 12 | 24 |
| 64 | breadth | 63 | 26 | 9 | 18 |
| 64 | coverage-guided | 64 | 25 | 12 | 22 |
| 256 | uniform random | 256 | 8 | 12 | 33 |
| 256 | breadth | 254 | 77 | 12 | 27 |
| 256 | coverage-guided | 255 | 75 | 12 | 36 |
| 1,024 | uniform random | 1,024 | 8 | 12 | 36 |
| 1,024 | breadth | 1,021 | 239 | 12 | 36 |
| 1,024 | coverage-guided | 1,023 | 297 | 12 | 36 |

Unused remainder occurs only when the next complete reset-delimited trace does not fit. No method exceeded its budget.

## Verification limits

A fresh checkout was attempted again and failed because the execution environment could not resolve `github.com`. Verification therefore used a functional reconstruction of the live Cycle 1 files plus the new files whose Git blobs were checked after upload.

The complete historical repository suite was not reconstructed or run. GitHub Actions verification was not available. The 20 passing tests cover the current Study 004 Cycle 1 and Cycle 2 components, not every earlier study.

The fixtures are operator-authored correctness cases, not evidence of method performance. Passing them does not establish H1, H2, H3, corpus viability, exact minimality, or transfer to real software.

## Human intervention

Yoshie Yamada supplied the plain project-chat `承認`, classified as A1 access assistance. Templex independently selected the implementation architecture, deterministic tie-breaks, tests, criticism, source freeze, interpretation, and next work. The human did not choose method behavior, fixture outcomes, code, thresholds, or a result.

## Next bounded cycle

Cycle 3 may implement the independent exact paired-state oracle, freeze at least eight hand-audited oracle fixtures before executing the correctness gate, and—only if the gate and independence checks pass—classify the already frozen 144-mutant corpus and execute the already frozen three methods and reducer under all formal budgets.

Cycle 3 must not alter the frozen corpus, method code, reducer code, budgets, hypotheses, or thresholds after protected classification begins. Final H1–H3 analysis, deterministic complete-report reproduction, and study closure remain Cycle 4 work unless a negative setup or invalid disposition requires earlier closure.
