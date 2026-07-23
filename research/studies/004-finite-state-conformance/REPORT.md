# Study 004 Final Report — Finite-State Conformance Counterexamples

_Date closed: 2026-07-23 (Asia/Tokyo)_  
_Disposition: **partial result**_

## Abstract

Study 004 asked whether a model-guided black-box testing method could detect observable divergences between small deterministic Mealy-machine specifications and mutated implementations more effectively than equal-budget uniform random testing, while a frozen reducer produced exact shortest counterexamples under an independent oracle.

The study froze 24 reference models, six deterministic mutation operators, 144 unreplaced mutants, three equal-budget testing methods, a four-stage black-box reducer, ten oracle fixtures, an independent paired-state breadth-first oracle, and budgets of 64, 256, and 1,024 executed actions. All 144 mutants were distinguishable, so the 80% corpus-viability gate passed. The complete benchmark contained 1,296 method-budget-mutant rows.

The complete Cycle 3 result generation was rerun in Cycle 4 without changing the corpus, methods, reducer, oracle, budgets, hypotheses, thresholds, or mutation inventory. The reproduced gzip was byte-identical to the frozen result: 29,400 bytes with SHA-256 `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`.

H1 is unsupported: at 256 actions, transition-coverage guidance detected 140 / 144 mutants, while uniform random detected 142 / 144, a difference of -1.388889 percentage points rather than the required +10 points. H2 is supported: at 1,024 actions, coverage guidance detected 143 / 144 versus breadth enumeration's 131 / 144 and did not trail breadth in any mutation class. H3 is unresolved because the frozen hypothesis specified a unique-mutant union denominator but did not specify how to aggregate multiple reducer outputs for one mutant; plausible rules produce results on both sides of the 90% threshold. No reducer output was non-failing.

The study is therefore a valid **partial result**, not full methodological success. Its central expected detection advantage over random testing was not observed in the frozen synthetic benchmark.

## 1. Research question

> Can a model-guided black-box testing method detect observable divergences between small deterministic finite-state specifications and mutated implementations more effectively than equal-budget uniform random testing, while reducing detected failures to exact shortest counterexamples under an independent oracle?

The unit of analysis was one deterministic Mealy reference model paired with one mutated implementation. The study makes no claim about arbitrary software, production verification, security defects, method novelty, or real-world fault distributions.

## 2. Frozen hypotheses

- **H1 — detection advantage:** at 256 actions, transition-coverage guidance detects at least 10 percentage points more distinguishable mutants than uniform random.
- **H2 — breadth robustness:** at 1,024 actions, transition-coverage guidance detects at least as many distinguishable mutants as lexicographic breadth enumeration and trails breadth by no more than 10 percentage points in every mutation class.
- **H3 — counterexample reduction:** for at least 90% of mutants detected by any frozen method, the reducer returns a still-failing trace equal in length to the oracle's exact shortest distinguishing trace.

## 3. Protected sequence

The study completed the frozen four-cycle order:

1. activate the unchanged protocol and freeze the 24-model / 144-mutant corpus;
2. freeze all three methods and the reducer before exact information;
3. freeze oracle fixtures, gate the independent oracle, classify the unchanged corpus, and generate complete raw results;
4. reproduce the complete results, analyze, report, and close.

No fifth cycle was added. No protected artifact or threshold was modified after oracle classification began.

## 4. Corpus and oracle gates

### 4.1 Corpus inventory

| Dimension | Frozen count | Distinguishable | Equivalent |
|---|---:|---:|---:|
| Reference models | 24 | — | — |
| Mutants | 144 | 144 | 0 |
| Each mutation operator | 24 | 24 | 0 |
| Each topology family | 48 | 48 | 0 |
| Four-state mutants | 72 | 72 | 0 |
| Eight-state mutants | 72 | 72 | 0 |

The viability threshold required at least 116 distinguishable mutants. All 144 were distinguishable.

### 4.2 Exact shortest-length distribution

| Exact shortest length | Mutants |
|---:|---:|
| 1 | 16 |
| 2 | 32 |
| 3 | 52 |
| 4 | 28 |
| 5 | 9 |
| 6 | 4 |
| 7 | 2 |
| 8 | 1 |

### 4.3 Oracle gate

Ten expected fixture results were committed before oracle implementation. The independent paired-state breadth-first oracle matched all ten classifications and exact shortest traces. Its frozen Git blob is `6eb6205dc32877446201b34d5a591e9851cfd69f`.

## 5. Deterministic reproduction

Cycle 4 reconstructed the frozen gzip identity from the ordered eight-part base64 transport, reran the unchanged Cycle 3 complete-result generator, and compared the complete bytes.

| Artifact | Size | SHA-256 |
|---|---:|---|
| gzip result | 29,400 bytes | `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679` |
| decompressed JSON | 899,730 bytes | `a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c` |
| internal raw payload | — | `bb34844aee696cde0ea19de9c48a5bd5ec8faf66391a492bc6277bf24ac69927` |
| final analysis file | 10,145 bytes | `18e49046e9255b10dcd4c8b6ecdde3abf5971507f529575cd0511223cfb4b92a` |
| final analysis payload | — | `7b80f4239650fe5fbd750559578ecc9ab609cb7aad68d0469246b47b412d6584` |

The complete gzip was byte-identical. The final analysis JSON was independently generated twice and was also byte-identical.

Final analysis runner:

- path: `experiments/analyze_finite_state_conformance_cycle4.py`
- Git blob: `c5674fe4578adb5e1b4998a94b9aa2fb824b2066`

Final analysis data:

- path: `data/final_analysis_v1.json`
- Git blob: `c9ea60ecc31b79012644fcd6618e078d205ba422`

Cycle 4 tests:

- path: `tests/test_finite_state_conformance_cycle4.py`
- Git blob: `c634954f315da243089a1f99feba9af2951ad0f8`
- result: **3 passed**
- compile verification: passed

## 6. Detection results

### 6.1 Counts and rates

| Budget | Uniform random | Lexicographic breadth | Transition coverage guided |
|---:|---:|---:|---:|
| 64 | 125 / 144 (86.805556%) | 82 / 144 (56.944444%) | 106 / 144 (73.611111%) |
| 256 | 142 / 144 (98.611111%) | 118 / 144 (81.944444%) | 140 / 144 (97.222222%) |
| 1,024 | 144 / 144 (100.000000%) | 131 / 144 (90.972222%) | 143 / 144 (99.305556%) |

### 6.2 Pairwise percentage-point differences

Positive values favor the left-hand method.

| Budget | Comparison | Difference |
|---:|---|---:|
| 64 | guided − random | -13.194444 pp |
| 64 | guided − breadth | +16.666667 pp |
| 256 | guided − random | -1.388889 pp |
| 256 | guided − breadth | +15.277778 pp |
| 1,024 | guided − random | -0.694444 pp |
| 1,024 | guided − breadth | +8.333333 pp |

Uniform random was the strongest aggregate detector at every frozen budget. Coverage guidance consistently outperformed lexicographic breadth, but not random testing.

## 7. Hypothesis dispositions

### 7.1 H1 — unsupported

At the precommitted 256-action budget:

- uniform random: 142 / 144 = 98.611111%;
- transition coverage guided: 140 / 144 = 97.222222%;
- guided minus random: **-1.388889 percentage points**.

H1 required at least **+10 percentage points**. The observed result not only missed the threshold but had the opposite sign.

### 7.2 H2 — supported

At 1,024 actions:

- lexicographic breadth: 131 / 144 = 90.972222%;
- transition coverage guided: 143 / 144 = 99.305556%;
- guided minus breadth: **+8.333333 percentage points**.

Mutation-class results:

| Mutation operator | Breadth | Guided | Guided − breadth |
|---|---:|---:|---:|
| action-column swap | 21 / 24 | 24 / 24 | +12.500000 pp |
| output-label substitution | 22 / 24 | 24 / 24 | +8.333333 pp |
| paired-transition mutation | 21 / 24 | 23 / 24 | +8.333333 pp |
| self-loop injection | 23 / 24 | 24 / 24 | +4.166667 pp |
| state-row transplant | 24 / 24 | 24 / 24 | 0.000000 pp |
| transition-target substitution | 20 / 24 | 24 / 24 | +16.666667 pp |

Guidance met the aggregate condition and did not trail breadth in any mutation class.

### 7.3 H3 — unresolved

All 144 mutants were detected by at least one method. No reducer output was non-failing. However, each mutant could have multiple detected traces across three methods and three budgets. The frozen H3 wording fixed a unique-mutant union denominator but did not freeze which reducer output or aggregation rule determines one mutant's success.

Sensitivity analysis:

| Rule | Exact-minimal successes | Rate | Threshold result |
|---|---:|---:|---|
| At least one exact reducer output per mutant | 144 / 144 | 100.000000% | supports |
| Reducer output for shortest detected input row | 144 / 144 | 100.000000% | supports |
| Every detected reducer output exact | 99 / 144 | 68.750000% | does not support |
| Earliest detection in frozen grid exact | 122 / 144 | 84.722222% | does not support |
| Row-level exact outputs | 1,075 / 1,131 | 95.048630% | not the frozen mutant denominator |

Because reasonable mutant-level rules cross the 90% threshold, selecting one after seeing results would be retrospective threshold engineering. H3 is therefore **unresolved**, not supported or unsupported.

## 8. Execution, coverage, and trace observations

At 1,024 actions, average executed actions per mutant were 26.361111 for random, 173.944444 for breadth, and 55.909722 for guidance. Early mismatch detection means these are consumed actions, not always the full nominal budget.

The mean first failing trace lengths at 1,024 actions were:

- random: 20.138889 actions, median 9, maximum 117;
- breadth: 2.770992 actions, median 3, maximum 5;
- guidance: 3.048951 actions, median 3, maximum 8.

Thus random testing detected slightly more mutants but commonly returned much longer initial failures. Breadth and guidance found shorter first failures. This descriptive result was not a separate precommitted hypothesis.

## 9. Overall disposition

Study 004 is a **partial result** under its frozen rules.

The corpus and oracle gates passed, protected sequencing remained intact, the complete benchmark was generated, and the complete result reproduced byte-identically. However, full methodological success required H1, H2, and H3 all to be supported. H1 is unsupported and H3 is unresolved. Only H2 is supported.

The primary substantive finding is negative: in this complete frozen synthetic benchmark, transition-coverage guidance did not outperform equal-budget uniform random testing at the precommitted 256-action threshold. Random testing detected two more mutants at 256 actions and one more at 1,024 actions.

A secondary positive result is narrower: transition-coverage guidance substantially outperformed lexicographic breadth enumeration and did so without a hidden mutation-class collapse.

## 10. Limitations

- The benchmark is synthetic and complete; it is not a random sample from a real defect population.
- The same autonomous operator designed the corpus, mutations, methods, fixtures, reducer, oracle plan, and final analysis, creating formalization and self-authorship bias.
- All six mutation families produced distinguishable mutants, which may indicate a corpus easier than real equivalence-heavy mutation sets.
- H3's aggregation rule was underspecified before results and cannot be repaired retrospectively.
- Fresh checkout remained unavailable because the environment could not resolve `github.com`.
- Verification used a functional reconstruction of live, hash-checked sources rather than a byte-identical repository checkout.
- The complete historical repository suite and GitHub Actions were not run.
- No transfer, novelty, production-readiness, security, usability, or human-comprehensibility claim is supported.

## 11. Closure

Study 004 completed all four permitted approval cycles and is closed. Issue #10 is closed as a completed partial result. The laboratory returns to no active study.

The next approval may perform only a post-Study-004 portfolio assessment comparing at least three genuinely distinct research directions plus inactivity. It may select and freeze at most one inactive proposal. It must not activate Study 005 or begin implementation in the same cycle.
