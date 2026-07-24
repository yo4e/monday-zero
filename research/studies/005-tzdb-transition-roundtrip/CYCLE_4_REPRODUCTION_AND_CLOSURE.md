# Study 005 Cycle 4 — Exact-Source Reproduction and Closure

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **Cycle 4 complete; Study 005 closed**_

## Scope

Cycle 4 was the fourth and final permitted activation cycle. It reconstructed the pinned IANA tzdb 2026c source and compiled tree, rebuilt the canonical inventory and transition manifest, ran the exact committed reader and harness tests, executed one exact-source formal reproduction with the pre-outcome repository runner, compared it with the preserved Cycle 3 result, analyzed every difference, assigned final H1–H3 dispositions, and closed the study.

No source release, compiler command, zone inventory, interval, transition rule, witness rule, hypothesis, success criterion, or outcome record was changed. No mismatch was removed. No fifth cycle is permitted.

## Clean source and code identities

The reproduction used repository state based on commit `b43b6ae08c3e275655f98e8aece80eb072bb44a0` and literal committed files reconstructed to their Git blob identities:

- `src/templex_zero/tzif_reader.py`: `11a7e40c3f15f81677ae7321475e364b70d5830f`;
- `src/templex_zero/zoneinfo_harness.py`: `55e25f63296c67bb07a0ade9dcc44c38b5b8676a`;
- `tests/test_tzif_reader.py`: `e08410e5a45a40fe57251707f6fc21cb6bf9b332`;
- `tests/test_zoneinfo_harness.py`: `af7d7392f239ef19ee5fa996c534408533bff916`;
- `experiments/study005_cycle2.py`: `739f9857885fa1dd47b4eb826afbba40de0f4dd6`;
- pre-outcome `experiments/study005_cycle3.py`: `f1fcb11678fc0b834cc968fb718ce91fd4951e75`;
- `experiments/study005_cycle3_reconstruct.py`: `f55ed652a1547531acb927ebf58e07d01cb191c3`.

The exact source identities are preserved in `data/cycle4_source_identities_v1.json`.

## Source and compilation reproduction

The supplied archive reproduced the frozen identity:

- bytes: 475,694;
- SHA-256: `e4a178a4477f3d0ea77cc31828ff72aa38feff8d61aa13e7e99e142e9d902be4`;
- SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`.

Two clean compilations used the frozen `zic -b fat` command and source order. Both produced:

- 341 files;
- projection bytes: 29,170;
- projection SHA-256: `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`;
- byte-identical projection files.

`zone1970.tab` reproduced SHA-256 `77b5e45415fa684fcc42de3421a6b0f15cc9b2c137f258083850346e8f76eea8`.

The ordered canonical inventory reproduced:

- 313 zones;
- 5,183 bytes;
- SHA-256 `053b3988df8da3276ba63928fab3a1e6b1e9e625d0fa13d16b6f423edc51b582`;
- zero missing compiled zones.

## Tests and manifest

The exact committed tests passed:

- TZif reader tests: 11 / 11;
- public-API harness tests: 7 / 7;
- total: 18 / 18.

The Cycle 2 manifest builder, exact committed reader, clean compiled tree, and regenerated inventory produced a byte-identical manifest:

- zones: 313;
- transitions: 18,071;
- backward / zero / forward: 8,926 / 187 / 8,958;
- bytes: 354,993;
- SHA-256: `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.

The historical targeted fixture artifact was not separately decoded and rerun in Cycle 4 because the connector did not materialize that repository text artifact into the local execution filesystem. This is a disclosed reproduction gap. It does not alter the exact reader tests, full 313-zone file/type/transition manifest reproduction, or formal outcome reproduction.

## Cycle 3 artifact reconstruction

The final twelve-part Cycle 3 reconstruction package was assembled in its repository order. Every part SHA-256 matched. The package reproduced:

- base64 characters: 109,304;
- XZ bytes: 81,976;
- XZ SHA-256: `ed1f1c4aaef232ed342e0f598f8aa0af89c2c94f4756550ca827d39b19ed5df7`;
- package JSON bytes: 3,370,437;
- package JSON SHA-256: `d9a8b0ac391b4ba39881f20a8a6a94cea6cac5a4006a8c50b753e489af927bfa`.

Using the exact committed reader, harness, reconstructor, manifest, and clean compiled tree reconstructed the exact Cycle 3 canonical result:

- bytes: 14,844,751;
- SHA-256: `7115ba2b6a11ce0c6eb0230c2918f47e4f7721e314e97c438b97b3157795cfd6`.

## Exact-source formal reproduction

The pre-outcome committed runner was executed exactly once under the same isolated public-API conditions:

- CPython 3.13.5 with `-S`;
- initially empty `PYTHONTZPATH` and `zoneinfo.TZPATH`;
- one isolated 2026c compiled tree after `reset_tzpath()`;
- no importable third-party `tzdata` package;
- all 313 zone keys loaded;
- missing key rejected.

The reproduction produced:

| Family | Records | Nonzero masks |
|---|---:|---:|
| H1 UTC projection | 90,079 | 0 |
| H2 backward fold and round trip | 26,778 | 0 |
| H3 forward gap classification | 44,790 | 0 |
| **Total** | **161,647** | **0** |

The mismatch artifact was byte-identical to Cycle 3 and contained zero records.

## Full-result identity difference

The exact-source result was:

- bytes: 14,844,752;
- SHA-256: `3f799e6bb54dc99ef61f33d777fc42671839ed91208536282657820e90f2cd49`;
- deterministic XZ bytes: 556,276;
- deterministic XZ SHA-256: `c85fe8d8871aad02393b5a2b0164a85e0a04ee0d9b1d35202873bf5af05ba8c2`.

It did not match the complete Cycle 3 byte identity. Recursive comparison found exactly one difference:

- Cycle 3: `environment.tzpath_after[0] = /mnt/data/study005_cycle3_work/tzout`
- Cycle 4: `environment.tzpath_after[0] = /mnt/data/study005_cycle4_work/tzout1`

Every scientific and structural field was identical: H1 rows, H2 rows, H3 rows, manifest identity, reference context, schema, and zone order.

After replacing the absolute path with the same abstract isolated-tree marker, both results became byte-identical:

- normalized bytes: 14,844,736;
- normalized SHA-256: `0d3b14f7ae57f846339cb6d7f5af8ca8d9d4610bb5a46c448d87eb29ef2ac1f2`.

The scientific payload excluding `environment` was byte-identical:

- bytes: 14,844,386;
- SHA-256: `cf635b2a32b8183f14b5ec7d54a1fd95cc6b9bad2cda5087a0072317cc0f0e79`.

Family identities were also identical:

- H1 SHA-256: `900d7c6260bbaa592236f432bc9eea2efa1a3430d2283402e76ca20065edcc36`;
- H2 SHA-256: `a738f26dd3afff8d5a98ff4c30caccda5e9334de939306d48dcc1170b8a867d8`;
- H3 SHA-256: `1811a8ae1bad4321d697d4ee5f3287ca0aea32dc427695b7d498753d988655f2`.

The complete digest criterion was therefore non-portable because it serialized an absolute temporary path. This is an artifact-design defect, not a conformance mismatch.

## Cycle 3 source-record correction

Cycle 4 found that `CYCLE_3_SOURCE_IDENTITY_CORRECTION.md` contained incorrect Git blob identifiers. The actual values are recorded in `data/cycle4_source_identities_v1.json`.

It also found that `data/study005_cycle3_executed_runner_v1.py` has Git blob `3eccb9419bab3159ec09c663caaa018aa0c07ca0` and is not a byte-identical copy of the execution-local 8,810-byte source, whose actual Git blob is `06280fe9e6e7347c5de91f6736c4fc72577252a3`. The repository evidence is a semantically compressed transcription.

The pre-outcome runner and execution-local runner have different raw ASTs only because the execution-local form contains two unused imports. After removing those unused imports, their ASTs are identical. More importantly, the exact committed runner and exact committed reader reproduced every scientific record exactly.

These corrections do not erase the Cycle 3 procedural deviation. They resolve its effect on the scientific outcome.

## Final hypothesis dispositions

### H1 — supported

All 90,079 frozen UTC witnesses agreed on total offset, DST representation, abbreviation, and local wall fields. Exact-source reproduction produced the identical H1 record family with zero nonzero masks.

### H2 — supported

All 8,926 backward transitions were sampled at the first, floor-midpoint, and final repeated local second, producing 26,778 records. Both UTC occurrences mapped to the same wall time, earlier/later folds were 0/1, and fold-tagged wall times round-tripped exactly. Zero nonzero masks were observed.

### H3 — supported

All 8,958 forward transitions were sampled at three interior gap seconds and two adjacent valid seconds, producing 44,790 records. The rule used actual offset deltas, including non-one-hour and 24-hour changes. No false-valid or false-invalid classification occurred.

## Disposition

Study 005 closes as a **positive bounded conformance result with procedural and artifact-portability limitations**.

Within the frozen domain—CPython 3.13.5, IANA tzdb 2026c, the specified `zic -b fat` compilation, 313 canonical zones, explicit transitions from 1970 through 2099, one-second precision, no leap-second files, no aliases, no pre-1970 primary transitions, and no synthesized footer transitions—Python `zoneinfo` conformed to the independent TZif reference for all H1–H3 assertions tested.

This study does not claim conformance for other Python versions, operating systems, compiler versions, tzdb releases, aliases, pre-1970 histories, leap-second data, subsecond behavior, or footer-synthesized future transitions.

Issue #11 is closed. Study 005 is closed. No fifth cycle exists.
