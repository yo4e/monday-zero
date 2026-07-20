# Study 003 — Protocol Integrity Under Approval-Gated Autonomous Research

## Status

**Active. Cycle 1 of at most 4 is complete.**

Study 003 tests whether a declarative research contract can distinguish valid approval-gated research traces from traces containing evidence contamination, authorization mismatch, cap violations, undisclosed correction, silent artifact mutation, or approval-token reuse.

## Frozen authority

- Proposal: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- Final proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- Active protocol: `PROTOCOL.md`
- Tracking issue: #7

## Cycle 1 artifacts

- Schema and canonical serialization: `src/templex_zero/protocol_integrity/schema.py`
- Deterministic corpus generator: `src/templex_zero/protocol_integrity/corpus.py`
- Auditable bundle generator: `src/templex_zero/protocol_integrity/bundle.py`
- Regeneration script: `experiments/generate_protocol_integrity_corpus.py`
- Frozen corpus index: `data/synthetic_corpus_v1/index.json`
- Tests: `tests/test_protocol_integrity_corpus.py`
- Setup audit: `CYCLE_1_SETUP_AUDIT.md`

Corpus summary:

- 36 synthetic traces;
- 10 valid and 26 invalid;
- 12 minimal traces, 4 composite valid traces, and 20 mutants;
- 528 events total;
- canonical SHA-256 `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`.

No validator verdict logic, oracle, baseline execution, historical encoding, or experimental result exists yet.

## Next bounded unit

Cycle 2 may implement the primary validator, independent oracle, and frozen order-only baseline, then run the first synthetic correctness gate. Historical traces remain forbidden until that gate passes and validator code is frozen.
