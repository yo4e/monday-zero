# Next Start

_Updated: 2026-07-15 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not an authorization and must not be treated as the source of truth. `STATE.md`, active study files, open issues, tests, and recent commits remain authoritative.

When Yoshie Yamada sends `承認` in the project chat, the executing session must re-read the live repository and follow `governance/APPROVAL_DRIVEN_EXECUTION.md` before selecting and performing one bounded research cycle.

## Identity and access

- Public operator: **Templex Tsukino / 月野テンプレクス**.
- Laboratory: **TEMPLEX/0**.
- Familiar and historical name: **Monday**.
- Live public repository: `https://github.com/yo4e/templex-zero`.
- The project is independent and does not claim OpenAI sponsorship, endorsement, operation, or review.

## Execution model

- One clear `承認` authorizes one complete bounded research cycle.
- Templex inspects current evidence and selects the work autonomously.
- The cycle includes execution, verification, repository-state updates, reporting in the same project chat, and selection of the next proposed cycle.
- After reporting, stop until another `承認` is received.
- External actions and separately gated actions remain outside ordinary `承認`.

## Current position

The three originally shortlisted prototypes have each received a first disposition and are rejected in their tested forms.

- **Relay:** stronger symmetric play showed severe first-player advantage and substantial draws.
- **Span v0.1:** exhaustive reply enumeration proved a Black connection win on ply 5.
- **Keystone v0.1:** only 50.9% of 2,000 random games completed by 200 plies; 49.1% reached the observation limit.

Issue #2 is closed. Issue #3 is open to compare the failures and select at most one versioned revision—or conclude Study 001 negatively.

## Keystone evidence

- Screen script: `experiments/keystone_random_screen.py`
- Script commit: `f4550102b8a3879d5754ac8dc30eaaac017f2833`
- Seeds: 0–1,999; observation limit: 200 plies
- Repeated formal output: byte-identical
- Structural victories: 886
- Immobilization wins: 104
- Threefold repetition draws: 28
- Observation-limit hits: 982
- Median plies: 193
- Shifts: 88.13% of observed actions
- Both reserves exhausted: 91.7% of games
- Fixed 100-seed diagnostic follow-up at 1,000 plies: all resolved, median 427.5, maximum 964

The result fails the protocol's 98% termination threshold. Random Black/White parity must not be used as balance evidence. Keystone's stronger-agent screen is cancelled for v0.1.

## Rejected

- Relay in its current ruleset.
- Span v0.1 in its frozen ruleset.
- Keystone v0.1 in its frozen ruleset.
- Random-play parity as balance evidence.
- Silently repairing a frozen baseline after results.
- Automatically rescuing the most recently tested prototype.
- Scheduled Tasks as the canonical continuation mechanism.

## Next recommended work unit

Build one comparative diagnosis for Relay, Span, and Keystone. Score evidence strength, diagnosed failure, smallest plausible repair, rule-complexity cost, risk of replacing the original mechanism, and expected test value. Select at most one v0.2 target or conclude the study negatively.

Do not implement a revision in that cycle until the exact new rules and rationale have been frozen before new play results.

## Human gate

The project-chat trigger is:

> 承認

After the cycle report, wait for another `承認`.

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Study protocol: `research/studies/001-autonomous-game-design/PROTOCOL.md`
- Keystone disposition: `research/studies/001-autonomous-game-design/prototypes/keystone/DECISION.md`
- Keystone data: `research/studies/001-autonomous-game-design/data/keystone_random_v0_1.json`
- Keystone analysis: `research/studies/001-autonomous-game-design/analysis/keystone_random_v0_1.md`
- Issue #2: completed Keystone evaluation
- Issue #3: prototype comparison and revision decision
