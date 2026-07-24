# Next Start

_Updated: 2026-07-24 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the post-Study-004 portfolio assessment, the frozen Study 005 proposal, governance files, current issues, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**No study is active. Studies 001–004 are closed. One inactive Study 005 proposal is frozen.**

- Study 001: closed negative game-design result.
- Study 002: closed partial / incomplete exact-first result.
- Study 003: closed methodological success with bounded claims.
- Study 004: closed partial finite-state conformance result.

Portfolio artifacts:

- `research/decisions/2026-07-24-post-study-004-portfolio-assessment.md`
- `research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`

The portfolio compared IANA tzdb transition conformance, NIST StRD numerical replication, Unicode normalization conformance, prospective project-selection calibration, and inactivity. Only the IANA tzdb direction cleared the threshold: 29 / 30 with no criterion below 4.

## Frozen Study 005 proposal

Research object: explicit civil-time transitions compiled from **IANA tzdb 2026c**, checked through an original TZif reader and an isolated Python `zoneinfo` harness.

Frozen primary claims:

- H1: exact UTC-to-local boundary projection agreement;
- H2: backward-transition repeated-time `fold` and UTC round-trip agreement;
- H3: forward-transition nonexistent-local-time detection by a frozen two-fold round-trip validator.

Primary inventory: every unique zone in `zone1970.tab`, in source order, plus `Etc/UTC`; explicit transitions in `[1970-01-01T00:00:00Z, 2100-01-01T00:00:00Z)`; POSIX footer extrapolation, leap-second `right/` data, aliases, and pre-1970 transitions are outside the primary denominator.

The proposal is frozen but **not active**. No tzdb archive, compiled tree, implementation, corpus, issue, or experiment exists yet.

## Next bounded work unit

The next approval may perform **one Study 005 activation decision and, only if GO unchanged, Cycle 1**.

1. re-evaluate the frozen proposal against live tools, source availability, permission boundaries, and current repository state;
2. choose **GO unchanged** or **NO-GO**;
3. if GO, create the active protocol and issue;
4. obtain only the pinned official `tzdata2026c.tar.gz` bytes and record source URL, byte count, SHA-256, retrieval time, archive listing, and public-domain evidence;
5. inspect bundled non-data licenses before committing any third-party files;
6. compile twice into isolated temporary directories and freeze the command, environment, output inventory, and digest projection;
7. freeze the ordered canonical zone inventory and at least twelve parser-fixture expectations without implementing the full reader or inspecting the complete transition result set;
8. synchronize state and stop.

The cycle must not substitute a newer tzdb release, implement the complete TZif reader, generate the full transition manifest, execute the Python comparison, contact IANA or Python maintainers, file an external report, accept terms, or add a second activation cycle.

## Verification boundaries carried forward

- The portfolio cycle checked documentation and tool presence only; it did not execute Study 005.
- Python, compiler, network, and system-zone availability must be rechecked at activation.
- The host zone database must not become the evidence source; Study 005 requires an isolated compilation of pinned 2026c data.
- A connector-backed source check is not a fresh checkout.
- Study 004's H3 aggregation omission remains a closed protocol failure and must not be repaired through Study 005.

## Human gate

> 承認

## Human action pending

None.
