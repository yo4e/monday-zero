# Proposed Study 005 — TZDB Transition Round-Trip Conformance

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **Frozen proposal — not active**_

## 1. Go / no-go status

**GO to a separately gated activation decision.**

This proposal does not activate Study 005, create an active-study issue, download or vendor tzdb source, compile zone files, implement a parser or harness, inspect the full transition corpus, or run an experiment. TEMPLEX/0 remains without an active study.

A later project-chat `承認` must re-read the live repository and make an independent activation **GO unchanged** or **NO-GO** decision. If activated unchanged, the study may perform Cycle 1 only.

The proposal follows `research/decisions/2026-07-24-post-study-004-portfolio-assessment.md`.

## 2. Research question

> Can a version-pinned transition corpus derived from IANA tzdb 2026c verify Python `zoneinfo` UTC-to-local projection, repeated-time `fold` handling, exact UTC round trips, and nonexistent-local-time detection at civil-time discontinuities using an independently implemented TZif reader?

The unit of analysis is one named canonical zone and one explicit transition record compiled from the pinned tzdb source. Boundary witnesses are UTC instants and local wall times immediately before, at, and after an offset transition.

The study evaluates conformance and regression properties for one pinned data release, runtime, compiler environment, zone inventory, date interval, and set of invariants. It does not attempt to establish the historical or political truth of tzdb, certify Python, compare all language runtimes, or predict future civil-time legislation.

## 3. Externally pinned referent

The source release is fixed now as:

- project: **IANA Time Zone Database**;
- release: **tzdb 2026c**;
- release date recorded by IANA: **2026-07-08**;
- source archive name: `tzdata2026c.tar.gz`;
- official release directory: `https://data.iana.org/time-zones/releases/`;
- public-domain statement: `https://data.iana.org/time-zones/tz-link.html`.

Activation must retrieve the archive only from an official IANA HTTPS location, record the exact URL, byte count, SHA-256 digest, retrieval time, and archive member listing before extraction. A newer release must not replace 2026c inside this study. Failure to obtain or identify the pinned bytes closes activation as NO-GO or a negative setup result; it does not authorize silent substitution.

The proposal relies on IANA's public-domain statement for tzdb data. Activation must separately inspect any bundled code or documentation licenses before deciding whether those files may be committed. The study may avoid redistribution by committing only source metadata, digests, generated manifests, original TEMPLEX/0 code, and result artifacts when that is sufficient.

## 4. Frozen hypotheses

### H1 — explicit UTC projection agreement

For every frozen boundary witness around every explicit transition in the corpus, Python `zoneinfo` reading the isolated tzdb 2026c compilation will agree with the independent TZif reader on:

- UTC offset;
- daylight-saving offset where represented;
- time-zone abbreviation;
- local calendar date and clock time.

Witnesses are the UTC seconds `t-1`, `t`, and `t+1` for transition instant `t`, plus the exact midpoints of the stable UTC intervals adjacent to the transition when those intervals intersect the frozen date range.

**Support criterion:** zero field disagreements across the complete frozen witness set.

A disagreement is not automatically a Python defect. It must first be classified as parser error, compilation mismatch, data-path mismatch, unsupported format interpretation, or unresolved implementation disagreement.

### H2 — backward-transition fold round trip

For every transition whose post-transition UTC offset is smaller than its pre-transition offset, the repeated local interval will be sampled at:

- its first representable second;
- its midpoint using integer floor division;
- its last representable second.

For each repeated wall time, the two UTC instants implied by the pre- and post-transition offsets must satisfy all of the following:

1. both UTC instants convert through `zoneinfo` to the same naive local wall time;
2. the earlier occurrence has `fold == 0`;
3. the later occurrence has `fold == 1`;
4. attaching the same zone and the corresponding fold value to the wall time converts back to the original UTC instant exactly.

**Support criterion:** all assertions pass for every frozen backward-transition sample.

### H3 — forward-transition gap detectability

For every transition whose post-transition UTC offset is larger than its pre-transition offset, the nonexistent local interval will be sampled at:

- its first nonexistent second;
- its midpoint using integer floor division;
- its last nonexistent second.

The frozen validator will classify a naive wall time as valid only when at least one of the two `fold` assignments survives an exact local-to-UTC-to-local round trip with the same wall fields and the same fold interpretation. It must satisfy:

1. every frozen interior gap sample is classified nonexistent;
2. the last valid local second before the gap is classified valid;
3. the first valid local second after the gap is classified valid;
4. no gap is assumed to be exactly one hour.

**Support criterion:** zero false-valid and zero false-invalid classifications across the complete frozen gap-boundary set.

This hypothesis tests the explicitly frozen round-trip validator, not a claim that Python offers a built-in nonexistent-time exception or validation API.

## 5. Frozen behavioral domain

### 5.1 Zone inventory

The primary inventory is every unique zone name present in tzdb 2026c `zone1970.tab`, in file order after comments and blank lines are removed, plus `Etc/UTC` as a no-transition control.

The study excludes aliases and compatibility links from the primary denominator. Links may be checked descriptively only after primary results are complete and may not affect H1–H3.

Activation must freeze:

- the exact `zone1970.tab` bytes and SHA-256;
- the ordered canonical zone list and SHA-256;
- the compiled output tree digest projection;
- any zone omitted because compilation produced no readable TZif file, with the omission treated as a setup failure rather than silently ignored.

### 5.2 Date range

Only explicit TZif transition records with transition instants in the half-open UTC interval

`[1970-01-01T00:00:00Z, 2100-01-01T00:00:00Z)`

belong to the primary corpus.

The primary study does not synthesize transitions from POSIX footer rules beyond the final explicit TZif transition. Footer presence, contents, and the final explicit-transition year must be reported by zone as descriptive metadata.

### 5.3 Time scale and precision

- POSIX seconds are used.
- Leap-second-aware `right/` zone files are excluded.
- Witness precision is one integer second.
- Negative timestamps are outside the primary interval.
- Subsecond behavior is outside scope.

### 5.4 Transition classes

Every retained explicit transition must be classified by offset delta:

- backward shift: delta < 0;
- no-offset transition: delta == 0;
- forward shift: delta > 0.

The report must additionally group nonzero shifts by absolute delta in seconds. No one-hour assumption is permitted in corpus generation, samples, assertions, or summaries.

## 6. Isolated compilation

Activation must compile tzdb 2026c into a study-local, untracked temporary directory before any Python `zoneinfo` comparison. It must not use the host's default `/usr/share/zoneinfo` as the evidence source.

The activation record must freeze:

- `zic` executable path and version output;
- complete command line;
- source file list and order;
- compilation environment fields that can affect output;
- output file inventory;
- deterministic digest projection over relative paths and bytes.

The intended command family is the installed `zic` compiler with explicit output directory and the ordinary civil-time source set. Cycle 1 may choose the exact compatible flags only before compilation and must record why. It may not alter source rules or remove inconvenient zones.

Two clean compilations must produce the same digest projection before the study advances. If they do not, the study closes as a negative setup result unless one bounded, disclosed correction identifies a non-semantic source of nondeterminism before any full transition outcomes are inspected.

## 7. Independent TZif reader

The primary reference instrument is an original, standard-library-only TZif reader implemented without importing Python `zoneinfo` internals or copying its parser.

It must read the compiled binary files and expose, at minimum:

- TZif version;
- ordered explicit transition timestamps;
- transition type indexes;
- UTC offsets;
- DST flags;
- abbreviations;
- footer bytes or parsed footer text as metadata;
- pre-first-transition type under the frozen interpretation;
- deterministic canonical serialization.

The reader must reject malformed indexes, truncated blocks, impossible abbreviation offsets, unsupported versions, and inconsistent count fields rather than manufacturing partial values.

### 7.1 Correctness fixtures

Before the full corpus is parsed, Cycle 1 must freeze at least twelve hand-audited fixture expectations drawn from the compiled 2026c files and independent command output. They must cover:

- a no-transition UTC control;
- a conventional one-hour backward shift;
- a conventional one-hour forward shift;
- a non-one-hour backward shift;
- a non-one-hour forward shift if present in the pinned corpus;
- a large civil-time discontinuity if present;
- an abbreviation-only transition if present;
- a zone with a POSIX footer;
- a zone with multiple historical type records;
- transitions on both sides of the year 2000;
- at least one negative UTC offset;
- at least one positive UTC offset.

Fixture expectations must include exact zone names, transition timestamps, adjacent type fields, and source-command evidence. `zdump` may be used as a secondary fixture reference, but it is not the full-corpus oracle and may not replace direct TZif parsing.

### 7.2 Parser gate

The reader must match all frozen fixtures exactly. At most one bounded correction cycle is allowed before full-corpus manifest generation. Any unresolved fixture mismatch closes the study without running the Python comparison.

After the gate passes, the reader source, fixture set, fixture expectations, and canonical serialization must be frozen before the full transition manifest is generated.

## 8. Python `zoneinfo` harness

The comparison harness must load only the isolated compiled tree by an explicitly recorded `zoneinfo` data path. It must verify that the requested zone key resolves from that tree and not silently fall back to host tzdata or a separately installed package.

The harness must record:

- Python implementation and version;
- `zoneinfo.TZPATH` before and after isolation;
- isolated tree digest projection;
- zone key;
- transition identifier;
- every UTC and local witness;
- expected fields from the frozen manifest;
- observed fields from `zoneinfo`;
- fold values;
- round-trip UTC results;
- classification and reason for every mismatch.

It may use public `zoneinfo` APIs only. It may not inspect CPython private parser state or substitute host `date`, system library conversion, or `zdump` output for the observed Python result.

## 9. Protected sequencing

After activation, the protected order is:

1. verify official source provenance, public-domain status, archive identity, and local tool availability;
2. record the active protocol unchanged from this proposal except for paths, typing, and compatible command flags;
3. extract and compile tzdb 2026c twice in isolated directories;
4. freeze source, command, compilation, zone-list, and fixture artifacts without parsing the full corpus through the new reader;
5. implement the independent TZif reader and fixture gate;
6. freeze the passing reader and generate the complete transition manifest;
7. implement and freeze the `zoneinfo` comparison and round-trip harness using only fixtures and synthetic miniature TZif-independent cases;
8. execute the complete frozen corpus once;
9. repeat from clean generated artifacts, compare deterministic projections, analyze, report, and close.

The study becomes invalid rather than retroactively repaired if:

- the full `zoneinfo` outcome set is inspected before the comparison rules and hypotheses are frozen;
- source release, zone inventory, date range, transition inclusion, witness selection, or success criteria change after full execution begins;
- mismatching zones or transitions are removed after observation;
- host-zone data is substituted for the isolated 2026c tree without disclosure;
- a newer tzdb release is substituted for 2026c.

## 10. Metrics and required artifacts

The final report must include:

- source URL, retrieval metadata, archive byte count, and SHA-256;
- source and compiled-tree inventories and digest projections;
- compiler and Python versions;
- ordered zone count;
- readable TZif file count;
- explicit transition count in range;
- transition counts by backward, zero-delta, and forward class;
- offset-delta distribution in seconds;
- witness counts by type;
- H1 comparison count and all disagreement fields;
- H2 repeated-time sample count and all fold or round-trip failures;
- H3 gap sample count, adjacent-valid count, false-valid count, and false-invalid count;
- parser fixture results;
- zones with footer rules and final explicit-transition years;
- complete machine-readable mismatch records;
- deterministic result digests for two runs;
- H1–H3 dispositions without threshold revision.

Required reusable artifacts are:

- source provenance record;
- compilation manifest;
- independent TZif reader;
- frozen transition manifest;
- deterministic witness generator;
- `zoneinfo` comparison harness;
- fold/gap round-trip validator;
- targeted tests;
- complete result data;
- final report and cycle audits.

## 11. Disposition rules

### Full bounded success

All of the following must hold:

- source and permission preflight passes;
- two isolated compilations match under the frozen digest projection;
- all canonical zone files are readable;
- the parser fixture gate passes;
- protected sequencing remains intact;
- H1, H2, and H3 are supported;
- the complete deterministic result projection reproduces byte-identically;
- the study closes within four approval cycles.

### Partial result

The study is partial if setup and parser gates pass and the complete comparison is valid, but one or more of H1–H3 is unsupported or unresolved without invalidating the remaining evidence.

### Negative setup result

The study closes before full comparison if:

- official source identity or the permission boundary cannot be established;
- the pinned archive cannot be obtained;
- isolated compilation cannot be reproduced;
- one or more primary canonical zone files cannot be compiled or read;
- the parser gate fails after the single permitted correction opportunity;
- data-path isolation cannot be demonstrated;
- protected sequencing is contaminated before a valid complete run.

### Operationally incomplete

The study closes as operationally incomplete if it cannot produce and repeat complete results within the cycle and resource caps. Partial output may be preserved but must not be represented as a complete corpus result.

## 12. Resource and cycle limits

From activation through closure, Study 005 has a maximum of **four approval cycles**:

1. activation, source and permission preflight, isolated compilation, zone inventory, and frozen parser fixtures;
2. independent TZif reader, fixture gate, and frozen transition manifest;
3. `zoneinfo` harness freeze and complete formal execution;
4. clean reproduction, analysis, final report, and closure.

No fifth cycle may be added. The active protocol may impose lower command, memory, file-size, and runtime caps before execution, but may not relax the four-cycle limit or alter the frozen question and hypotheses.

The implementation should remain standard-library-only. It may invoke the already available local `zic` and `zdump` commands after recording their identity. It may not use paid services, external compute accounts, third-party repository changes, private data, secrets, or human subjects.

## 13. Verification requirements

Every applicable cycle must record:

- targeted deterministic tests;
- parser fixture comparison;
- clean compilation reproduction;
- canonical serialization reproduction;
- compile or syntax verification of original code;
- source/blob identity checks through the repository connector;
- complete deterministic projection comparison;
- explicit fresh-checkout and full-regression status;
- all corrections and excluded evidence.

A connector-backed source check is not a fresh checkout. A functional reconstruction must not be described as a byte-identical repository replay.

## 14. Claims not supported

Even full bounded success would not establish that:

- tzdb 2026c is historically, geographically, legally, or politically correct;
- Python `zoneinfo` is correct for all releases, platforms, runtimes, compilers, or data sources;
- no untested datetime defect exists;
- future civil-time rules are known;
- POSIX footer extrapolation is correct;
- pre-1970 data is complete or accurate;
- leap-second behavior is correct;
- Windows time-zone APIs or mappings agree;
- local-time arithmetic is generally safe;
- the round-trip validator is a production authorization, scheduling, billing, legal-deadline, or safety system;
- a recorded disagreement is a Python defect before parser, compiler, source, and data-path alternatives are eliminated.

## 15. Human intervention boundary

A plain activation `承認` is A1 access assistance. The human does not select zones, transitions, witnesses, parser results, mismatch classifications, hypothesis dispositions, or conclusions.

A separate explicit human decision is required before accepting terms, resolving a material licensing ambiguity, contacting IANA or Python maintainers, filing an external bug report, changing repository visibility, publishing through a new channel, or presenting the result as a validated defect disclosure.

Any human change to the source version, research question, zone inventory, date range, hypotheses, criteria, result interpretation, or public framing must be recorded at its actual A-level.

## 16. Activation decision

A later approval must choose one of:

- **GO unchanged:** activate this proposal as the Study 005 protocol and perform Cycle 1 only;
- **NO-GO:** record why the proposal does not justify activation and remain inactive.

Activation may clarify repository paths, type annotations, temporary-directory layout, exact compatible `zic` flags, serialization field names, and test organization before outcome inspection. It may not change the pinned tzdb release, research question, zone inventory rule, date range, hypotheses, witness semantics, parser independence requirement, protected sequence, disposition rules, or four-cycle limit.
