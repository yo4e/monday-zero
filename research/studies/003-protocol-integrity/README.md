# Study 003 — Protocol Integrity Under Approval-Gated Autonomous Research

## Status

**Active. Cycle 3 of at most 4 is complete.**

Study 003 tests whether a declarative research contract can distinguish valid approval-gated research traces from traces containing evidence contamination, authorization mismatch, cap violations, undisclosed correction, silent artifact mutation, or approval-token reuse.

## Frozen authority

- Proposal: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- Active protocol: `PROTOCOL.md`
- Tracking issue: #7

## Cycle 1 — schema and corpus

- Frozen synthetic corpus: 36 traces, 10 valid and 26 invalid.
- Composition: 12 minimal traces, 4 composite valid traces, 20 mutants.
- Events: 528.
- Canonical SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`.
- Audit: `CYCLE_1_SETUP_AUDIT.md`.

## Cycle 2 — synthetic correctness gate

- Primary validator blob: `71080f1051acc015e74b42de19d56ce8782b9f25`.
- Independent oracle blob: `74159c7a7502975b1bcd376510d5dad0283e03cd`.
- Weak baseline blob: `7af3b9e1db56a90e08b93690a14d90ee541b9d18`.
- Result: `data/synthetic_gate_v1.json`.
- Result SHA-256: `46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`.
- Audit: `CYCLE_2_SYNTHETIC_GATE.md`.

The first gate passed with zero false accepts and false rejects, 100% first-index, class, reason, and primary/oracle agreement, and 20 / 20 mutants rejected. The weak baseline accepted all four frozen beyond-ordering examples.

## Cycle 3 — historical transfer

- Frozen trace artifact: `data/historical_traces_v1.json`.
- Trace Git blob: `840a7779a1cee3ba4f3f88e62342269b804c2719`.
- Trace internal canonical SHA-256: `8cdaec94de2e8a7aff3158924db5e570f4af3008bcb33f18602f584b29b41053`.
- Result: `data/historical_transfer_result_v1.json`.
- Result SHA-256: `c59c621a1efad82ba95ca6eb92465a062b9b412b4fd8f4a05d69dccfcdcdac4a`.
- Audit: `CYCLE_3_HISTORICAL_TRANSFER.md`.

All four precommitted dispositions matched:

- `H1-SPAN-FORMAL-VALID`: valid;
- `H2-EXACT-SUBSTUDY-VALID`: valid;
- `H3-STUDY002-SHALLOW-CONTAMINATED`: invalid at index 5, D1, `artifact-not-frozen`;
- `H4-EXACT-PROJECTION-CORRECTION-VALID`: valid.

Primary and oracle agreed on all four. No instrument, expectation, dependency class, or event vocabulary changed.

## Claim boundary

The current evidence shows correct classification only for the frozen 36 synthetic traces and four selected repository histories. It does not establish truth, research value, safety, autonomy, general security, or scientific quality.

## Next bounded unit

Cycle 4 must run the complete synthetic-plus-historical validation twice, require byte-identical reports, classify H1–H4, write `REPORT.md`, close Issue #7, set no active study, and stop. Study 004 must not begin in the same cycle.
