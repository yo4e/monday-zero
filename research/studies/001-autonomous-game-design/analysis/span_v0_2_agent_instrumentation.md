# Span v0.2 Participant-Aware Agent Instrumentation

_Date: 2026-07-16 (Asia/Tokyo)_

## Scope

This record verifies the measurement tools required before any formal Span v0.2 play screen. It does not provide balance or strategic-depth evidence.

## Added instrumentation

- `src/templex_zero/span_v0_2_agents.py`
  - random legal-action agent;
  - participant-perspective evaluation;
  - depth-limited minimax with seeded tie-breaking;
  - one search budget for opening placement, swap, and later placements.
- `src/templex_zero/span_v0_2_match.py`
  - participant-indexed agent selection;
  - opening placement and swap-use recording;
  - final participant-color ownership;
  - participant winner and color winner;
  - connection or immobilization mode;
  - action plies, placements, and legal-action counts.
- `tests/test_span_v0_2_agents.py`
  - seven deterministic tests covering terminal scoring, participant-color symmetry, immediate wins, legal and seeded swap-window choice, invalid terminal calls, invalid depth, and reproducible complete matches.

## Evaluation design

The geometric features remain color-symmetric: minimum connection cost, maximum component span, color mobility, and component count. Before scoring, the root participant is mapped to the color they currently own. A swap therefore changes the participant's evaluated side without recoloring the board or changing the heuristic.

Minimax maximizes when the root participant is to move and minimizes when the other participant is to move. The legal-action generator includes the singleton swap action only during the frozen opening window, so the same search procedure and depth decide whether to swap.

## Verification

A local reconstruction of the live source and tests produced:

- `PYTHONPATH=src python -m pytest -q`: **52 passed**;
  - 45 pre-existing Relay, Span v0.1, Keystone, and Span v0.2 rule cases;
  - 7 new participant-aware agent and match cases.
- `PYTHONPATH=src python -m compileall -q src tests`: completed without error.

The match regression used two identical depth-2 agents and a fixed seed. Repeated execution returned an identical result and terminated within Span's finite placement bound.

## What this establishes

- terminal scores follow participant identity after a swap;
- transposing the board and exchanging colors preserves participant evaluation;
- an immediate win is selected for the participant who owns the winning color;
- the swap opening is searched as an ordinary legal choice under the same budget;
- seeded tie-breaking is reproducible;
- match records distinguish participant order from color ownership and retain branching observations.

## Limitations

- The heuristic is inherited from the v0.1 instrument and is not a proof of optimal play.
- Depth-limited minimax may still miss forced lines beyond its horizon.
- The deterministic tests establish instrumentation consistency, not fairness.
- No formal random screen, equal-budget tournament, strategic-signal comparison, or opening analysis has been run for v0.2.
- No prior-art or similarity search has yet been performed.
- Verification used a locally reconstructed tree; the repository has no GitHub Actions workflow.

## Decision

Advance Span v0.2 to reproducible empirical screening without changing the frozen rules or instrumentation. The formal experiment script must be committed before execution, record its code version and seeds, report participant and color results separately, and be rerun to confirm deterministic aggregate output.
