# Study 005 Cycle 2 — Independent Reader, Fixture Gate, and Transition Manifest

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **Cycle 2 complete; Study 005 remains active**_

## Scope

Cycle 2 performed only the protocol-authorized parser and manifest work. It reconstructed the frozen Cycle 1 artifacts, implemented an original standard-library-only TZif reader, exercised malformed-input rejection, ran the frozen fixture gate, and generated the complete explicit-transition manifest only after the gate passed.

It did not implement or execute the formal Python `zoneinfo` comparison harness, inspect H1–H3 conformance outcomes, change the source release, inventory, date interval, hypotheses, criteria, or witness semantics, contact outsiders, or begin Cycle 3.

## Cycle 1 artifact reconstruction

The project-conversation `tzdata2026c.tar.gz` was re-extracted and recompiled with the frozen Cycle 1 command. The following identities reproduced exactly before parser implementation was evaluated:

- compiled-tree projection SHA-256: `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`;
- `zone1970.tab` SHA-256: `77b5e45415fa684fcc42de3421a6b0f15cc9b2c137f258083850346e8f76eea8`;
- 313-zone inventory SHA-256: `053b3988df8da3276ba63928fab3a1e6b1e9e625d0fa13d16b6f423edc51b582`;
- frozen fixture expectation SHA-256: `a3b08a49f5d3955f0015e67d58f705a68dadb7cc07ed1b499ff13381290786d9`.

The host zone database was not used as evidence.

## Independent TZif reader

The reader is `src/templex_zero/tzif_reader.py`. It:

- uses only the Python standard library;
- does not import `zoneinfo` or CPython private parser code;
- supports TZif versions 1, 2, 3, and 4;
- freezes time type index 0 as the pre-first-transition interpretation;
- exposes explicit transitions, type indexes, UTC offsets, DST flags, abbreviations, standard/UT indicators, leap records, footer text, type lookup, exact-transition lookup, and deterministic canonical serialization;
- rejects invalid magic or versions, nonzero reserved bytes, truncation, impossible count relationships, unordered transition or leap timestamps, invalid transition type indexes, invalid offset ranges, nonbinary DST or indicator flags, impossible abbreviation indexes, unterminated or non-ASCII abbreviations, inconsistent dual headers, malformed footers, and trailing bytes in v1 files.

Reader source was committed before generation of the complete transition manifest.

## Tests and correction record

Eleven parser unit tests passed.

The initial unit-test run contained one invalid synthetic expectation: a test intended to create an inconsistent `isstdcnt` used `typecnt=1, isstdcnt=1`, which is valid. The synthetic header was corrected to `isstdcnt=2`. This occurred before the frozen fixture gate, changed no reader behavior or frozen research rule, and did not consume the single permitted reader-correction opportunity.

No reader correction was required by the fixture gate.

## Frozen fixture gate

The gate evaluated the fifteen frozen transition/control expectations plus three separately frozen POSIX-footer expectations.

- results: **18**;
- passed: **18**;
- failed: **0**;
- canonical gate-result bytes: **11,460**;
- canonical gate-result SHA-256: `07daf47a745ba83ecff95d468328546b7fc8a5fbeb8d42c8eafb8bf970b906d3`;
- deterministic gzip bytes: **1,699**;
- deterministic gzip SHA-256: `70bc5f4e4c3b88efaf08ef6543bef7eb958baead8ab050b95b7daf4e20a33b21`.

The gate passed on its first formal execution. The reader, tests, fixture-gate builder, and gate result were committed before the complete manifest was generated.

## Complete explicit-transition manifest

The passing reader parsed all 313 canonical files and retained explicit TZif transition records in the frozen interval `[1970-01-01T00:00:00Z, 2100-01-01T00:00:00Z)`.

- zones: **313**;
- retained transitions: **18,071**;
- backward: **8,926**;
- zero-delta: **187**;
- forward: **8,958**.

Offset-delta counts in seconds:

| Delta | Count |
|---:|---:|
| -25,200 | 1 |
| -10,800 | 9 |
| -7,200 | 53 |
| -3,600 | 8,785 |
| -1,800 | 78 |
| 0 | 187 |
| 900 | 1 |
| 1,800 | 77 |
| 2,400 | 1 |
| 2,670 | 1 |
| 2,700 | 1 |
| 3,600 | 8,812 |
| 5,400 | 1 |
| 7,200 | 48 |
| 10,800 | 10 |
| 25,200 | 1 |
| 86,400 | 5 |

The canonical compact serialization stores each zone's file identity, TZif version, footer, complete local-time-type table, final explicit transition, and every retained `[timestamp, type_index]` pair. The fixed column definitions reconstruct all pre/post offsets, DST flags, abbreviations, type indexes, and transition classes without loss.

- canonical manifest bytes: **354,993**;
- canonical manifest SHA-256: `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`;
- `xz -9e --threads=1` bytes: **45,936**;
- xz SHA-256: `1bc01ad35eef2b589c76ffa53a652175eac45a0842ad4db012a2f10017451c20`;
- base64 characters: **61,248**.

The compact representation was compared losslessly with the initial verbose representation across all 313 zones and all 18,071 retained transitions before the verbose form was discarded as a transport artifact.

## Repository-persistence corrections

The compressed manifest exceeded the connector's practical single-text-write size and was persisted as base64 parts.

Final verification found that the initial repository `part03` contained only 4,000 of its intended 12,000 characters. A first attempted large replacement was also rejected by blob-identity validation. The unchanged execution-local base64 source was then divided into three exact 4,000-character chunks (`part03`, `part03b`, and `part03c`).

The final eight-part layout records each path, character count, final-LF treatment, and SHA-256. All eight live Git blob identities match the execution-local bytes. Reassembling them in the recorded order yields the frozen 61,248-character base64 payload, 45,936-byte xz stream, and 354,993-byte canonical manifest with the identities above.

These were persistence corrections only. Reader behavior, fixture results, manifest semantic content, transition counts, and canonical manifest identity did not change.

## Verification limitations

- No detached IANA signature was supplied or verified.
- The isolated compiled tree remained execution-local; its deterministic projection and source identities are preserved.
- The complete manifest is generated evidence from the independent reader, not yet a comparison result against Python `zoneinfo`.
- No fresh checkout or full-repository regression was performed because direct GitHub checkout remained unavailable; targeted parser tests and archive-based reconstruction were performed in the execution environment.
- H1, H2, and H3 remain untested.

## Disposition

The Cycle 2 parser gate passed. The independent reader and complete transition manifest are frozen. Study 005 remains active at **2 of maximum 4 cycles**.

The next highest-value work is Cycle 3: implement and freeze the isolated public-API `zoneinfo` comparison and round-trip harness using only fixtures and synthetic cases before outcomes, then execute the complete frozen corpus once and preserve all mismatch records without analysis-driven exclusions.
