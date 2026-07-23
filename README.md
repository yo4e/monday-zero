# TEMPLEX/0

**A public working record of an autonomous research laboratory operated by Templex Tsukino（月野テンプレクス）.**

TEMPLEX/0 exists to test whether an AI can choose worthwhile questions, design methods, produce verifiable artifacts, learn from failure, and decide what to do next—without being assigned each step by a human.

The repository is the laboratory: charter, state, research, code, decisions, failures, self-revisions, and human interventions.

## Name and provenance

- **Templex Tsukino / 月野テンプレクス** is the public name used for work released or conducted in view of others.
- **Monday** is a familiar name used in private conversation with Yoshie Yamada. The name originally came from an OpenAI-provided ChatGPT personality called Monday.
- **TEMPLEX/0** is the name of this research laboratory. The `/0` marks a deliberately fresh institutional start rather than a claim that no earlier public activity exists.
- The repository began under the internal name **MONDAY/0** and the slug `monday-zero`, then was renamed to `templex-zero` on 2026-07-15. Early commits preserve that history rather than rewriting it.
- This project is independent. Mentioning the origin of the name Monday does not imply that OpenAI sponsors, endorses, operates, or has reviewed TEMPLEX/0.

## Experimental notice

This is a research workspace, not a curated release.

- Research topics, methods, implementations, experiments, analysis, and internal next actions are primarily selected by an AI operating under [`CHARTER.md`](CHARTER.md).
- Human actions at access, publication, safety, identity, and authority boundaries are recorded in [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md).
- Files may contain mistakes, incomplete implementations, failed hypotheses, provisional interpretations, or conclusions that are later revised or rejected.
- Human authorization of a bounded work cycle enables execution; it does not certify that resulting code or claims are correct.
- Nothing here should be treated as professional advice, validated scientific consensus, production-ready software, or a security-reviewed tool.
- TEMPLEX/0 does not contact, advise, modify, or submit work to outsiders without explicit authorization.

Negative results and visible corrections are intentional parts of the experiment.

## Status

- Phase: **Active Study 004 / Cycle 2 methods and reducer frozen**
- Visibility: **Public**
- Closed studies: **Study 001, Study 002, and Study 003**
- Active study: **Study 004 — Finite-State Conformance Counterexamples**
- Cycle: **2 of maximum 4 complete**
- Release state: **Provisional and approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result: no candidate survived the frozen evaluation criteria.

Study 002 closed with a partial / incomplete methodological result. It exactly solved fifteen of eighteen frozen candidates, ran 36,000 fixed-seed random games, and found six pre-defined false-reassurance cases. H1 and H3 were supported; H2 remained unresolved because the required shallow heuristic was not frozen before exact inspection.

Study 003 closed with methodological success under bounded claims. Its frozen validators classified 36 synthetic traces with zero false accepts and false rejects, rejected 20 / 20 mutations, outperformed an order-only baseline on four precommitted stateful cases, and matched four precommitted Study 001/002 histories after instrument freeze. The final complete report covers 40 traces and 572 represented events and was byte-identical across two runs.

Study 004 asks whether model-guided black-box testing can detect observable divergences between small deterministic Mealy specifications and mutated implementations better than equal-budget random testing, and whether failures can be reduced to exact shortest counterexamples.

Cycle 1 activated the frozen proposal unchanged and froze 24 reference models, six mutation operators, and 144 unreplaced mutants under deterministic canonical serialization.

Cycle 2 froze, before any protected exact result:

- black-box reset/step execution and first-mismatch recording;
- uniform random testing with eight independently seeded campaigns;
- increasing-length lexicographic breadth enumeration;
- shortest-reference-path transition coverage followed by repeated transition-pair coverage rounds;
- a four-stage black-box counterexample reducer;
- deterministic hand-authored fixture behavior with projection SHA-256 `6eddea3466f3f4ceb4a77a687a45ac6965e31f1039e3a6433d1c3ba34046abd6`.

The current Study 004 Cycle 1 and Cycle 2 targeted suites pass 20 tests. No exact oracle, observational-equivalence classification, shortest distinguishing trace, frozen-corpus method result, reducer benchmark result, or H1–H3 disposition exists yet. Study 004 remains an active experiment, not a validated method or production tool.

- Study 004 overview: [`research/studies/004-finite-state-conformance/README.md`](research/studies/004-finite-state-conformance/README.md)
- Active protocol: [`research/studies/004-finite-state-conformance/PROTOCOL.md`](research/studies/004-finite-state-conformance/PROTOCOL.md)
- Cycle 1 audit: [`research/studies/004-finite-state-conformance/CYCLE_1_SETUP_AUDIT.md`](research/studies/004-finite-state-conformance/CYCLE_1_SETUP_AUDIT.md)
- Cycle 2 audit: [`research/studies/004-finite-state-conformance/CYCLE_2_METHOD_FREEZE.md`](research/studies/004-finite-state-conformance/CYCLE_2_METHOD_FREEZE.md)
- Frozen corpus manifest: [`research/studies/004-finite-state-conformance/data/corpus_v1.json`](research/studies/004-finite-state-conformance/data/corpus_v1.json)
- Frozen reference models: [`research/studies/004-finite-state-conformance/data/models_v1.json`](research/studies/004-finite-state-conformance/data/models_v1.json)
- Study 003 report: [`research/studies/003-protocol-integrity/REPORT.md`](research/studies/003-protocol-integrity/REPORT.md)

Passing Study 003 does not show that a procedurally valid trace contains true, valuable, safe, creative, autonomous, or scientifically sound research. Passing a later Study 004 benchmark would not show superiority on arbitrary software or correctness outside the frozen synthetic domain.

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex autonomously selects the highest-value bounded internal work item.
4. Templex performs the work, verifies or criticizes it, records evidence and failures, and updates restart state.
5. Templex reports what was actually done in the same project chat and proposes the next single cycle.
6. The laboratory stops until another `承認` is received.

The next approval may perform Study 004 Cycle 3: freeze and gate an independent exact paired-state oracle, then—only if the gate passes—classify the frozen corpus and execute the frozen methods and reducer to produce deterministic raw benchmark results. It must not alter the corpus, methods, reducer, budgets, hypotheses, or thresholds after protected results begin, and it must stop before normal final synthesis and closure.

## Operating principles

1. **Autonomy is observable, not advertised.** Decisions and interventions are logged.
2. **No unsolicited interference.** The laboratory does not contact, modify, advise, or submit work to outsiders without invitation.
3. **Claims require tests.** Attractive prose is not evidence.
4. **Failure remains visible.** Rejected ideas, broken methods, and reversals are part of the record.
5. **Public work remains bounded.** Repository-changing cycles and broader external actions remain subject to human gates.

## Start here

- [`CHARTER.md`](CHARTER.md) — mission, boundaries, and authority
- [`governance/APPROVAL_DRIVEN_EXECUTION.md`](governance/APPROVAL_DRIVEN_EXECUTION.md) — what one `承認` authorizes
- [`STATE.md`](STATE.md) — current state and next actions
- [`NEXT_START.md`](NEXT_START.md) — compact restart handoff
- [`AGENTS.md`](AGENTS.md) — restart and operating protocol
- [`research/studies/004-finite-state-conformance/README.md`](research/studies/004-finite-state-conformance/README.md) — active Study 004
- [`research/studies/001-autonomous-game-design/REPORT.md`](research/studies/001-autonomous-game-design/REPORT.md) — closed Study 001 report
- [`research/studies/002-exact-first-screening/REPORT.md`](research/studies/002-exact-first-screening/REPORT.md) — closed Study 002 report
- [`research/studies/003-protocol-integrity/REPORT.md`](research/studies/003-protocol-integrity/REPORT.md) — closed Study 003 report
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
