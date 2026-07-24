# Study 005 Protocol — TZDB Transition Round-Trip Conformance

_Date activated: 2026-07-24 (Asia/Tokyo)_  
_Status: **Closed — Cycle 4 of maximum 4 completed; positive bounded conformance result**_

## 1. Authority and frozen source

This active protocol instantiated the frozen proposal at:

- `research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`

The proposal remains the pre-activation record. This protocol changed no research question, hypothesis, corpus rule, witness semantic, criterion, protected sequence, disposition rule, or cycle limit during execution.

Activation decision: **GO unchanged**.

Pinned external referent:

- project: IANA Time Zone Database;
- release: **2026c**;
- official release date: **2026-07-08**;
- archive: `tzdata2026c.tar.gz`;
- official versioned URL: `https://www.iana.org/time-zones/repository/releases/tzdata2026c.tar.gz`;
- observed byte count: **475,694**;
- observed SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`;
- observed SHA-256: `e4a178a4477f3d0ea77cc31828ff72aa38feff8d61aa13e7e99e142e9d902be4`;
- internal `version`: `2026c`;
- member count: 32;
- permission record: top-level `LICENSE` states the default public-domain boundary; the three conditionally BSD-licensed named files are absent.

The source bytes were supplied unchanged through the project conversation as A1 access assistance. The archive itself and extracted third-party files were not committed. Only metadata, digests, original TEMPLEX/0 artifacts, and generated manifests were committed.

## 2. Research question

> Can a version-pinned transition corpus derived from IANA tzdb 2026c verify Python `zoneinfo` UTC-to-local projection, repeated-time `fold` handling, exact UTC round trips, and nonexistent-local-time detection at civil-time discontinuities using an independently implemented TZif reader?

The unit of analysis is one canonical zone and one explicit transition record compiled from the pinned source. The study is a bounded conformance and regression study for one release, runtime, compiler environment, inventory, interval, and invariant set.

## 3. Frozen hypotheses

### H1 — explicit UTC projection agreement

For every frozen witness around every retained explicit transition, isolated Python `zoneinfo` and the independent TZif reader must agree on UTC offset, DST offset where represented, abbreviation, and local calendar/clock fields.

Witnesses are `t-1`, `t`, `t+1`, and exact integer midpoints of the stable UTC intervals adjacent to transition `t` where those intervals intersect the date range.

Support requires zero field disagreements across the complete frozen witness set.

### H2 — backward-transition fold round trip

For each backward transition, sample the first, integer-floor midpoint, and last repeated local second. Both implied UTC instants must map to the same wall time; the earlier occurrence must have `fold=0`; the later must have `fold=1`; and each fold-tagged wall time must round-trip exactly to its original UTC instant.

Support requires every assertion to pass for every frozen backward-transition sample.

### H3 — forward-transition gap detectability

For each forward transition, sample the first, integer-floor midpoint, and last nonexistent local second. A wall time is valid only when at least one fold assignment survives an exact local→UTC→local round trip with matching wall fields and fold interpretation. Interior gap samples must be nonexistent, adjacent valid seconds must be valid, and no one-hour assumption is allowed.

Support requires zero false-valid and zero false-invalid classifications.

## 4. Frozen behavioral domain

### Zone inventory

The primary inventory is every unique zone name in 2026c `zone1970.tab`, in first-occurrence file order after comments and blank lines are removed, plus `Etc/UTC` as a no-transition control.

Aliases and compatibility links are outside the primary denominator. Any missing compiled primary zone is a setup failure, not a silent omission.

### Date and time domain

- explicit TZif transitions in `[1970-01-01T00:00:00Z, 2100-01-01T00:00:00Z)`;
- POSIX seconds at one-second precision;
- no `right/` leap-second files;
- no pre-1970 transitions in the primary corpus;
- no subsecond claims;
- no synthesized transitions from POSIX footer rules beyond the last explicit record.

Transitions are classified by offset delta as backward, zero-delta, or forward, and nonzero shifts are grouped by absolute seconds. No one-hour assumption is permitted.

## 5. Frozen Cycle 1 compilation plan

### Tool identity

- Python: `/opt/pyvenv/bin/python3` (CPython 3.13.5 at activation preflight)
- `zic`: `/usr/sbin/zic` (Debian glibc 2.41-12+deb13u2)
- `zdump`: `/usr/bin/zdump` (Debian glibc 2.41-12+deb13u2)

### Source list and order

1. `africa`
2. `antarctica`
3. `asia`
4. `australasia`
5. `europe`
6. `northamerica`
7. `southamerica`
8. `etcetera`

`backward` is excluded because aliases and compatibility links are outside the primary denominator. `backzone` is excluded because pre-1970 supplementary histories are outside the primary domain. `factory` is excluded because `Factory` is not in the canonical inventory. Leap-second inputs are excluded.

### Command family frozen before compilation

For each clean output directory `OUT`:

```text
env -i PATH=/usr/sbin:/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC \
  /usr/sbin/zic -b fat -d OUT \
  africa antarctica asia australasia europe northamerica southamerica etcetera
```

Rationale:

- `-b fat` preserves complete TZif blocks rather than choosing slim representation;
- `-d OUT` prevents host-zone substitution;
- no `-L` means ordinary POSIX civil-time files rather than leap-second `right/` data;
- no `-r` or `-R` truncation is applied;
- a minimal fixed environment reduces environmental variation.

Two clean compilations must have identical deterministic projections. The projection is UTF-8 lines sorted by bytewise relative path, each line containing relative path, byte length, and SHA-256 of file bytes; the projection file itself is SHA-256 hashed.

## 6. Frozen fixture policy

Cycle 1 freezes at least twelve targeted hand-audited expectations before the independent reader exists. Fixtures must cover:

- no-transition UTC;
- conventional one-hour backward and forward shifts;
- non-one-hour backward and forward shifts when present;
- a large civil-time discontinuity when present;
- a zero-offset or abbreviation-only transition when present;
- a POSIX footer;
- multiple historical types;
- transitions before and after 2000;
- negative and positive offsets.

Each transition fixture records zone, UTC transition second, pre/post local representation, UTC offset, DST flag, abbreviation, delta, source command, and targeted source-text evidence where practical. `zdump` is secondary fixture evidence only and is not the full-corpus oracle.

Cycle 1 may inspect only targeted fixture zones and compilation structure. It must not implement the independent reader or inspect the complete transition outcome set.

## 7. Protected sequence

1. verify source provenance, permission, archive identity, and tools;
2. freeze this active protocol;
3. compile twice in isolation;
4. freeze source, compilation, zone-list, and fixture artifacts;
5. implement the independent reader and fixture gate in Cycle 2;
6. freeze the passing reader and complete transition manifest;
7. freeze the `zoneinfo` harness;
8. execute the complete corpus once;
9. reproduce cleanly, analyze, report, and close.

The study is invalid rather than retroactively repaired if final outcome data are inspected early, frozen definitions change after execution begins, inconvenient records are removed, host data are substituted, or another tzdb release replaces 2026c.

## 8. Cycle and disposition limits

Maximum activation cycles:

1. activation, source/permission preflight, isolated compilation, zone inventory, fixtures;
2. independent reader, fixture gate, complete transition manifest;
3. harness freeze and complete formal execution;
4. clean reproduction, analysis, report, closure.

No fifth cycle is permitted.

Setup closes negatively if official source identity or permission fails, the archive is unavailable, isolated compilation is not reproducible, a primary canonical zone is missing/unreadable, the parser gate fails after its one correction opportunity, data-path isolation cannot be demonstrated, or protected sequencing is contaminated.

## 9. Human intervention boundary

The activation `承認`, source transfer, and later cycle approvals were A1 access assistance. Yoshie Yamada did not select the question, release, hypotheses, domain, compiler flags, source order, fixture zones, interpretations, or results.

A separate explicit decision remains required before terms acceptance, external contact, defect reporting, permission changes, or publication through a new channel.

## 10. Final disposition

Cycle 4 used the exact committed reader, harness, tests, Cycle 2 builder, pre-outcome Cycle 3 runner, and result reconstructor. It reproduced the pinned archive, two byte-identical 341-file compilation projections, the 313-zone inventory, and the byte-identical 18,071-transition manifest.

The exact-source formal reproduction produced:

- H1: 90,079 records, zero mismatches — **supported**;
- H2: 26,778 records, zero mismatches — **supported**;
- H3: 44,790 records, zero mismatches — **supported**.

The Cycle 3 and Cycle 4 scientific record families were byte-identical. Their complete result digests differed only because the serialized `environment.tzpath_after[0]` contained different absolute temporary paths. The full-result identity was therefore non-portable; this is an artifact-design limitation rather than a conformance mismatch.

Study 005 closes as a **positive bounded conformance result with procedural and artifact-portability limitations**. See `REPORT.md` and `CYCLE_4_REPRODUCTION_AND_CLOSURE.md`.

Issue #11 is closed. Study 005 is closed. No fifth cycle exists.
