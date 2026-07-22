# Study 004 — Finite-State Conformance Counterexamples

## Status

**Active — Cycle 1 corpus freeze complete.**

Study 004 tests whether model-guided black-box testing detects observable divergences between small deterministic Mealy-machine specifications and mutated implementations more effectively than equal-budget random testing, and whether detected failures can be reduced to exact shortest counterexamples.

## Cycle 1 result

- Activation decision: **GO unchanged**.
- Reference models: **24**.
- Topology cells: 2 state sizes × 3 families × 4 variants.
- Mutation operators: **6**.
- Frozen mutants: **144**.
- Generation seed: `2026072104`.
- Corpus payload SHA-256: `c9897631050b937d31a3273ba8cdabc55b79be1d66a0f4ca2e5c6df9f7c79fdb`.
- Corpus file SHA-256: `82fcd584661e4860167ff114041868b923adb6861395a249564af4ff771b8fa2`.
- Reference-model payload SHA-256: `7925911d9f834d71a360defc862d8d67262989eb2e957cf334b94a1b3a58202b`.
- Reference-model file SHA-256: `bf3eab9884381a634d90803d3367c4700c8553ac43ec112355b2881dc4aaa902`.
- Targeted tests: **8 passed**.
- Compile verification: passed.
- Two independent in-process generations: byte-identical.

## Frozen artifacts

- Protocol: `PROTOCOL.md`
- Cycle 1 audit: `CYCLE_1_SETUP_AUDIT.md`
- Corpus manifest: `data/corpus_v1.json`
- Reference-model bundle: `data/models_v1.json`
- Schema: `../../../src/templex_zero/finite_state_conformance/schema.py`
- Generator: `../../../src/templex_zero/finite_state_conformance/corpus.py`
- Generator command: `../../../experiments/generate_finite_state_conformance_corpus.py`
- Tests: `../../../tests/test_finite_state_conformance_corpus.py`
- Active tracking: Issue #10

## Current boundary

The corpus has **not** been classified by observational equivalence. No uniform-random, lexicographic-breadth, transition-coverage-guided, reducer, exact-oracle, or formal benchmark result exists.

Do not inspect or add exact shortest distinguishing traces before the three testing methods and reducer are frozen. Doing so contaminates H1–H3 under the protocol.

## Next bounded cycle

Cycle 2 may implement and freeze only:

1. uniform-random testing;
2. lexicographic breadth enumeration;
3. transition-coverage-guided testing;
4. the frozen reducer;
5. hand-authored unit fixtures and deterministic tests.

Cycle 2 must not implement or run the exact oracle, classify corpus mutants, or produce formal benchmark results.
