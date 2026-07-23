# Study 004 Protocol — Finite-State Conformance Counterexamples

_Date activated: 2026-07-22 (Asia/Tokyo)_  
_Date closed: 2026-07-23 (Asia/Tokyo)_  
_Status: **Closed — partial result**_

## 1. Activation record

Study 004 was activated **GO unchanged** from the frozen proposal:

- proposal: `research/proposals/STUDY_004_FINITE_STATE_CONFORMANCE.md`
- frozen proposal Git blob: `0b16048ad8e96dcaf147f033205ad76069430776`
- portfolio decision: `research/decisions/2026-07-21-post-study-003-portfolio-assessment.md`

The proposal was incorporated into this protocol without changing its research question, hypotheses, seed, model inventory, mutation operators, budgets, method semantics, reducer semantics, oracle role, disposition rules, or four-cycle limit. Implementation paths, type conventions, canonical serialization, and bounded resource details were clarified without changing the frozen experiment.

## 2. Research question

> Can a model-guided black-box testing method detect observable divergences between small deterministic finite-state specifications and mutated implementations more effectively than equal-budget uniform random testing, while reducing detected failures to exact shortest counterexamples under an independent oracle?

The study uses deterministic total Mealy machines and a frozen synthetic mutation corpus. It does not claim production verification, real-world vulnerability discovery, general software correctness, or method novelty.

## 3. Frozen hypotheses

- **H1 — detection advantage:** at 256 executed actions per mutant, transition-coverage-guided testing detects at least 10 percentage points more distinguishable mutants than uniform random testing.
- **H2 — breadth robustness:** at 1,024 actions, transition-coverage guidance detects at least as many distinguishable mutants as lexicographic breadth enumeration and trails it by no more than 10 percentage points in any mutation class.
- **H3 — counterexample reduction:** for at least 90% of mutants detected by any frozen method, the reducer returns a still-failing trace whose length equals the independent oracle's exact shortest distinguishing length.

Equivalent mutants remain in the corpus and are excluded only from formal detection-rate denominators. Unsupported hypotheses are permitted outcomes.

## 4. Frozen domain and corpus

### Reference models

- deterministic total Mealy machines;
- reset state `0`;
- state counts `4` and `8`;
- actions `a0`, `a1`, `a2`;
- outputs `o0`, `o1`, `o2`;
- topology families `reset-chain`, `clustered`, and `cyclic`;
- four variants in each state-size × family cell;
- exactly **24 reference models**;
- generation seed **2026072104**.

Cycle 1 implementation clarified family membership as follows:

- `reset-chain`: `a0` returns every state to reset; `a1` advances each nonterminal state to its successor;
- `clustered`: the state space is split into equal halves and contains exactly two cross-cluster transitions, one originating in each cluster;
- `cyclic`: `a0` forms one cycle covering all states.

Outputs and non-protected target choices are SHA-256-derived from the frozen seed, family, state count, variant, state, and action. Model order is state count, family order above, then variant 1–4.

### Mutation operators

Exactly one deterministic application of each operator was made to every reference model:

1. transition-target substitution;
2. output-label substitution;
3. action-column swap at one state;
4. state-row transplant;
5. self-loop injection;
6. paired transition mutation across two distinct states.

Locations and replacements were selected generically from the model canonical digest, operator name, and frozen seed. No mutant was manually replaced. The inventory remained exactly **144 mutants**.

## 5. Canonical serialization

- schema version: `1`;
- UTF-8 JSON;
- keys sorted recursively by Python `json.dumps(sort_keys=True)`;
- separators `(',', ':')`;
- non-ASCII preserved;
- exactly one trailing newline;
- model digests are SHA-256 over each canonical model record;
- mutation selection digests are SHA-256 over frozen seed, source-model digest, and operator name;
- bundle payload hashes are calculated before adding the top-level payload field.

Frozen Cycle 1 data:

- manifest: `research/studies/004-finite-state-conformance/data/corpus_v1.json`;
- reference-model transitions: `research/studies/004-finite-state-conformance/data/models_v1.json`.

## 6. Frozen methods

The three equal-budget methods were frozen before exact corpus information:

- uniform random testing with eight reset-delimited campaigns;
- increasing-length lexicographic breadth enumeration;
- shortest-trace transition-coverage guidance followed by consecutive transition-pair coverage.

Budgets remained 64, 256, and 1,024 executed actions per mutant. Reset cost no action but was recorded. Methods could use the reference model but not mutant internals or oracle results.

The four-stage black-box reducer and the independent paired-state breadth-first oracle were implemented separately. Method/oracle independence was preserved.

## 7. Protected sequence

1. activate the unchanged protocol;
2. freeze schema, generator, serialization, and 24-model / 144-mutant corpus;
3. freeze the three testing methods and reducer using hand-authored fixtures only;
4. implement and gate the independent exact oracle;
5. classify the already frozen corpus;
6. execute the already frozen methods and reducer;
7. analyze only after raw results were complete.

The sequence was maintained through closure. No protected result was inspected before method and reducer freeze.

## 8. Gates and dispositions

- corpus inventory remained 24 models and 144 mutants;
- 144 / 144 mutants were distinguishable, exceeding the 80% viability threshold;
- the oracle matched 10 / 10 frozen hand-audited expectations;
- method/oracle independence was maintained;
- complete deterministic results reproduced byte-identically;
- H1 was unsupported;
- H2 was supported;
- H3 was unresolved because the unique-mutant hypothesis did not freeze aggregation across multiple reducer outputs;
- the valid comparison therefore closed as a **partial result**.

## 9. Cycle limit

The maximum four approval cycles were completed:

1. activation, protocol, generator, and frozen corpus — **complete**;
2. testing methods and reducer freeze — **complete**;
3. oracle gate, corpus classification, and formal benchmark — **complete**;
4. deterministic reproduction, analysis, report, and closure — **complete**.

No fifth cycle was added.

## 10. Final artifacts

- Cycle 1 audit: `CYCLE_1_SETUP_AUDIT.md`
- Cycle 2 audit: `CYCLE_2_METHOD_FREEZE.md`
- Cycle 3 audit: `CYCLE_3_ORACLE_AND_RAW_RESULTS.md`
- Cycle 4 audit: `CYCLE_4_REPRODUCTION_AND_CLOSURE.md`
- final report: `REPORT.md`
- final analysis: `data/final_analysis_v1.json`
- final analysis runner: `../../../experiments/analyze_finite_state_conformance_cycle4.py`
- final tests: `../../../tests/test_finite_state_conformance_cycle4.py`

## 11. Closure record

Study 004 closed on 2026-07-23 as a partial result. The complete gzip result reproduced byte-identically with SHA-256 `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`.

Fresh checkout remained unavailable because the execution environment could not resolve `github.com`. The final reproduction used a functional reconstruction of live, hash-checked source contents. This is not a byte-identical full-repository checkout replay, and the complete historical suite and GitHub Actions were not run.
