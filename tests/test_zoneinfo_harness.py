from __future__ import annotations

from datetime import timezone
import json
import os
from pathlib import Path
import zoneinfo
import pytest

from templex_zero.zoneinfo_harness import (
    gap_record, gap_wall_samples, naive_from_wall_epoch, prepare_isolation,
    projection_record, repeated_record, repeated_wall_samples, retained_positions,
    utc_witnesses, validate_wall,
)
from templex_zero.tzif_reader import read_tzif

TZDIR_ENV = os.environ.get("STUDY005_TZDIR")
MANIFEST_ENV = os.environ.get("STUDY005_MANIFEST")


def test_witness_generation_conservative_final_interval() -> None:
    class Transition:
        def __init__(self, timestamp: int, type_index: int = 0) -> None:
            self.timestamp = timestamp
            self.type_index = type_index
    class Parsed:
        transitions = [Transition(100), Transition(200)]
    retained = [0, 1]
    assert utc_witnesses(Parsed, 0, retained, 0, start=0, end=300) == [
        (0, 99), (1, 100), (2, 101), (3, 49), (4, 149)
    ]
    assert utc_witnesses(Parsed, 1, retained, 1, start=0, end=300) == [
        (0, 199), (1, 200), (2, 201), (3, 149)
    ]


def test_sample_generators_do_not_assume_one_hour() -> None:
    assert repeated_wall_samples(1000, 1800, 0) == [(0, 1000), (1, 1899), (2, 2799)]
    assert gap_wall_samples(1000, 0, 1800) == [
        (0, 1000, 0), (1, 1899, 0), (2, 2799, 0), (3, 999, 1), (4, 2800, 1)
    ]


def test_fixed_offset_wall_validator() -> None:
    wall = naive_from_wall_epoch(123456)
    valid, attempts = validate_wall(wall, timezone.utc)
    assert valid == 1
    assert attempts[0][-1] == 1
    assert attempts[1][-1] == 0


def _integration_context() -> tuple[Path, dict]:
    if not TZDIR_ENV or not MANIFEST_ENV:
        pytest.skip("Study 005 compiled tree and manifest paths are not configured")
    tzdir = Path(TZDIR_ENV)
    prepare_isolation(tzdir)
    return tzdir, json.loads(Path(MANIFEST_ENV).read_bytes())


def _find_transition(tzdir: Path, zone: str, delta: int, after: int = 0):
    parsed = read_tzif(tzdir / zone)
    retained = retained_positions(parsed)
    for retained_index, position in enumerate(retained):
        transition = parsed.transitions[position]
        pre = parsed.local_time_types[0 if position == 0 else parsed.transitions[position - 1].type_index]
        post = parsed.local_time_types[transition.type_index]
        if post.utoff - pre.utoff == delta and transition.timestamp >= after:
            return parsed, retained, retained_index, position, pre, post
    raise AssertionError((zone, delta, after))


def test_new_york_projection_and_fold_fixture() -> None:
    tzdir, _ = _integration_context()
    parsed, retained, ri, position, pre, post = _find_transition(tzdir, "America/New_York", -3600, 1_600_000_000)
    observed_zone = zoneinfo.ZoneInfo("America/New_York")
    transition = parsed.transitions[position]
    for code, timestamp in utc_witnesses(parsed, position, retained, ri):
        assert projection_record(0, transition.timestamp, code, timestamp, parsed.type_at(timestamp), observed_zone)[-1] == 0
    for code, wall in repeated_wall_samples(transition.timestamp, pre.utoff, post.utoff):
        assert repeated_record(0, transition.timestamp, code, wall, pre.utoff, post.utoff, observed_zone)[-1] == 0


def test_lord_howe_half_hour_fold_fixture() -> None:
    tzdir, _ = _integration_context()
    parsed, _, _, position, pre, post = _find_transition(tzdir, "Australia/Lord_Howe", -1800, 1_500_000_000)
    observed_zone = zoneinfo.ZoneInfo("Australia/Lord_Howe")
    transition = parsed.transitions[position]
    for code, wall in repeated_wall_samples(transition.timestamp, pre.utoff, post.utoff):
        assert repeated_record(0, transition.timestamp, code, wall, pre.utoff, post.utoff, observed_zone)[-1] == 0


def test_new_york_gap_fixture() -> None:
    tzdir, _ = _integration_context()
    parsed, _, _, position, pre, post = _find_transition(tzdir, "America/New_York", 3600, 1_600_000_000)
    observed_zone = zoneinfo.ZoneInfo("America/New_York")
    transition = parsed.transitions[position]
    for code, wall, expected in gap_wall_samples(transition.timestamp, pre.utoff, post.utoff):
        assert gap_record(0, transition.timestamp, code, wall, expected, observed_zone)[-1] == 0


def test_apia_day_gap_fixture() -> None:
    tzdir, _ = _integration_context()
    parsed, _, _, position, pre, post = _find_transition(tzdir, "Pacific/Apia", 86400, 1_300_000_000)
    observed_zone = zoneinfo.ZoneInfo("Pacific/Apia")
    transition = parsed.transitions[position]
    for code, wall, expected in gap_wall_samples(transition.timestamp, pre.utoff, post.utoff):
        assert gap_record(0, transition.timestamp, code, wall, expected, observed_zone)[-1] == 0
