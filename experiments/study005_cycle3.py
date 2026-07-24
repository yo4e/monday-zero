"""Study 005 Cycle 3 isolated zoneinfo formal execution."""
from __future__ import annotations

import argparse
from collections import Counter
import json
import lzma
from pathlib import Path
import platform
import sys
from typing import Any
import zoneinfo

from templex_zero.tzif_reader import read_tzif
from templex_zero.zoneinfo_harness import (
    END, START, canonical_json, gap_record, gap_wall_samples, prepare_isolation,
    projection_record, repeated_record, repeated_wall_samples, retained_positions,
    sha256, utc_witnesses, verify_manifest_row,
)

EXPECTED_MANIFEST_SHA256 = "11b154ad96d5dbe74494f303739164489953c8cb857757703c3bac84aae6bdf4"


def run(tzdir: Path, manifest_path: Path, formal: bool, target_zones: set[str] | None) -> tuple[bytes, bytes, bytes]:
    manifest_bytes = manifest_path.read_bytes()
    if sha256(manifest_bytes) != EXPECTED_MANIFEST_SHA256:
        raise RuntimeError("frozen transition manifest identity mismatch")
    manifest = json.loads(manifest_bytes)
    if manifest["date_interval"] != [START, END] or manifest["source_release"] != "2026c":
        raise RuntimeError("frozen manifest domain mismatch")

    isolation = prepare_isolation(tzdir)
    if formal:
        if not sys.flags.no_site:
            raise RuntimeError("formal execution requires python -S")
        if isolation["tzdata_spec_present"]:
            raise RuntimeError("formal execution exposed a third-party tzdata package")
        if isolation["tzpath_before"]:
            raise RuntimeError("formal execution must start with empty TZPATH before reset")

    try:
        zoneinfo.ZoneInfo("TEMPLEX/DefinitelyMissing")
    except zoneinfo.ZoneInfoNotFoundError:
        missing_key_rejected = True
    else:
        missing_key_rejected = False
        raise RuntimeError("missing isolation key unexpectedly resolved")

    columns = manifest["columns"]
    all_zone_names = [row[0] for row in manifest["zones"]]
    selected_rows = manifest["zones"] if target_zones is None else [row for row in manifest["zones"] if row[0] in target_zones]
    if formal and len(selected_rows) != len(manifest["zones"]):
        raise RuntimeError("formal execution must include the full frozen zone inventory")

    # The compact Cycle 2 manifest omits the pre-type index for the first retained
    # transition. The already-frozen reader and exact file identity provide that
    # context without changing the manifest or consulting Python outcomes.
    nonselfcontained_first_pretype = 0
    isolation_loaded = 0
    h1_rows: list[list[Any]] = []
    h2_rows: list[list[Any]] = []
    h3_rows: list[list[Any]] = []
    mismatch_rows: list[list[Any]] = []
    h1_masks: Counter[int] = Counter()
    h2_masks: Counter[int] = Counter()
    h3_masks: Counter[int] = Counter()

    zone_index = {name: i for i, name in enumerate(all_zone_names)}
    for row in selected_rows:
        item = dict(zip(columns, row))
        name = item["zone"]
        zi = zone_index[name]
        parsed = read_tzif(tzdir / name)
        verify_manifest_row(row, columns, tzdir, parsed)
        observed_zone = zoneinfo.ZoneInfo(name)
        isolation_loaded += 1
        retained = retained_positions(parsed)
        if retained:
            first_pos = retained[0]
            first_pre = 0 if first_pos == 0 else parsed.transitions[first_pos - 1].type_index
            if first_pre != 0:
                nonselfcontained_first_pretype += 1

        for retained_index, position in enumerate(retained):
            transition = parsed.transitions[position]
            pre_index = 0 if position == 0 else parsed.transitions[position - 1].type_index
            post_index = transition.type_index
            pre = parsed.local_time_types[pre_index]
            post = parsed.local_time_types[post_index]
            delta = post.utoff - pre.utoff

            for witness_code, utc_ts in utc_witnesses(parsed, position, retained, retained_index):
                rec = projection_record(zi, transition.timestamp, witness_code, utc_ts, parsed.type_at(utc_ts), observed_zone)
                h1_rows.append(rec)
                h1_masks[rec[-1]] += 1
                if rec[-1]:
                    mismatch_rows.append([1] + rec)

            if delta < 0:
                for sample_code, wall_ts in repeated_wall_samples(transition.timestamp, pre.utoff, post.utoff):
                    rec = repeated_record(zi, transition.timestamp, sample_code, wall_ts, pre.utoff, post.utoff, observed_zone)
                    h2_rows.append(rec)
                    h2_masks[rec[-1]] += 1
                    if rec[-1]:
                        mismatch_rows.append([2] + rec)
            elif delta > 0:
                for sample_code, wall_ts, expected_valid in gap_wall_samples(transition.timestamp, pre.utoff, post.utoff):
                    rec = gap_record(zi, transition.timestamp, sample_code, wall_ts, expected_valid, observed_zone)
                    h3_rows.append(rec)
                    h3_masks[rec[-1]] += 1
                    if rec[-1]:
                        mismatch_rows.append([3] + rec)

    result = {
        "environment": {
            **isolation,
            "platform": platform.platform(),
            "missing_key_rejected": int(missing_key_rejected),
            "formal": int(formal),
        },
        "h1": {
            "columns": ["zone_index", "transition_timestamp", "witness_code", "utc_timestamp", "expected_offset", "observed_offset", "expected_isdst", "observed_dst_seconds", "observed_isdst", "expected_abbreviation", "observed_abbreviation", "expected_wall_epoch", "observed_wall_epoch", "observed_fold", "mismatch_mask"],
            "rows": h1_rows,
        },
        "h2": {
            "columns": ["zone_index", "transition_timestamp", "sample_code", "wall_epoch", "pre_offset", "post_offset", "earlier_utc", "later_utc", "earlier_observed_wall", "later_observed_wall", "earlier_fold", "later_fold", "fold0_roundtrip_utc", "fold1_roundtrip_utc", "mismatch_mask"],
            "rows": h2_rows,
        },
        "h3": {
            "attempt_columns": ["fold", "utc_timestamp", "roundtrip_wall_epoch", "roundtrip_fold", "valid"],
            "columns": ["zone_index", "transition_timestamp", "sample_code", "wall_epoch", "expected_valid", "observed_valid", "fold0_attempt", "fold1_attempt", "mismatch_mask"],
            "rows": h3_rows,
        },
        "manifest": {"bytes": len(manifest_bytes), "sha256": sha256(manifest_bytes)},
        "reference_context": {
            "first_retained_pretype_not_zero_zones": nonselfcontained_first_pretype,
            "source": "frozen reader plus exact TZif file identity; manifest fields verified before each zone",
        },
        "schema": "templex-zero.study005.zoneinfo-formal-results.v1",
        "zones": all_zone_names,
    }
    raw = canonical_json(result)
    mismatches = canonical_json({
        "columns": ["hypothesis", "hypothesis_record_fields"],
        "rows": mismatch_rows,
        "schema": "templex-zero.study005.zoneinfo-mismatches.v1",
    })
    summary = canonical_json({
        "formal": int(formal),
        "h1_mask_counts": {str(k): v for k, v in sorted(h1_masks.items())},
        "h1_records": len(h1_rows),
        "h2_mask_counts": {str(k): v for k, v in sorted(h2_masks.items())},
        "h2_records": len(h2_rows),
        "h3_mask_counts": {str(k): v for k, v in sorted(h3_masks.items())},
        "h3_records": len(h3_rows),
        "isolation_loaded_zones": isolation_loaded,
        "manifest_sha256": sha256(manifest_bytes),
        "mismatch_records": len(mismatch_rows),
        "reference_first_pretype_sidecar_zones": nonselfcontained_first_pretype,
        "result_bytes": len(raw),
        "result_sha256": sha256(raw),
        "schema": "templex-zero.study005.zoneinfo-formal-summary.v1",
        "zone_count": len(selected_rows),
    })
    return raw, mismatches, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tzdir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--formal", action="store_true")
    parser.add_argument("--target-zone", action="append", default=[])
    args = parser.parse_args()
    targets = None if not args.target_zone else set(args.target_zone)
    raw, mismatches, summary = run(args.tzdir, args.manifest, args.formal, targets)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "zoneinfo_formal_results_v1.json.xz").write_bytes(
        lzma.compress(raw, format=lzma.FORMAT_XZ, preset=9 | lzma.PRESET_EXTREME)
    )
    (args.output_dir / "zoneinfo_mismatches_v1.json.xz").write_bytes(
        lzma.compress(mismatches, format=lzma.FORMAT_XZ, preset=9 | lzma.PRESET_EXTREME)
    )
    (args.output_dir / "zoneinfo_formal_summary_v1.json").write_bytes(summary)


if __name__ == "__main__":
    main()
