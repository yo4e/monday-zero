# Study 005 — TZDB Transition Round-Trip Conformance

_Status: Active; Cycle 1 of maximum 4 completed._

Study 005 tests a version-pinned IANA tzdb 2026c transition corpus against an independently implemented TZif reader and an isolated Python `zoneinfo` harness.

## Current position

Cycle 1 activated the frozen protocol and completed source/permission preflight, two deterministic isolated compilations, canonical zone inventory freezing, and targeted parser-fixture freezing.

No independent TZif reader, complete transition manifest, Python comparison harness, formal corpus execution, or hypothesis result exists yet.

## Frozen artifacts

- `PROTOCOL.md` — active frozen protocol
- `CYCLE_1_ACTIVATION.md` — activation and verification audit
- `data/source_provenance_v1.json` — exact archive identity and permission metadata
- `data/compilation_summary_v1.json` — compiler, command, environment, and deterministic compilation summary
- `data/compiled_tree_projection_v1.tsv.gz.b64` — gzip/base64 encoded full 341-file path/size/SHA-256 projection
- `data/canonical_zone_identity_v1.json` — `zone1970.tab` and inventory identities
- `data/canonical_zones_v1.txt.gz.b64` — gzip/base64 encoded ordered 313-zone inventory
- `data/fixture_expectations_v1.json.gz.b64` — gzip/base64 encoded 15 frozen targeted fixture expectations
- `data/targeted_zdump_evidence_v1.txt.gz.b64` — gzip/base64 encoded targeted command output
- `data/artifact_digests_v1.json` — original uncompressed artifact digests

The `.gz.b64` files decode with base64 and then gzip. The uncompressed byte counts and SHA-256 identities are recorded in `artifact_digests_v1.json`.

## Next cycle

Cycle 2 may implement the original standard-library-only TZif reader, test it against all 15 frozen fixtures, use at most one bounded correction if needed, and freeze the complete transition manifest only after the fixture gate passes.