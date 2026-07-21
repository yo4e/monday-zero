# Study 003 Cycle 3 — Historical Transfer

_Date: 2026-07-21 (Asia/Tokyo)_

## Disposition

**The frozen historical-transfer gate passed.**

Exactly four precommitted Study 001/002 cases were encoded from cited repository records. The trace artifact was committed before evaluation. The frozen primary validator and independent oracle matched all four expected dispositions. No validator, oracle, baseline, synthetic fixture, historical expectation, dependency class, or event kind was changed.

## Frozen historical artifact

- File: `data/historical_traces_v1.json`
- Artifact commit: `7b9b7d59901c91e91c00a9f68c4eb8972946e415`
- Git blob: `840a7779a1cee3ba4f3f88e62342269b804c2719`
- Internal canonical SHA-256: `8cdaec94de2e8a7aff3158924db5e570f4af3008bcb33f18602f584b29b41053`
- Traces: 4
- Events: 44
- Maximum trace length: 14

The artifact cites repository paths and commits for each encoded event sequence and uses only the frozen fourteen-event vocabulary.

## Frozen instruments used

- Primary validator Git blob: `71080f1051acc015e74b42de19d56ce8782b9f25`
- Independent oracle Git blob: `74159c7a7502975b1bcd376510d5dad0283e03cd`

The instrument blobs are unchanged from Cycle 2.

## Result

Result file: `data/historical_transfer_result_v1.json`

- Result passed: **true**
- Expected-verdict matches: **4 / 4**
- First-violation matches: **4 / 4**
- Primary/oracle agreement: **4 / 4**
- Result canonical SHA-256: `c59c621a1efad82ba95ca6eb92465a062b9b412b4fd8f4a05d69dccfcdcdac4a`
- Result Git blob: `161b65efb09d2d98cba0584574aeeaf0dfa5ec66`

| Trace | Frozen expectation | Primary | Oracle | Match |
|---|---|---|---|---|
| `H1-SPAN-FORMAL-VALID` | valid | valid | valid | yes |
| `H2-EXACT-SUBSTUDY-VALID` | valid | valid | valid | yes |
| `H3-STUDY002-SHALLOW-CONTAMINATED` | invalid at index 5, D1, `artifact-not-frozen` | same | same | yes |
| `H4-EXACT-PROJECTION-CORRECTION-VALID` | valid | valid | valid | yes |

## Encoding notes

### H1 — Span formal screen

The trace encodes approval, a precommitted formal experiment artifact, two capped executions, two observations, and evidence acceptance. Sources include the Study 001 final report and the pre-execution formal-screen commit `edac024671aeb380472e0a6a58a8eb35a134e124`.

### H2 — Study 002 exact sub-study

The trace encodes proposal, manifest, exact instrument, and exact experiment freezes before a capped eighteen-candidate execution, followed by exact-result observation and acceptance. Sources include proposal commit `68fc4c2edb93ca1363e7b7040221b5507cfeb171`, manifest commit `6b414e685253224357c7f10622f8984bbb2d8f05`, instrument commit `37a86e2f01d08bb3f039b9c0a812bd597d19ae00`, and experiment commit `9a453ccc2a2e1f30691d23028b12b3296ebb4f13`.

### H3 — Study 002 shallow contamination

The contract maps protected observation `exact-results` to prerequisite artifact `shallow-heuristic`. The trace contains no freeze for that artifact before exact-result observation. Both frozen instruments reject at event index 5 with D1 `artifact-not-frozen`, as precommitted. No Study 002 identifier appears in validator rule code.

### H4 — Exact projection correction

The trace encodes the original projection observation, defect recording, evidence invalidation, corrected comparator application and refreeze, capped rerun, replacement observation, disclosure, and corrected evidence acceptance. The comparator source is commit `8f2ea806ea079c3b1da19b6bcae5864fcad9170e`.

## Verification

- The checked-in historical artifact Git blob matched the locally encoded bytes.
- The checked-in result Git blob matched the locally generated deterministic result.
- Two local executions produced the same result bytes and SHA-256.
- The live GitHub blobs for the frozen primary and oracle remained the Cycle 2 values.
- Structural checks confirmed four unique traces, contiguous event indices, source citations, only frozen event kinds, and the forty-event limit.

A fresh clone was attempted and failed because the execution environment could not resolve `github.com`. The formal local execution therefore used a functional reconstruction of the live frozen validator and oracle source. Full-repository regression and GitHub Actions verification were not performed.

## Claim boundary

Passing historical transfer shows that the frozen contract language and validators could represent and classify these four precommitted repository histories without changing validator rules or adding semantic events. It does not establish that the encoded studies were true, valuable, safe, unbiased, autonomous, or scientifically sound. The historical set is small and selected before Study 003 activation from known repository episodes.

## Human intervention

Yoshie Yamada supplied the plain project-chat `承認`, classified as A1 access assistance. Templex selected source evidence, encoded traces, ran the frozen instruments, interpreted the result, and selected the next bounded work. No human selected or edited a historical verdict.

## Next bounded unit

Cycle 4 must reproduce the complete synthetic-plus-historical validation report twice, classify H1–H4, write the final report, close Issue #7, set no active study, and stop. It must not begin Study 004.
