# Study 005 Cycle 3 — Isolated `zoneinfo` Formal Execution

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **Cycle 3 complete; Study 005 remains active**_

## Scope

Cycle 3 reconstructed the frozen tzdb 2026c evidence, froze a public-API Python `zoneinfo` harness before complete outcomes, proved an isolated data path, executed the complete 313-zone frozen corpus exactly once, and preserved the mechanical result and mismatch records.

It did not alter the source release, compilation command, zone inventory, date interval, transition manifest bytes, witness rules after outcomes, hypotheses, or success criteria. It did not exclude mismatches, contact outsiders, file a defect report, perform the Cycle 4 clean reproduction and synthesis, or close the study.

## Reconstructed preconditions

Before harness execution, the trusted project-conversation archive was re-extracted and compiled with the frozen Cycle 1 command. The following identities reproduced exactly:

- archive SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`;
- compiled-tree projection SHA-256: `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`;
- `zone1970.tab` SHA-256: `77b5e45415fa684fcc42de3421a6b0f15cc9b2c137f258083850346e8f76eea8`;
- ordered 313-zone inventory SHA-256: `053b3988df8da3276ba63928fab3a1e6b1e9e625d0fa13d16b6f423edc51b582`;
- compact transition manifest: 354,993 bytes, SHA-256 `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.

The host zone database was not used as evidence.

## Pre-outcome manifest correction of claim

Before complete Python outcomes were run, reconstruction showed that the Cycle 2 compact manifest was not independently self-contained for the pre-transition type of the first retained post-1970 transition. It stores retained transition pairs and complete type tables but omits earlier transition records.

- 274 canonical zones had a first-retained-transition pre-type index other than zero;
- using type zero would change the first-transition delta in all 274;
- it would change the backward/zero/forward class in 36.

The manifest bytes and digest were not changed. The previously frozen independent reader and exact TZif file bytes were used to recover the transition context. Before comparisons, the runner verified each manifest row's file size, file SHA-256, local-time-type table, and retained transition list against those exact TZif bytes.

Cycle 2's description of the compact file as independently self-contained or lossless without the frozen reader and source bytes is therefore withdrawn. It remains a lossless generated representation when interpreted with those frozen dependencies.

## Harness freeze before formal outcomes

The following were committed before the complete formal execution:

- `src/templex_zero/zoneinfo_harness.py`;
- `tests/test_zoneinfo_harness.py`;
- `experiments/study005_cycle3.py`;
- `CYCLE_3_HARNESS_FREEZE.md`;
- `data/harness_freeze_identity_v1.json`.

Seven targeted tests passed before formal execution:

1. conservative explicit-interval midpoint generation;
2. non-one-hour repeated and gap samples;
3. fixed-offset two-fold validation;
4. New York UTC projection and one-hour fold;
5. Lord Howe half-hour fold;
6. New York gap detection;
7. Apia 24-hour gap detection.

### Frozen H1 records

For each retained transition, the runner used `t-1`, `t`, `t+1`, the left explicit-interval midpoint, and a right midpoint only when a later retained explicit transition supplied an endpoint. It compared:

- total UTC offset;
- TZif `isdst` representation against whether public `datetime.dst()` was nonzero, while preserving signed DST seconds;
- abbreviation;
- local calendar and clock fields.

### Frozen H2 records

For every backward transition, the first, floor midpoint, and final repeated local second were tested using the actual offset delta. Both UTC instants, observed folds, wall values, and fold-tagged local-to-UTC round trips were preserved.

### Frozen H3 records

For every forward transition, the first, floor midpoint, and final gap second plus the two adjacent valid seconds were tested without a one-hour assumption. Both fold assignments were preserved. An assignment survived only when local→UTC→local returned identical wall fields and the same fold.

## Isolation and exact formal command

The public `zoneinfo` data path was constrained by:

- CPython `-S`;
- initially empty `PYTHONTZPATH` and `zoneinfo.TZPATH`;
- public `zoneinfo.reset_tzpath()` with only the isolated 2026c compiled directory;
- no importable third-party `tzdata` package;
- successful resolution of all 313 requested keys;
- required `ZoneInfoNotFoundError` for `TEMPLEX/DefinitelyMissing`.

Observed environment:

- CPython 3.13.5;
- `no_site = 1`;
- `tzdata_spec_present = false`;
- `tzpath_before = []`;
- `tzpath_after = ["/mnt/data/study005_cycle3_work/tzout"]`;
- missing key rejected.

Formal command:

```text
env -i PATH=/opt/pyvenv/bin:/usr/sbin:/usr/bin:/bin \
  LANG=C LC_ALL=C TZ=UTC \
  PYTHONPATH=/mnt/data/study005_cycle3_work/repo_src:/mnt/data/study005_cycle3_work \
  PYTHONTZPATH= \
  /opt/pyvenv/bin/python3 -S \
  /mnt/data/study005_cycle3_work/experiments/study005_cycle3.py \
  --formal \
  --tzdir /mnt/data/study005_cycle3_work/tzout \
  --manifest /mnt/data/study005_cycle3_work/artifacts/transition_manifest_compact_v1.json \
  --output-dir /mnt/data/study005_cycle3_work/results/formal
```

The complete formal corpus was executed **exactly once**. It was not rerun after inspecting results or while correcting repository transport artifacts.

## Mechanical formal result

The single formal execution produced:

| Record family | Records | Zero mask | Nonzero mask |
|---|---:|---:|---:|
| H1 UTC projection | 90,079 | 90,079 | 0 |
| H2 repeated-time fold and round trip | 26,778 | 26,778 | 0 |
| H3 gap and adjacent-valid classification | 44,790 | 44,790 | 0 |
| **Total** | **161,647** | **161,647** | **0** |

All 313 zones loaded from the isolated tree. The separate canonical mismatch artifact contains zero mismatch records.

One progress message during execution incorrectly stated `159,647` total records. That was an arithmetic/transcription error in the chat update. The immutable family counts sum to **161,647**, which is the value recorded here. No result artifact used the erroneous total.

These are mechanical Cycle 3 counts, not the final hypothesis dispositions. Cycle 4 must reproduce the execution from the exact repository source, inspect the complete records and limitations, and decide H1–H3 and study closure.

## Result identities

Full canonical result:

- bytes: **14,844,751**;
- SHA-256: `7115ba2b6a11ce0c6eb0230c2918f47e4f7721e314e97c438b97b3157795cfd6`;
- deterministic XZ bytes: **556,336**;
- deterministic XZ SHA-256: `e2593978c40961bfbed9791f639d16da304fefa32bada8701732f0644a04bf55`.

Mismatch artifact:

- canonical JSON bytes: **120**;
- canonical SHA-256: `d04a86ebb75c5bc5459945710c863470e647278d562c00e017303d186c0b85c1`;
- XZ bytes: **172**;
- XZ SHA-256: `80275696cfa5f8e25a981a2150c38eac4cd73341cccee9ee25d763b7a9e29d8c`.

## Reconstructible preservation

The 14.8 MB canonical result was represented by a reconstruction package containing the observed values that cannot be derived from the frozen reference plus every nonzero record. `experiments/study005_cycle3_reconstruct.py` combines that package with the frozen manifest, reader semantics, and exact compiled tree without invoking `zoneinfo` again.

Reconstruction package:

- JSON bytes: **3,370,437**;
- JSON SHA-256: `d9a8b0ac391b4ba39881f20a8a6a94cea6cac5a4006a8c50b753e489af927bfa`;
- XZ bytes: **81,976**;
- XZ SHA-256: `ed1f1c4aaef232ed342e0f598f8aa0af89c2c94f4756550ca827d39b19ed5df7`;
- base64 characters: **109,304**.

Repository persistence uses twelve files in the exact order recorded by `data/zoneinfo_formal_artifacts_v1.json`. Reassembly reproduced the package digests, reconstructed the exact 14,844,751-byte canonical result, matched the original formal result byte-for-byte, and reproduced the deterministic 556,336-byte XZ stream.

### Persistence corrections

The connector transport required visible corrections:

1. the first intended `part02` creation was not present on the live branch;
2. a replacement `part02` existed but its Git blob identity did not match the execution-local original;
3. it was deleted and replaced by three exact 4,000-character chunks: `part02a`, `part02b`, and `part02c`;
4. all final live part identities were checked against the execution-local source;
5. final concatenation and all XZ/JSON/result identities passed.

These were repository-persistence corrections only. The formal execution was not rerun and result bytes were not changed.

## Execution-source limitation

A material procedural limitation remains. The local formal execution imported `repo_src/templex_zero/tzif_reader.py`, a small compatibility bridge to an independently implemented local parser, rather than the literal frozen GitHub `src/templex_zero/tzif_reader.py` blob.

The local parser reproduced the exact frozen transition manifest and the runner verified every manifest row's source-file identity, type table, and retained transition list before comparison. This strongly constrains semantic divergence, but it is not equivalent to having executed the exact repository reader source.

Cycle 4 must therefore perform clean reproduction using the exact repository source and require the same manifest, summary, mismatch, canonical-result, and deterministic-XZ identities before final conclusions. Cycle 3 does not conceal or waive this requirement.

## Verification limitations

- No detached IANA signature was supplied or verified.
- No fresh repository checkout was available during Cycle 3.
- The compiled tree was execution-local; its deterministic projection and source identities remain preserved.
- The compact manifest depends on the frozen reader and exact TZif source for first-retained-transition context.
- The exact repository reader source was not the parser module imported by the formal local run.
- Zero mechanical mismatch records are not yet the final scientific disposition.

## Disposition

Cycle 3 completed its bounded objective. The isolated `zoneinfo` harness was frozen before outcomes, the complete corpus was executed once, every result was preserved, and no mismatch was excluded.

Study 005 remains active at **3 of maximum 4 cycles**. The next and final permitted cycle is Cycle 4: clean reproduction from exact repository source, identity comparison, analysis, final H1–H3 dispositions, report, issue closure, and study closure. No fifth cycle is permitted.
