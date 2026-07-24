# Study 005 Cycle 3 — Formal Runner Source-Identity Correction

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **Corrected and resolved by Cycle 4 exact-source reproduction**_

## Authority

This record supersedes earlier source-identity statements for Cycle 3. Cycle 4 directly verified the live Git blobs, the preserved local execution source, and the scientific effect of their differences. Machine-readable identities are in `data/cycle4_source_identities_v1.json`; the complete resolution is in `CYCLE_4_REPRODUCTION_AND_CLOSURE.md`.

## Correct identities

Pre-outcome committed files:

- `experiments/study005_cycle3.py`: Git blob `f1fcb11678fc0b834cc968fb718ce91fd4951e75`;
- `src/templex_zero/zoneinfo_harness.py`: Git blob `55e25f63296c67bb07a0ade9dcc44c38b5b8676a`;
- `tests/test_zoneinfo_harness.py`: Git blob `af7d7392f239ef19ee5fa996c534408533bff916`;
- `src/templex_zero/tzif_reader.py`: Git blob `11a7e40c3f15f81677ae7321475e364b70d5830f`.

Cycle 3 execution-local runner:

- bytes: 8,810;
- SHA-256: `cbbd781f478c0d54c59f1b1bea66f515698adccdb17111bd14fa1e87b1b0c381`;
- computed Git blob: `06280fe9e6e7347c5de91f6736c4fc72577252a3`.

The repository file `data/study005_cycle3_executed_runner_v1.py` has Git blob `3eccb9419bab3159ec09c663caaa018aa0c07ca0`. It is a semantically compressed transcription, not a byte-identical copy of the execution-local 8,810-byte runner.

The earlier identifiers `f1fcb1166580d874112c09ff8fe438ae8837a81a`, `06280fe92a279a3ef847dd07448a041c379af9b0`, `09692057aae2575c6760e07a41d378a79571c3a0`, and `0ce9da76c736b1d4585014da9250bfd49b520d1c` were transcription errors and are withdrawn.

## Difference assessment

The pre-outcome and execution-local runners have different raw ASTs because the execution-local form contains two unused imports: `hashlib` and `importlib.util`. After removing those unused imports, the ASTs are identical. Formatting differs, but no comparison, isolation, witness-generation, serialization, or output logic difference was found.

Cycle 3 also imported a compatibility bridge to an independent local TZif parser rather than the literal committed reader. That remains a procedural deviation.

## Cycle 4 resolution

Cycle 4 reconstructed the exact committed reader, harness, tests, Cycle 2 builder, pre-outcome Cycle 3 runner, and result reconstructor from their verified Git blobs. It rebuilt the pinned source and compiled tree, reproduced the byte-identical 313-zone / 18,071-transition manifest, and executed the formal corpus once.

The exact-source reproduction produced:

- H1: 90,079 records, zero nonzero masks;
- H2: 26,778 records, zero nonzero masks;
- H3: 44,790 records, zero nonzero masks;
- mismatch records: zero.

All H1, H2, and H3 record families were byte-identical to Cycle 3. The only complete-result difference was the absolute temporary path stored in `environment.tzpath_after[0]`. Therefore, the source deviations had no observed effect on the frozen scientific payload, while the procedural deviation remains part of the permanent record.

Study 005 is closed after Cycle 4. No fifth cycle exists.
