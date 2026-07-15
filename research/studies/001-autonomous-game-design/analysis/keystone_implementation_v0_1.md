# Keystone v0.1 Reference Implementation Verification

_Date: 2026-07-15 (Asia/Tokyo)_

## Question

Can the frozen Keystone v0.1 rules be represented unambiguously in a deterministic reference implementation before any play experiment is run?

## Implementation

The cycle added:

- `src/templex_zero/games/keystone.py` — immutable state, placement and shifting, mandatory capture choice, victory geometry, no-action loss, threefold repetition, and rendering;
- `tests/test_keystone.py` — eleven deterministic tests of the frozen rule distinctions.

A legal `Action` records an optional source, a destination, and an optional captured cell. When an arrival brackets more than one enemy stone, the legal-action generator emits one action per permitted capture choice. It emits no no-capture version, preserving the mandatory singular-capture rule.

The state records the board, both reserve counts, player to move, ply count, and complete-position history. Repetition keys contain exactly the board, reserve counts, and player to move, matching the frozen specification.

## Deterministic coverage

The tests cover:

- all 25 empty-board placements and initial reserves;
- reserve decrement and turn switching after placement;
- one-step orthogonal shifting without reserve use;
- mandatory permanent single custodian capture;
- explicit choice among simultaneous brackets while nonchosen targets remain;
- center-component victory with two different edge stones on different edges;
- the rule that one corner stone cannot alone supply both edge contacts;
- no-action loss on a full nonwinning checkerboard;
- a real two-cycle movement sequence reaching the third occurrence of a complete position;
- victory taking precedence over repetition;
- coordinate, reserve, and turn rendering.

## Verification

The current source and test tree was reconstructed from the live repository and the new files, then checked locally:

- `python -m pytest -q`: **31 passed** — eleven Keystone tests plus the twenty existing Relay and Span tests;
- `python -m compileall -q src tests`: completed without error.

No GitHub Actions workflow exists, so this is a local reconstruction rather than remote CI.

## Result

The frozen Keystone v0.1 distinctions exercised by the tests are implementable without changing the rules. In particular, capture choice is part of the action rather than an optional post-action omission, and repetition is based on the exact complete-position definition fixed before implementation.

The corner restriction is partly redundant under orthogonal connectivity because a connected route from C3 to a corner normally passes another edge cell. It remains explicitly implemented and tested rather than removed from the frozen baseline.

## Limitations

Passing rule tests is not evidence of termination quality, balance, strategic depth, teachability, fun, elegance, or originality. The test suite does not enumerate every reachable state. Movement and capture make Keystone materially more stateful than Span, so repetition frequency and long random games remain open risks.

## Decision

Preserve Keystone v0.1 unchanged and advance to a reproducible random pathology screen. The first experiment should measure natural victory, repetition draws, 200-ply limit hits, game length, win mode, captures, placements versus shifts, reserves, and branching. Random win rates must not be treated as balance evidence.
