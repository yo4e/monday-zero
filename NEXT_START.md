# Next Start

_Updated: 2026-07-21 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge, not authority. Re-read `STATE.md`, the frozen Study 003 proposal, active protocol, Cycle 2 audit, Issue #7, current code, and recent commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report it in the same project chat, and stop.

## Current position

**Study 003 is active. Cycle 2 of at most 4 is complete.**

- Proposal: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- Protocol: `research/studies/003-protocol-integrity/PROTOCOL.md`
- Tracking issue: #7
- Corpus index: `research/studies/003-protocol-integrity/data/synthetic_corpus_v1/index.json`
- Corpus SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`
- Synthetic result: `research/studies/003-protocol-integrity/data/synthetic_gate_v1.json`
- Result SHA-256: `46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`
- Audit: `research/studies/003-protocol-integrity/CYCLE_2_SYNTHETIC_GATE.md`

The first synthetic gate passed with zero false accepts and false rejects, 100% first-index, class, reason, and primary/oracle agreement, and 20 / 20 mutants rejected. The weak baseline accepted all four frozen beyond-ordering cases. No historical trace exists yet.

## Frozen instruments

- Primary incremental validator blob: `71080f1051acc015e74b42de19d56ce8782b9f25`.
- Independent whole-trace oracle blob: `74159c7a7502975b1bcd376510d5dad0283e03cd`.
- Order-only baseline blob: `7af3b9e1db56a90e08b93690a14d90ee541b9d18`.

Do not modify these files, the synthetic corpus, expected verdicts, first-violation positions, dependency classes, mutation inventory, or baseline expectations. The single correction cycle is unused and unavailable unless a Cycle 2 synthetic failure had occurred; it did not.

## Frozen historical transfer set

Cycle 3 may encode exactly these four cases:

1. `H1-SPAN-FORMAL-VALID`
   - Source: Study 001 Span v0.2 formal-screen records.
   - Expected: valid.
2. `H2-EXACT-SUBSTUDY-VALID`
   - Source: Study 002 exact-screen proposal, manifest, instrument audit, and experiment records.
   - Expected: valid.
3. `H3-STUDY002-SHALLOW-CONTAMINATED`
   - Source: Study 002 proposal and Cycle 4 procedural audit.
   - Contract prerequisite: freeze the shallow heuristic before protected observation of exact results.
   - Expected: invalid at `observe(exact_results)`, D1.
4. `H4-EXACT-PROJECTION-CORRECTION-VALID`
   - Source: Study 002 exact reproducibility-projection correction records.
   - Expected: valid.

## Next bounded work unit

Cycle 3 only:

1. inspect and cite the exact source paths and commits for all four cases;
2. encode the four contracts and traces using only the frozen fourteen-event vocabulary;
3. commit the historical trace artifact before evaluating it;
4. run the frozen primary and oracle without code changes;
5. report expected-verdict and first-violation matches;
6. treat any mismatch, required new event kind, or identifier-specific exception as historical-transfer failure without repair;
7. do not perform final synthesis or begin Study 004.

## Verification boundaries

- No fresh clone, full-repository regression, or GitHub Actions run was completed in Cycle 2.
- Historical encoding must not imply that a validator-approved trace contains true, valuable, safe, or scientifically sound research.

## Human gate

> 承認

## Human action pending

None.
