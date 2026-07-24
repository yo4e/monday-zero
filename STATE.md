# State

_Last updated: 2026-07-24_

## Phase

**No active study / inactive Study 005 proposal frozen**

## Laboratory

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Repository: `yo4e/templex-zero`
- Execution model: `governance/APPROVAL_DRIVEN_EXECUTION.md`

## Closed studies

- **Study 001:** negative autonomous-game-design conclusion.
- **Study 002:** partial / incomplete exact-first result; H1 and H3 supported, H2 unresolved.
- **Study 003:** methodological success with bounded procedural claims.
- **Study 004:** partial finite-state conformance result; H1 unsupported, H2 supported, H3 unresolved.

## Post-Study-004 portfolio decision

- Assessment: `research/decisions/2026-07-24-post-study-004-portfolio-assessment.md`
- Decision: **GO to one frozen proposal; remain inactive**.
- Selected direction: **IANA tzdb transition round-trip conformance**.
- Frozen proposal: `research/proposals/STUDY_005_TZDB_TRANSITION_ROUNDTRIP.md`
- Pinned external referent: **IANA tzdb 2026c**.
- Score: **29 / 30** under the frozen portfolio criteria.
- Open active-study issue: **none**.
- No source archive, compiled data, implementation, transition corpus, or experiment was created in the portfolio cycle.

## Proposal boundary

The proposal asks whether an independently implemented TZif reader and a version-isolated Python `zoneinfo` harness can verify explicit UTC projection, backward-transition `fold` round trips, and forward-transition gap detection across the canonical tzdb 2026c zone inventory.

It is frozen but **not active**. It permits negative, partial, or full bounded results and has a maximum of four approval cycles after activation.

## Next bounded work

The next approval must independently inspect the frozen Study 005 proposal and choose:

- **GO unchanged:** activate Study 005 and perform Cycle 1 only: official-source and permission preflight, isolated double compilation, canonical zone inventory, and frozen parser fixtures; or
- **NO-GO:** record why activation is not justified and remain inactive.

The next cycle must not implement the full TZif reader, generate the complete transition manifest, execute the `zoneinfo` comparison, contact outsiders, accept terms, or file an external defect report.

## Verification limitation

The portfolio decision used live repository evidence, official public documentation, and bounded local tool-presence checks. It did not download tzdb 2026c or execute Study 005. Current availability of Python 3.13.5, `zoneinfo`, `zic`, and `zdump` is feasibility evidence only and must be rechecked at activation.

Fresh checkout and full-repository regression were not required for this documentation-only portfolio cycle and were not performed.

## Human action currently needed

None.
