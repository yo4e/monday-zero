# Study 002 — Exact-First Screening of Compact Games

## Status

**Active. Setup cycle 1 of at most 6 is complete.**

Study 002 was activated on 2026-07-16 from the frozen proposal at commit `68fc4c2edb93ca1363e7b7040221b5507cfeb171`.

## Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

This is a methodological study, not a renewed attempt to rescue Span or to produce a publication-ready game.

## Frozen setup artifacts

- [`PROTOCOL.md`](PROTOCOL.md) — active commitments and stopping rules
- [`GRAMMAR.md`](GRAMMAR.md) — candidate grammar, seed, canonicalization, and enumeration order
- [`FIXTURES.md`](FIXTURES.md) — four hand-audited reachable state graphs
- `src/templex_zero/exact_first/schema.py` — declarative game schema and deterministic state transitions
- `src/templex_zero/exact_first/fixtures.py` — machine-readable fixture specifications and graphs
- `src/templex_zero/exact_first/grammar.py` — frozen grammar constants; intentionally emits no candidates
- `tests/test_exact_first_schema.py`
- `tests/test_exact_first_fixtures.py`

## Current result

The representation can express and validate the three proposed mechanism families plus fixture-only explicit rules. In local reconstruction:

- 10 new deterministic tests passed;
- the four enumerated reachable graphs matched the hand-audited graphs exactly;
- candidate boundaries reject non-3×3/4×4 boards, masked boards, missing symmetry declarations, fixture-only openings and patterns, and rule text above 250 words;
- `compileall` completed without error.

No exact solver exists yet. No candidate manifest has been generated. No random, shallow, or exact candidate result has been observed.

## Frozen candidate design

The future manifest contains exactly 18 candidates:

- 3×3 and 4×4 boards;
- adjacency growth, component expansion/merger, and local blocking/pattern families;
- exactly three candidates in each of the six board-size × family cells;
- seeded SHA-256 ranking of statically canonical parameter tuples;
- no manual ranking or replacement.

## Next bounded cycle

Generate and freeze the 18-entry manifest from the frozen grammar without evaluating play. Add human-readable rule text and static validation records for every entry. Do not implement the exact solver or run candidate games in that same cycle.
