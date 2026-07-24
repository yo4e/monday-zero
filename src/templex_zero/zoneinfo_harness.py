"""Frozen public-API zoneinfo harness for TEMPLEX/0 Study 005 Cycle 3."""
from __future__ import annotations

import calendar
from datetime import UTC, datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any, Iterable
import zoneinfo

START = 0
END = 4_102_444_800
UTC_WITNESS_CODES = {"t_minus_1": 0, "at_transition": 1, "t_plus_1": 2, "left_midpoint": 3, "right_midpoint": 4}
REPEATED_SAMPLE_CODES = {"first": 0, "midpoint": 1, "last": 2}
GAP_SAMPLE_CODES = {"first_gap": 0, "midpoint_gap": 1, "last_gap": 2, "before_gap": 3, "after_gap": 4}


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def prepare_isolation(tzdir: Path) -> dict[str, Any]:
    before = list(zoneinfo.TZPATH)
    zoneinfo.ZoneInfo.clear_cache()
    zoneinfo.reset_tzpath([str(tzdir.resolve())])
    after = list(zoneinfo.TZPATH)
    expected = [str(tzdir.resolve())]
    if after != expected:
        raise RuntimeError(f"zoneinfo TZPATH isolation failed: {after!r} != {expected!r}")
    return {
        "python_executable": sys.executable,
        "python_implementation": sys.implementation.name,
        "python_version": sys.version,
        "no_site": int(sys.flags.no_site),
        "tzdata_spec_present": importlib.util.find_spec("tzdata") is not None,
        "tzpath_before": before,
        "tzpath_after": after,
    }


def wall_epoch(value: datetime) -> int:
    naive = value.replace(tzinfo=None)
    return calendar.timegm((naive.year, naive.month, naive.day, naive.hour, naive.minute, naive.second))


def naive_from_wall_epoch(value: int) -> datetime:
    return datetime.fromtimestamp(value, UTC).replace(tzinfo=None)


def retained_positions(parsed: Any, start: int = START, end: int = END) -> list[int]:
    return [i for i, item in enumerate(parsed.transitions) if start <= item.timestamp < end]


def utc_witnesses(parsed: Any, position: int, retained: list[int], retained_index: int, start: int = START, end: int = END) -> list[tuple[int, int]]:
    """Return labeled UTC witnesses without extrapolating a final explicit interval through footer rules.

    Midpoints use the inclusive integer-second interval. The right midpoint is
    omitted for the final retained explicit transition because the study excludes
    synthesized footer transitions and therefore has no represented stable
    endpoint after that transition.
    """
    t = parsed.transitions[position].timestamp
    out: list[tuple[int, int]] = []
    if t - 1 >= start:
        out.append((UTC_WITNESS_CODES["t_minus_1"], t - 1))
    if start <= t < end:
        out.append((UTC_WITNESS_CODES["at_transition"], t))
    if t + 1 < end:
        out.append((UTC_WITNESS_CODES["t_plus_1"], t + 1))
    left_start = start if retained_index == 0 else parsed.transitions[retained[retained_index - 1]].timestamp
    if left_start <= t - 1:
        out.append((UTC_WITNESS_CODES["left_midpoint"], (left_start + t - 1) // 2))
    if retained_index + 1 < len(retained):
        next_t = parsed.transitions[retained[retained_index + 1]].timestamp
        if t <= next_t - 1:
            out.append((UTC_WITNESS_CODES["right_midpoint"], (t + next_t - 1) // 2))
    return out


def projection_record(zone_key: str, transition_ts: int, witness_code: int, utc_ts: int, expected: Any, observed_zone: zoneinfo.ZoneInfo) -> list[Any]:
    observed = datetime.fromtimestamp(utc_ts, UTC).astimezone(observed_zone)
    observed_offset = int(observed.utcoffset().total_seconds())
    dst_value = observed.dst()
    observed_dst = None if dst_value is None else int(dst_value.total_seconds())
    observed_isdst = int(bool(observed_dst))
    observed_abbr = observed.tzname()
    expected_wall = utc_ts + expected.utoff
    observed_wall = wall_epoch(observed)
    mismatch = 0
    if observed_offset != expected.utoff:
        mismatch |= 1
    if observed_isdst != int(expected.isdst):
        mismatch |= 2
    if observed_abbr != expected.abbreviation:
        mismatch |= 4
    if observed_wall != expected_wall:
        mismatch |= 8
    return [zone_key, transition_ts, witness_code, utc_ts, expected.utoff, observed_offset, int(expected.isdst), observed_dst, observed_isdst, expected.abbreviation, observed_abbr, expected_wall, observed_wall, observed.fold, mismatch]


def repeated_wall_samples(transition_ts: int, pre_offset: int, post_offset: int) -> list[tuple[int, int]]:
    if post_offset >= pre_offset:
        raise ValueError("not a backward transition")
    first = transition_ts + post_offset
    last = transition_ts + pre_offset - 1
    midpoint = (first + last) // 2
    return [(REPEATED_SAMPLE_CODES["first"], first), (REPEATED_SAMPLE_CODES["midpoint"], midpoint), (REPEATED_SAMPLE_CODES["last"], last)]


def repeated_record(zone_key: str, transition_ts: int, sample_code: int, wall_ts: int, pre_offset: int, post_offset: int, observed_zone: zoneinfo.ZoneInfo) -> list[Any]:
    wall = naive_from_wall_epoch(wall_ts)
    earlier_utc = wall_ts - pre_offset
    later_utc = wall_ts - post_offset
    earlier = datetime.fromtimestamp(earlier_utc, UTC).astimezone(observed_zone)
    later = datetime.fromtimestamp(later_utc, UTC).astimezone(observed_zone)
    fold0_utc = int(wall.replace(tzinfo=observed_zone, fold=0).astimezone(UTC).timestamp())
    fold1_utc = int(wall.replace(tzinfo=observed_zone, fold=1).astimezone(UTC).timestamp())
    earlier_wall = wall_epoch(earlier)
    later_wall = wall_epoch(later)
    mismatch = 0
    if earlier_wall != wall_ts or later_wall != wall_ts:
        mismatch |= 1
    if earlier.fold != 0:
        mismatch |= 2
    if later.fold != 1:
        mismatch |= 4
    if fold0_utc != earlier_utc:
        mismatch |= 8
    if fold1_utc != later_utc:
        mismatch |= 16
    return [zone_key, transition_ts, sample_code, wall_ts, pre_offset, post_offset, earlier_utc, later_utc, earlier_wall, later_wall, earlier.fold, later.fold, fold0_utc, fold1_utc, mismatch]


def gap_wall_samples(transition_ts: int, pre_offset: int, post_offset: int) -> list[tuple[int, int, int]]:
    if post_offset <= pre_offset:
        raise ValueError("not a forward transition")
    first = transition_ts + pre_offset
    last = transition_ts + post_offset - 1
    midpoint = (first + last) // 2
    return [
        (GAP_SAMPLE_CODES["first_gap"], first, 0),
        (GAP_SAMPLE_CODES["midpoint_gap"], midpoint, 0),
        (GAP_SAMPLE_CODES["last_gap"], last, 0),
        (GAP_SAMPLE_CODES["before_gap"], first - 1, 1),
        (GAP_SAMPLE_CODES["after_gap"], last + 1, 1),
    ]


def validate_wall(wall: datetime, observed_zone: zoneinfo.ZoneInfo) -> tuple[int, list[list[Any]]]:
    attempts: list[list[Any]] = []
    any_valid = False
    target_wall = wall_epoch(wall)
    for fold in (0, 1):
        aware = wall.replace(tzinfo=observed_zone, fold=fold)
        utc_value = int(aware.astimezone(UTC).timestamp())
        back = datetime.fromtimestamp(utc_value, UTC).astimezone(observed_zone)
        back_wall = wall_epoch(back)
        valid = back_wall == target_wall and back.fold == fold
        attempts.append([fold, utc_value, back_wall, back.fold, int(valid)])
        any_valid = any_valid or valid
    return int(any_valid), attempts


def gap_record(zone_key: str, transition_ts: int, sample_code: int, wall_ts: int, expected_valid: int, observed_zone: zoneinfo.ZoneInfo) -> list[Any]:
    observed_valid, attempts = validate_wall(naive_from_wall_epoch(wall_ts), observed_zone)
    mismatch = int(observed_valid != expected_valid)
    return [zone_key, transition_ts, sample_code, wall_ts, expected_valid, observed_valid, attempts[0], attempts[1], mismatch]


def verify_manifest_row(row: list[Any], columns: list[str], tzdir: Path, parsed: Any) -> None:
    item = dict(zip(columns, row))
    path = tzdir / item["zone"]
    data = path.read_bytes()
    if len(data) != item["file_bytes"] or sha256(data) != item["file_sha256"]:
        raise RuntimeError(f"file identity mismatch for {item['zone']}")
    observed_types = [[x.utoff, int(x.isdst), x.abbreviation, x.abbreviation_index, None if x.is_standard is None else int(x.is_standard), None if x.is_ut is None else int(x.is_ut)] for x in parsed.local_time_types]
    observed_transitions = [[x.timestamp, x.type_index] for x in parsed.transitions if START <= x.timestamp < END]
    if observed_types != item["local_time_types"]:
        raise RuntimeError(f"type table mismatch for {item['zone']}")
    if observed_transitions != item["retained_transitions"]:
        raise RuntimeError(f"transition list mismatch for {item['zone']}")
