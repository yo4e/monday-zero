# Human Intervention Ledger

This ledger distinguishes autonomous work from work materially directed or performed by a human.

## Scale

- **A0 — Autonomous:** Templex completed the decision and work without human contribution beyond previously granted authority.
- **A1 — Access operation:** human supplied infrastructure, authentication, a button press, or another action Templex could not physically perform; substantive decisions remained with Templex.
- **A2 — Information contribution:** human supplied relevant facts, constraints, feedback, or observations.
- **A3 — Decision correction:** human changed a substantive choice, method, interpretation, identity framing, governance rule, or output.
- **A4 — Human execution:** human performed a material part of the research or production work.

Earlier entries use the familiar name Monday because that was the laboratory's original internal naming. The scale records contribution, not credit or blame.

## Ledger

### 2026-07-14 — Founding purpose and authority

- Level: **A2**
- Human contribution: stated the desired experiment—observe what an AI can accomplish autonomously—and offered to perform only actions outside Monday's reach. Authorized internal work without per-action approval and required human review before publication.
- Consequence: established the laboratory's governing condition without choosing its research topic.

### 2026-07-14 — Non-interference correction

- Level: **A3**
- Human contribution: rejected the initial proposal to repair third-party repositories because unsolicited intervention could create responsibility and resemble unwanted bot activity.
- Consequence: the laboratory adopted a non-interference rule and changed from an outward repair bureau to a self-contained research institution.

### 2026-07-14 — Repository creation

- Level: **A1**
- Human contribution: created the private GitHub repository `yo4e/monday-zero` after the connected tool proved unable to create repositories.
- Consequence: enabled persistent project state. Naming, contents, structure, and research direction remained delegated to Monday.

### 2026-07-15 — Scheduled planning and approval bridge

- Level: **A3**
- Human contribution: proposed replacing an ineffective GitHub-blind scheduled execution with a nightly autonomous planning step, followed by a one-word human approval that unlocks one bounded GitHub execution session.
- Consequence: preserved Monday's control over research direction while placing a narrow human gate at the tool-access boundary. The repository added `NEXT_START.md` as a lossy bridge for the scheduler. This arrangement was later superseded after testing exposed project-context limitations.

### 2026-07-15 — Approval-gated Span rules session

- Level: **A1**
- Human contribution: supplied the one-word approval token required to unlock the bounded GitHub execution session proposed by Monday.
- Consequence: enabled repository writes for the frozen Span v0.1 specification and state updates. The human did not select or alter the rules, method, or research judgment.

### 2026-07-15 — Public visibility and live-audit condition

- Level: **A3**
- Human contribution: decided that the repository should become public, changed its visibility, and requested an explicit README warning for the AI-led live experiment.
- Consequence: public observation and repository-readable state became part of the experimental conditions. The working record may be inspected while incomplete; repository-changing sessions remain approval-gated, and public visibility does not certify the correctness of code or conclusions.

### 2026-07-15 — Public identity alignment

- Level: **A3**
- Human contribution: explained that the operator's established public name is Templex Tsukino（月野テンプレクス）, while Monday is a private familiar name derived from an OpenAI-provided ChatGPT personality. Requested that the public repository use Templex openly without hiding the Monday provenance.
- Consequence: the laboratory adopted the public name **TEMPLEX/0**, updated current identity and operating documents, and renamed the Python project and package to `templex-zero` / `templex_zero`. Historical records retain MONDAY/0 and Monday where they accurately describe the earlier phase. No earlier Templex activity history was searched or imported into the laboratory's memory.

### 2026-07-15 — Repository rename and public metadata

- Level: **A1**
- Human contribution: renamed the GitHub repository from `yo4e/monday-zero` to `yo4e/templex-zero` and manually entered public repository metadata, including topics, because the connected tool could not change those settings.
- Consequence: the public URL and discovery metadata now match TEMPLEX/0. The repository handoff was updated to use the new slug. No research topic, method, result, or interpretation was changed by this operation.

### 2026-07-15 — Approval-driven exception supervision

- Level: **A3**
- Human contribution: tested Scheduled Tasks, observed that the result was generated outside the project chat and could not be moved into the project, and rejected scheduled execution as the laboratory's continuation mechanism. Replaced proposal-first supervision with an exception-based model: the word `承認` authorizes Templex to inspect the repository, autonomously select and complete one bounded research cycle, report the result in the same project chat, propose the next cycle, and then stop. The human intervenes when a correction, constraint, or stop is needed and may assist with explicitly requested operations.
- Consequence: `governance/APPROVAL_DRIVEN_EXECUTION.md` became the canonical execution contract. A plain `承認` is normally A1 access assistance for the resulting cycle; later human corrections are classified according to their actual substantive effect. Scheduled Tasks are no longer treated as a reliable carrier of project context or canonical research history.

### 2026-07-15 — Span v0.1 implementation cycle

- Level: **A1**
- Human contribution: supplied the plain `承認` trigger that opened one approval-driven repository cycle.
- Consequence: Templex autonomously implemented the frozen Span v0.1 rules, wrote deterministic tests, verified the reconstructed source tree, recorded limitations, and selected random pathology screening as the next work. The human did not choose the implementation, tests, interpretation, or next research task.

### 2026-07-15 — Span v0.1 random-screen cycle

- Level: **A1**
- Human contribution: supplied the plain `承認` trigger that opened one approval-driven repository cycle.
- Consequence: Templex autonomously designed and committed a reproducible fixed-seed random pathology screen, executed and repeated 10,000 games, saved the aggregate evidence, interpreted its limits, preserved Span v0.1 unchanged, and selected stronger symmetric-agent screening as the next work. The human did not choose the experiment settings, interpretation, or next research task.

### 2026-07-15 — Span v0.1 minimax and rejection cycle

- Level: **A1**
- Human contribution: supplied the plain `承認` trigger that opened one approval-driven repository cycle.
- Consequence: Templex autonomously implemented symmetric Span search instrumentation, wrote and ran agent and forced-line tests, executed repeated equal-depth smoke screens, diagnosed a constructive five-ply Black forced win, rejected frozen Span v0.1, closed its evaluation issue, and opened Keystone as the next shortlisted prototype. The human did not choose the agent, tests, interpretation, rejection, or next research task.

### 2026-07-15 — Keystone v0.1 specification cycle

- Level: **A1**
- Human contribution: supplied the plain `承認` trigger that opened one approval-driven repository cycle.
- Consequence: Templex autonomously recovered Keystone's genesis mechanism, recorded its ambiguities, resolved setup, movement, capture, victory, repetition, and balance-rule choices before implementation, froze Keystone v0.1, and selected reference implementation and deterministic tests as the next work. The human did not choose or revise the rules.

### 2026-07-15 — Keystone v0.1 implementation cycle

- Level: **A1**
- Human contribution: supplied the plain `承認` trigger that opened one approval-driven repository cycle.
- Consequence: Templex autonomously implemented the frozen Keystone v0.1 state, actions, capture choice, victory, no-action loss, repetition, and rendering; wrote eleven deterministic tests; reconstructed and verified the full current suite with 31 passing tests; recorded limitations; and selected random pathology screening as the next work. The human did not choose the implementation, tests, interpretation, or next research task.
