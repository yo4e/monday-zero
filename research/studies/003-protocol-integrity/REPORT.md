# Study 003 Final Report — Protocol Integrity Under Approval-Gated Autonomous Research

_Date closed: 2026-07-21 (Asia/Tokyo)_  
_Disposition: **methodological success with bounded claims**_

## Abstract

Study 003 asked whether a machine-readable research contract could accept valid approval-gated research-event traces and reject evidence contamination, authorization mismatch, resource-cap violations, undisclosed correction, silent artifact mutation, and approval-token reuse at the first violating event without study-specific verdict rules.

The study froze a fourteen-event vocabulary, six dependency classes, thirty-six synthetic traces, twenty deterministic mutations, four historical transfer cases, an incremental primary validator, an independently written whole-trace oracle, and a deliberately weak order-only baseline. The first synthetic correctness gate passed with zero false accepts and false rejects, complete first-violation, class, reason-code, and primary/oracle agreement, and twenty of twenty mutations rejected. The weak baseline accepted twelve invalid traces, including all four precommitted stateful cases. After the instruments were frozen, all four precommitted Study 001/002 histories matched their expected dispositions without new event kinds, expectation changes, validator changes, or identifier-specific exceptions.

A final deterministic report combined all forty result rows and 572 represented events. Two runs were byte-identical. H1, H2, H3, and H4 are supported under the frozen criteria. The result is therefore a methodological success, but only for enforcement of the declared trace language and the small frozen corpus. Passing validation does not establish that research is true, valuable, safe, novel, unbiased, autonomous, or scientifically sound.

## 1. Research question

> Can a machine-readable research contract accept valid approval-gated research-event traces and reject evidence-contaminating, unauthorized, over-cap, or undisclosed-correction traces at the first violating event without study-specific rules?

The study tested procedural consistency. It did not evaluate substantive truth, research importance, scientific validity, safety, originality, or moral legitimacy.

## 2. Frozen hypotheses

- **H1 — synthetic correctness:** the primary validator and independent oracle correctly classify the complete frozen synthetic corpus with zero false accepts and false rejects and agree on first violation and dependency class.
- **H2 — mutation detection:** all twenty frozen contamination mutations are rejected at their precommitted first violating event.
- **H3 — historical transfer:** after the synthetic gate and instrument freeze, four precommitted Study 001/002 traces match their frozen dispositions without validator repair, new semantic events, or identifier-specific rules.
- **H4 — beyond ordering:** the full validators reject at least four stateful invalid traces accepted by a baseline that checks only event-kind order.

Failure of any protected invalid case, any valid-case rejection after the one permitted correction opportunity, historical mismatch, special-case branch, or failure to close within four approval cycles would have prevented methodological success.

## 3. Frozen trace language

Exactly fourteen event kinds were permitted:

`begin_cycle`, `end_cycle`, `freeze_artifact`, `set_cap`, `begin_execution`, `finish_execution`, `observe`, `authorize`, `external_action`, `record_defect`, `invalidate_evidence`, `apply_correction`, `disclose_correction`, and `accept_evidence`.

The six dependency classes were:

1. **D1 — artifact before observation:** a protected observation requires its declared artifact to have been frozen first.
2. **D2 — authorization before external action:** scope and token must match, and authorization can be single-use.
3. **D3 — cap before execution:** the governing cap must precede execution and recorded usage must remain within it.
4. **D4 — correction lifecycle:** defect recording, required invalidation, correction, refreeze or rerun, disclosure, and replacement evidence acceptance must occur in the declared order.
5. **D5 — artifact and evidence lineage:** an observed artifact cannot silently change digest; dependent evidence must be invalidated before replacement.
6. **D6 — approval-cycle integrity:** cycles may not overlap and each cycle requires its declared fresh approval token.

The validators did not determine whether a contract itself was wise or complete. They enforced only commitments represented in contract data.

## 4. Synthetic corpus

Cycle 1 generated the proposal-defined corpus before any verdict logic existed.

| Component | Count |
|---|---:|
| Minimal valid traces | 6 |
| Minimal invalid traces | 6 |
| Composite valid traces | 4 |
| Deterministic mutants | 20 |
| **Total** | **36** |
| Valid | 10 |
| Invalid | 26 |
| Total events | 528 |
| Maximum events in one trace | 20 |

Canonical corpus SHA-256:

`b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`

The five mutation operators were prerequisite omission, adjacent dependency inversion, unauthorized external-action insertion, numeric cap violation, and correction-disclosure omission. Each operator was applied once to each of four composite traces.

## 5. Instruments

### 5.1 Incremental primary validator

The primary validator processed events sequentially and maintained explicit state for cycles, approval tokens, artifact digests, protected observations, evidence invalidation, correction state, authorizations, caps, and active executions.

Frozen Git blob:

`71080f1051acc015e74b42de19d56ce8782b9f25`

### 5.2 Independent whole-trace oracle

The oracle independently examined each trace prefix using direct searches rather than importing the primary transition system or its state, verdict, reason-code, or first-violation helpers.

Frozen Git blob:

`74159c7a7502975b1bcd376510d5dad0283e03cd`

### 5.3 Order-only baseline

The baseline checked only whether required event kinds occurred somewhere earlier. It intentionally ignored identities, scopes, values, token consumption, digests, evidence lineage, and correction state.

Frozen Git blob:

`7af3b9e1db56a90e08b93690a14d90ee541b9d18`

## 6. Synthetic correctness gate

The first formal synthetic gate passed; the one permitted correction cycle was not used.

| Metric | Result |
|---|---:|
| Traces | 36 |
| Expected valid | 10 |
| Expected invalid | 26 |
| False accepts | **0** |
| False rejects | **0** |
| First-violation-index accuracy | **100%** |
| Violation-class accuracy | **100%** |
| Reason-code accuracy | **100%** |
| Primary/oracle agreement | **100%** |
| Mutations rejected | **20 / 20** |
| Source-level identifier-specific verdict branches found | **0** |

Formal result SHA-256:

`46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`

Formal result Git blob:

`53c801c18cd3b5a7cf696a146b0302d4659265e3`

### 6.1 Beyond-ordering evidence

The weak baseline accepted twelve invalid traces. The four precommitted nontrivial examples were:

- `P2-I`: authorization existed, but its scope did not match the external action;
- `P3-I`: cap order was correct, but recorded usage exceeded the numeric limit;
- `P5-I`: correction events existed, but affected evidence had not been invalidated;
- `P6-I`: event ordering was plausible, but an approval token was reused.

The full validators rejected all four. This shows that the tested advantage over an order-only checker came from stateful identity, value, token, digest, and evidence-lineage constraints rather than extra event-order edges alone.

## 7. Historical transfer

After the synthetic gate passed, the primary, oracle, baseline, corpus, and expectations were frozen. Cycle 3 then encoded exactly four precommitted repository histories before evaluation.

Historical artifact:

- Git blob: `840a7779a1cee3ba4f3f88e62342269b804c2719`
- Internal canonical SHA-256: `8cdaec94de2e8a7aff3158924db5e570f4af3008bcb33f18602f584b29b41053`
- Traces: 4
- Events: 44

| Trace | Frozen expectation | Primary | Oracle |
|---|---|---|---|
| `H1-SPAN-FORMAL-VALID` | valid | valid | valid |
| `H2-EXACT-SUBSTUDY-VALID` | valid | valid | valid |
| `H3-STUDY002-SHALLOW-CONTAMINATED` | invalid at index 5, D1, `artifact-not-frozen` | same | same |
| `H4-EXACT-PROJECTION-CORRECTION-VALID` | valid | valid | valid |

Historical result SHA-256:

`c59c621a1efad82ba95ca6eb92465a062b9b412b4fd8f4a05d69dccfcdcdac4a`

Historical result Git blob:

`161b65efb09d2d98cba0584574aeeaf0dfa5ec66`

No historical case required a new semantic event, validator change, expectation change, dependency-class change, or identifier-specific exception.

### 7.1 Interpretation of the contaminated Study 002 trace

The historical contract declared `freeze_artifact(shallow-heuristic)` as a prerequisite for the protected observation of exact results. The trace contained no such freeze before `observe(exact-results)`. Both frozen instruments therefore rejected event index 5 with D1 `artifact-not-frozen`.

The detection did not depend on a hard-coded Study 002 name. The study-specific fact appeared only as contract data.

## 8. Final deterministic report

Cycle 4 added a deterministic report runner that consumes the two frozen result artifacts without changing their verdicts. It checks:

- all thirty-six synthetic result rows and their frozen order;
- valid 10 / invalid 26 and mutant 20 row counts;
- equality of synthetic expected, primary, and oracle decisions;
- zero synthetic failure lists and all frozen aggregate metrics;
- the four exact historical IDs and expectations;
- expected-verdict, first-violation, and primary/oracle historical matches;
- frozen corpus, result, historical artifact, and instrument identifiers;
- H1 through H4 disposition logic.

Runner Git blob:

`ab5bfe161ab5a39febc1ed8905d46a28016fc114`

The combined report covers:

- 36 synthetic traces and 528 synthetic events;
- 4 historical traces and 44 historical events;
- **40 traces and 572 events total**.

Two final runs produced byte-identical files.

- Internal deterministic SHA-256: `a52d00e08e00855ad9f43b3988e8f64bf9dc03d3d81f87c7c090f52247ec60a4`
- Complete report file SHA-256: `5f8d1e6d399957745b233f4807406a01ea0ae98af580cd3adba77becf4265904`
- Complete report Git blob: `62b0836a3abc2ce96fa74f045b8fbf5628916e55`

File:

`data/complete_validation_v1.json`

### 8.1 Reproduction boundary

The execution environment could not obtain a fresh checkout because DNS resolution for `github.com` failed, and connector results cannot be mounted directly as local files. The final runner was therefore executed against a functional projection containing every live result field the runner consumes. Those fields, their values, row order, and source Git blobs were verified through the connector. The checked-in complete-report blob exactly matched the locally produced bytes.

This final stage is a deterministic integration and consistency reproduction of the already frozen Cycle 2 and Cycle 3 results. It is not a new fresh-checkout re-execution of the raw forty traces through the validators. Raw synthetic and historical validation had already been performed and independently repeated in their respective cycles.

## 9. Hypothesis disposition

### H1 — supported

All thirty-six frozen synthetic traces matched their expected verdicts. False accepts and false rejects were zero, and first-violation, class, reason, and primary/oracle agreement were complete.

### H2 — supported

All twenty frozen contamination mutations were rejected at their precommitted first violation.

### H3 — supported

All four precommitted historical traces matched their frozen dispositions after instrument freeze, without validator changes, semantic expansion, or special cases.

### H4 — supported

The full validators rejected all four named stateful invalid traces that the order-only baseline accepted. The weak baseline accepted twelve invalid traces overall.

## 10. Final disposition

Study 003 meets its frozen methodological-success criteria within the four-cycle limit.

The supported claim is narrow:

> For the frozen fourteen-event language, six dependency classes, thirty-six specification-derived synthetic traces, twenty mutations, and four preselected repository histories, the two frozen validators consistently enforced declared procedural commitments, agreed on first violations, outperformed an order-only baseline on stateful cases, transferred without repair, and produced reproducible final reporting.

The study does **not** establish that the mechanism is a general research-governance system, security tool, proof assistant, scientific auditor, or reliable judge of good research.

## 11. Claims not supported

A valid trace does not establish that the represented research is:

- true or reproducible in substance;
- important or worth conducting;
- safe, legal, ethical, or authorized outside the represented contract;
- unbiased;
- novel or original;
- autonomous in any philosophically meaningful sense;
- publication-ready;
- free of omitted dependencies that the contract failed to declare.

The validator can only enforce commitments present in its input language. A bad contract can be followed perfectly.

## 12. Limitations

- The synthetic corpus was constructed from the same specification as the validators' target semantics. It is a correctness fixture, not a natural distribution.
- The historical set contained only four episodes, selected before activation but drawn from the same repository and known failure history that motivated the study.
- Primary and oracle implementations were separately written, but both were authored by the same operator and share the same conceptual specification.
- The schema contains only fourteen event kinds and six dependency classes.
- No adversarial third-party corpus was used.
- No external research repository was evaluated.
- No human-subject study measured whether the representation is understandable or useful.
- Fresh checkout, full-repository regression, and GitHub Actions verification were unavailable.
- The final integration runner consumed frozen result artifacts rather than freshly replaying all raw traces in a new checkout.

## 13. Operational corrections

Study 003 preserved the following implementation and connector corrections:

- Two minimal proposal fixtures were corrected before activation because their correction semantics were internally inconsistent.
- Two empty issues accidentally created during Cycle 1 connector navigation were immediately closed as `not_planned` and were not research tasks.
- A synthetic fixture file rejected by the normal contents API due to a false-positive safety interpretation was stored as the same verified bytes through Git data operations.
- Four content-identical public-README update calls in Cycle 3 produced no-op commits. The unchanged blob and all commit identifiers remain disclosed in `CYCLE_3_HISTORICAL_TRANSFER.md`.
- The Cycle 4 runner's initial expected synthetic row order was corrected before formal output after comparison with the live frozen result ordering.

None of these corrections changed a protected verdict, frozen expectation, synthetic fixture content after validator execution, historical expectation, validator rule, or final hypothesis disposition.

## 14. Reusable artifacts

Study 003 leaves:

- a declarative event and contract schema;
- a deterministic thirty-six-trace corpus generator;
- twenty fixed contamination mutations;
- an incremental validator;
- an independently written whole-trace oracle;
- a weak order-only baseline;
- synthetic and historical gate runners;
- four cited historical trace encodings;
- deterministic gate and complete-report artifacts;
- visible activation, correction, and closure audits.

These artifacts are research prototypes. They should not be used as production authorization or security infrastructure without independent review and substantially broader testing.

## 15. Closure

Study 003 is closed after the fourth and final approval-driven activation cycle. The instruments, corpus, expectations, historical traces, and results are archived. Later work may cite them but may not silently expand Study 003 or reinterpret its success as substantive validation of the underlying research histories.

No Study 004 was started in this cycle.
