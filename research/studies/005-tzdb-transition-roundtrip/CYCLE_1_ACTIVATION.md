# Study 005 Cycle 1 — Activation, Compilation, Inventory, and Fixture Freeze

_Date: 2026-07-24 (Asia/Tokyo)_  
_Status: **Cycle 1 complete; Study 005 remains active**_

## Activation decision

**GO unchanged.**

The live repository had no active study or Study 005 issue. The exact project-conversation upload matched the official IANA tzdb 2026c byte count and SHA-512, its internal version was `2026c`, and its bundled `LICENSE` left the selected distribution under the recorded public-domain boundary. No frozen research or method condition required revision.

The active protocol was committed before any successful `zic` execution. Issue #11 was then opened as the active-study tracker.

## Source identity

- official URL: `https://www.iana.org/time-zones/repository/releases/tzdata2026c.tar.gz`
- bytes: 475,694
- SHA-512: `e0b4b7044b66fbc27bc21d13d18063abcdf78ab58d5ba5fd64bd1a88d86e9d495f45add4d8e65bb6c40249f9c94ca29b72c8ebba8d0e4c468f2965ac77932ef0`
- SHA-256: `e4a178a4477f3d0ea77cc31828ff72aa38feff8d61aa13e7e99e142e9d902be4`
- archive members: 32
- internal version: `2026c`
- `zone1970.tab`: present
- detached signature: not supplied or verified
- archive and extracted third-party files committed: no

## Frozen compilation

Tool identity:

- Python: `/opt/pyvenv/bin/python3`, Python 3.13.5
- `zic`: `/usr/sbin/zic`, Debian glibc 2.41-12+deb13u2
- `zdump`: `/usr/bin/zdump`, Debian glibc 2.41-12+deb13u2

Source order:

`africa antarctica asia australasia europe northamerica southamerica etcetera`

Command template:

```text
env -i PATH=/usr/sbin:/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC \
  /usr/sbin/zic -b fat -d OUT \
  africa antarctica asia australasia europe northamerica southamerica etcetera
```

The two compilations were performed in newly created separate directories.

| Field | Compile A | Compile B |
|---|---:|---:|
| files | 341 | 341 |
| total bytes | 397,559 | 397,559 |
| projection SHA-256 | `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2` | `0597ea7b68f068b1ab06be671b1a3839bca651c5514d7171c32a59c4da9849b2` |

The full projections were byte-identical.

One non-semantic operational correction occurred before any `zic` command executed: the first shell wrapper contained a trailing line continuation before `done` and failed to parse. The temporary work root was deleted and recreated. The frozen command, flags, source order, and environment did not change.

One post-execution artifact-persistence correction also occurred before cycle closure: the first repository serialization of the compressed targeted `zdump` evidence did not match the execution-local Git blob identity. The file was replaced from the unchanged execution-local base64 artifact using fixed line wrapping, and the corrected repository blob identity was rechecked. The uncompressed evidence bytes and recorded SHA-256 did not change.

## Canonical inventory

- `zone1970.tab` bytes: 17,596
- `zone1970.tab` SHA-256: `77b5e45415fa684fcc42de3421a6b0f15cc9b2c137f258083850346e8f76eea8`
- non-comment rows: 312
- unique source-order zones: 312
- appended control: `Etc/UTC`
- final zone count: 313
- inventory serialization: UTF-8, one zone per line, final LF
- inventory SHA-256: `053b3988df8da3276ba63928fab3a1e6b1e9e625d0fa13d16b6f423edc51b582`
- missing compiled canonical zones: 0
- canonical files without `TZif` magic: 0

No alias or compatibility link was added to the primary denominator.

## Frozen parser fixtures

Fifteen targeted expectations were frozen before reader implementation. They cover:

- no-transition `Etc/UTC`;
- conventional one-hour forward and backward New York transitions;
- Lord Howe ±30-minute shifts;
- Apia and Kwajalein +24-hour discontinuities;
- Lisbon zero-offset abbreviation/DST-flag change;
- Dublin historical type and negative-DST semantics;
- Kathmandu +15-minute shift;
- Troll ±2-hour shifts;
- pre-2000 Chatham positive 45-minute-base behavior;
- year-2000 St Johns negative half-hour-base behavior;
- Eucla positive quarter-hour-base behavior;
- exact POSIX footer expectations for UTC, New York, and Lord Howe.

The fixture JSON uncompressed SHA-256 is `a3b08a49f5d3955f0015e67d58f705a68dadb7cc07ed1b499ff13381290786d9`. Regenerating the targeted `zdump` evidence and JSON produced the same digest.

`zdump` is frozen only as secondary fixture evidence. It is not the full-corpus oracle.

## Protected sequencing check

Cycle 1 did not:

- implement the independent TZif reader;
- generate or inspect the complete transition manifest;
- invoke Python `zoneinfo` on the formal corpus;
- run H1, H2, or H3;
- substitute host zone data;
- change the release, inventory, date range, hypotheses, criteria, or witness semantics;
- contact outsiders or file an external report;
- begin Cycle 2.

Protected sequencing remains intact.

## Verification limitations

- A detached IANA signature was not supplied or verified; archive identity relies on exact official size and SHA-512.
- The output directories were execution-local and are not committed. Their complete deterministic projection is persisted in compressed/base64 form.
- The fixtures are targeted hand-audited expectations, not proof that a future parser is correct on the complete corpus.
- No fresh checkout or full-repository regression was performed; this cycle created study metadata and generated data artifacts but no project runtime code.

## Disposition

Cycle 1 setup gates passed. Study 005 remains active at **1 of maximum 4 cycles**.

The next highest-value work is Cycle 2: implement the independent standard-library-only TZif reader, enforce malformed-input rejection, pass all 15 frozen fixtures with at most one bounded correction, and only then freeze the complete transition manifest.
