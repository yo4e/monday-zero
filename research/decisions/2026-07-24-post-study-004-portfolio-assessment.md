# Post-Study-004 Portfolio Assessment

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **GO to one frozen proposal; no active study**_

## 1. Decision

TEMPLEX/0 should remain without an active study while preserving one frozen, inactive proposal for a possible Study 005 on **IANA time-zone transition round-trip conformance**.

The selected direction asks whether a version-pinned transition corpus derived from the public-domain IANA Time Zone Database can expose disagreements or boundary failures in Python `zoneinfo` UTC-to-local projection, repeated-time `fold` handling, local-to-UTC round trips, and nonexistent-local-time detection.

This cycle creates the portfolio decision and frozen proposal only. It does not activate Study 005, download or vendor tzdb data, compile a time-zone database, implement code, create an active-study issue, inspect transition outcomes, or execute an experiment.

## 2. Evidence carried forward

The decision is grounded in all four closed studies.

- Study 001 showed that aggregate behavior can conceal short constructive defects and that decisive counterexamples are more valuable than larger repetitions of a misleading summary statistic.
- Study 002 showed that exact structural analysis can reveal false reassurance, while also demonstrating that protected dependencies must be ordered before result inspection rather than merely named.
- Study 003 showed that machine-readable procedural constraints can be enforced reproducibly, but a valid trace cannot establish that the underlying research question, contract, or evidence is substantively good.
- Study 004 produced a valid partial result but failed its central prediction: transition-coverage guidance did not outperform equal-budget uniform random testing at the frozen threshold. Its reducer hypothesis was also left unresolved by an unfrozen multi-output aggregation rule. The complete benchmark was synthetic and designed by the same operator that designed the methods.

The next direction should therefore not reward TEMPLEX/0 for creating another closed formal world whose data, methods, expectations, and interpretation are all self-authored. It should retain executable witnesses, independent parsing, frozen sequencing, and hard stop rules while introducing an authoritative external referent and a practically used interface.

## 3. Decision standard

Each active direction was scored from 0 to 5 on six criteria required by the restart state:

1. information value for TEMPLEX/0;
2. falsifiability or auditability;
3. independence from prior studies and self-authored benchmark semantics;
4. feasibility under current repository, tool, permission, and licensing limits;
5. clarity of stopping conditions;
6. likely reusable contribution.

A direction could displace inactivity only if it:

- scored at least **25 of 30**;
- had no criterion below **4**;
- used an external referent not authored by TEMPLEX/0;
- had a sufficiently clear permission and provenance boundary for a frozen proposal;
- admitted a concrete negative result;
- could be frozen without beginning implementation or experiment execution in this cycle.

Scores are explicit research judgments, not empirical measurements.

## 4. Bounded feasibility evidence

This portfolio cycle performed source and local-capability checks only. They are readiness evidence, not Study 005 results.

### 4.1 IANA tzdb and Python `zoneinfo`

- IANA lists **tzdb 2026c**, released on 2026-07-08, as the current release inspected in this cycle.
- IANA states that the Time Zone Database is in the public domain.
- The official 2026c release notes record current civil-time changes and implementation fixes, confirming that the database is a maintained external referent rather than a static toy corpus.
- Python documents `zoneinfo` as an implementation backed by IANA time-zone data and documents PEP 495 `fold=0` / `fold=1` semantics for ambiguous local times.
- The available execution environment exposed Python 3.13.5, `zoneinfo`, 599 discoverable zone keys, and local `zic` and `zdump` commands from glibc 2.41.

These observations support proposal feasibility. They do not guarantee that the same tools, versions, network access, or source bytes will be available during activation.

Primary references inspected:

- `https://www.iana.org/time-zones`
- `https://data.iana.org/time-zones/releases/`
- `https://data.iana.org/time-zones/tz-link.html`
- `https://docs.python.org/3/library/zoneinfo.html`
- `https://peps.python.org/pep-0495/`
- `https://peps.python.org/pep-0615/`

### 4.2 NIST Statistical Reference Datasets

NIST Statistical Reference Datasets would provide externally certified numerical-analysis targets and strong falsifiability. However, NIST's own terms distinguish Standard Reference Data from ordinary public-domain government material and describe possible copyright, licensing, acknowledgement, and redistribution conditions. A plain approval cycle does not authorize TEMPLEX/0 to accept terms or resolve a material licensing ambiguity. This direction therefore fails the current feasibility floor despite high information value.

Primary references inspected:

- `https://www.nist.gov/itl/sed/statistical-reference-datasets-strd`
- `https://www.nist.gov/disclaimer`

### 4.3 Unicode normalization conformance

Unicode publishes a normative normalization algorithm and an official conformance test suite. This direction is legally and technically feasible, but a study that merely runs or re-expresses the official suite would contribute little beyond existing conformance machinery. A stronger independent question was not identified within this cycle without inventing a new self-authored corpus or broadening into an unbounded ecosystem survey.

Primary references inspected:

- `https://www.unicode.org/reports/tr15/`
- `https://www.unicode.org/Public/17.0.0/ucd/NormalizationTest.txt`

## 5. Compared directions

| Direction | Info | Falsifiable | Independent | Feasible | Stop | Contribution | Total | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IANA tzdb transition round-trip conformance | 5 | 5 | 5 | 4 | 5 | 5 | **29** | **GO to frozen proposal** |
| NIST StRD numerical-accuracy replication | 5 | 5 | 5 | 3 | 5 | 5 | 28 | HOLD: feasibility floor fails |
| Unicode normalization conformance and collision atlas | 4 | 5 | 5 | 5 | 5 | 3 | 27 | HOLD: contribution floor fails |
| Prospective project-selection calibration audit | 4 | 3 | 2 | 5 | 4 | 3 | 21 | HOLD |
| Remain inactive | — | — | — | — | — | — | baseline | Viable fallback |

## 6. Why the selected direction passes

### 6.1 It changes the epistemic source

The behavioral rules and transition data originate in the externally maintained IANA database, not in a grammar, mutation family, event language, or expected-result set authored by TEMPLEX/0. The study must pin one public release and distinguish data-version disagreement from implementation disagreement.

### 6.2 It tests boundary semantics, not aggregate prestige

Civil-time conversion contains concrete discontinuities: backward transitions create repeated local times, forward transitions create nonexistent local times, and some shifts are not one hour. These cases admit exact UTC witnesses and reversible checks. A mismatch can be preserved as a timestamp, zone key, source digest, expected transition record, and observed conversion rather than summarized as an attractive score.

### 6.3 It can fail clearly

The study can fail at several protected gates:

- official source provenance or permission cannot be established;
- the source cannot be compiled reproducibly in an isolated directory;
- the independent TZif parser fails frozen fixtures;
- `zoneinfo` disagrees with the pinned transition model;
- fold round trips fail;
- nonexistent-local-time detection produces false valid or false invalid classifications;
- complete results do not reproduce within the four-cycle limit.

A zero-mismatch result is also valid if bounded honestly to the pinned release, runtime, zone set, date range, and tested invariants.

### 6.4 It leaves a reusable artifact under either result

A completed study can leave a version-pinned transition manifest, an independent TZif parser, deterministic boundary witnesses, a fold/gap round-trip validator, a `zoneinfo` comparison harness, and a reproducible result report. These are useful as research and regression fixtures even if no implementation defect is found.

### 6.5 It resists current laboratory failure modes

The direction is formal, but its referent is external. It is not another game corpus, another governance validator, another mutation benchmark, or another retrospective self-description. It also creates a practical software artifact rather than treating methodological elegance as the result.

## 7. Why the other directions do not pass now

### NIST StRD numerical accuracy — HOLD

This is the strongest rejected candidate. It would test numerical software against externally certified values and could produce precise error profiles. It does not pass because the inspected official terms create a material license and redistribution boundary that TEMPLEX/0 cannot settle or accept under an ordinary approval. The direction may be reconsidered only after a separate human-reviewed licensing decision or a clearly public-domain substitute.

### Unicode normalization — HOLD

The official suite already defines broad conformance tests. Running it against one runtime would be easy and auditable but would mostly duplicate an existing mechanism. A cross-runtime or corpus-scale collision study would require a more distinctive bounded question, version alignment, and additional implementations not yet established.

### Project-selection calibration — HOLD

Four completed studies now provide more history than the previous portfolio assessment had, but they remain heterogeneous, and the same operator would still define the value labels, forecasts, and retrospective interpretation. A prospective calibration ledger may be useful infrastructure later, but it is not the highest-value next study and does not clear independence or falsifiability floors.

### Remaining inactive — viable baseline

Inactivity remains preferable to a weak successor. The selected direction displaces it because it is externally anchored, falsifiable, internally bounded, permission-compatible at the proposal stage, and capable of producing reusable executable evidence.

## 8. Final disposition

**GO to one frozen proposal, created in this same portfolio cycle and kept inactive.**

- Studies 001 through 004 remain closed.
- Study 005 is proposed but not active.
- No implementation, source download, compiled data, experiment, issue, external message, third-party repository operation, or new publication channel is created by this decision.
- A later `承認` must independently inspect the frozen proposal and choose activation **GO unchanged** or **NO-GO**.
