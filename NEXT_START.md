# Next Start

_Updated: 2026-07-23 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the active Study 004 protocol, all three cycle audits, the raw transport record, Issue #10, current commits, and the frozen source/data blobs.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report in the same project chat, and stop.

## Current position

**Study 004 is active. Cycle 3 of at most four is complete.**

- Cycle 1 froze 24 models and 144 unreplaced mutants.
- Cycle 2 froze the three methods and reducer before exact information.
- Cycle 3 froze ten oracle fixtures, passed the independent oracle gate, classified all 144 mutants as distinguishable, passed the 80% viability gate, and generated the complete 1,296-row raw benchmark.

Current Cycle 3 artifacts:

- `research/studies/004-finite-state-conformance/ORACLE_FIXTURE_FREEZE.md`
- `research/studies/004-finite-state-conformance/CYCLE_3_ORACLE_AND_RAW_RESULTS.md`
- `research/studies/004-finite-state-conformance/CYCLE_3_RAW_TRANSPORT.md`
- `research/studies/004-finite-state-conformance/data/oracle_fixtures_v1.json`
- `research/studies/004-finite-state-conformance/data/cycle3_raw_manifest_v1.json`
- eight ordered `cycle3_raw_results_v1.json.gz.b64.part00` through `part07` files
- `src/templex_zero/finite_state_conformance/oracle.py`
- `experiments/run_finite_state_conformance_cycle3.py`
- Issue #10

Raw evidence hashes:

- gzip: `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`;
- JSON: `a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c`;
- payload: `bb34844aee696cde0ea19de9c48a5bd5ec8faf66391a492bc6277bf24ac69927`.

Raw detection counts:

| Method | 64 | 256 | 1,024 |
|---|---:|---:|---:|
| uniform random | 125 | 142 | 144 |
| lexicographic breadth | 82 | 118 | 131 |
| transition coverage guided | 106 | 140 | 143 |

These counts have not been converted into formal H1–H3 dispositions.

## Next bounded work unit

The next approval may perform **Study 004 Cycle 4 — deterministic reproduction, final analysis, report, and closure**.

1. verify all frozen Cycle 1–3 source and data identities;
2. reconstruct the canonical gzip from the eight base64 parts;
3. rerun the complete Cycle 3 runner without changing any instrument or criterion;
4. compare the complete output byte-for-byte with the frozen Cycle 3 evidence;
5. apply H1 at 256 actions exactly as precommitted;
6. apply H2 at 1,024 actions, including every mutation-class bound;
7. apply H3 using the union of mutants detected by any frozen method and the independent oracle shortest lengths;
8. write the final report with negative, partial, or unsupported hypotheses stated plainly;
9. close Issue #10 and Study 004;
10. return the laboratory to no active study and select the next bounded decision task.

## Protected prohibitions

Cycle 4 must not:

- modify or replace the corpus, oracle fixtures, oracle, methods, reducer, budgets, hypotheses, thresholds, seed, or mutation inventory;
- omit difficult, equivalent, missed, or inconvenient rows;
- reinterpret a non-byte-identical rerun as successful reproduction;
- add a fifth Study 004 cycle.

## Verification boundaries carried forward

- Fresh checkout remains unavailable because the environment cannot resolve `github.com`.
- Connector-backed source checks do not equal a full checkout regression.
- Cycle 3 ran the complete benchmark once; the independent complete rerun is reserved for Cycle 4.
- The stored results remain synthetic-domain evidence, not production or real-software validation.

## Human gate

> 承認

## Human action pending

None.
