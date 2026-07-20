# Next Start

_Updated: 2026-07-21 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the frozen Study 003 proposal, active protocol, Issue #7, current code, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report it in the same project chat, and stop.

## Current position

**Study 003 is active. Cycle 1 of at most 4 is complete.**

- Proposal: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- Protocol: `research/studies/003-protocol-integrity/PROTOCOL.md`
- Tracking issue: #7
- Corpus index: `research/studies/003-protocol-integrity/data/synthetic_corpus_v1/index.json`
- Corpus SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`

Cycle 1 created schema, canonical serialization, a deterministic generator, and exactly 36 synthetic traces: 10 valid and 26 invalid. Targeted tests passed 8 cases. No validator result or historical encoding exists.

## Frozen boundaries

- Do not alter the 36 traces, expected verdicts, first-violation indices, dependency classes, mutation inventory, or baseline expectations after validator work begins.
- Do not encode historical traces before the synthetic gate passes and validator code is frozen.
- Do not share transition, state, verdict, reason-code, or first-violation helpers between the primary validator and oracle.
- Do not add study-, path-, commit-, candidate-, or trace-ID-specific verdict branches.
- Do not reopen Study 001 or repair Study 002.
- Do not begin Study 004.

## Next bounded work unit

Cycle 2 only:

1. implement the primary incremental state-machine validator;
2. independently implement the whole-trace oracle using prefix predicates;
3. implement the deliberately weak order-only baseline;
4. run all three on the frozen 36-trace corpus;
5. report false accepts, false rejects, first-violation accuracy, class accuracy, oracle agreement, mutation coverage, and named baseline false accepts;
6. do not encode or evaluate historical traces.

Required result is zero false accepts and false rejects, 100% first-index and class accuracy, 100% primary/oracle agreement, all twenty mutants rejected, and the four named nontrivial invalid traces accepted by the weak baseline. If the gate fails, do not change corpus expectations; Cycle 3 becomes the sole correction cycle.

## Human gate

> 承認

## Human action pending

None.
