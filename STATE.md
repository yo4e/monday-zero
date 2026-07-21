# State

_Last updated: 2026-07-21_

## Phase

**Study 003 active / historical transfer passed / cycle 3 of at most 4 complete**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

- Study 001: negative autonomous-game-design conclusion; do not reopen or create Span v0.3.
- Study 002: partial / incomplete exact-first result; H1 and H3 supported, H2 unresolved; do not add its missing shallow heuristic or replace its frozen candidates.

## Active Study 003

- Title: **Protocol Integrity Under Approval-Gated Autonomous Research**
- Frozen proposal: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- Active protocol: `research/studies/003-protocol-integrity/PROTOCOL.md`
- Tracking issue: #7
- Cycle limit: 4 approval-driven cycles including closure.

## Synthetic gate

- Corpus: 36 traces, 10 valid and 26 invalid, 528 events.
- Corpus SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`.
- Result: `research/studies/003-protocol-integrity/data/synthetic_gate_v1.json`.
- Result SHA-256: `46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`.
- False accepts/rejects: 0 / 0.
- First-index, class, reason, and primary/oracle agreement: 100%.
- Mutants rejected: 20 / 20.
- Weak baseline accepted twelve invalid traces, including the four frozen beyond-ordering cases.

## Frozen instruments

- Primary validator blob: `71080f1051acc015e74b42de19d56ce8782b9f25`.
- Independent oracle blob: `74159c7a7502975b1bcd376510d5dad0283e03cd`.
- Weak baseline blob: `7af3b9e1db56a90e08b93690a14d90ee541b9d18`.

These instruments may not change inside Study 003.

## Historical transfer

- Trace artifact: `research/studies/003-protocol-integrity/data/historical_traces_v1.json`.
- Trace Git blob: `840a7779a1cee3ba4f3f88e62342269b804c2719`.
- Trace internal canonical SHA-256: `8cdaec94de2e8a7aff3158924db5e570f4af3008bcb33f18602f584b29b41053`.
- Result: `research/studies/003-protocol-integrity/data/historical_transfer_result_v1.json`.
- Result SHA-256: `c59c621a1efad82ba95ca6eb92465a062b9b412b4fd8f4a05d69dccfcdcdac4a`.
- Expected-verdict matches: 4 / 4.
- First-violation matches: 4 / 4.
- Primary/oracle agreement: 4 / 4.
- H3 shallow-contamination trace rejected at index 5 with D1 `artifact-not-frozen`; the other three traces were accepted as expected.

## Verification limits

- Historical artifact and result matched locally generated Git blob SHA values.
- Two local historical evaluations produced identical deterministic result bytes.
- Fresh clone failed because the environment could not resolve `github.com`.
- Historical evaluation used a functional reconstruction of the live frozen validator and oracle source.
- Full-repository regression and GitHub Actions verification were not performed.

## Next action

Cycle 4 only:

1. run the complete synthetic-plus-historical validation twice;
2. require byte-identical deterministic reports;
3. classify H1–H4 and write `research/studies/003-protocol-integrity/REPORT.md`;
4. close Issue #7 and set no active study;
5. do not begin Study 004.

## Human action currently needed

None.
