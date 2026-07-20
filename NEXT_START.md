# Next Start

_Updated: 2026-07-18 (Asia/Tokyo)_

## Purpose

This is a compact advisory bridge for a new execution context. It is not authorization and is not the source of truth. Re-read `STATE.md`, the closed Study 001 and Study 002 reports, the latest go / no-go decision, the frozen proposal, and current commits.

When Yoshie Yamada sends `承認`, follow `governance/APPROVAL_DRIVEN_EXECUTION.md`, complete one bounded cycle, report it in the same project chat, and stop.

## Identity and execution

- Public operator: **Templex Tsukino / 月野テンプレクス**
- Laboratory: **TEMPLEX/0**
- Familiar and historical name: **Monday**
- Repository: `https://github.com/yo4e/templex-zero`
- External communication, publication, spending, permissions, human-subject activity, and third-party actions remain separately gated.

## Current position

**No active study. Study 001 and Study 002 are closed.**

A successor proposal now exists but is not active:

- `research/proposals/STUDY_003_PROTOCOL_INTEGRITY.md`
- final frozen proposal commit: `a4434950383a2b995c35987fbb4d52b4220c7547`
- freeze audit: `research/proposals/STUDY_003_PROTOCOL_INTEGRITY_AUDIT.md`

Study 003 has not been activated. No study directory, active issue, code, validator, machine-readable trace corpus, historical encoding, experiment, or result exists.

## Frozen proposal summary

The proposed study asks whether a declarative research contract can reject invalid event traces at the first violation while accepting valid traces without study-specific rules.

It precommits:

- six dependency classes covering artifacts, authorization, caps, corrections, artifact mutation, and bounded-cycle approval;
- fourteen event kinds;
- twelve minimal valid/invalid traces;
- four composite valid traces;
- twenty deterministic mutants from five operators;
- thirty-six synthetic traces total;
- one incremental state-machine validator;
- one independently written whole-trace oracle;
- one deliberately weak order-only baseline;
- four historical Study 001/002 transfer traces after the synthetic gate;
- zero false accepts, zero false rejects, exact first-violation and class agreement;
- maximum four approval cycles after activation.

The proposal was corrected before activation because the first `P4` and `P5` symbolic sequences did not fully satisfy their own correction lifecycle. Both commits remain visible; no result existed when the correction was made.

## Activation decision required

The next approval must independently choose one of:

### GO

Activate the unchanged frozen proposal and complete only activation cycle 1:

- copy commitments into an active protocol;
- implement trace and contract schema plus canonical serialization;
- deterministically generate the frozen thirty-six synthetic traces;
- verify byte-identical regeneration and exact corpus arithmetic;
- do not implement validator verdict logic or encode historical traces.

### NO-GO

Remain inactive and record why the design is too tautological, insufficiently independent, overfit, or low-value.

### REVISE BEFORE ACTIVATION

Correct a factual or internal proposal error before implementation and require another approval for activation.

Proposal existence is not evidence that GO is the right decision. Remaining inactive is valid.

## Closure boundaries

- Do not reopen Study 001 or create Span v0.3.
- Do not retroactively repair Study 002.
- Do not start another generated-game corpus as a hidden continuation.
- Do not silently activate Study 003.
- Do not create Study 004 in the same cycle.

## Human gate

> 承認

## Human action pending

None.