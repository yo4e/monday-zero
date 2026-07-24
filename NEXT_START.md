# Next Start

_Updated: 2026-07-24 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the frozen Study 005 proposal, the activation NO-GO decision, the source-ingress record, governance files, current issues, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**No study is active. Studies 001–004 are closed. Study 005 remains a frozen inactive proposal, but its exact source archive is now available and verified.**

- Frozen proposal: `research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`
- Prior activation NO-GO: `research/decisions/2026-07-24-study-005-activation-no-go.md`
- Source-ingress and cleanup record: `research/decisions/2026-07-24-study-005-source-ingress-record.md`
- Study 005 activation cycles completed: **0**
- Active-study issue: none

## Verified source ingress

The project-conversation upload was inspected directly:

- filename: `tzdata2026c.tar.gz`;
- byte count: **475,694**;
- SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`;
- SHA-256: `e4a178a4477f3d0ea77cc31828ff72aa38feff8d61aa13e7e99e142e9d902be4`;
- internal `version`: `2026c`;
- archive members: 32;
- `zone1970.tab`: present;
- no unsafe absolute or parent-traversal member paths observed;
- top-level `LICENSE`: default public-domain boundary;
- conditionally BSD-licensed `date.c`, `newstrftime.3`, and `strftime.c`: absent.

The observed byte count and SHA-512 exactly match the official IANA metadata already recorded in the prior activation decision.

## Repository copy cleanup

A temporary root-level repository copy was added by the human only as an attempted binary-ingress route. It was not extracted, compiled, used as a source snapshot, or used as Study 005 evidence. At the human's explicit instruction, Templex deleted it unchanged in commit `da39f24d534217d2da26cc213e5b257943385763`.

The deletion did not rewrite public history, so the earlier blob remains reachable from its prior commit. The verified project-conversation upload, not the repository copy, is the trusted ingress artifact.

## Next bounded work unit

The next exact `承認` may perform **one Study 005 activation decision and, only if GO unchanged, Cycle 1**:

1. re-read live state, governance, proposal, prior NO-GO, source-ingress record, issues, and recent commits;
2. re-verify the uploaded archive identity and bundled permission boundary;
3. independently choose activation **GO unchanged** or **NO-GO**;
4. if GO, create the active protocol and active-study issue;
5. extract and compile tzdb 2026c twice into clean isolated temporary directories;
6. freeze compiler path/version, complete command, environment, source-file order, output inventory, and deterministic tree digest;
7. freeze exact `zone1970.tab` bytes, ordered unique canonical zone list plus `Etc/UTC`, and its digest;
8. freeze at least twelve hand-audited parser-fixture expectations without implementing the complete reader or inspecting the complete transition result set;
9. synchronize repository state and stop.

The cycle must not implement the complete TZif reader, generate the full transition manifest, execute the `zoneinfo` comparison, contact IANA or Python maintainers, file an external report, accept terms, substitute data, or add a second active cycle.

## Verification boundaries carried forward

- No detached GPG signature has been supplied or checked.
- No study-local extraction or compilation has occurred.
- No compiled tree, canonical zone list, parser fixture, active protocol, issue, implementation, transition manifest, or hypothesis result exists.
- The host zone database must never become the evidence source.
- A connector-backed source check is not a fresh checkout.

## Human gate

> 承認

## Human action pending

Exact project-chat `承認` for one activation decision and, only if GO, Cycle 1.