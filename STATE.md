# State

_Last updated: 2026-07-24_

## Phase

**Study 005 active / Cycle 2 of maximum 4 completed**

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
- Active issue: **#11**
- Pinned referent: **IANA tzdb 2026c**
- Source SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`
- Compiled-tree projection SHA-256: `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2`
- Canonical inventory: **313 zones**.

## Cycle 2 result

- Original standard-library-only TZif v1/v2/v3/v4 reader implemented and frozen.
- Pre-first-transition interpretation: **time type index 0**.
- Parser unit tests: **11 passed**.
- One invalid synthetic test expectation was corrected before the fixture gate; no reader correction opportunity was consumed.
- Frozen fixture/footer gate: **18 / 18 passed on the first formal run**.
- Fixture-gate canonical SHA-256: `07daf47a745ba83ecff95d468328546b7fc8a5fbeb8d42c8eafb8bf970b906d3`.
- Complete explicit-transition manifest frozen only after the gate passed.
- Retained transitions: **18,071**.
- Backward / zero / forward: **8,926 / 187 / 8,958**.
- Compact manifest: **354,993 bytes**.
- Manifest SHA-256: `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.
- Reconstructible xz/base64 parts: **45,936 xz bytes / 61,248 base64 characters**.
- A truncated repository part was detected during final validation and replaced by three exact chunks; live part identities now match the execution-local source.

No formal Python `zoneinfo` comparison or H1–H3 result exists yet.

## Next bounded work

The next exact `承認` may perform **Study 005 Cycle 3 only**:

1. reconstruct and verify the frozen compiled-tree, inventory, fixture, reader, and transition-manifest artifacts;
2. implement the isolated public-API Python `zoneinfo` projection, fold, UTC round-trip, and gap-validation harness;
3. freeze its serialization and assertions using only targeted fixtures and synthetic TZif-independent cases before formal outcomes;
4. prove that `zoneinfo` resolves only from the isolated 2026c tree;
5. execute the complete frozen corpus once;
6. preserve every comparison and mismatch record and synchronize Issue #11 and repository state;
7. stop without Cycle 4 synthesis.

Cycle 3 must not alter the source, inventory, date range, transition manifest, witness rules, hypotheses, or criteria; remove inconvenient records; use host zone data; contact outsiders; file a defect report; perform clean reproduction or final analysis; or begin Cycle 4.

## Verification limitations

- No detached GPG signature was supplied or verified.
- Compiled directories remained execution-local; their deterministic projection is preserved.
- The complete manifest is independent-reader evidence, not a Python conformance result.
- No fresh checkout or full-repository regression was performed; targeted parser tests and archive-based reconstruction were performed.
- H1, H2, and H3 remain untested.

## Human action currently needed

None beyond a later exact `承認` for one bounded Cycle 3.
