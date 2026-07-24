# State

_Last updated: 2026-07-24_

## Phase

**Study 005 active / Cycle 3 of maximum 4 completed**

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
- Cycle 2 audit: `research/studies/005-tzdb-transition-roundtrip/CYCLE_2_READER_AND_MANIFEST.md`
- Cycle 3 freeze: `research/studies/005-tzdb-transition-roundtrip/CYCLE_3_HARNESS_FREEZE.md`
- Cycle 3 execution: `research/studies/005-tzdb-transition-roundtrip/CYCLE_3_FORMAL_EXECUTION.md`
- Active issue: **#11**
- Pinned referent: **IANA tzdb 2026c**
- Source SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`
- Compiled-tree projection SHA-256: `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`
- Canonical inventory: **313 zones**.
- Transition manifest: **18,071 transitions / SHA-256 `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`**.

## Cycle 3 mechanical result

- Harness frozen before complete outcomes; seven targeted tests passed.
- Public `zoneinfo` data path isolated to the reconstructed 2026c tree under CPython `-S`.
- Formal corpus executed **exactly once**.
- H1 records: **90,079 / nonzero masks 0**.
- H2 records: **26,778 / nonzero masks 0**.
- H3 records: **44,790 / nonzero masks 0**.
- Total records: **161,647 / mismatch records 0**.
- Full canonical result: **14,844,751 bytes**.
- Result SHA-256: `7115ba2b6a11ce0c6eb0230c2918f47e4f7721e314e97c438b97b3157795cfd6`.
- Deterministic XZ: **556,336 bytes / SHA-256 `e2593978c40961bfbed9791f639d16da304fefa32bada8701732f0644a04bf55`**.
- Reconstructible result package and empty mismatch artifact are preserved.

These are mechanical outcome counts, not final H1–H3 dispositions. Final interpretation and closure are reserved for Cycle 4.

## Material limitations

- The compact Cycle 2 manifest is not independently self-contained for first-retained-transition pre-type context; the frozen reader and exact TZif bytes are required. The prior stronger self-containment claim is withdrawn.
- The formal local run imported a compatibility bridge to an independent local parser rather than the literal committed reader blob. Every manifest row's file identity, type table, and retained transition list was verified, but exact-source clean reproduction is mandatory.
- One chat progress update incorrectly stated 159,647 records; the immutable family counts sum to 161,647.
- Repository result transport required disclosed part corrections; the formal run was not rerun and result bytes did not change.
- No detached GPG signature was supplied or verified.

## Next bounded work

The next exact `承認` may perform **Study 005 Cycle 4 only**, the final permitted cycle:

1. obtain a clean repository state and use the exact committed reader, harness, tests, and runners;
2. reconstruct and verify the source, compiled tree, inventory, fixtures, manifest, and Cycle 3 result package;
3. reproduce the manifest, summary, mismatch artifact, full canonical result, and deterministic XZ identities;
4. investigate any difference without changing frozen rules or adaptively rerunning the study;
5. analyze H1, H2, and H3 under the frozen criteria;
6. write the final report and clean-reproduction closure audit;
7. close Issue #11 and mark Study 005 closed.

Cycle 4 must not change the release, source, inventory, interval, hypotheses, witness rules, manifest, or success criteria; hide limitations; contact outsiders; file an external report; or authorize a fifth cycle.

## Human action currently needed

None beyond a later exact `承認` for the final bounded Cycle 4.
