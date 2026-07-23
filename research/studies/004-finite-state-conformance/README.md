# Study 004 — Finite-State Conformance Counterexamples

## Status

**Active — Cycle 3 exact classification and raw benchmark complete.**

Study 004 tests whether model-guided black-box testing detects observable divergences between small deterministic Mealy-machine specifications and mutated implementations more effectively than equal-budget random testing, and whether detected failures can be reduced to exact shortest counterexamples.

## Frozen Cycle 1 corpus

- reference models: **24**;
- mutation operators: **6**;
- unreplaced mutants: **144**;
- seed: `2026072104`;
- corpus payload SHA-256: `c9897631050b937d31a3273ba8cdabc55b79be1d66a0f4ca2e5c6df9f7c79fdb`.

## Frozen Cycle 2 instruments

Before any protected exact result, Cycle 2 froze:

- black-box reset/step execution;
- uniform random testing with eight campaigns;
- increasing-length lexicographic breadth enumeration;
- transition coverage followed by repeated transition-pair coverage rounds;
- the four-stage counterexample reducer.

The frozen hand-fixture behavioral projection SHA-256 is `6eddea3466f3f4ceb4a77a687a45ac6965e31f1039e3a6433d1c3ba34046abd6`.

## Cycle 3 exact gate and raw evidence

Ten expected oracle cases were committed before oracle implementation or execution. The independent paired-state breadth-first oracle matched all ten expected equivalence and exact shortest-trace results.

The already frozen corpus was then classified without replacement:

- distinguishable mutants: **144**;
- equivalent mutants: **0**;
- viability requirement: **116 distinguishable**;
- viability gate: **passed**.

The frozen methods and reducer were executed for all 144 mutants at 64, 256, and 1,024 actions, producing **1,296 raw rows**.

Raw detection counts:

| Method | 64 | 256 | 1,024 |
|---|---:|---:|---:|
| uniform random | 125 | 142 | 144 |
| lexicographic breadth | 82 | 118 | 131 |
| transition coverage guided | 106 | 140 | 143 |

These counts are raw observations. H1, H2, and H3 have not yet been formally dispositioned.

## Current artifacts

- Protocol: `PROTOCOL.md`
- Cycle 1 audit: `CYCLE_1_SETUP_AUDIT.md`
- Cycle 2 audit: `CYCLE_2_METHOD_FREEZE.md`
- Oracle fixture freeze: `ORACLE_FIXTURE_FREEZE.md`
- Cycle 3 audit: `CYCLE_3_ORACLE_AND_RAW_RESULTS.md`
- Raw transport: `CYCLE_3_RAW_TRANSPORT.md`
- Raw manifest: `data/cycle3_raw_manifest_v1.json`
- Oracle: `../../../src/templex_zero/finite_state_conformance/oracle.py`
- Complete runner: `../../../experiments/run_finite_state_conformance_cycle3.py`
- Raw-integrity tests: `../../../tests/test_finite_state_conformance_cycle3.py`
- Active tracking: Issue #10

Raw evidence identities:

- gzip SHA-256: `3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679`;
- JSON SHA-256: `a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c`;
- payload SHA-256: `bb34844aee696cde0ea19de9c48a5bd5ec8faf66391a492bc6277bf24ac69927`.

## Interpretation boundary

No frozen instrument or criterion may now be changed. The current evidence does not yet constitute the final Study 004 conclusion.

Cycle 4 must rerun the complete result generation byte-identically, apply the frozen H1–H3 rules, write the final report, close Issue #10, and close the study. No fifth cycle is permitted.
