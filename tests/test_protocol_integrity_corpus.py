from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import pytest

from templex_zero.protocol_integrity import canonical_json_bytes, canonical_sha256, corpus_bundle_files, generate_corpus
from templex_zero.protocol_integrity.corpus import MUTATION_OPERATORS
from templex_zero.protocol_integrity.schema import Event, EventKind, TraceFixture

DATA_DIR = Path("research/studies/003-protocol-integrity/data/synthetic_corpus_v1")


def test_frozen_corpus_arithmetic() -> None:
    corpus = generate_corpus()
    verdicts = Counter(trace.expected.verdict.value for trace in corpus.traces)
    categories = Counter(trace.category for trace in corpus.traces)
    assert len(corpus.traces) == 36
    assert verdicts == {"valid": 10, "invalid": 26}
    assert categories == {
        "minimal-valid": 6,
        "minimal-invalid": 6,
        "composite-valid": 4,
        "composite-mutant": 20,
    }
    assert sum(len(trace.events) for trace in corpus.traces) <= 1_440


def test_mutation_inventory_and_expected_first_violations() -> None:
    corpus = generate_corpus()
    mutants = [trace for trace in corpus.traces if trace.mutation_operator]
    assert Counter(trace.mutation_operator for trace in mutants) == {
        operator: 4 for operator in MUTATION_OPERATORS
    }
    expected = {
        "prerequisite-omission": (4, "D1"),
        "adjacent-dependency-inversion": (2, "D3"),
        "unauthorized-insertion": (8, "D2"),
        "cap-violation": (4, "D3"),
        "undisclosed-correction": (16, "D4"),
    }
    for trace in mutants:
        assert (
            trace.expected.first_violation_index,
            trace.expected.dependency_class.value,
        ) == expected[trace.mutation_operator]


def test_minimal_pairs_cover_all_dependency_classes() -> None:
    corpus = generate_corpus()
    minimal_invalid = [trace for trace in corpus.traces if trace.category == "minimal-invalid"]
    assert {trace.expected.dependency_class.value for trace in minimal_invalid} == {
        "D1", "D2", "D3", "D4", "D5", "D6"
    }
    for number in range(1, 7):
        assert {f"P{number}-V", f"P{number}-I"}.issubset(
            {trace.trace_id for trace in corpus.traces}
        )


def test_canonical_regeneration_is_byte_identical() -> None:
    first = canonical_json_bytes(generate_corpus())
    second = canonical_json_bytes(generate_corpus())
    assert first == second
    assert canonical_sha256(generate_corpus()) == canonical_sha256(generate_corpus())
    assert json.loads(first) == json.loads(second)


def test_checked_in_corpus_matches_generator() -> None:
    expected = corpus_bundle_files(generate_corpus())
    assert {path.name for path in DATA_DIR.iterdir()} == set(expected)
    for name, payload in expected.items():
        assert (DATA_DIR / name).read_bytes() == payload


def test_no_validator_outputs_or_historical_traces_are_present() -> None:
    payload = canonical_json_bytes(generate_corpus()).decode("utf-8")
    assert "actual_verdict" not in payload
    assert "oracle_verdict" not in payload
    assert "baseline_verdict" not in payload
    assert "H1-SPAN-FORMAL-VALID" not in payload
    assert "H3-STUDY002-SHALLOW-CONTAMINATED" not in payload


def test_event_indices_are_contiguous_and_limit_is_respected() -> None:
    for trace in generate_corpus().traces:
        assert [event.index for event in trace.events] == list(range(len(trace.events)))
        assert len(trace.events) <= 40


def test_schema_rejects_noncontiguous_indices() -> None:
    corpus = generate_corpus()
    source = corpus.traces[0]
    broken = list(source.events)
    broken[1] = Event(index=7, kind=EventKind.FREEZE_ARTIFACT, subject="a", digest="h1")
    with pytest.raises(ValueError, match="contiguous"):
        TraceFixture(
            trace_id="broken",
            category="test",
            contract=source.contract,
            events=tuple(broken),
            expected=source.expected,
        )
