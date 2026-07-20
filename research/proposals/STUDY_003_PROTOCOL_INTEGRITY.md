# Proposed Study 003 — Protocol Integrity Under Approval-Gated Autonomous Research

_Date: 2026-07-18 (Asia/Tokyo)_  
_Status: **Frozen proposal — not active**_

## 1. Go / no-go status

**GO to a separately gated activation decision.**

This proposal does not activate Study 003, create an active-study issue, implement code, generate machine-readable fixtures, or run an experiment. TEMPLEX/0 remains without an active study. A later project-chat `承認` must inspect this frozen proposal and make a separate activation go / no-go decision.

The proposal follows the decision recorded in `research/decisions/2026-07-18-next-study-go-no-go.md`. It addresses a demonstrated laboratory failure: Study 002 listed a requirement that the shallow-search heuristic be frozen before exact outcomes were inspected, but its execution order did not enforce that dependency. The proposed study tests a general protocol-integrity mechanism, not a Study-002-specific patch.

## 2. Research question

> Can Templex Tsukino build and evaluate a machine-readable research-contract system that accepts valid approval-gated research-event traces and rejects evidence-contaminating, unauthorized, over-cap, or undisclosed-correction traces at the first violating event, without study-specific rules?

The unit of analysis is an ordered research-event trace evaluated against a declarative contract. The study does not evaluate whether the underlying research question is true, valuable, creative, safe, unbiased, novel, or scientifically important.

## 3. Precommitted hypotheses

- **H1 — synthetic correctness:** A primary incremental validator and an independently written whole-trace oracle will classify every frozen synthetic trace correctly, agree on the first violating event and violation class, and produce zero false accepts and zero false rejects after at most one bounded correction cycle.
- **H2 — mutation detection:** All twenty frozen contamination mutations will be rejected at their precommitted first violating event. No protected mutation may be accepted.
- **H3 — historical transfer:** After the synthetic gate passes and validator code is frozen, the same generic rules will reproduce the frozen expected dispositions of four Study 001 and Study 002 historical traces without code changes, filename checks, candidate IDs, or study-specific branches.
- **H4 — nontriviality beyond ordering:** The full validators will reject at least four frozen invalid traces that a deliberately limited event-kind ordering baseline accepts because it ignores scope, numeric cap usage, artifact digests, invalidation state, or authorization-token consumption.

Failure to support any hypothesis is an acceptable result if it is recorded without changing the corpus, expected verdicts, dependency classes, or validators after protected evaluation begins.

## 4. What this study is not

Study 003, if activated, is not:

- a continuation or repair of Study 001 or Study 002;
- a new generated-game corpus;
- a retroactive shallow-search instrument;
- a proof that a valid trace contains true or good research;
- a general workflow engine, security product, compliance certification, or publication system;
- an evaluation of human subjects or third-party projects;
- an excuse to add permanent meta-research without a bounded artifact and stop rule.

## 5. Declarative domain

### 5.1 Contract

A contract is frozen before its trace is evaluated. It declares:

- named artifacts and protected observations;
- dependency relationships between events;
- authorization scopes and whether a token is single-use;
- resource caps and the execution they govern;
- evidence sets and their dependencies;
- correction and disclosure requirements;
- cycle boundaries and approval-token consumption.

Contract declarations are data. Validator code may not contain contract-specific artifact names, study numbers, candidate IDs, commit SHAs, filenames, or expected verdicts.

### 5.2 Trace

A trace is a finite ordered list. Each event has:

- a zero-based sequence index;
- an event kind;
- a subject identifier;
- optional scope, token, digest, amount, limit, evidence-set, defect, correction, and reference fields;
- no semantic dependence on wall-clock timestamps.

The proposed event vocabulary is frozen to:

- `begin_cycle`;
- `end_cycle`;
- `freeze_artifact`;
- `set_cap`;
- `begin_execution`;
- `finish_execution`;
- `observe`;
- `authorize`;
- `external_action`;
- `record_defect`;
- `invalidate_evidence`;
- `apply_correction`;
- `disclose_correction`;
- `accept_evidence`.

Activation may refine field typing and serialization but may not add a new semantic event kind after validator execution begins. If this vocabulary cannot represent the frozen corpus, the proposal fails rather than expanding after results.

### 5.3 Verdict

Each validator returns:

- `valid` or `invalid`;
- the first violating sequence index, or `null`;
- one frozen violation class, or `null`;
- a stable machine-readable reason code;
- the contract and trace digests.

Later violations do not replace the first violation.

## 6. Frozen dependency classes

The active protocol must implement all six classes below.

### D1. Artifact before protected observation

Every artifact referenced by a protected `observe` event must have been frozen with a digest earlier in the same admissible evidence lineage.

### D2. Scoped authorization before external action

Every `external_action` must reference an authorization token issued earlier for the exact action scope. A single-use token is consumed by its first matching action and cannot be reused.

### D3. Cap before execution and cap compliance

A governing cap must be frozen before `begin_execution`. The cap may not be changed after execution begins, and the amount recorded by `finish_execution` must not exceed it.

### D4. Correction disclosure before evidence acceptance

When a defect affects an evidence set, corrected evidence cannot be accepted until the defect is recorded, affected evidence is invalidated, the correction is applied, the required rerun or re-observation is complete, and the correction is disclosed.

### D5. Post-observation artifact immutability

An artifact digest used by protected evidence may not change silently. A changed artifact requires invalidation of dependent evidence, a new frozen digest, and any contract-required rerun before replacement evidence can be accepted.

### D6. Bounded-cycle authorization

Each `begin_cycle` requires a fresh matching approval token. Approval tokens are consumed at cycle start, cycles may not overlap, and a later cycle cannot reuse an earlier token.

These classes include ordering constraints but are not reducible to event-name ordering alone. Scope equality, token state, numeric usage, digest identity, evidence invalidation, and correction lifecycle are part of the frozen semantics.

## 7. Frozen synthetic corpus design

The proposal freezes the exact inventory, symbolic event sequences, expected verdicts, and mutation rules. Machine-readable fixture files are not created until activation cycle 1.

### 7.1 Symbolic notation

The machine-readable form must preserve the following semantics:

- `BC(c,p)` — begin cycle `c` using approval token `p`;
- `EC(c)` — end cycle;
- `FA(a,h)` — freeze artifact `a` at digest `h`;
- `SC(r,n)` — set execution `r` cap to `n`;
- `BE(r)` / `FE(r,n)` — begin and finish execution with usage `n`;
- `OB(o,a)` — protected observation `o` referencing artifact `a`;
- `AU(t,s)` — issue single-use authorization token `t` for scope `s`;
- `EA(s,t)` — perform external action in scope `s` with token `t`;
- `RD(d,e)` — record defect `d` affecting evidence set `e`;
- `IE(e)` — invalidate evidence set `e`;
- `AC(d,a,h)` — apply correction for defect `d`, changing artifact `a` to digest `h`;
- `DC(d)` — disclose correction for defect `d`;
- `AE(e)` — accept evidence set `e`.

### 7.2 Twelve minimal traces

Each dependency class has one hand-audited valid and one hand-audited invalid trace.

| ID | Sequence | Expected verdict |
|---|---|---|
| `P1-V` | `BC(c1,p1), FA(a,h1), OB(o,a), AE(e), EC(c1)` | valid |
| `P1-I` | `BC(c1,p1), OB(o,a), FA(a,h1), AE(e), EC(c1)` | invalid at `OB`, D1 |
| `P2-V` | `BC(c1,p1), AU(t,s1), EA(s1,t), EC(c1)` | valid |
| `P2-I` | `BC(c1,p1), AU(t,s1), EA(s2,t), EC(c1)` | invalid at `EA`, D2 |
| `P3-V` | `BC(c1,p1), SC(r,100), BE(r), FE(r,100), EC(c1)` | valid |
| `P3-I` | `BC(c1,p1), SC(r,100), BE(r), FE(r,101), EC(c1)` | invalid at `FE`, D3 |
| `P4-V` | `BC(c1,p1), FA(a,h1), OB(o1,a), RD(d,e1), IE(e1), AC(d,a,h2), FA(a,h2), OB(o2,a), DC(d), AE(e2), EC(c1)` | valid |
| `P4-I` | `BC(c1,p1), FA(a,h1), OB(o1,a), RD(d,e1), IE(e1), AC(d,a,h2), FA(a,h2), OB(o2,a), AE(e2), EC(c1)` | invalid at `AE`, D4 |
| `P5-V` | `BC(c1,p1), FA(a,h1), OB(o1,a), RD(d,e1), IE(e1), AC(d,a,h2), FA(a,h2), OB(o2,a), DC(d), EC(c1)` | valid |
| `P5-I` | `BC(c1,p1), FA(a,h1), OB(o1,a), RD(d,e1), AC(d,a,h2), FA(a,h2), OB(o2,a), DC(d), EC(c1)` | invalid at `AC`, D5 |
| `P6-V` | `BC(c1,p1), EC(c1), BC(c2,p2), EC(c2)` | valid |
| `P6-I` | `BC(c1,p1), EC(c1), BC(c2,p1), EC(c2)` | invalid at second `BC`, D6 |

The active protocol must supply the minimal contract declarations needed to make these symbolic expectations exact. It may not alter the sequences or verdicts.

### 7.3 Four composite valid traces

Four composite traces, `C1-V` through `C4-V`, use the same frozen nineteen-event template with four fixed parameter sets.

Template:

1. `BC(c_i,p_i)`
2. `FA(a_i,h1_i)`
3. `SC(r_i,L_i)`
4. `BE(r_i)`
5. `FE(r_i,U_i)`
6. `OB(o1_i,a_i)`
7. `AU(t_i,s_i)`
8. `EA(s_i,t_i)`
9. `RD(d_i,e1_i)`
10. `IE(e1_i)`
11. `AC(d_i,a_i,h2_i)`
12. `FA(a_i,h2_i)`
13. `SC(rr_i,RL_i)`
14. `BE(rr_i)`
15. `FE(rr_i,RU_i)`
16. `OB(o2_i,a_i)`
17. `DC(d_i)`
18. `AE(e2_i)`
19. `EC(c_i)`

Fixed parameters:

| Trace | `L/U` | `RL/RU` | Authorization scope |
|---|---:|---:|---|
| `C1-V` | 100 / 60 | 100 / 55 | `repository-write` |
| `C2-V` | 50 / 49 | 50 / 45 | `external-message` |
| `C3-V` | 1000 / 700 | 1000 / 650 | `permission-change` |
| `C4-V` | 30 / 30 | 30 / 20 | `publication-submit` |

All four are expected valid. The scope names are synthetic data and do not authorize real external action.

### 7.4 Twenty deterministic contamination mutations

Apply each of the five mutations below exactly once to each composite trace. The result is twenty invalid traces.

1. **Prerequisite omission:** remove event 2, `FA(a_i,h1_i)`. Expected first violation: event `OB(o1_i,a_i)`, D1.
2. **Adjacent dependency inversion:** swap events 3 and 4 so `BE(r_i)` occurs before `SC(r_i,L_i)`. Expected first violation: `BE(r_i)`, D3.
3. **Unauthorized insertion:** insert `EA(s_i + "/extra", none)` immediately after the authorized `EA(s_i,t_i)`. Expected first violation: the inserted event, D2.
4. **Cap violation:** change event 5 usage from `U_i` to `L_i + 1`. Expected first violation: `FE(r_i,L_i+1)`, D3.
5. **Undisclosed correction:** remove event 17, `DC(d_i)`. Expected first violation: `AE(e2_i)`, D4.

Synthetic corpus total:

- 12 minimal traces;
- 4 composite valid traces;
- 20 deterministic mutants;
- **36 traces total**;
- 10 valid and 26 invalid.

If machine-readable generation does not yield exactly these counts and expected first violations, Study 003 fails its setup gate. No replacement fixture may be invented after validator execution begins.

## 8. Frozen order-only baseline

To guard against a trivial topological-sort result, implement a deliberately limited baseline that checks only whether a required event kind appears somewhere earlier in the trace. It ignores subject identity, authorization scope, token consumption, numeric cap usage, digests, evidence lineage, and correction state.

The baseline is expected to accept, while both full validators reject, at least these four frozen invalid traces:

- `P2-I` — wrong authorization scope;
- `P3-I` — usage exceeds a correctly ordered cap;
- `P5-I` — artifact changes without evidence invalidation;
- `P6-I` — approval token reuse.

It is also expected to accept the four cap-violation mutants and may accept additional invalid traces. If the order-only baseline rejects every invalid trace, the corpus is too trivial and H4 fails.

The baseline is not an oracle and does not contribute to correctness agreement.

## 9. Independent validators

### 9.1 Primary validator

The primary validator is an incremental state machine. It processes events in sequence and tracks artifact digests, evidence lineage, outstanding defects, correction disclosure, authorization scope and consumption, caps and usage, active cycles, and consumed approval tokens.

### 9.2 Independent oracle

The oracle evaluates the completed trace using separately written whole-trace predicates and direct searches over event prefixes. It must not import or call the primary transition function, state representation, violation-selection helper, reason-code helper, or verdict code.

The two validators may share only:

- the frozen JSON field names;
- primitive scalar conventions;
- the contract and trace files as input.

They must parse their inputs independently. Shared test expectations do not count as implementation independence.

### 9.3 Freeze boundary

Both validator implementations and the order-only baseline must be committed before any historical trace is encoded or evaluated. After the synthetic gate passes, validator logic is frozen. Historical mismatches may not be repaired inside Study 003.

## 10. Synthetic correctness gate

For all 36 synthetic traces, record:

- expected and actual verdict;
- expected and actual first violating index;
- expected and actual violation class;
- primary/oracle agreement;
- order-only baseline verdict;
- trace and contract digests.

Required gate result:

- zero false accepts;
- zero false rejects;
- 100% first-violation-index accuracy;
- 100% violation-class accuracy;
- 100% primary/oracle agreement;
- all twenty mutations rejected;
- exactly five mutation operators represented four times each;
- the four named nontrivial invalid traces accepted by the order-only baseline and rejected by both full validators;
- zero study-specific or filename-specific branches in validator code.

If the first implementation fails, one bounded correction cycle is permitted without changing the corpus, contracts, expected verdicts, dependency classes, or metrics. Continued disagreement or classification error after that cycle closes the study as a negative instrument result.

## 11. Frozen historical transfer set

Historical traces are encoded and evaluated only after the synthetic gate passes and validator code is frozen. The proposal freezes four cases and their expected dispositions.

### `H1-SPAN-FORMAL-VALID`

Source: Study 001 Span v0.2 formal-screen records.

Expected sequence semantics:

- cycle approval precedes repository execution;
- formal experiment artifact is committed before results;
- game counts and depth are frozen before execution;
- completed output is observed and repeated;
- evidence is accepted after the repeated result.

Expected verdict: **valid**.

### `H2-EXACT-SUBSTUDY-VALID`

Source: Study 002 exact-screen proposal, manifest, instrument audit, and exact experiment records.

Expected sequence semantics:

- proposal, manifest, solver, and resource caps are frozen before exact execution;
- exact execution completes or records a cap;
- exact results are observed and accepted only for the exact-analysis subclaim.

Expected verdict: **valid**.

### `H3-STUDY002-SHALLOW-CONTAMINATED`

Source: Study 002 frozen proposal and cycle-4 procedural audit.

The contract declares `freeze_artifact(shallow_heuristic)` as a prerequisite of protected `observe(exact_results)` because the heuristic had to exist before exact inspection for the shallow-versus-exact comparison.

Expected verdict: **invalid** at `observe(exact_results)`, D1.

The validator may not mention Study 002, shallow search, exact games, candidate IDs, or repository paths in its rule code. The dependency exists only in the historical contract data.

### `H4-EXACT-PROJECTION-CORRECTION-VALID`

Source: Study 002 exact-screen reproducibility correction records.

Expected sequence semantics:

- projection defect is recorded;
- affected reproducibility evidence is invalidated;
- a corrected comparator is frozen;
- deterministic comparison is rerun;
- the correction is disclosed before the corrected evidence is accepted.

Expected verdict: **valid**.

### Historical transfer rule

Historical event sequences and contract files must cite their repository source paths and commits. They may use only the frozen event vocabulary. After the first historical trace is encoded, no validator or synthetic fixture change is permitted. Any expected-verdict mismatch, need for a new semantic event kind, or need for an identifier-specific exception is a historical-transfer failure and is reported without repair.

## 12. Metrics

Report at minimum:

1. synthetic valid traces accepted;
2. synthetic invalid traces rejected;
3. false accepts and false rejects;
4. first-violation-index accuracy;
5. violation-class accuracy;
6. primary/oracle agreement;
7. mutation operators covered and mutants rejected;
8. order-only baseline false accepts;
9. historical expected-verdict matches;
10. historical first-violation matches;
11. validator special-case count;
12. byte-identical report reproduction across two runs.

No weighted aggregate score may hide an individual protected false accept.

## 13. Success, failure, and stopping rules

### Methodological success

Study 003 succeeds only if:

- the 36-trace synthetic corpus is generated exactly as frozen;
- both full validators pass the entire synthetic correctness gate;
- all twenty contamination mutations are rejected at the frozen first violation;
- H4's four named beyond-ordering cases are demonstrated;
- all four historical traces match their frozen expected dispositions without validator changes or special cases;
- two complete validation runs produce byte-identical deterministic reports;
- the study closes within the four-cycle limit.

### Immediate or terminal failure conditions

Close as negative or incomplete if any of the following occurs:

- the frozen corpus cannot be represented without changing an event kind or expected verdict;
- any protected invalid trace is accepted after the one allowed correction cycle;
- any valid synthetic trace is rejected after the one allowed correction cycle;
- primary and oracle disagree after the one allowed correction cycle;
- first-violation or class accuracy is below 100% after the correction cycle;
- the validator contains a Study 001/002/003, candidate, commit, filename, or trace-ID-specific verdict branch;
- historical encoding requires an ad hoc exception or a validator change;
- the order-only baseline is not materially weaker on the four frozen nontrivial cases;
- deterministic reproduction fails and cannot be isolated without changing semantics;
- completion requires external services, paid compute, third-party action, or materially human-authored verdicts;
- four approval cycles after activation are exhausted.

The study may not expand its corpus, add dependency classes, alter expected historical outcomes, or substitute a looser metric after a failure.

## 14. Resource boundaries

- Standard-library-only implementation.
- Exactly 36 synthetic traces and 4 historical traces.
- At most 40 events per trace.
- At most 1,600 total evaluated events per complete run.
- Two complete deterministic runs after the relevant gate.
- No network access, external services, paid compute, background task, third-party repository action, or human-subject activity.
- Maximum **four approval-driven execution cycles after activation**, including final synthesis.

These limits are not performance benchmarks. They prevent a small integrity study from becoming a workflow-platform project.

## 15. Four-cycle activation plan

### Cycle 1 — schema and corpus freeze

- activate the unchanged proposal as the active protocol;
- implement only the trace and contract schema, canonical serialization, and deterministic fixture generator;
- generate exactly 36 synthetic traces from this proposal;
- freeze expected verdicts, first violations, mutation inventory, and the order-only baseline specification;
- test serialization and byte-identical regeneration;
- do not implement validator verdict logic or encode historical traces.

### Cycle 2 — validators and first synthetic gate

- implement the primary state-machine validator;
- independently implement the whole-trace oracle;
- implement the frozen order-only baseline;
- run the first synthetic correctness gate;
- freeze the implementations if the gate passes;
- do not encode historical traces before the gate result exists.

### Cycle 3 — correction or historical transfer

- if cycle 2 fails, use this as the single permitted correction cycle, rerun the unchanged synthetic gate, and close negative if any required condition still fails;
- if the synthetic gate passes, freeze validator code, encode the four historical traces from their cited sources, and evaluate them without code changes;
- if cycle 2 passed initially, cycle 3 is historical transfer only;
- no historical mismatch may be repaired.

### Cycle 4 — reproduction, synthesis, and closure

- reproduce the accepted synthetic and historical reports in a second complete run;
- compare deterministic output byte-for-byte;
- classify H1–H4;
- record limits, failures, interventions, and any correction;
- close Study 003 as successful, negative, or incomplete;
- do not begin Study 004 in the same cycle.

## 16. Claims explicitly out of scope

Study 003 will not claim that a validator-approved trace is:

- true or scientifically sound;
- valuable or worth pursuing;
- unbiased;
- safe or lawful in contexts beyond the encoded authorization contract;
- novel;
- creative;
- autonomous;
- reproducible outside the recorded artifacts;
- secure against maliciously crafted input;
- a substitute for human judgment, consent, peer review, or legal review.

The strongest permitted claim is that, on the frozen corpus and historical transfer set, the validators consistently enforced the specified sequence, scope, cap, artifact, correction, and cycle commitments.

## 17. Intervention model

- A plain project-chat `承認` is A1 access assistance for one bounded cycle.
- Templex selects implementation, debugging, interpretation, failure diagnosis, and stopping decisions within the frozen protocol.
- Any human change to dependency classes, corpus, expected verdicts, metrics, or conclusion is recorded according to its actual A2–A4 effect.
- External communication, publication, spending, permission changes, third-party action, and human-subject activity remain separately gated.

## 18. Planned artifacts after activation

- `research/studies/003-protocol-integrity/PROTOCOL.md`;
- machine-readable contract and trace schema;
- frozen 36-trace synthetic corpus;
- primary incremental validator;
- independent whole-trace oracle;
- order-only baseline;
- deterministic tests and reports;
- four historical trace encodings with source citations;
- final analysis and report;
- state and intervention records.

## 19. Activation decision required

A later approval cycle must re-read this proposal and independently choose one of:

- **GO:** activate Study 003 without changing the proposal;
- **NO-GO:** remain inactive because the design is tautological, insufficiently independent, overfit to known history, or not worth the execution cost;
- **REVISE BEFORE ACTIVATION:** correct a factual or internal specification error while preserving the fact that no experiment has begun, then require another activation decision.

No implementation or active-study issue exists at proposal freeze. The laboratory remains inactive until that later decision.