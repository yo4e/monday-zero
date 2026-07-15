# Keystone v0.1 Random Pathology Screen

_Date: 2026-07-15 (Asia/Tokyo)_

## Question

Does frozen Keystone v0.1 terminate reliably under random legal play, and do its placement, shifting, capture, reserve, branching, and repetition behaviors justify stronger-agent evaluation?

Random-play win rates are not treated as balance evidence.

## Formal configuration

- Script: `experiments/keystone_random_screen.py`
- Script/code version: `f4550102b8a3879d5754ac8dc30eaaac017f2833`
- Games: 2,000
- Seeds: 0 through 1,999
- Independent pseudorandom generator per game
- Observation limit: 200 plies
- Python: 3.13.5
- Manual exclusions: none

The configured run was executed twice. Both JSON outputs had SHA-256 `bdbdaa2821a16a38078308f38d272e9cb0d3ec8e353e54f0fbcfa06e2d0d849d` and were byte-for-byte identical.

## Formal results

| Measure | Result |
|---|---:|
| Completed by 200 plies | 1,018 / 2,000 (50.9%) |
| Observation-limit hits | 982 (49.1%) |
| Structural victories | 886 (44.3%) |
| Immobilization wins | 104 (5.2%) |
| Threefold-repetition draws | 28 (1.4%) |
| Black wins | 504 |
| White wins | 486 |
| Minimum plies | 11 |
| Median plies | 193 |
| Mean plies | 133.327 |
| 90th percentile | 200 |
| Mean legal actions | 12.6330 |
| Maximum legal actions | 35 |

The protocol requires at least 98% random termination within 200 plies, unless a justified draw rule actually resolves the remaining play. Keystone v0.1 misses that threshold by 47.1 percentage points. Its threefold rule resolves only 1.4% of games within the observation window and does not explain away the 49.1% limit rate.

Black won 504 games and White 486. This near parity is not balance evidence because more than half the games were draws or censored at the observation limit, and random parity previously concealed strategic defects in Relay and Span.

## Action profile

Across 266,654 observed actions:

- placements: 31,640 (11.87%);
- shifts: 235,014 (88.13%);
- captures: 12,618, or 6.309 per game;
- games with no capture: 102;
- both reserves exhausted at termination or censoring: 1,834 games (91.7%).

The game does not fail because nothing can happen. Captures occur and branching remains substantial. It fails because, once reserves empty, the remaining legal structure permits long sequences of shifts without reliable progress toward victory, immobilization, or the exact third occurrence needed for a repetition draw.

## End-mode diagnosis

All 982 observation-limit games used all sixteen placements and then contained exactly 184 shifts. Their mean capture count was 8.915. At least one position occurred twice in 79.9% of these limit games, but only exact third occurrences terminate; broad wandering through many related positions therefore remains uncaught.

For comparison:

| End mode | Games | Median plies | Mean shifts | Mean captures |
|---|---:|---:|---:|---:|
| Structural victory | 886 | 41 | 41.13 | 2.98 |
| Immobilization | 104 | 163 | 141.43 | 9.81 |
| Repetition | 28 | 131.5 | 113.36 | 7.25 |
| 200-ply limit | 982 | 200 | 184.00 | 8.92 |

Structural victories themselves often occur within the study's practical 8–80-ply target. The pathology is a bifurcation: some games resolve normally, while a very large second population enters an extended movement phase.

## Exploratory longer-horizon follow-up

This was not part of the formal threshold test. To distinguish permanent nontermination from merely impractical duration, the first 100 formal seeds that hit 200 plies were rerun with a 1,000-ply limit using the same script function.

- 5 ended in structural victory;
- 63 ended by immobilization;
- 32 ended by threefold repetition;
- 0 still reached the 1,000-ply limit;
- median duration: 427.5 plies;
- mean duration: 463.02 plies;
- maximum duration: 964 plies.

The rules eventually resolve this fixed diagnostic sample, but at durations far outside the protocol's practical target. The draw condition is therefore logically valid but operationally inadequate.

## Decision

**Reject Keystone v0.1 in its frozen form.**

A stronger symmetric-agent screen is cancelled for this version. Search quality cannot rescue a ruleset that fails the precommitted random termination threshold this severely, and a strong agent might merely learn to exploit or avoid the long movement phase without making the baseline practically acceptable.

The rules, implementation, tests, script, and negative data remain preserved. Any repair must be a separately frozen version. Study 001 should now compare the failure modes and repair costs of Relay, Span, and Keystone before choosing one versioned revision or concluding the study negatively.

## Limitations

- Random play does not establish optimal duration, balance, strategic depth, or human experience.
- The 1,000-ply follow-up used a deterministic diagnostic subset rather than all 982 limit seeds.
- No deliberate similarity search or human playtest has been conducted.
- The diagnosis identifies excessive post-reserve shifting as the observed mechanism, but it does not prove which rule revision would preserve the intended game while fixing duration.
