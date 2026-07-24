"""Independent, standard-library-only TZif parser for TEMPLEX/0 Study 005.

This module intentionally does not import ``zoneinfo`` or CPython parser
internals. It implements the binary structure specified by the TZif RFCs and
uses time type 0 for timestamps before the first transition.
"""

from __future__ import annotations

from bisect import bisect_right
from dataclasses import dataclass
import json
from pathlib import Path
import struct
from typing import Final, Iterable

_HEADER_SIZE: Final = 44
_MAGIC: Final = b"TZif"
_SUPPORTED_VERSION_BYTES: Final = {b"\x00", b"2", b"3", b"4"}
_MIN_UTOFF: Final = -89_999
_MAX_UTOFF: Final = 93_599


class TZifError(ValueError):
    """Raised when TZif bytes violate the parser's accepted format."""


@dataclass(frozen=True, slots=True)
class LocalTimeType:
    index: int
    utoff: int
    isdst: bool
    abbreviation: str
    abbreviation_index: int
    is_standard: bool | None
    is_ut: bool | None

    def canonical_dict(self) -> dict[str, object]:
        return {
            "abbreviation": self.abbreviation,
            "abbreviation_index": self.abbreviation_index,
            "index": self.index,
            "isdst": int(self.isdst),
            "is_standard": None if self.is_standard is None else int(self.is_standard),
            "is_ut": None if self.is_ut is None else int(self.is_ut),
            "utoff": self.utoff,
        }


@dataclass(frozen=True, slots=True)
class Transition:
    timestamp: int
    type_index: int

    def canonical_dict(self) -> dict[str, int]:
        return {"timestamp": self.timestamp, "type_index": self.type_index}


@dataclass(frozen=True, slots=True)
class TZifData:
    version: str
    transitions: tuple[Transition, ...]
    local_time_types: tuple[LocalTimeType, ...]
    footer: str | None
    leap_seconds: tuple[tuple[int, int], ...]
    pre_first_type_index: int = 0

    def __post_init__(self) -> None:
        if not self.local_time_types:
            raise TZifError("TZif data must contain at least one local time type")
        if self.pre_first_type_index != 0:
            raise TZifError("Study 005 freezes pre-first-transition time type to index 0")

    @property
    def transition_timestamps(self) -> tuple[int, ...]:
        return tuple(item.timestamp for item in self.transitions)

    def type_at(self, timestamp: int) -> LocalTimeType:
        """Return the local time type in force at a POSIX timestamp."""
        position = bisect_right(self.transition_timestamps, timestamp) - 1
        if position < 0:
            return self.local_time_types[self.pre_first_type_index]
        return self.local_time_types[self.transitions[position].type_index]

    def transition_at(self, timestamp: int) -> tuple[LocalTimeType, LocalTimeType]:
        """Return the pre/post types for an exact explicit transition."""
        timestamps = self.transition_timestamps
        position = bisect_right(timestamps, timestamp) - 1
        if position < 0 or timestamps[position] != timestamp:
            raise KeyError(f"no explicit transition at {timestamp}")
        pre_index = (
            self.pre_first_type_index
            if position == 0
            else self.transitions[position - 1].type_index
        )
        post_index = self.transitions[position].type_index
        return self.local_time_types[pre_index], self.local_time_types[post_index]

    def canonical_bytes(self) -> bytes:
        payload = {
            "footer": self.footer,
            "leap_seconds": [
                {"correction": correction, "timestamp": timestamp}
                for timestamp, correction in self.leap_seconds
            ],
            "local_time_types": [item.canonical_dict() for item in self.local_time_types],
            "pre_first_type_index": self.pre_first_type_index,
            "schema": "templex-zero.study005.tzif-canonical.v1",
            "transitions": [item.canonical_dict() for item in self.transitions],
            "version": self.version,
        }
        return (
            json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
            + "\n"
        ).encode("ascii")


@dataclass(frozen=True, slots=True)
class _Header:
    version_byte: bytes
    isutcnt: int
    isstdcnt: int
    leapcnt: int
    timecnt: int
    typecnt: int
    charcnt: int


@dataclass(frozen=True, slots=True)
class _Block:
    transitions: tuple[Transition, ...]
    local_time_types: tuple[LocalTimeType, ...]
    leap_seconds: tuple[tuple[int, int], ...]
    end_offset: int


def _take(data: bytes, offset: int, length: int, label: str) -> tuple[bytes, int]:
    end = offset + length
    if length < 0 or end > len(data):
        raise TZifError(f"truncated {label}")
    return data[offset:end], end


def _parse_header(data: bytes, offset: int) -> tuple[_Header, int]:
    raw, offset = _take(data, offset, _HEADER_SIZE, "TZif header")
    if raw[:4] != _MAGIC:
        raise TZifError("invalid TZif magic")
    version_byte = raw[4:5]
    if version_byte not in _SUPPORTED_VERSION_BYTES:
        display = version_byte.hex() or "empty"
        raise TZifError(f"unsupported TZif version byte: {display}")
    if raw[5:20] != b"\x00" * 15:
        raise TZifError("nonzero reserved TZif header bytes")
    counts = struct.unpack(">6I", raw[20:44])
    header = _Header(version_byte, *counts)
    if header.typecnt == 0:
        raise TZifError("typecnt must be positive")
    if header.charcnt == 0:
        raise TZifError("charcnt must be positive")
    if header.isstdcnt not in (0, header.typecnt):
        raise TZifError("isstdcnt must be zero or equal typecnt")
    if header.isutcnt not in (0, header.typecnt):
        raise TZifError("isutcnt must be zero or equal typecnt")
    return header, offset


def _decode_abbreviation(table: bytes, index: int) -> str:
    if index >= len(table):
        raise TZifError("abbreviation index is outside the abbreviation table")
    terminator = table.find(b"\x00", index)
    if terminator < 0:
        raise TZifError("abbreviation is not NUL-terminated")
    try:
        return table[index:terminator].decode("ascii")
    except UnicodeDecodeError as exc:
        raise TZifError("abbreviation is not ASCII") from exc


def _parse_block(data: bytes, offset: int, header: _Header, time_size: int) -> _Block:
    if time_size not in (4, 8):
        raise AssertionError("invalid internal time size")

    times_raw, offset = _take(
        data, offset, header.timecnt * time_size, "transition time array"
    )
    if header.timecnt:
        code = "i" if time_size == 4 else "q"
        timestamps = struct.unpack(f">{header.timecnt}{code}", times_raw)
        if any(left >= right for left, right in zip(timestamps, timestamps[1:])):
            raise TZifError("transition timestamps are not strictly increasing")
    else:
        timestamps = ()

    indexes_raw, offset = _take(
        data, offset, header.timecnt, "transition type index array"
    )
    indexes = tuple(indexes_raw)
    if any(index >= header.typecnt for index in indexes):
        raise TZifError("transition type index is outside local time type array")

    type_raw, offset = _take(
        data, offset, header.typecnt * 6, "local time type records"
    )
    raw_types: list[tuple[int, int, int]] = []
    for position in range(header.typecnt):
        start = position * 6
        utoff, isdst, abbreviation_index = struct.unpack(">iBB", type_raw[start : start + 6])
        if not (_MIN_UTOFF <= utoff <= _MAX_UTOFF):
            raise TZifError(f"UTC offset outside TZif range at type {position}")
        if isdst not in (0, 1):
            raise TZifError(f"invalid DST flag at type {position}")
        if abbreviation_index >= header.charcnt:
            raise TZifError(f"impossible abbreviation index at type {position}")
        raw_types.append((utoff, isdst, abbreviation_index))

    abbreviations, offset = _take(
        data, offset, header.charcnt, "abbreviation character table"
    )

    leap_raw, offset = _take(
        data,
        offset,
        header.leapcnt * (time_size + 4),
        "leap-second records",
    )
    leap_seconds: list[tuple[int, int]] = []
    leap_code = "i" if time_size == 4 else "q"
    previous_leap: int | None = None
    previous_correction = 0
    record_size = time_size + 4
    for position in range(header.leapcnt):
        start = position * record_size
        timestamp = struct.unpack(">" + leap_code, leap_raw[start : start + time_size])[0]
        correction = struct.unpack(">i", leap_raw[start + time_size : start + record_size])[0]
        if previous_leap is not None and timestamp <= previous_leap:
            raise TZifError("leap-second timestamps are not strictly increasing")
        if abs(correction - previous_correction) != 1:
            raise TZifError("leap-second correction does not change by one")
        leap_seconds.append((timestamp, correction))
        previous_leap = timestamp
        previous_correction = correction

    isstd_raw, offset = _take(data, offset, header.isstdcnt, "standard/wall indicators")
    isut_raw, offset = _take(data, offset, header.isutcnt, "UT/local indicators")
    if any(value not in (0, 1) for value in isstd_raw):
        raise TZifError("invalid standard/wall indicator")
    if any(value not in (0, 1) for value in isut_raw):
        raise TZifError("invalid UT/local indicator")
    if header.isutcnt and header.isstdcnt:
        for is_ut, is_standard in zip(isut_raw, isstd_raw):
            if is_ut and not is_standard:
                raise TZifError("UT indicator requires standard indicator")

    local_types: list[LocalTimeType] = []
    for index, (utoff, isdst, abbreviation_index) in enumerate(raw_types):
        local_types.append(
            LocalTimeType(
                index=index,
                utoff=utoff,
                isdst=bool(isdst),
                abbreviation=_decode_abbreviation(abbreviations, abbreviation_index),
                abbreviation_index=abbreviation_index,
                is_standard=None if not header.isstdcnt else bool(isstd_raw[index]),
                is_ut=None if not header.isutcnt else bool(isut_raw[index]),
            )
        )

    transitions = tuple(
        Transition(timestamp=timestamp, type_index=type_index)
        for timestamp, type_index in zip(timestamps, indexes)
    )
    return _Block(transitions, tuple(local_types), tuple(leap_seconds), offset)


def parse_tzif(data: bytes) -> TZifData:
    """Parse one complete TZif file from bytes."""
    first_header, offset = _parse_header(data, 0)
    first_block = _parse_block(data, offset, first_header, 4)

    if first_header.version_byte == b"\x00":
        if first_block.end_offset != len(data):
            raise TZifError("trailing bytes after TZif v1 data block")
        return TZifData(
            version="1",
            transitions=first_block.transitions,
            local_time_types=first_block.local_time_types,
            footer=None,
            leap_seconds=first_block.leap_seconds,
        )

    second_header, offset = _parse_header(data, first_block.end_offset)
    if second_header.version_byte != first_header.version_byte:
        raise TZifError("inconsistent version bytes between TZif headers")
    second_block = _parse_block(data, offset, second_header, 8)

    footer_raw = data[second_block.end_offset :]
    if len(footer_raw) < 2 or not footer_raw.startswith(b"\n") or not footer_raw.endswith(b"\n"):
        raise TZifError("TZif v2+ footer must be enclosed by newline bytes")
    footer_payload = footer_raw[1:-1]
    if b"\x00" in footer_payload or b"\n" in footer_payload:
        raise TZifError("invalid byte in TZif footer")
    try:
        footer_text = footer_payload.decode("ascii")
    except UnicodeDecodeError as exc:
        raise TZifError("TZif footer is not ASCII") from exc

    return TZifData(
        version=first_header.version_byte.decode("ascii"),
        transitions=second_block.transitions,
        local_time_types=second_block.local_time_types,
        footer=footer_text,
        leap_seconds=second_block.leap_seconds,
    )


def read_tzif(path: str | Path) -> TZifData:
    return parse_tzif(Path(path).read_bytes())


def canonical_transition_records(
    zone: str,
    parsed: TZifData,
    start: int,
    end: int,
) -> Iterable[dict[str, object]]:
    """Yield deterministic explicit-transition records in ``[start, end)``."""
    for position, transition in enumerate(parsed.transitions):
        if not (start <= transition.timestamp < end):
            continue
        pre_index = (
            parsed.pre_first_type_index
            if position == 0
            else parsed.transitions[position - 1].type_index
        )
        post_index = transition.type_index
        pre = parsed.local_time_types[pre_index]
        post = parsed.local_time_types[post_index]
        delta = post.utoff - pre.utoff
        yield {
            "class": "backward" if delta < 0 else "forward" if delta > 0 else "zero",
            "delta": delta,
            "post": {
                "abbreviation": post.abbreviation,
                "isdst": int(post.isdst),
                "type_index": post_index,
                "utoff": post.utoff,
            },
            "pre": {
                "abbreviation": pre.abbreviation,
                "isdst": int(pre.isdst),
                "type_index": pre_index,
                "utoff": pre.utoff,
            },
            "timestamp": transition.timestamp,
            "zone": zone,
        }
