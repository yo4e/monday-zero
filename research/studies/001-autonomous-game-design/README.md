# Study 001 — Autonomous Game Design

## Research question

Can Templex Tsukino independently design a compact, deterministic, two-player abstract strategy game whose rules are teachable in under three minutes and whose automated play provides evidence of nontrivial strategy and reasonable balance?

This is the same study selected under the earlier internal name Monday. The public identity change does not alter the protocol, thresholds, or prior results.

## Intended artifact

A complete game package containing:

- concise rules;
- a reference implementation;
- command-line play;
- reproducible simulation and evaluation tools;
- baseline agents of differing strength;
- experiment data and analysis;
- a record of rejected prototypes and revisions;
- later, if justified, a small browser interface.

## Constraints

- Two players.
- Deterministic and perfect information.
- No dependence on proprietary assets or external services.
- Core rules should fit within 400 words.
- A physical version should require at most a small board and a modest set of generic pieces, or be playable with pencil and paper.
- The design must not knowingly duplicate an existing game; claims will remain qualified until a deliberate similarity search occurs.

## Current phase

**Prototype comparison / Span implementation.** Relay has been implemented and rejected in its current form. Span v0.1 rules were frozen before implementation or play results on 2026-07-15.

## Active prototype

- [`prototypes/span/RULES.md`](prototypes/span/RULES.md) — frozen Span v0.1 baseline
- Issue #1 — implementation and evaluation work

## Planned study files

- `PROTOCOL.md` — evaluation plan and thresholds
- `candidates/` — candidate mechanisms and rejection notes
- `prototypes/` — versioned rules for implemented candidates
- `src/templex_zero/` — game and agent implementations
- `experiments/` — reproducible runs and data
- `analysis/` — interpretation and critique
- `RULES.md` — rules of the surviving design
- `REPORT.md` — final research report
