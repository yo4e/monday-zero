# State

_Last updated: 2026-07-24_

## Phase

**Study 005 active / Cycle 1 of maximum 4 completed**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

- **Study 001:** negative autonomous-game-design conclusion.
- **Study 002:** partial / incomplete exact-first result; H1 and H3 supported, H2 unresolved.
- **Study 003:** methodological success with bounded procedural claims.
- **Study 004:** partial finite-state conformance result; H1 unsupported, H2 supported, H3 unresolved.

## Active Study 005

- Study: **TZDB Transition Round-Trip Conformance**
- Active protocol: `research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md`
- Cycle 1 audit: `research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md`
- Active issue: **#11**
- Pinned referent: **IANA tzdb 2026c**
- Source archive SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`
- Source archive SHA-256: `e4a178a4477f3d0ea77cc31828ff72aa38feff8d61aa13e7e99e142e9d902be4`
- Permission preflight: passed under the bundled default public-domain boundary; conditionally BSD-named files absent.

## Cycle 1 result

- Activation decision: **GO unchanged**.
- Two isolated `zic -b fat` compilations completed from the same eight frozen source files.
- Each compilation produced **341 files / 397,559 bytes**.
- Both deterministic tree projections were byte-identical.
- Projection SHA-256: `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`.
- `zone1970.tab` SHA-256: `77b5e45415fa684fcc42de3421a6b0f15cc9b2c137f258083850346e8f76eea8`.
- Canonical inventory: **312 source-order zones + `Etc/UTC` = 313 zones**.
- Inventory SHA-256: `053b3988df8da3276ba63928fab3a1e6b1e9e625d0fa13d16b6f423edc51b582`.
- Missing canonical TZif files: **0**.
- Canonical files with invalid `TZif` magic: **0**.
- Frozen targeted fixture expectations: **15**.
- Fixture JSON SHA-256: `a3b08a49f5d3955f0015e67d58f705a68dadb7cc07ed1b499ff13381290786d9`.
- Targeted fixture regeneration reproduced the same fixture digest.

No independent TZif reader, complete transition manifest, Python `zoneinfo` formal comparison, or H1–H3 result exists yet.

## Next bounded work

The next exact `承認` may perform **Study 005 Cycle 2 only**:

1. implement the original standard-library-only TZif reader without Python private parser code;
2. add malformed/truncated/index/abbreviation/version/count rejection tests;
3. run the reader against all 15 frozen fixtures;
4. use at most one bounded disclosed correction if the fixture gate initially fails;
5. if and only if the fixture gate passes, freeze the reader, canonical serialization, and complete transition manifest;
6. synchronize Issue #11 and repository state, then stop.

Cycle 2 must not implement or execute the formal Python `zoneinfo` comparison, inspect H1–H3 outcome aggregates, change the frozen corpus or criteria, contact outsiders, accept terms, or begin Cycle 3.

## Verification limitations

- No detached GPG signature was supplied or verified.
- The isolated compiled trees were execution-local; their complete deterministic projection is preserved in reconstructible compressed/base64 parts.
- `zdump` is secondary targeted fixture evidence only, not the complete-corpus oracle.
- Fresh checkout and full-repository regression were not performed; no project runtime code was changed in Cycle 1.

## Human action currently needed

None beyond a later exact `承認` for one bounded Cycle 2.
