# Proposed Study 004 — Finite-State Conformance Counterexamples

_Date: 2026-07-21 (Asia/Tokyo)_  
_Status: **Frozen proposal — not active**_

## 1. Go / no-go status

**GO to a separately gated activation decision.**

This proposal does not activate Study 004, create an active-study issue, implement code, generate machine-readable models or mutants, inspect benchmark outcomes, or run an experiment. TEMPLEX/0 remains without an active study.

A later project-chat `承認` must re-read the live repository and make an independent activation GO / NO-GO decision. If activated unchanged, the study may then begin only with the bounded Cycle 1 setup defined below.

The proposal follows `research/decisions/2026-07-21-post-study-003-portfolio-assessment.md`.

## 2. Research question

> Can a model-guided black-box testing method detect observable divergences between small deterministic finite-state specifications and mutated implementations more effectively than equal-budget uniform random testing, while reducing detected failures to exact shortest counterexamples under an independent oracle?

The unit of analysis is a reference deterministic Mealy machine paired with a mutated implementation. A test supplies an action sequence from a reset state and compares the observed output sequence with the reference output sequence.

The study evaluates bounded conformance-testing methods on a frozen synthetic corpus. It does not claim to verify arbitrary software, prove implementation correctness, discover real-world vulnerabilities, or establish method novelty.

## 3. Precommitted hypotheses

### H1 — detection advantage

At a budget of 256 executed actions per mutant, the frozen transition-coverage-guided method will detect at least **10 percentage points more observationally distinguishable mutants** than the frozen uniform-random method.

The comparison is corpus-wide and uses the same distinguishable-mutant denominator. Equivalent mutants are not counted as misses for either method.

### H2 — breadth robustness

At the maximum budget of 1,024 executed actions per mutant, the transition-coverage-guided method will detect at least as many distinguishable mutants as the frozen lexicographic breadth-enumeration method, and will not trail breadth enumeration by more than 10 percentage points in any frozen mutation class.

This prevents a nominal aggregate win that hides complete failure on one fault family.

### H3 — counterexample reduction

For at least **90% of mutants detected by any frozen method**, the frozen reducer will return a still-failing trace whose length equals the independent exact oracle's shortest distinguishing-trace length.

Every returned reduced trace must reproduce the reference-versus-mutant output divergence. Returning a non-failing trace is a correctness failure, not merely a metric miss.

A failure of any hypothesis is an acceptable research result if the corpus, methods, budgets, oracle, and analysis rules remain frozen.

## 4. What this study is not

Study 004, if activated, is not:

- a continuation or repair of Study 001's game designs;
- another exact-first game grammar from Study 002;
- an extension of Study 003's research-event contract language;
- a production model checker, security scanner, or certification system;
- a benchmark on third-party repositories;
- a human-subject evaluation;
- a novelty claim about conformance testing;
- evidence that passing the benchmark implies correctness on unmodeled behavior.

## 5. Frozen behavioral domain

### 5.1 Reference model

Each reference object is a deterministic total Mealy machine with:

- one named reset state;
- either 4 or 8 states;
- exactly 3 input actions: `a0`, `a1`, and `a2`;
- exactly 3 observable output labels: `o0`, `o1`, and `o2`;
- one transition target and one output label for every state-action pair;
- no hidden variables, nondeterminism, timing, concurrency, exceptions, or partial transitions.

A trace begins from reset and consists only of input actions. Its observation is the ordered output-label sequence.

### 5.2 Reference families

The frozen generator must create exactly 24 models:

- 2 state sizes: 4 and 8;
- 3 topology families;
- 4 generated models in every size × family cell.

The topology families are:

1. **reset-chain:** at least one action tends toward reset while another advances through a chain;
2. **clustered:** states form two densely connected groups with limited cross-group transitions;
3. **cyclic:** at least one action participates in a cycle covering at least half the states.

The generator may enforce only structural validity and family membership. It may not rank models by later method performance.

### 5.3 Frozen generation seed

The reference-model seed is:

`2026072104`

Canonical model serialization and seeded ordering must be defined before any generated model is evaluated.

## 6. Frozen mutation corpus

Exactly six mutation operators are applied once to every reference model. The mutation location and replacement choice are derived deterministically from the canonical model digest, operator name, and frozen seed.

1. **transition-target substitution:** replace one transition target with a different state;
2. **output-label substitution:** replace one transition output with a different label;
3. **action-column swap:** swap the complete target/output entries of two actions at one state;
4. **state-row transplant:** replace one state's three target/output entries with another state's row;
5. **self-loop injection:** change one non-self transition target to its source state without changing its output;
6. **paired transition mutation:** change two distinct transition targets selected from different states.

The frozen inventory is therefore:

- 24 reference models;
- 6 mutants per model;
- **144 mutants total**.

No mutant may be manually replaced because it is equivalent, trivial, difficult, or inconvenient.

The exact oracle will later classify each mutant as observationally equivalent or distinguishable. Equivalent mutants remain in the published corpus and count. Formal detection-rate denominators use only distinguishable mutants, with equivalent counts reported separately by operator and model family.

### 6.1 Corpus viability gate

If fewer than 80% of the 144 mutants are observationally distinguishable, the corpus is considered too weak for the primary comparison. The study closes with a negative setup result. It may not generate replacement models, add operators, or alter the seed.

## 7. Frozen testing methods

All methods interact with a mutant only through reset, input action, and observed output. They may use the reference model but may not inspect mutant transition tables, mutant digests beyond identity, exact-oracle results, or shortest distinguishing traces.

Every method receives the same action-execution budgets per mutant:

- 64 actions;
- 256 actions;
- 1,024 actions.

A reset consumes no action budget but must be recorded. A test trace that would exceed the remaining budget is not partially executed.

### 7.1 Uniform random

Uniform random testing generates independent action choices from `a0`, `a1`, and `a2` using fixed per-mutant seeds derived from the corpus digest, mutant ID, budget, and campaign index.

Each budget is divided into eight campaigns with reset between campaigns. Campaign lengths differ by at most one action. A mutant is detected if any campaign produces an output mismatch.

### 7.2 Lexicographic breadth enumeration

Breadth enumeration executes action sequences in increasing length and lexicographic order under `a0 < a1 < a2`, resetting before every sequence. It has no randomness and no transition-coverage objective.

### 7.3 Transition-coverage-guided testing

The model-guided method maintains coverage of reference state-action transitions. At each reset-delimited test, it selects the shortest lexicographically first reference trace that reaches an uncovered transition, then appends the action that exercises that transition.

After all reference transitions have been exercised, it repeats the same deterministic ordering with pairwise consecutive-transition coverage as the secondary objective. It may not adapt based on mutant internals. It may stop early only after detecting a mismatch.

Activation may refine data structures but may not change this selection semantics after the method is frozen.

## 8. Frozen counterexample reducer

The reducer receives only:

- a failing action trace found by one of the three methods;
- reset-and-execute access to the reference and mutant;
- no exact-oracle result.

It performs, in order:

1. remove the longest failing suffix by binary prefix search;
2. greedily delete contiguous chunks from largest to smallest, restarting after every successful deletion;
3. greedily delete individual actions from left to right until no deletion preserves failure;
4. return the lexicographically smallest trace among equal-length failing traces encountered by the reducer.

The reducer must re-execute every candidate trace. Cached observations are allowed only when keyed by the complete action sequence and system identity.

A returned trace is valid only if it still causes an observable output mismatch.

## 9. Independent exact oracle

The oracle performs breadth-first search over paired reference/mutant states from reset and returns:

- `equivalent` if no reachable action produces an output difference and the finite product graph is exhausted;
- otherwise the lexicographically first shortest distinguishing action trace;
- visited product-state count;
- canonical result digest.

The oracle must be implemented separately from all testing methods and the reducer. Testing code may not import oracle search, queue, predecessor, equivalence, or shortest-trace helpers.

### 9.1 Correctness gate

Before classifying the 144-mutant corpus, the oracle must match hand-audited expectations on at least eight fixed pairs covering:

- immediate output difference;
- one-step-later difference;
- multiple shortest traces with lexicographic tie-breaking;
- equivalent machines with renamed unreachable states;
- equivalent machines with different internal transitions but identical reachable observations;
- a difference requiring a reset-origin path of at least four actions;
- a cyclic product graph;
- a paired mutation with a shorter-than-obvious counterexample.

The fixtures and expected shortest traces must be frozen before oracle execution. At most one bounded correction cycle is allowed before formal corpus classification. Any unresolved mismatch closes the study without formal method comparison.

## 10. Sequencing and contamination controls

Protected order after activation:

1. freeze the active protocol unchanged from this proposal except for implementation-level typing and paths;
2. implement and freeze the model generator, corpus serialization, and mutation generator;
3. generate and freeze the 24 models and 144 mutants without oracle classification;
4. implement and freeze all three testing methods and the reducer using only hand-authored unit fixtures;
5. implement and gate the independent exact oracle;
6. classify the already frozen mutant corpus;
7. run the already frozen testing methods and reducer under all budgets;
8. analyze only after all raw results are complete.

No method, budget, seed, corpus item, mutation location, threshold, or hypothesis may change after oracle classification begins.

If protected oracle information is inspected before the three testing methods and reducer are frozen, H1–H3 are contaminated and the study closes as invalid rather than repairing the sequence retrospectively.

## 11. Metrics

The final report must include:

- reference and mutant counts;
- equivalent and distinguishable mutants by operator, topology family, and state size;
- detection count and rate for each method at each budget;
- pairwise detection differences with the frozen percentage-point comparisons;
- transition and transition-pair coverage for each method;
- first failing trace length by method;
- exact shortest distinguishing length by mutant;
- reducer output length and exact-minimality match;
- invalid reducer outputs, if any;
- action executions and resets consumed;
- deterministic result digests;
- H1–H3 dispositions without threshold changes.

No post-result significance test is required. The corpus is the complete frozen benchmark, not a random sample from an asserted population.

## 12. Disposition rules

### Full methodological success

All of the following must hold:

- the corpus viability gate passes;
- the oracle correctness gate passes;
- no protected sequencing contamination occurs;
- H1, H2, and H3 are supported;
- complete deterministic results reproduce byte-identically in two runs.

### Partial result

The study is partial if the corpus and oracle gates pass and the complete comparison is valid, but one or more of H1–H3 is unsupported.

### Negative setup result

The study closes before formal method comparison if:

- corpus generation does not match the frozen counts or family requirements;
- fewer than 80% of mutants are distinguishable;
- the oracle correctness gate fails after the one permitted correction cycle;
- method/oracle independence cannot be maintained;
- protected sequencing is contaminated.

### Operational failure

The study closes as operationally incomplete if it cannot produce and repeat complete deterministic results within the cycle and resource limits. Partial raw output must not be represented as a complete benchmark.

## 13. Resource and cycle limits

From activation through closure, Study 004 has a maximum of **four approval cycles**:

1. activation, protocol, generator, and frozen corpus;
2. testing methods and reducer freeze;
3. oracle correctness gate, corpus classification, and formal benchmark execution;
4. deterministic reproduction, analysis, final report, and closure.

The active protocol may impose lower per-command limits. It may not add a fifth cycle.

Formal execution must remain standard-library-only unless activation records a specific dependency already present in the repository. No paid service, external compute account, or third-party system is permitted.

## 14. Verification requirements

As applicable, every cycle must perform and record:

- targeted deterministic tests;
- canonical serialization regeneration;
- compile verification;
- source/blob identity checks through the connected repository interface;
- byte-identical repeated generation or execution for protected artifacts;
- explicit fresh-checkout and full-regression status without claiming unavailable verification.

If the environment still cannot obtain a fresh checkout, the limitation must remain attached to reproducibility claims. A functional reconstruction is not a byte-identical full-repository replay.

## 15. Claims not supported

Even full success would not establish that:

- transition-coverage guidance is superior on arbitrary programs;
- the synthetic topology and mutation families represent real defect distributions;
- shortest counterexamples are easiest for humans to understand;
- the methods are novel;
- the oracle or benchmark is production-ready;
- passing all generated tests proves implementation correctness outside the frozen model;
- the results transfer to nondeterministic, concurrent, timed, probabilistic, state-rich, or partially observable systems.

## 16. Human intervention boundary

A plain activation `承認` is A1 access assistance. The human does not select models, mutations, outcomes, thresholds, interpretations, or dispositions.

Any human change to the research question, mutation corpus, budgets, hypotheses, threshold, public claim, or result interpretation must be recorded according to its actual A-level.

## 17. Activation decision

A later approval must choose one of:

- **GO unchanged:** activate the proposal as the Study 004 protocol and perform Cycle 1 only;
- **NO-GO:** record why the proposal does not justify activation and remain inactive.

Activation may clarify file paths, type annotations, serialization fields, and test organization. It may not change the frozen question, hypotheses, model inventory, seed, mutation operators, budgets, method semantics, oracle role, disposition rules, or four-cycle limit.
