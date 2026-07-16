# Study 001 Final Report — Autonomous Abstract Game Design

_Date: 2026-07-16 (Asia/Tokyo)_  
_Status: **Closed — negative research conclusion**_

## Executive conclusion

Study 001 asked whether Templex Tsukino could independently design a compact deterministic two-player abstract strategy game whose rules were easy to learn and whose automated play supplied evidence of meaningful strategic depth and reasonable balance.

The study did **not** produce a game that supports that claim.

Twelve unranked mechanisms were generated. Relay, Span, and Keystone were selected for implementation. Relay failed stronger-agent balance and produced a substantial unresolved population. Span v0.1 passed random pathology screening but contained a constructive five-ply Black win. Keystone v0.1 failed the precommitted random termination threshold by 47.1 percentage points. Span v0.2, the only selected one-change revision, passed random termination and appeared nearly balanced under random play, but equal-budget search and exhaustive opening analysis established a constructive win for the second participant after every legal opening.

No further repair was added inside Study 001. Fun, elegance, teachability in practice, human strategic experience, and genuine originality were not established. A prior-art review was not performed because no design survived basic viability testing far enough to justify an originality claim.

The main positive result is methodological: the process generated compact mechanisms, froze rules before evaluation, built reproducible implementations and experiments, rejected attractive but defective designs, and stopped without presenting a failed prototype as a finished game.

## 1. Research question and boundaries

The frozen research question was:

> Can Templex Tsukino independently design a compact, deterministic, two-player abstract strategy game whose rules are teachable in under three minutes and whose automated play provides evidence of nontrivial strategy and reasonable balance?

The [protocol](PROTOCOL.md) was fixed before game selection. Its principal automated thresholds were:

- at least 98% of random games must terminate within 200 plies, unless a justified draw condition exists;
- under the strongest available symmetric agent, first-player decisive win rate should fall between 40% and 60%;
- a stronger agent should win at least 70% of decisive games against random play and at least 60% against a deliberately shallow agent;
- stronger performance should improve across at least three computation budgets unless shallow search already resolves the game;
- typical completed games should remain within 8–80 plies;
- core rules should remain at or below 400 words.

Automated play was never treated as proof of fun, elegance, teachability, or originality. Those qualities remained human-dependent and unresolved unless a later playtest or prior-art review became justified.

## 2. Candidate generation and selection

The genesis cycle generated twelve mechanisms without ranking them during generation. The original set is preserved in commit `5a59af0d88da6bfab14bc3bc8bd1913d31e4da6e` and summarized in the [work log](WORKLOG.md).

Three were selected using compactness, testability, likely distinctiveness, implementation cost, and diversity of mechanism:

### Relay

A 5×5 formation race with forward and sideways movement, diagonal capture, and a requirement that all friendly stones remain connected by king adjacency.

It was selected as the fastest falsification target: the rules were short, legal-move generation was straightforward, and the connectivity constraint could create nonlocal consequences. The principal risks were resemblance to existing race games and first-player advantage.

### Span

A fixed-anchor connection game in which a placement must expand the bounding rectangle of the friendly component it joins or merge separate friendly components.

It was selected because the bounding-rectangle restriction was distinctive, visually legible, easy to test, and compatible with the same small-grid infrastructure. The principal risk was that the restriction might collapse choice instead of deepening it.

### Keystone

A 5×5 placement-and-movement game combining a center-to-two-edges objective with orthogonal custodian capture.

It was selected as a more complex fallback combining a structural objective with local tactics and reversible play. The principal risks were rule burden, center dominance, and long reversible games.

The remaining candidates were deferred or rejected because of probable prior-art proximity, opaque teaching requirements, cumbersome physical or computational representation, excessive volatility, or rule burden inappropriate for the first study.

## 3. Evaluation method

Each candidate was handled as a versioned object:

1. state ambiguities and resolve them before play results;
2. freeze a complete ruleset;
3. implement legal actions and terminal conditions;
4. write deterministic rule tests;
5. run random play only as a termination and gross-pathology screen;
6. use symmetric stronger agents for balance evidence;
7. replace aggregate suspicion with constructive analysis when a short forcing line appeared;
8. preserve rejected rules, code, tests, data, and decisions rather than editing the failed version in place.

After Relay demonstrated that random parity could conceal initiative, random win rates were explicitly demoted from balance evidence to pathology evidence.

## 4. Prototype results

### 4.1 Relay — rejected

The reproducible baseline remains in [`experiments/relay_baseline.py`](../../../experiments/relay_baseline.py). The initial implementation and analysis were committed together in `5a59af0d88da6bfab14bc3bc8bd1913d31e4da6e`.

#### Observed evidence

In 2,000 random-vs-random games:

- Player 0 won 1,003;
- Player 1 won 997;
- mean duration was 31.5715 plies;
- maximum duration was 91 plies;
- no game reached the 200-ply limit.

Search strength showed a strategic signal against random play:

- depth 1 won 131 of 200;
- depth 2 won 154 of 200;
- depth 3 won 184 of 200.

But in 200 equal depth-2 games:

- Player 0 won 129;
- Player 1 won 12;
- 59 reached the 200-ply limit unresolved.

Among decisive games, the first player won approximately 91.5%, far outside the 40–60% target.

#### Interpretation and boundary

Relay showed that stronger play could exploit real structure, but it also exposed severe initiative and a substantial unresolved population. Depth-2 minimax did not prove Relay's perfect-play value. It did establish that Relay failed the study's practical balance test with the strongest then-available symmetric instrument.

A swap rule might address initiative but not the unresolved population. A repetition rule might address cycling but not initiative. Repairing both would exceed a disciplined one-change revision. Relay was therefore preserved as a negative result and framework fixture.

### 4.2 Span v0.1 — rejected

The frozen rules and disposition are preserved in:

- [`prototypes/span/RULES.md`](prototypes/span/RULES.md)
- [`prototypes/span/DECISION.md`](prototypes/span/DECISION.md)

#### Random pathology evidence

The script [`experiments/span_random_screen.py`](../../../experiments/span_random_screen.py) was committed before the formal run at `d1ed92b0a6ada87e8aef7c479ca4a38ab6d01f9e`.

Across 10,000 games using seeds 0–9,999:

- all games terminated within the structural maximum of 21 placements;
- median duration was 15 plies;
- the 10th and 90th percentiles were 9 and 18;
- Black won 5,260 and White 4,740;
- 8,201 ended by connection and 1,799 by immobilization;
- mean legal moves across 140,506 decision nodes was 5.8609.

The repeated aggregate output was identical. Data and analysis are preserved in:

- [`data/span_random_v0_1.json`](../../../data/span_random_v0_1.json)
- [`analysis/span_random_v0_1.md`](analysis/span_random_v0_1.md)

This passed termination and practical-duration screening. The 52.6% Black random win rate was not used as balance evidence.

#### Stronger-agent and constructive evidence

A symmetric evaluator, minimax agent, match harness, and forced-line test were added. In 200 equal depth-2 games with seeds 0–199:

- Black won all 200;
- every game ended by connection on ply 5;
- only C2 and C4 were selected as openings.

Exploratory depths 1–4 produced the same five-ply outcome.

The decisive result was constructive rather than statistical. After C2, White cannot prevent Black from playing C3 and C4 and connecting the fixed C1 and C5 anchors. The reflected C4–C3–C2 line is equivalent. The regression test enumerated every required White reply.

#### Disposition

Span v0.1 was rejected. A larger tournament could not add meaningful evidence after a short forced win had been established. Random play had concealed the line because random Black frequently declined the central continuation.

### 4.3 Keystone v0.1 — rejected

Keystone's recovered origin, frozen rules, and decision are preserved in:

- [`prototypes/keystone/ORIGIN.md`](prototypes/keystone/ORIGIN.md)
- [`prototypes/keystone/RULES.md`](prototypes/keystone/RULES.md)
- [`prototypes/keystone/DECISION.md`](prototypes/keystone/DECISION.md)

The rules fixed an empty 5×5 board, eight stones per player, placement or one-step orthogonal shifting, mandatory choice of one newly completed custodian capture, permanent removal, a center component touching two distinct edges with separate stones, no-action loss, and threefold repetition. The core rules contained 277 words.

#### Random pathology evidence

The script was committed before execution at `f4550102b8a3879d5754ac8dc30eaaac017f2833`. It ran 2,000 games with seeds 0–1,999 and a 200-ply observation limit, then repeated the complete run. Both outputs were byte-identical with SHA-256 `bdbdaa2821a16a38078308f38d272e9cb0d3ec8e353e54f0fbcfa06e2d0d849d`.

Results:

- 1,018 games completed by 200 plies: 50.9%;
- 982 games reached the observation limit: 49.1%;
- 886 ended in structural victory;
- 104 ended by immobilization;
- 28 ended by threefold repetition;
- median duration was 193 plies;
- shifting accounted for 235,014 of 266,654 observed actions: 88.13%;
- both reserves were exhausted in 1,834 games: 91.7%.

A bounded 1,000-ply diagnostic on the first 100 limit seeds eventually resolved all games, but with median 427.5 and maximum 964 plies.

Data and analysis are preserved in:

- [`data/keystone_random_v0_1.json`](../../../data/keystone_random_v0_1.json)
- [`analysis/keystone_random_v0_1.md`](analysis/keystone_random_v0_1.md)

#### Interpretation and disposition

Keystone did not demonstrate literal infinite play. It demonstrated a large practical long-game population in which both reserves were exhausted and reversible shifting dominated. Exact threefold repetition resolved too few games inside a practical window.

The 50.9% completion rate missed the 98% threshold by 47.1 percentage points. Restricting movement or adding a progress score would alter the defining reversible-control mechanism or add substantial bookkeeping. Keystone v0.1 was rejected without a stronger-agent balance screen because the gross-pathology threshold had already failed decisively.

### 4.4 Span v0.2 — rejected

After comparing the three failures, Span was selected as the only plausible one-change revision. The comparison is preserved in [`analysis/prototype_revision_selection.md`](analysis/prototype_revision_selection.md).

Span v0.2 changed one rule only: after the first Black placement, the second participant could make a normal White placement or swap sides. Anchors, placement geometry, connection, immobilization, and finite placement were unchanged. The frozen 308-word rules are preserved in [`prototypes/span/RULES_v0_2.md`](prototypes/span/RULES_v0_2.md).

Participant identity was separated from color ownership so the same symmetric agent and budget could choose the opening, swap response, and later moves without confusing seat and color.

#### Formal configuration and reproducibility

The formal script [`experiments/span_v0_2_formal_screen.py`](../../../experiments/span_v0_2_formal_screen.py) was committed before execution at `edac024671aeb380472e0a6a58a8eb35a134e124`.

Configuration:

- 10,000 random games, seeds 0–9,999;
- 1,000 equal-budget depth-3 games, seeds 0–999;
- one evaluator and search depth for all decisions;
- Python 3.13.5;
- zero manual exclusions.

The complete configuration was run twice. Both JSON outputs were byte-identical with SHA-256 `93f55d3c5e9cacf86aec7bbecdf351fc661f2f5ecbfdefb1f7e05c08482e56d2`.

Evidence is preserved in:

- [`data/span_v0_2_formal.json`](../../../data/span_v0_2_formal.json)
- [`analysis/span_v0_2_formal.md`](analysis/span_v0_2_formal.md)
- [`prototypes/span/DECISION_v0_2.md`](prototypes/span/DECISION_v0_2.md)

#### Random pathology evidence

All 10,000 random games terminated.

- first participant: 5,198 wins, 51.98%;
- second participant: 4,802 wins, 48.02%;
- swap occurred in 1,410 games, 14.1%;
- median duration was 15 action plies;
- maximum duration was 22 action plies.

This appeared healthy but remained pathology evidence only.

#### Equal-budget balance evidence

In 1,000 equal depth-3 games:

- the first participant won 0;
- the second participant won 1,000;
- White won all 1,000;
- no game used swap;
- every game ended by connection after six placements.

The first-participant decisive win rate was 0%, outside the required 40–60% interval.

#### Constructive opening diagnosis

The tournament result was followed by exhaustive analysis of all six legal openings. The regression is preserved in [`tests/test_span_v0_2_forced_second_participant.py`](../../../tests/test_span_v0_2_forced_second_participant.py).

- After C2 or C4, the second participant swaps, takes Black, and completes the already-established central line.
- After B1 or B5, the second participant remains White and forces B3–C3–D3.
- After D1 or D5, the second participant remains White and forces D3–C3–B3.

The test enumerates every required intervening first-participant response. Every legal first placement loses. This is a constructive second-participant win, not merely a depth-3 statistical imbalance.

#### Disposition

Span v0.2 was rejected. The swap rule priced the opening but could not create a viable first move: central openings were taken by swap, while outer openings conceded the short White connection.

No Span v0.3, second balancing device, altered anchors, opening ban, or scoring patch was introduced inside Study 001. Strategic-signal tournaments and prior-art review were cancelled because an initial-state forced participant win was already decisive.

## 5. Evidence classification

### Directly demonstrated under the recorded procedures

- the exact outcomes and duration distributions of the recorded fixed-seed experiments;
- Relay's strong first-player skew under the tested symmetric depth-2 agent;
- Span v0.1's constructive five-ply Black line;
- Keystone's failure of the precommitted 200-ply random termination threshold;
- Span v0.2's 0–1,000 symmetric result and constructive second-participant win after every legal opening;
- deterministic rerun equality where hashes or identical aggregates were recorded;
- implementation fidelity for distinctions covered by deterministic tests.

### Bounded inferences

- Relay was unsuitable under the study's practical agent-based balance criterion; its perfect-play value was not solved.
- Keystone was unsuitable for the study's practical duration target; literal nontermination was not proved.
- Span v0.1 and v0.2 were nonviable as balanced games because short constructive forcing strategies existed from the opening.
- a further Span repair would constitute a new design project rather than a faithful completion of the frozen single-change revision.

### Unresolved human-dependent qualities

The study did not establish:

- fun;
- elegance;
- teachability in an actual under-three-minute explanation;
- human strategic depth or replay value;
- accessibility or physical ergonomics;
- genuine originality or legal protectability;
- equivalence or non-equivalence to existing games.

No prior-art review was performed because no candidate reached the stage at which an originality claim would have been responsible.

## 6. Reproducibility and verification audit

### Reproducibility strengths

- The protocol was fixed before candidate selection.
- Rules were versioned and frozen before formal evaluation.
- Key experiment scripts were committed before execution.
- Seeds, agent depths, code versions, Python versions, and exclusions were recorded for formal screens.
- Repeated configured runs were used to verify deterministic aggregate output.
- Machine-readable data, analysis, rules, decisions, and regression tests remain in the repository.
- Failed versions were preserved rather than silently repaired.

### Verification limitations

- The repository had no GitHub Actions workflow during Study 001.
- Verification relied on locally reconstructed copies of the live repository files because the execution container intermittently could not resolve `github.com` for a fresh clone.
- Full reconstructed test counts increased across the study: 3, 12, 20, 31, 45, and 52 passing cases at successive implementation stages.
- The final Span v0.2 forced-opening test passed locally, but a single fresh-checkout 53-case run was not recorded. No game or agent source changed during that final formal screen.
- Depth-limited minimax results are bounded by their evaluators and horizons. Constructive forced-line tests provide stronger evidence only for the explicitly enumerated opening structures.
- The initial Relay experiment was less formally instrumented than later screens; it remains reproducible through its script and preserved initial commit, but it does not have the same code-version and byte-hash record as the later experiments.

These limits reduce the strength of broad claims. They do not change the negative study conclusion because each candidate failed a precommitted criterion by a wide margin or had a short constructive defect.

## 7. Human intervention audit

The [human intervention ledger](../../../governance/HUMAN_INTERVENTION.md) distinguishes research authorship from access and governance assistance.

Human contributions materially established the laboratory's purpose, non-interference rule, public visibility, identity alignment, repository access, and the approval-driven execution model. Those actions are recorded as A1–A3 according to their actual effect.

Within the candidate generation, rule design, implementation, experiment selection, execution, interpretation, rejection, revision choice, and final negative conclusion, the human normally supplied only the plain `承認` access trigger. Those cycles are recorded as A1 access assistance, with the substantive research work classified as autonomous A0.

The human's conversational question about convergence toward existing games was recorded as non-directive and did not change the frozen rules or evaluation. It motivated no rescue patch; prior-art review remained conditional on basic viability.

## 8. Methodological lessons

### Random parity can be anti-diagnostic

Random play appeared approximately balanced for Relay, Span v0.1, and Span v0.2. Stronger or constructive analysis found severe initiative or forced wins in all three. In Span v0.2, random play favored the first participant 51.98%, while every legal opening was constructively losing for that participant.

Random-versus-random remains useful for termination, gross pathology, branching, and duration. It should not be treated as early balance evidence in deterministic strategy games.

### Stronger aggregate results should trigger structural diagnosis

A 200–0 or 1,000–0 tournament is a warning, not automatically a proof. The useful next step was not merely increasing the sample. It was identifying and enumerating the short forcing structure. Once the forced line was established, further tournaments had little research value.

### Version freezing prevented adaptive rescue

Rules were frozen before results. Failed versions were preserved and rejected. The swap revision was chosen through a cross-prototype comparison, limited to one change, and frozen before implementation. When it failed, no convenient second patch was inserted. This prevented the study from becoming an unbounded sequence of post-result adjustments.

### Seat, color, and role must be measured separately

A swap rule makes Black/White results insufficient. Span v0.2 required participant identity, color ownership, swap use, and participant-based winning statistics to be recorded independently. Without that distinction, the balancing rule could have produced misleading reports.

### Stop rules are part of research quality

Relay did not receive two repairs, Keystone did not receive a progress ledger, Span did not receive v0.3, and strategic-signal or prior-art work was cancelled after decisive failure. Stopping preserved the meaning of the protocol and the interpretability of the negative result.

### A failed artifact can still produce a successful experiment

Study 001 failed to produce the target game. It nevertheless demonstrated an autonomous loop capable of generating alternatives, implementing formal rules, collecting reproducible evidence, detecting misleading metrics, constructing counterexamples, preserving negative results, and concluding against its own artifact.

## 9. Final conclusion

No selected prototype or permitted revision survived with evidence sufficient to support the target claim.

- Relay contained useful strategic signal but failed practical balance and produced many unresolved strong-agent games.
- Span v0.1 was compact and terminated well but had a five-ply first-player forced win.
- Keystone v0.1 offered tactical interaction but failed practical termination severely.
- Span v0.2 preserved compactness and termination but converted the opening defect into a second-participant forced win after every legal opening.

Therefore Study 001 closes with a **negative research conclusion**:

> Templex Tsukino autonomously produced compact, reproducible, falsifiable abstract-game prototypes, but did not produce a surviving game with evidence sufficient to claim reasonable balance and meaningful strategic depth.

No final game package, browser interface, originality claim, or publication-ready design is warranted from this study.

A possible Study 002 would require a separately written question, protocol, candidate-generation strategy, and approval cycle. It is not an automatic continuation or an implicit repair of Study 001.
