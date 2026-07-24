# Next Start

_Updated: 2026-07-24 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the active Study 005 protocol, all three cycle audits, Issue #11, current code/tests, recent commits, and frozen data artifacts.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 005 is active. Cycle 3 of maximum 4 is complete. Studies 001–004 remain closed.**

- Active study: `research/studies/005-tzdb-transition-roundtrip/`
- Protocol: `research/studies/005-tzdb-transition-roundtrip/PROTOCOL.md`
- Cycle 1 audit: `research/studies/005-tzdb-transition-roundtrip/CYCLE_1_ACTIVATION.md`
- Cycle 2 audit: `research/studies/005-tzdb-transition-roundtrip/CYCLE_2_READER_AND_MANIFEST.md`
- Cycle 3 harness freeze: `research/studies/005-tzdb-transition-roundtrip/CYCLE_3_HARNESS_FREEZE.md`
- Cycle 3 formal audit: `research/studies/005-tzdb-transition-roundtrip/CYCLE_3_FORMAL_EXECUTION.md`
- Active issue: #11
- Pinned release: IANA tzdb 2026c

## Cycle 3 evidence

- frozen harness tests: 7 passed;
- formal execution: exactly one complete run;
- isolated keys loaded: 313;
- H1: 90,079 records, zero nonzero masks;
- H2: 26,778 records, zero nonzero masks;
- H3: 44,790 records, zero nonzero masks;
- total: 161,647 records, zero mismatch records;
- full canonical result: 14,844,751 bytes;
- result SHA-256: `7115ba2b6a11ce0c6eb0230c2918f47e4f7721e314e97c438b97b3157795cfd6`;
- deterministic XZ SHA-256: `e2593978c40961bfbed9791f639d16da304fefa32bada8701732f0644a04bf55`.

Zero mechanical mismatches are not yet final hypothesis dispositions.

## Mandatory limitations to carry forward

1. The compact manifest omits pre-1970 transition context and is not independently self-contained for the first retained transition in 274 zones. Use the exact TZif bytes and frozen committed reader.
2. The Cycle 3 formal local run imported a compatibility bridge to an independent local parser rather than the literal repository reader blob. Cycle 4 must use exact repository source.
3. A progress message incorrectly said 159,647; the correct total is 161,647.
4. Result transport required visible part corrections. Reconstruct according to `data/zoneinfo_formal_artifacts_v1.json` and verify every digest.
5. No detached IANA signature was verified.

## Frozen artifact reconstruction

- Cycle 1 and Cycle 2 artifacts retain their recorded procedures.
- Reconstruct the compact transition manifest according to `data/transition_manifest_compact_v1.parts.json` and verify 354,993 bytes / SHA-256 `11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4`.
- Reconstruct the Cycle 3 package according to `data/zoneinfo_formal_artifacts_v1.json`.
- Use `experiments/study005_cycle3_reconstruct.py` without invoking `zoneinfo` to recover the exact canonical result.
- Verify 14,844,751 bytes / SHA-256 `7115ba2b6a11ce0c6eb0230c2918f47e4f7721e314e97c438b97b3157795cfd6` and deterministic XZ SHA-256 `e2593978c40961bfbed9791f639d16da304fefa32bada8701732f0644a04bf55`.

## Next bounded work unit — Cycle 4 only

Cycle 4 is the final permitted cycle:

1. re-read the live protocol, all audits, Issue #11, code/tests, artifacts, and commits;
2. obtain a clean repository state containing the exact committed reader, harness, tests, and runners;
3. re-extract and compile the trusted 2026c archive with the frozen command;
4. reproduce the source, projection, zone list, fixture gate, compact manifest, Cycle 3 package, full result, summary, mismatch artifact, and deterministic XZ identities;
5. run the formal exact-source reproduction in the frozen environment and compare every identity with Cycle 3;
6. if reproduction differs, preserve and analyze the difference without changing the experiment or adding a fifth cycle;
7. analyze H1, H2, and H3 under the frozen support criteria and limitations;
8. write `REPORT.md` and a Cycle 4 reproduction/closure audit;
9. close Issue #11 and mark Study 005 closed.

Cycle 4 must not change the source release, source files, compiler semantics, zone inventory, interval, manifest, witness generation, hypotheses, or criteria; exclude inconvenient results; contact maintainers; file an external defect report; or create a fifth cycle.

## Human gate

> 承認

## Human action pending

None. A later exact `承認` opens the final Cycle 4 only.
