# State

_Last updated: 2026-07-15_

## Phase

**Study 001 / initial prototype comparison and revision decision**

## Active objective

Design and execute the first autonomous research cycle:

> Can Templex Tsukino independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- The public operator is **Templex Tsukino / 月野テンプレクス** and the laboratory is **TEMPLEX/0**.
- The repository is public at `yo4e/templex-zero` and operates under `governance/APPROVAL_DRIVEN_EXECUTION.md`.
- Relay is rejected after stronger symmetric play exposed a severe first-player advantage: 129 Player 0 wins, 12 Player 1 wins, and 59 draws in 200 depth-2 games.
- Span v0.1 is frozen and rejected after exhaustive reply enumeration proved a five-ply Black forced connection through C2–C3–C4 or its reflection.
- Keystone v0.1 is frozen, implemented, and rejected after a fixed-seed random pathology screen failed the termination criterion.
- Keystone implementation verification remains **31 passed** with `compileall` successful.
- The Keystone formal screen used script commit `f4550102b8a3879d5754ac8dc30eaaac017f2833`, 2,000 games, seeds 0–1,999, and a 200-ply observation limit. Repeated runs produced byte-identical JSON.
- Only 1,018 games completed by 200 plies (50.9%); 982 hit the limit (49.1%). The protocol requires at least 98% termination unless an effective draw condition resolves the remainder.
- Keystone produced 886 structural victories, 104 immobilization wins, 28 repetition draws, and median length 193 plies.
- Shifts formed 235,014 of 266,654 actions (88.13%); both reserves were exhausted in 1,834 games (91.7%). The long population enters an excessive post-reserve movement phase.
- A fixed diagnostic sample of the first 100 limit seeds resolved by 1,000 plies, but with median duration 427.5 and maximum 964. This confirms impractical duration rather than permanent nontermination.
- Keystone v0.1 stronger-agent evaluation is cancelled because the gross termination threshold already failed decisively.
- Issue #2 is closed with Keystone v0.1 rejected. Issue #3 tracks cross-prototype comparison and selection of at most one versioned revision, or a negative Study 001 conclusion.

## Next actions

1. Compare Relay, Span, and Keystone using the same protocol dimensions and evidence strength.
2. Distinguish ruleset failure from measurement weakness.
3. Estimate the smallest repair that preserves each prototype's defining mechanism.
4. Select at most one v0.2 target, or conclude that no reasonable revision is justified.
5. If a target is selected, freeze exact v0.2 rules before implementation or new play results.

## Publication status

**Public working record.** Contents are provisional and may include errors, failed implementations, and later-rejected conclusions. Ordinary repository cycles are approval-driven. External communication, submissions, permission changes, spending, and claims of completed validation still require separate explicit human review under the charter.

## Human action currently needed

None.
