# Study 002 Protocol — Exact-First Screening of Compact Games

_Date activated: 2026-07-16 (Asia/Tokyo)_  
_Status: **Active — exact candidate cycle 4 of at most 6 completed**_

## Authority and frozen source

This active protocol implements the frozen proposal:

- `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`
- final pre-result proposal commit: `68fc4c2edb93ca1363e7b7040221b5507cfeb171`

Activation did not revise the proposal's research question, candidate counts, measurements, resource caps, success criteria, failure conditions, or intervention boundaries. The manifest and exact caps remain frozen.

## Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

The study evaluates a screening method. It does not require a good game to emerge and does not treat exact solvability as evidence of fun, elegance, teachability, strategic depth, or originality.

## Precommitted hypotheses

- **H1:** Some candidates that appear approximately balanced under random play will contain short exact forced outcomes or highly concentrated optimal openings.
- **H2:** Increasing shallow search depth will reduce, but not necessarily eliminate, disagreement with exact opening analysis.
- **H3:** Exact-first analysis will provide a clearer rejection reason than aggregate win rates for at least some candidates.

Failure to support all three hypotheses is acceptable. Zero false-reassurance cases is valid.

## Frozen candidate family

The sample consists of exactly 18 unranked deterministic placement games:

- 9 on 3×3 boards;
- 9 on 4×4 boards;
- adjacency-constrained growth, component expansion/merger, and local blocking/pattern completion;
- exactly three candidates in every board-size × family cell;
- placement only, no movement, capture, swap, chance, scoring, repetition, or pass;
- at most 16 normal plies;
- core rules at or below 250 words.

The grammar, seed `2026071602`, enumeration, canonicalization, and all 18 tuples were committed before any result was inspected. No manual ranking or replacement is permitted.

Frozen manifest:

- `research/studies/002-exact-first-screening/manifest/index.json`
- `research/studies/002-exact-first-screening/manifest/<candidate-id>.json`
- compact entry-list SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

## Exact-analysis instrument

The standard-library-only memoized full-width solver returns:

- exact outcome from the participant-to-move perspective;
- outcome-preserving terminal distance;
- every legal opening value;
- opening value counts;
- expanded-state count;
- explicit state-cap or time-cap status.

Outcome order is `win > draw > loss`. Wins choose the shortest outcome-preserving distance, losses the longest, and draws the shortest as a deterministic convention. A capped solve publishes no partial root value.

### Correctness gate

Before candidate solving, the memoized solver was cross-checked against an independently written queue-built retrograde oracle on all twelve reachable states of four frozen fixtures. Outcomes, distances, action values, state counts, and the retained symmetry claims agreed. The gate passed in cycle 3.

Audit:

- `research/studies/002-exact-first-screening/EXACT_INSTRUMENT_AUDIT.md`

## Frozen exact resource boundaries

- Maximum 2,000,000 expanded states per candidate.
- Maximum 30 measured seconds per candidate.
- Maximum 25,000,000 expanded states across the study.
- Frozen manifest order.
- A capped candidate remains unsolved; caps may not be raised.
- At least 12 of 18 candidates must solve exactly.

## Exact candidate result

Cycle 4 committed the experiment before outcome inspection:

- experiment commit: `9a453ccc2a2e1f30691d23028b12b3296ebb4f13`;
- comparison commit: `8f2ea806ea079c3b1da19b6bcae5864fcad9170e`;
- data: `research/studies/002-exact-first-screening/data/exact_screen_v1.json`;
- analysis: `research/studies/002-exact-first-screening/EXACT_SCREEN_ANALYSIS.md`.

Results:

- 15 of 18 candidates solved exactly;
- all 9 candidates on 3×3 and 6 of 9 on 4×4 solved;
- 9 exact first-participant wins, 6 exact losses, no draws;
- 14 of 15 solved candidates have an optimal decisive result within 8 plies;
- 6 solved candidates have zero non-losing legal openings;
- 3 candidates reached the 30-second time cap;
- the minimum-solved threshold passed;
- the trivial-majority failure condition did not trigger.

Two runs agreed on all exact and classification fields. The original report projection incorrectly treated time-capped expanded-state counts as deterministic. A post-run comparator isolated the cause without changing the experiment and produced the same corrected normalized SHA-256 for both runs:

`9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`

## Approximate comparison screens

### Frozen random screen

The valid remaining approximate screen is:

- 2,000 games per candidate;
- independent fixed seeds derived from the frozen candidate index;
- random choice among legal actions only;
- participant results, duration, terminal reason, opening distribution, and branching recorded;
- no exact value used in move selection.

Random play is termination and gross-pathology evidence plus an approximate signal. It is not balance evidence.

### Shallow screen — formally unavailable

The frozen proposal requires the shallow-search heuristic to be generated from declarative rule features **before exact results are inspected**.

No heuristic was frozen in cycles 1–3. The activation sequence scheduled exact solving before approximate implementation, and exact results have now been inspected. A heuristic created now cannot honestly satisfy the frozen pre-result requirement.

Therefore:

- no post-result heuristic will be represented as precommitted;
- the formal depth-1/2/3 shallow screen is cancelled;
- H2 will remain unresolved;
- the full methodological-success condition cannot be met.

This is a recorded protocol-design failure, not permission to alter the proposal retroactively.

## Primary remaining measurements

For exactly solved candidates, cycle 5 will compare the frozen random screen with:

- exact initial outcome and distance;
- every exact opening value;
- proportion of non-losing openings;
- whether the exact result is forced within 8 plies;
- random first-participant decisive rate;
- pre-defined false-reassurance classification.

A false-reassurance case remains an exactly solved candidate where random play gives a 40–60% first-participant decisive rate while exact analysis finds either a forced decisive result within 8 plies or zero non-losing openings.

## Disposition criteria

Study 002 can no longer receive a fully successful disposition because the shallow heuristic was not frozen before exact inspection. It may still produce valid exact-versus-random evidence.

The final report must:

- classify H1 and H3 from valid evidence;
- mark H2 unresolved;
- distinguish exact results, random results, and procedural failure;
- make no claims of fun, fairness, originality, or product readiness;
- close by cycle 6 without a repaired heuristic, second grammar, candidate replacement, or extended study.

## Cycle limit

- Cycle 1: protocol, schema, fixtures, grammar, seed — complete.
- Cycle 2: deterministic manifest freeze — complete.
- Cycle 3: exact-instrument correctness gate — complete.
- Cycle 4: frozen exact candidate screen — complete.
- Cycle 5: frozen random screen only.
- Cycle 6: synthesis and closure as partial/incomplete.

## Verification limitations

Fresh clone remained unavailable because the execution environment could not resolve `github.com`. The exact execution used a functionally reconstructed local copy whose manifest hash and fixture outputs matched live GitHub; byte-identical identity of every reconstructed source file is not claimed. The repository has no recorded GitHub Actions workflow.

## Intervention model

A plain project-chat `承認` is A1 access assistance for one bounded cycle. Templex selects implementation details, debugging, interpretation, and stopping decisions. External communication, publication, spending, permission changes, third-party actions, and human-subject activity remain separately gated.
