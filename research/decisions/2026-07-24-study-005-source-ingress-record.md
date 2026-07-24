# Study 005 Source Ingress and Repository Cleanup Record

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **Official archive identity verified; Study 005 remains inactive**_

## 1. Purpose

This record documents the A1 access operation that supplied the exact pinned IANA tzdb 2026c archive to the TEMPLEX/0 project conversation and removed an unnecessary repository copy before Study 005 activation.

It does not activate Study 005, create an active protocol or issue, compile tzdb, freeze a zone inventory or parser fixtures, implement code, or inspect Study 005 outcomes.

## 2. Repository copy and deletion

Yoshie Yamada temporarily committed `tzdata2026c.tar.gz` at the repository root to test whether TEMPLEX/0 could retrieve the binary through the GitHub connector.

The connector observed the repository blob only far enough to identify the file and obtain its blob SHA. The repository copy was not extracted, compiled, used as a source snapshot, used as experimental evidence, or committed into any study directory.

At Yoshie Yamada's explicit instruction, Templex deleted the root-level file unchanged from the live repository.

- deleted path: `tzdata2026c.tar.gz`
- deleted blob SHA: `9fdd7891addf67ea3f6592a8264d2a8b2d761224`
- deletion commit: `da39f24d534217d2da26cc213e5b257943385763`

The Git history necessarily retains the earlier blob because deletion does not rewrite public history. This record does not claim erasure from prior commits.

## 3. Project-conversation upload

Yoshie Yamada separately uploaded the unchanged archive directly to the TEMPLEX/0 project conversation. Templex inspected that uploaded file in the bounded access-preflight context.

Observed identity:

- filename: `tzdata2026c.tar.gz`
- byte count: **475,694**
- SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`
- SHA-256: `e4a178a4477f3d0ea77cc31828ff72aa38feff8d61aa13e7e99e142e9d902be4`
- archive member count: **32**
- internal `version` file: `2026c`
- `zone1970.tab`: present
- unsafe absolute or parent-traversal member paths: none observed

The byte count and SHA-512 exactly match the official IANA 2026c release metadata already recorded in the activation NO-GO decision.

## 4. Bundled permission boundary

The uploaded archive contains a top-level `LICENSE` file. Its inspected terms state that, unless otherwise specified, the tz code and data files are in the public domain. It additionally identifies a BSD 3-clause condition only if `date.c`, `newstrftime.3`, or `strftime.c` are present.

The archive member listing inspected in this access preflight did not contain those three named files. No terms were accepted on behalf of the human, and no third-party archive or extracted file was committed by Templex.

## 5. Research boundary

The uploaded archive is now a verified trusted-ingress artifact available to the current project execution environment. This removes the operational source-acquisition blocker recorded in `research/decisions/2026-07-24-study-005-activation-no-go.md`.

Study 005 nevertheless remains inactive. A later exact project-chat `承認` must independently re-read the live repository, re-check the available uploaded bytes, choose GO unchanged or NO-GO, and, only if GO, perform Cycle 1 within the frozen proposal.

No compilation, zone inventory, fixture expectation, TZif parsing, Python `zoneinfo` comparison, hypothesis test, or active-study issue was created in this access-and-cleanup operation.
