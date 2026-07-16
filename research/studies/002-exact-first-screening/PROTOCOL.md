# Study 002 Protocol — Exact-First Screening of Compact Games

_Date activated: 2026-07-16 (Asia/Tokyo)_  
_Status: **Active — manifest cycle 2 of at most 6 completed**_

## Authority and frozen source

This active protocol implements the frozen proposal:

- `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`
- final pre-result proposal commit: `68fc4c2edb93ca1363e7b7040221b5507cfeb171`

Activation did not revise the proposal's research question, candidate counts, measurements, resource caps, success criteria, failure conditions, or intervention boundaries. If this file and the frozen proposal disagree, stop before candidate evaluation.

## Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

The study evaluates a screening method. It does not require a good game to emerge and does not treat exact solvability as evidence of fun, elegance, teachability, strategic depth, or originality.

## Precommitted hypotheses

- **H1:** Some candidates that appear approximately balanced under random play will contain short exact forced outcomes or highly concentrated optimal openings.
- **H2:** Increasing shallow search depth will reduce, but not necessarily eliminate, disagreement with exact opening analysis.
- **H3:** Exact-first analysis will provide a clearer rejection reason than aggregate win rates for at least some candidates.

Failure to support all three hypotheses is acceptable. Zero false-reassurance cases is valid.

## Frozen candidate family

The sample consists of exactly **18** unranked candidates:

- 9 on 3×3 boards;
- 9 on 4×4 boards;
- three mechanism families:
  1. adjacency-constrained growth;
  2. component expansion or merger;
  3. local blocking and pattern completion;
- exactly three candidates in every board-size × family cell.

All candidates are deterministic, alternating, two-player, perfect-information placement games. Every normal action fills exactly one empty cell. Movement, capture, swap, chance, hidden information, scoring, repetition, and pass actions are excluded. Candidate boards use every cell, contain at most 16 normal plies, state intended participant/color symmetry, and keep core rules at or below 250 words.

The grammar, seed `2026071602`, deterministic enumeration, canonicalization, and all 18 rule tuples were committed before random, shallow, or exact results were inspected. Within each cell, the manifest took the first three distinct statically valid candidates in frozen seeded order. No manual ranking or replacement was permitted.

The frozen manifest is:

- `research/studies/002-exact-first-screening/manifest/index.json`
- `research/studies/002-exact-first-screening/manifest/README.md`
- `research/studies/002-exact-first-screening/manifest/<candidate-id>.json`

The compact full-entry list has SHA-256:

`cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

The manifest is immutable except to correct a factual or technical error. Candidate replacement, reordering, polishing, or a second grammar is prohibited.

## Declarative representation

The shared representation encodes:

- board size and playable cells;
- player to move and immutable placement states;
- mechanism family;
- neighborhood relation;
- first-move scope;
- placement predicate and parameters;
- goal predicate and parameters;
- no-legal-action resolution;
- intended symmetry and rule-word count.

Candidate schema validation rejects out-of-scope board sizes, masked boards, asymmetric declarations, fixture-only explicit openings, fixture-only explicit winning patterns, and rule text above 250 words.

## Exact-analysis instrument

Implement a standard-library-only generic engine and memoized full-width solver that returns:

- exact outcome from the participant-to-move perspective: win, draw, or loss;
- distance to terminal under outcome-preserving optimal play;
- exact value of each legal opening action;
- number of winning, drawing, and losing opening actions;
- reachable or expanded-state count;
- whether a configured cap was reached.

### Correctness gate

Before candidate solving:

1. cross-check the memoized solver against an independently written brute-force enumerator on every frozen fixture and every reachable fixture state;
2. compare outcome, distance, and every opening-action value;
3. exhaustively check participant/color symmetry on fixture states where symmetry is claimed;
4. reject the instrument if disagreement remains after one bounded implementation-debugging cycle.

Symmetry reduction may be added only after a no-reduction reference solve agrees on all fixtures and all 3×3 candidates.

## Frozen fixtures

The four pre-candidate fixtures are recorded in:

- `research/studies/002-exact-first-screening/FIXTURES.md`
- `src/templex_zero/exact_first/fixtures.py`

They cover immediate victory, draw by exhausted actions, branching actions with different winners, and a constrained adjacency-growth chain. Fixtures 1 and 2 claim color-role symmetry. Fixtures 3 and 4 are treated as asymmetric.

## Resource boundaries

- Maximum **2,000,000 expanded states per candidate**.
- Maximum **30 seconds of measured solver time per candidate** in the recorded reference environment.
- Maximum **25,000,000 expanded states across the study**.
- Candidates are solved strictly in frozen manifest order.
- If the total state cap is reached, all later entries are unsolved.
- A capped candidate remains unsolved; caps may not be raised inside Study 002.
- No paid compute, external solver service, continuous background task, or unpublished manual intervention.

At least **12 of 18 candidates** must solve exactly for the comparison to proceed. Fewer than 12 closes the study as an instrument-or-scope failure.

## Approximate comparison screens

For every valid candidate, whether or not exact solving completes:

### Random screen

- 2,000 games;
- independent fixed seeds derived from the frozen candidate index;
- participant and color results recorded separately where relevant;
- duration, terminal reason, opening distribution, and branching recorded.

Random play is termination and gross-pathology evidence plus an approximate signal. It is not balance evidence.

### Shallow symmetric screen

- depths 1, 2, and 3;
- 200 games per depth;
- identical agents in both seats;
- seeded tie-breaking;
- one evaluation procedure per candidate across seats and depths;
- participant results, opening distribution, duration, and branching recorded.

The heuristic must be generated from declarative rule features before exact results are inspected. Candidate-specific rescue terms are prohibited.

## Primary measurements

For exactly solved candidates, report:

1. exact initial outcome and distance;
2. exact values of every legal opening;
3. number and proportion of non-losing openings;
4. whether either participant has a forced result within 8 plies;
5. random first-participant decisive rate;
6. shallow first-participant decisive rates at depths 1–3;
7. exact/approximate classification disagreements;
8. disagreement change by search depth;
9. state count and solver cost.

A **false-reassurance case** is an exactly solved candidate where an approximate screen gives a 40–60% first-participant decisive rate while exact analysis finds either a forced decisive result within 8 plies or zero non-losing legal opening actions for the first participant. This label does not certify candidates outside it as fair or good.

## Methodological success

Study 002 succeeds as an experiment if:

- the solver passes all independent correctness checks;
- at least 12 candidates solve within frozen caps;
- all configured approximate screens are reproducible;
- the exact/approximate comparison and limitations are reported without changing candidates or metrics;
- H1–H3 are classified as supported, contradicted, or unresolved.

## Immediate failure conditions

Close without repair if:

- independent solvers disagree after one implementation-debugging cycle;
- fewer than 18 distinct valid candidates survive static generation;
- fewer than 12 candidates solve within caps;
- more than half of exactly solved candidates terminate on or before ply 2;
- reproducibility fails and cannot be isolated within one bounded cycle;
- completion requires external services, paid compute, or materially human-authored candidate ranking.

The static grammar-failure condition did not trigger: all six cells produced at least three valid candidates under the frozen rules.

## Cycle limit

Study 002 receives at most **six approval-driven execution cycles after activation**, including final synthesis.

- Cycle 1: protocol, schema, fixtures, grammar, seed — completed without candidate generation.
- Cycle 2: deterministic 18-entry manifest freeze — completed without candidate play or solving.
- Later cycles: exact instrument, frozen candidate solves, approximate screens, and synthesis as evidence permits.

At the limit the study closes as completed, negative, or incomplete. It may not expand into a second grammar, game polishing, prior-art review, human playtesting, or product development.

## Claims out of scope

Study 002 will not claim that:

- an exactly solved candidate is fun or strategically deep;
- approximate 40–60% results establish fairness;
- a candidate is original;
- the family represents all abstract games;
- solver failure implies game quality;
- a survivor is ready for publication or human play.

A structurally interesting survivor may be preserved only as a possible subject of a separately scoped later study.

## Verification record so far

Cycle 1 recorded 10 targeted setup tests. Cycle 2 recorded 7 targeted manifest tests, byte-identical regeneration, successful compilation, and exact Git blob identity for the generator, script, test, and all 21 manifest files.

Fresh clone remained unavailable because the execution environment could not resolve `github.com`. A combined setup-plus-manifest rerun attempted with an incomplete reconstructed schema was discarded and is not evidence. The repository has no recorded GitHub Actions workflow.

## Intervention model

A plain project-chat `承認` is A1 access assistance for one bounded cycle. Templex selects implementation details, debugging, interpretation, and stopping decisions. Human changes to the question, grammar, thresholds, interpretation, or public framing are classified by their actual A2–A4 effect.

External communication, publication, spending, permission changes, third-party actions, and human-subject activity remain separately gated.
