# Proposed Study 002 — Exact-First Screening of Compact Games

_Date: 2026-07-16 (Asia/Tokyo)_  
_Status: **Frozen proposal — not active**_

## 1. Go / no-go decision

**GO, as a separately scoped methodological study.**

Study 001 should not be continued or repaired. Its strongest transferable result was that random and shallow aggregate play can look healthy while short forced structures make a game nonviable. The next useful question is therefore not whether Templex can immediately invent a better game, but whether an exact-first screening method can detect those defects before a candidate receives bespoke development or quality claims.

This proposal does not authorize execution. Study 002 becomes active only after a later project-chat `承認` is received against this frozen proposal.

## 2. Alternatives considered

### A. Exact-first screening of generated finite games — selected

- **Expected information value:** high. Directly tests the principal methodological lesson from Study 001.
- **Implementation cost:** moderate. Requires a small declarative game model, exact solver, fixtures, candidate generator, and comparison screens.
- **External action:** none. Standard-library code and repository-local data are sufficient.
- **Stop criteria:** exact solver cross-checks, fixed state-expansion caps, fixed candidate count, and a six-cycle study limit.
- **Reason selected:** it can succeed with a positive, negative, or null result and produces a reusable testable artifact rather than another unsupported game claim.

### B. Prior-art and convergence mapping for the twelve Study 001 mechanisms — deferred

- **Expected information value:** moderate to high for originality and design lineage.
- **Implementation cost:** moderate.
- **External action:** requires deliberate web and literature search, source qualification, and subjective similarity judgments.
- **Stop criteria:** possible, but ontology and coverage would be difficult to precommit without preliminary research.
- **Reason deferred:** no Study 001 candidate survived basic viability, and a similarity map would not test the evaluation failure that most strongly affected the study.

### C. Human playability and teachability study — no-go now

- **Expected information value:** high for qualities automation cannot establish.
- **Implementation cost:** moderate operationally but high in human dependence.
- **External action:** requires recruitment or sustained human play, consent, instructions, and subjective reporting.
- **Stop criteria:** sample size and interpretation would require a separate human-research design.
- **Reason rejected:** there is no viable candidate worth imposing on human participants, and the work would materially change the autonomy experiment.

### D. Repository CI and reproducibility hardening as a standalone study — deferred as infrastructure

- **Expected information value:** low as an independent research question, though operational value is real.
- **Implementation cost:** low to moderate.
- **External action:** GitHub workflow creation is internal repository work, but runner behavior and permissions add infrastructure dependence.
- **Stop criteria:** straightforward.
- **Reason deferred:** this is enabling engineering, not a sufficient next research question. A future active study may add CI when it directly supports its protocol.

## 3. Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

The study evaluates a screening method. It does not require a good game to emerge, and it does not claim that exact solvability establishes fun, elegance, teachability, strategic depth, or originality.

## 4. Precommitted hypotheses

- **H1:** Some candidates that appear approximately balanced under random play will contain short exact forced outcomes or highly concentrated optimal openings.
- **H2:** Increasing shallow search depth will reduce, but not necessarily eliminate, disagreement with exact opening analysis.
- **H3:** Exact-first analysis will provide a clearer rejection reason than aggregate win rates for at least some candidates.

Failure to support any hypothesis is an acceptable result. The study succeeds methodologically if it executes the frozen comparison honestly and reports a null result when appropriate.

## 5. Candidate family

Generate exactly **18** unranked candidate rules from a frozen grammar:

- 9 candidates on 3×3 boards;
- 9 candidates on 4×4 boards;
- exactly 6 candidates from each of three mechanism families:
  1. adjacency-constrained growth;
  2. component expansion or merger;
  3. local blocking and pattern completion;
- therefore exactly **3 candidates in each board-size × mechanism-family cell**.

All candidates must satisfy these static boundaries before evaluation:

- deterministic, two-player, alternating, perfect information;
- placement only: every normal action fills exactly one empty cell;
- no movement, capture, swap, chance, hidden information, scoring, repetition, or pass action;
- at most 16 normal plies;
- core rules at or below 250 words;
- legal actions and terminal conditions expressible in the shared declarative model;
- intended player/color symmetry stated explicitly;
- exact duplicates removed only by static canonicalization before the candidate set is frozen.

The first execution cycle must freeze a deterministic enumeration rule. Within each of the six board-size × family cells, the manifest contains the first three distinct valid candidates emitted by the seeded generator after static canonicalization. No manual ranking or replacement is permitted.

The candidate grammar, generation seed, enumeration order, canonicalization rule, and all 18 rule tuples must be committed before any random, shallow, or exact result is inspected. If static generation produces fewer than 18 distinct valid candidates, the grammar fails; do not invent replacements after seeing play results.

## 6. Exact-analysis instrument

Implement a standard-library-only generic engine and memoized full-width solver that returns:

- exact outcome from the participant-to-move perspective: win, draw, or loss;
- distance to terminal under outcome-preserving optimal play;
- exact value of each legal opening action;
- number of winning, drawing, and losing opening actions;
- reachable-state count;
- whether the configured resource cap was reached.

### Correctness checks

Before candidate solving:

1. define at least four hand-audited toy fixtures with known state graphs and outcomes;
2. cross-check the memoized solver against an independently written brute-force enumerator on every fixture;
3. exhaustively verify participant/color symmetry on the fixture states where symmetry is claimed;
4. reject the instrument if any outcome, distance, or opening-action value disagrees.

Symmetry reduction may be added only if a no-reduction reference solve first agrees on all fixtures and all 3×3 candidates.

## 7. Resource boundaries

- Maximum **2,000,000 expanded states per candidate**.
- Maximum **30 seconds of measured solver time per candidate** in the recorded reference environment.
- Maximum **25,000,000 expanded states across the study**.
- A capped candidate is recorded as unsolved; its cap may not be raised inside Study 002.
- Candidates are solved strictly in frozen manifest order. If the total state cap is reached, every later manifest entry is recorded as unsolved without reordering.
- No paid compute, external solver service, continuous background task, or unpublished manual intervention.

At least **12 of 18 candidates** must be solved exactly for the comparison study to proceed. If fewer than 12 are solved, close Study 002 as an instrument-or-scope failure without replacing candidates or raising caps.

## 8. Approximate comparison screens

For every valid candidate, whether or not exact solving completes:

### Random screen

- 2,000 games;
- independent fixed seeds derived from the frozen candidate index;
- record participant and color results separately where relevant;
- record duration, terminal reason, opening distribution, and branching.

Random play is interpreted only as termination and gross-pathology evidence plus an approximate signal to compare with exact results.

### Shallow symmetric screen

- depths 1, 2, and 3;
- 200 games per depth with identical agents in both seats;
- seeded tie-breaking;
- one evaluation procedure per candidate across seats and depths;
- record participant results, opening distribution, duration, and branching.

The heuristic must be generated from the declarative rule features before exact results are inspected. No candidate-specific rescue term may be added after comparison begins.

## 9. Primary measurements

For exactly solved candidates, report:

1. exact initial outcome and distance;
2. exact values of all legal openings;
3. number and proportion of non-losing openings;
4. whether either participant has a forced result within 8 plies;
5. random first-participant decisive rate;
6. shallow first-participant decisive rate at depths 1–3;
7. classification disagreements between approximate screens and exact opening structure;
8. how disagreement changes with search depth;
9. state count and solver cost.

A **false-reassurance case** is pre-defined as an exactly solved candidate where an approximate screen gives a 40–60% first-participant decisive rate while exact analysis finds either:

- a forced decisive result within 8 plies; or
- zero non-losing legal opening actions for the first participant.

This definition is a diagnostic label, not a claim that candidates outside it are balanced or good.

## 10. Success, failure, and stopping rules

### Methodological success

Study 002 succeeds as an experiment if:

- the solver passes all independent correctness checks;
- at least 12 candidates are solved within the frozen caps;
- all configured approximate screens are reproducible;
- the exact/approximate comparison table and limitations are reported without changing the candidate set or metrics;
- the study concludes whether the hypotheses were supported, contradicted, or unresolved.

No minimum number of false-reassurance cases is required. Zero is a valid result.

### Immediate failure conditions

Close the study without repair if:

- the independent solvers disagree after one implementation-debugging cycle;
- fewer than 18 distinct valid candidates survive static generation;
- fewer than 12 candidates solve within the frozen caps;
- more than half of the exactly solved candidates terminate trivially on or before ply 2, indicating a degenerate frozen grammar;
- reproducibility fails and the cause cannot be isolated within one bounded cycle;
- completion would require external services, paid compute, or materially human-authored candidate ranking.

### Study limit

Study 002 receives at most **six approval-driven execution cycles after activation**, including final synthesis. At the limit it closes as completed, negative, or incomplete. It may not silently expand into game polishing, prior-art review, human playtesting, or a second candidate grammar.

## 11. Claims explicitly out of scope

Study 002 will not claim:

- that an exactly solved candidate is fun or strategically deep;
- that approximate 40–60% results establish fairness;
- that any candidate is original;
- that the 18-candidate family represents all abstract games;
- that solver failure implies game quality;
- that a surviving candidate is ready for publication or human play.

A structurally interesting survivor may be preserved as a possible subject of a later separately scoped study, but it is not an automatic product outcome.

## 12. Intervention model

- Plain project-chat `承認` remains A1 access assistance for one bounded cycle.
- Templex selects implementation details, candidates produced by the frozen grammar, debugging methods, interpretation, and stopping decisions.
- Human changes to the question, grammar, thresholds, interpretation, or public framing are logged according to their actual A2–A4 effect.
- External communication, publication, spending, permissions, third-party repository actions, and human-subject activity remain separately gated.

## 13. Planned artifacts after activation

- `research/studies/002-exact-first-screening/PROTOCOL.md`
- frozen grammar and candidate manifest;
- declarative game engine;
- exact solver and independent fixture enumerator;
- deterministic tests;
- random and shallow-screen scripts;
- machine-readable results;
- analysis and final report;
- intervention and state updates.

## 14. First execution cycle after activation

On the next approval, if this proposal remains uncorrected:

1. activate Study 002 without changing this proposal;
2. create its protocol by copying the frozen commitments into the active study directory;
3. define and test the declarative rule schema;
4. define the four hand-audited solver fixtures and their expected state graphs;
5. freeze the candidate-generation grammar, enumeration rule, and seed;
6. do **not** generate or evaluate the 18 candidates yet.

That cycle determines whether the proposed representation and correctness fixtures are precise enough to support the study before candidate results exist.
