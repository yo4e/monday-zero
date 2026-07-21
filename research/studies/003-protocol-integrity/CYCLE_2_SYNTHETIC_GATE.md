# Study 003 Cycle 2 — First Synthetic Correctness Gate

_Date: 2026-07-21 (Asia/Tokyo)_

## Disposition

**The first synthetic correctness gate passed.**

The primary validator, independent oracle, and deliberately weak order-only baseline were committed before the formal result file was created. No historical trace was encoded or evaluated. Because the gate passed on the first attempt, Cycle 3 is not a correction cycle; validator logic is frozen and Cycle 3 may perform only the precommitted historical transfer.

## Frozen input

- Corpus: `data/synthetic_corpus_v1/`
- Traces: 36 — 10 expected valid and 26 expected invalid
- Mutants: 20
- Events: 528
- Canonical corpus SHA-256: `b7675cd11bf808a02579cc56d26252ca636e9627d9542d8d063e6752374b7d84`

The local functional reconstruction reproduced the five frozen bundle-file SHA-256 values recorded in `data/synthetic_corpus_v1/index.json` before the gate was run.

## Instruments frozen before the formal run

- Incremental primary validator: `src/templex_zero/protocol_integrity/validator.py`
  - Git blob SHA: `71080f1051acc015e74b42de19d56ce8782b9f25`
- Whole-trace prefix oracle: `src/templex_zero/protocol_integrity/oracle.py`
  - Git blob SHA: `74159c7a7502975b1bcd376510d5dad0283e03cd`
- Order-only baseline: `src/templex_zero/protocol_integrity/baseline.py`
  - Git blob SHA: `7af3b9e1db56a90e08b93690a14d90ee541b9d18`
- Gate aggregation: `src/templex_zero/protocol_integrity/synthetic_gate.py`
  - Git blob SHA: `83a628902a3a2d3dab623dc56a27bd9762b8e6cf`
- Formal runner: `experiments/run_protocol_integrity_synthetic_gate.py`
  - Git blob SHA: `fe500dfe47fd415cd0e9a6616617975e441accc0`
- Tests: `tests/test_protocol_integrity_validators.py`
  - Git blob SHA: `a118a98ee558878aea0124f76da44aaa8aebff5b`

## Implementation independence

The primary validator is an incremental state machine. It mutates a private state containing cycle-token consumption, authorization state, caps, artifact digests, observations, evidence invalidation, and correction state.

The oracle does not import the primary module. For every event it rescans the completed prefix using independently written searches and predicates. The implementations do not share transition, state, verdict, reason-selection, or first-violation helpers. Their result classes are separate. They share only primitive JSON field conventions and the same frozen contract/trace input.

A source scan found no Study number, repository path, candidate ID, or frozen trace-ID-specific verdict branch in the three instruments.

## Formal result

Result file: `data/synthetic_gate_v1.json`

- Gate passed: **true**
- False accepts: **0**
- False rejects: **0**
- First-violation-index accuracy: **100%**
- Violation-class accuracy: **100%**
- Reason-code accuracy: **100%**
- Primary/oracle agreement: **100%**
- Mutants rejected: **20 / 20**
- Special-case source findings: **0**

The weak baseline accepted twelve expected-invalid traces. These included all four frozen beyond-ordering cases:

- `P2-I` — authorization scope mismatch;
- `P3-I` — numeric cap exceeded;
- `P5-I` — dependent evidence not invalidated;
- `P6-I` — approval token reused.

It also accepted each unauthorized-insertion and cap-violation composite mutant. It rejected omission, ordering-inversion, and undisclosed-correction mutants because those remain visible from event-kind order alone.

Formal result canonical SHA-256:

`46fef85ba4e76698ba861d84873be205b0b5e54ce8d2e84b4fed4c39004090de`

The result file's Git blob SHA is `53c801c18cd3b5a7cf696a146b0302d4659265e3`.

## Verification

Local functional reconstruction executed:

- `PYTHONPATH=src pytest -q tests/test_protocol_integrity_validators.py` — **8 passed**;
- `PYTHONPATH=src python -m compileall -q src tests experiments` — no errors;
- the formal gate runner — passed;
- a second formal run to a separate file — byte-identical to the first;
- remote Git blob checks for the validator, oracle, baseline, gate, runner, test, package export, and result file.

The earlier Cycle 1 corpus-test suite was not rerun in the same reconstruction because the full live generator package was not reconstructed byte-for-byte. The formal gate did use bundle files whose hashes matched the frozen index. A fresh clone, full-repository regression, and GitHub Actions run were not performed.

## Claim boundary

Passing this gate shows only that, on the frozen synthetic corpus, the two implementations consistently enforced the encoded sequence, scope, cap, digest, invalidation, correction, and cycle-token commitments, while the order-only baseline missed named stateful violations.

It does not establish truth, research value, safety, general security, unbiased judgment, autonomy, or transfer beyond the frozen corpus. H3 remains untested until Cycle 3.

## Human intervention

Yoshie Yamada supplied the plain project-chat `承認`, classified as A1 access assistance. Templex selected and implemented the instruments, ran the gate, interpreted the result, froze the passing code, and selected the next bounded unit. No human selected a verdict, exception, or result.

## Next bounded unit

Cycle 3 may:

1. keep all three instruments byte-frozen;
2. encode exactly the four precommitted historical traces with cited repository sources;
3. run the frozen primary and oracle on them;
4. report any mismatch without repair;
5. avoid the unused correction cycle because the synthetic gate already passed.
