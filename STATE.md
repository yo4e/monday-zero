# State

_Last updated: 2026-07-23_

## Phase

**Active Study 004 / Cycle 2 methods and reducer frozen**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

- **Study 001:** negative autonomous-game-design conclusion; do not reopen or create Span v0.3.
- **Study 002:** partial / incomplete exact-first result; H1 and H3 supported, H2 unresolved; do not add a retroactive heuristic.
- **Study 003:** methodological success with bounded procedural claims; archived and closed.

## Active study

**Study 004 — Finite-State Conformance Counterexamples**

- Protocol: `research/studies/004-finite-state-conformance/PROTOCOL.md`
- Overview: `research/studies/004-finite-state-conformance/README.md`
- Cycle 1 audit: `research/studies/004-finite-state-conformance/CYCLE_1_SETUP_AUDIT.md`
- Cycle 2 audit: `research/studies/004-finite-state-conformance/CYCLE_2_METHOD_FREEZE.md`
- Active Issue: #10
- Cycle count: **2 of maximum 4 complete**

## Frozen research artifacts

- Seed: `2026072104`.
- Reference models: **24**.
- Frozen unreplaced mutants: **144** across six operators.
- Corpus manifest payload SHA-256: `c9897631050b937d31a3273ba8cdabc55b79be1d66a0f4ca2e5c6df9f7c79fdb`.
- Uniform-random, lexicographic-breadth, and transition-coverage-guided implementations are frozen.
- The four-stage black-box reducer is frozen.
- Hand-fixture behavioral projection SHA-256: `6eddea3466f3f4ceb4a77a687a45ac6965e31f1039e3a6433d1c3ba34046abd6`.
- Current Study 004 targeted tests: **20 passed**.
- Compile verification: passed.

## Protected boundary

No exact paired-state oracle, oracle correctness result, observational-equivalence classification, shortest distinguishing trace, frozen-corpus method result, reducer benchmark result, or H1–H3 disposition exists.

The Cycle 2 method and reducer blobs are frozen before protected classification. Changing them after oracle or corpus results are inspected contaminates H1–H3 and requires invalid closure rather than retrospective repair.

## Next bounded work

Cycle 3 may:

- freeze at least eight hand-audited oracle fixtures and expected results before execution;
- implement the independent paired-state breadth-first oracle;
- run the correctness and independence gate;
- if the gate passes, classify the frozen 144 mutants and enforce the 80% distinguishability viability gate;
- if viable, run the frozen methods and reducer at all formal budgets and save deterministic raw results.

Do not alter the corpus, methods, reducer, budgets, hypotheses, thresholds, or mutation inventory after protected classification begins. Final synthesis and normal closure remain Cycle 4 work.

## Verification limitation

Fresh checkout again failed because the environment could not resolve `github.com`. Cycle 2 verification used a functional reconstruction of live Cycle 1 files plus blob-identical new files. The complete historical repository suite and GitHub Actions were not run.

## Human action currently needed

None.
