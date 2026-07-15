# Next Start

_Updated: 2026-07-16 (Asia/Tokyo)_

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

Relay, Span v0.1, and Keystone v0.1 are rejected in their tested forms.

- **Relay:** stronger symmetric play showed severe first-player advantage and substantial unresolved games; one rule would not address both symptoms.
- **Span v0.1:** exhaustive reply enumeration proved a Black connection win on ply 5, but random termination and practical duration were sound.
- **Keystone v0.1:** only 50.9% of 2,000 random games completed by 200 plies; fixing the post-reserve movement phase would require a larger redesign.

A common comparison selected **Span v0.2** as the only revision target. The decision is recorded in `analysis/prototype_revision_selection.md`.

## Frozen Span v0.2

- Rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES_v0_2.md`
- Frozen before implementation or new play results on 2026-07-16.
- The only rule change from v0.1 is an opening swap option.
- First participant makes one normal Black placement.
- Second participant either makes one normal White placement or swaps sides.
- A swap exchanges participant ownership of colors, goals, and all existing stones without changing the board.
- The swap consumes the second participant's turn; the opening participant, now White, moves next.
- No further swap is available.
- Anchors, expansion, merger, victory, immobilization, and finite termination are unchanged.
- Core rules: 308 words.
- No v0.2 implementation or play result exists yet.

## Rejected revision paths

- Relay swap-only repair: does not address the 200-ply unresolved population.
- Relay repetition-only repair: does not address the initiative advantage.
- Span anchor changes or C2/C4 opening bans: overly tailored to the observed line and lack a principled replacement geometry.
- Keystone arbitrary ply draw: reclassifies censorship without creating progress.
- Keystone movement restriction or new score: changes its defining reversible-control mechanism or adds substantial bookkeeping.
- Multiple simultaneous v0.2 projects.

## Next recommended work unit

Implement frozen Span v0.2 under `src/templex_zero/` while separating participant identity from color ownership. Add deterministic tests for:

- swap availability only after the first Black placement;
- normal White placement expiring the swap option;
- unchanged board and stones after swap;
- exchanged participant-color ownership;
- the opening participant moving next as White;
- swap being unavailable thereafter;
- unchanged v0.1 expansion, merge, connection, and immobilization behavior.

Run the full existing test suite and compile checks. Do not run balance experiments until implementation fidelity is established.

## Human gate

The project-chat trigger is:

> 承認

After the cycle report, wait for another `承認`.

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Study protocol: `research/studies/001-autonomous-game-design/PROTOCOL.md`
- Revision comparison: `research/studies/001-autonomous-game-design/analysis/prototype_revision_selection.md`
- Span v0.1 rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES.md`
- Span v0.1 disposition: `research/studies/001-autonomous-game-design/prototypes/span/DECISION.md`
- Span v0.2 rules: `research/studies/001-autonomous-game-design/prototypes/span/RULES_v0_2.md`
- Issue #3: completed prototype comparison
- New implementation issue: Span v0.2 implementation and evaluation
