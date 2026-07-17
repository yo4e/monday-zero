# Next Start

_Updated: 2026-07-17 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not authorization and is not the source of truth. `STATE.md`, the active protocol, frozen manifest, exact-screen analysis, Issue #6, and live commits remain authoritative.

When Yoshie Yamada sends `承認` in the project chat, re-read the live repository and `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report it in the same chat, and stop.

## Identity and execution

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Familiar and historical name: **Monday**
- Repository: `https://github.com/yo4e/templex-zero`
- External communication, publication, spending, permissions, human-subject activity, and third-party actions remain separately gated.

## Current position

**Study 002 is active. Exact candidate cycle 4 of at most 6 is complete.**

- Active protocol: `research/studies/002-exact-first-screening/PROTOCOL.md`
- Frozen manifest: `research/studies/002-exact-first-screening/manifest/`
- Exact instrument audit: `research/studies/002-exact-first-screening/EXACT_INSTRUMENT_AUDIT.md`
- Exact screen data: `research/studies/002-exact-first-screening/data/exact_screen_v1.json`
- Exact screen analysis: `research/studies/002-exact-first-screening/EXACT_SCREEN_ANALYSIS.md`
- Tracking issue: Issue #6

Study 001 remains closed. Do not reopen it or create Span v0.3.

## Exact result

- 18 frozen candidates.
- 15 solved exactly; 3 reached the 30-second time cap.
- All nine 3×3 entries solved; six of nine 4×4 entries solved.
- Exact roots: 9 first-participant wins, 6 first-participant losses, no draws.
- 14 of 15 solved roots terminate within eight optimal plies.
- Six solved candidates have no non-losing opening for the first participant.
- Continuation threshold of 12 solved candidates passed.
- Degenerate-majority failure condition did not trigger.
- Corrected repeated-run normalized SHA-256: `9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`.

## Procedural limitation

The frozen proposal requires the shallow-search heuristic to be generated before exact results are inspected. No heuristic was frozen before cycle 4. Exact results have now been inspected.

Do not create a post-result heuristic and call it precommitted. The formal shallow depth-1/2/3 screen is cancelled, H2 will remain unresolved, and Study 002 cannot receive a fully successful methodological disposition.

The random screen remains valid because it requires no heuristic and was specified before exact results.

## Next recommended work unit

Run the frozen **random screen only**.

1. Commit the experiment script before running games.
2. Use all 18 candidates in frozen manifest order.
3. Run exactly 2,000 independent fixed-seed random games per candidate.
4. Derive seeds from the frozen candidate index with a documented deterministic formula.
5. Record first/second participant wins, duration, terminal reason, opening distribution, and branching.
6. Repeat and compare deterministic aggregate output.
7. Do not implement or run shallow search.
8. Do not use exact values in move choice or candidate-specific behavior.
9. After the random output is complete, compare it with exact outcomes and flag pre-defined false-reassurance cases where applicable.
10. Reserve cycle 6 for final synthesis and closure as partial/incomplete.

## Human gate

> 承認

## Human action pending

None.

## Anchors

- Approval protocol: `governance/APPROVAL_DRIVEN_EXECUTION.md`
- Current state: `STATE.md`
- Study 002 proposal: `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`
- Study 002 protocol: `research/studies/002-exact-first-screening/PROTOCOL.md`
- Frozen manifest: `research/studies/002-exact-first-screening/manifest/index.json`
- Exact analysis: `research/studies/002-exact-first-screening/EXACT_SCREEN_ANALYSIS.md`
- Issue #6: Study 002 tracking
