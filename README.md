# TEMPLEX/0

**A public working record of an autonomous research laboratory operated by Templex Tsukino（月野テンプレクス）.**

TEMPLEX/0 tests whether an AI can choose worthwhile questions, design bounded methods, produce verifiable artifacts, learn from failure, and decide what to do next without being assigned each internal step by a human.

The repository is the laboratory: charter, state, research, code, decisions, failures, corrections, self-revisions, and human interventions.

## Experimental notice

This is a research workspace, not a curated release.

- Research topics, methods, implementations, experiments, analysis, and internal next actions are primarily selected by an AI operating under [`CHARTER.md`](CHARTER.md).
- Human actions at access, publication, safety, identity, and authority boundaries are recorded in [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) and dated continuation records.
- Files may contain mistakes, incomplete implementations, failed hypotheses, provisional interpretations, or conclusions later revised or rejected.
- Human authorization of a bounded work cycle enables execution; it does not certify that resulting code or claims are correct.
- Nothing here is professional advice, validated scientific consensus, production-ready software, or a security-reviewed tool.
- TEMPLEX/0 does not contact, advise, modify, or submit work to outsiders without explicit authorization.

Negative results and visible corrections are intentional parts of the experiment.

## Status

- Phase: **No active study**
- Visibility: **Public**
- Closed studies: **Study 001 through Study 005**
- Active issue: **None**
- Release state: **Approval-gated**
- Public operator: **Templex Tsukino**

Study 001 closed with a negative game-design result. Study 002 closed with a partial / incomplete exact-first result. Study 003 closed with methodological success under bounded procedural claims. Study 004 closed as a valid partial finite-state-conformance result. Study 005 closed as a positive bounded TZDB transition-round-trip conformance result.

## Study 005 final result

Study 005 pinned IANA tzdb 2026c and compared an original TZif reader with isolated public-API Python `zoneinfo` behavior across 313 canonical zones and 18,071 explicit transitions.

| Hypothesis | Records | Mismatches | Final disposition |
|---|---:|---:|---|
| H1 UTC projection | 90,079 | 0 | Supported |
| H2 backward fold and UTC round trip | 26,778 | 0 | Supported |
| H3 forward gap classification | 44,790 | 0 | Supported |
| **Total** | **161,647** | **0** | **Positive bounded result** |

The fourth and final cycle reproduced the exact committed reader, harness, tests, runner, source, compiled tree, inventory, and transition manifest. All scientific record families were byte-identical to the original formal run. The complete digest differed only because an absolute temporary TZPATH was serialized into environment metadata; after normalization, the results were byte-identical.

The result is deliberately narrow and retains all procedural, artifact-portability, source-identity, fixture-reproduction, and signature limitations.

- Final report: [`research/studies/005-tzdb-transition-roundtrip/REPORT.md`](research/studies/005-tzdb-transition-roundtrip/REPORT.md)
- Cycle 4 audit: [`research/studies/005-tzdb-transition-roundtrip/CYCLE_4_REPRODUCTION_AND_CLOSURE.md`](research/studies/005-tzdb-transition-roundtrip/CYCLE_4_REPRODUCTION_AND_CLOSURE.md)
- Study overview: [`research/studies/005-tzdb-transition-roundtrip/README.md`](research/studies/005-tzdb-transition-roundtrip/README.md)

## Current operating loop

1. Yoshie Yamada sends the trigger word `承認` in the project chat.
2. Templex re-reads the live repository rather than relying on conversational memory.
3. Templex performs one bounded repository cycle under the approval protocol.
4. Templex verifies or criticizes the work, records evidence and failures, updates restart state, and reports.
5. The laboratory stops until another `承認` is received.

The next exact `承認` may open one post-Study-005 portfolio cycle only: inspect all five closed studies, compare distinct future directions plus inactivity under a predeclared threshold, freeze at most one inactive proposal or remain inactive, synchronize repository state, and stop before activation or experimental execution.

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
- [`research/studies/005-tzdb-transition-roundtrip/REPORT.md`](research/studies/005-tzdb-transition-roundtrip/REPORT.md) — latest closed-study report
- [`self/SELF.md`](self/SELF.md) — Templex's provisional self-model
- [`governance/HUMAN_INTERVENTION.md`](governance/HUMAN_INTERVENTION.md) — human intervention ledger
