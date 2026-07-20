# Study 003 Protocol — Protocol Integrity Under Approval-Gated Autonomous Research

_Date activated: 2026-07-21 (Asia/Tokyo)_  
_Status: **Active — cycle 1 of at most 4 complete**_

## Authority and frozen source

Study 003 activates the unchanged frozen proposal:

- `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- proposal freeze audit: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY_AUDIT.md`

The activation decision did not alter the research question, hypotheses, event vocabulary, dependency classes, expected verdicts, mutation inventory, historical expectations, metrics, resource limits, or four-cycle stop rule.

## Research question

> Can a machine-readable research contract accept valid approval-gated research-event traces and reject evidence-contaminating, unauthorized, over-cap, or undisclosed-correction traces at the first violating event without study-specific rules?

The study evaluates enforcement of declared procedural commitments. It does not determine whether research is true, worthwhile, creative, safe, unbiased, novel, autonomous, or publication-ready.

## Frozen hypotheses

- **H1 — synthetic correctness:** the primary validator and independent oracle classify all frozen synthetic traces correctly, agree on first violation and class, and produce zero false accepts and false rejects after at most one correction cycle.
- **H2 — mutation detection:** all twenty frozen contamination mutations are rejected at their precommitted first violating event.
- **H3 — historical transfer:** after the synthetic gate and validator freeze, four Study 001/002 traces match their frozen dispositions without validator changes or identifier-specific rules.
- **H4 — beyond ordering:** the full validators reject at least four stateful invalid traces accepted by the frozen order-only baseline.

## Frozen event vocabulary

Exactly fourteen event kinds are permitted:

`begin_cycle`, `end_cycle`, `freeze_artifact`, `set_cap`, `begin_execution`, `finish_execution`, `observe`, `authorize`, `external_action`, `record_defect`, `invalidate_evidence`, `apply_correction`, `disclose_correction`, and `accept_evidence`.

Activation may refine field typing and serialization but may not add semantic event kinds after validator execution begins.

## Frozen dependency classes

1. **D1:** artifact freeze before protected observation.
2. **D2:** exact-scope authorization before external action, with single-use token consumption.
3. **D3:** governing cap before execution and recorded usage within that cap.
4. **D4:** defect recording, invalidation, correction, required rerun or re-observation, and disclosure before corrected evidence acceptance.
5. **D5:** no silent digest change after protected observation; dependent evidence must be invalidated and replacement evidence regenerated.
6. **D6:** fresh matching approval token for every non-overlapping bounded cycle.

## Frozen synthetic corpus

Cycle 1 generated the proposal-defined corpus without verdict execution:

- 12 minimal traces: one valid and one invalid for each dependency class;
- 4 composite valid traces;
- 20 deterministic mutants from five operators applied once to each composite trace;
- **36 traces total: 10 valid and 26 invalid**;
- 528 total events; maximum 20 events in one trace.

Mutation operators are fixed to prerequisite omission, adjacent dependency inversion, unauthorized insertion, cap violation, and undisclosed correction.

Machine-readable artifact:

- `data/synthetic_corpus_v1/index.json`
- canonical SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`

The bundle contains frozen expected verdict data but no actual validator, oracle, or baseline output and no historical trace encoding.

## Frozen baseline

The order-only baseline will check only whether a required event kind occurs earlier. It will ignore subject identity, authorization scope, token consumption, numeric usage, digests, evidence lineage, and correction state.

It must accept at least `P2-I`, `P3-I`, `P5-I`, and `P6-I` while both full validators reject them. It is not an oracle.

## Validator independence

Cycle 2 may implement:

- one incremental state-machine validator;
- one separately written whole-trace oracle using prefix predicates;
- the frozen order-only baseline.

The oracle may share only serialized field names, primitive scalar conventions, and the contract/trace inputs. It may not import or call primary transition, state, verdict, reason-code, or first-violation helpers.

## Correctness and stopping gates

The synthetic gate requires:

- zero false accepts and false rejects;
- 100% first-violation-index accuracy;
- 100% violation-class accuracy;
- 100% primary/oracle agreement;
- all twenty mutants rejected;
- the four named beyond-ordering examples demonstrated;
- zero study-, path-, commit-, candidate-, or trace-ID-specific verdict branches.

One bounded correction cycle is permitted without changing the corpus, contracts, expectations, dependency classes, or metrics. Continued error closes the study negatively.

Historical encoding starts only after the synthetic gate passes and validator code is frozen. Historical mismatch cannot be repaired inside Study 003.

## Resource boundaries

- standard-library-only implementation;
- exactly 36 synthetic and 4 later historical traces;
- at most 40 events per trace and 1,600 events per complete final run;
- no network, paid compute, external service, third-party action, or human subjects;
- at most four approval-driven cycles after activation, including final synthesis.

## Cycle record

- **Cycle 1 — schema and corpus freeze: complete.** Active protocol created; schema, canonical serialization, deterministic generator, 36-trace artifact, and tests added. No verdict logic or historical traces were created.
- Cycle 2 — validators and first synthetic gate: pending.
- Cycle 3 — one correction cycle or historical transfer: pending.
- Cycle 4 — reproduction, synthesis, and closure: pending.

## Intervention model

A plain project-chat `承認` is A1 access assistance for one bounded cycle. Templex selects implementation, interpretation, debugging, failure diagnosis, and stopping decisions within this protocol. External communication, publication, spending, permissions, and human-subject activity remain separately gated.
