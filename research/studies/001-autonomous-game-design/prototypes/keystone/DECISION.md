# Keystone v0.1 Disposition

_Date: 2026-07-15 (Asia/Tokyo)_

## Decision

**Reject Keystone v0.1 in its frozen form.**

## Decisive evidence

The fixed-seed random pathology screen ran 2,000 games with a 200-ply observation limit using script commit `f4550102b8a3879d5754ac8dc30eaaac017f2833`.

Only 1,018 games completed by 200 plies, a 50.9% completion rate. The Study 001 protocol requires at least 98% random termination within 200 plies unless a justified draw condition resolves the remainder. Keystone's threefold rule produced only 28 draws, while 982 games reached the observation limit.

The limit population exhausted both reserves and then spent 184 plies shifting. Across all games, shifts formed 88.13% of observed actions. A fixed exploratory sample of 100 limit seeds did eventually resolve by 1,000 plies, but with median duration 427.5 and maximum 964, far outside the practical target.

## Interpretation

Keystone's structural victory can occur at a practical length, but the frozen combination of unrestricted shifting and exact threefold repetition creates a large second population of excessively long games. Captures and branching do not prevent this drift.

Random Black/White wins were close, but this is not balance evidence and cannot offset the termination failure.

## Consequence

- Preserve `RULES.md` unchanged as the v0.1 baseline.
- Preserve the reference implementation, tests, script, aggregate data, and analysis.
- Cancel stronger-agent evaluation for v0.1 because the precommitted gross-pathology threshold has already failed decisively.
- Do not silently impose a movement phase, progress counter, capture restriction, or alternative repetition rule.
- Any repair must be a separately specified and frozen version.
- Before revising the latest candidate by default, compare Relay, Span, and Keystone failure modes and repair costs.

## Evidence

- `../../data/keystone_random_v0_1.json`
- `../../analysis/keystone_random_v0_1.md`
- `../../../../experiments/keystone_random_screen.py`
- `../../../../src/templex_zero/games/keystone.py`
- `../../../../tests/test_keystone.py`
