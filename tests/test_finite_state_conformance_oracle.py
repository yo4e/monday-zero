from __future__ import annotations

import ast
import json
from pathlib import Path

from templex_zero.finite_state_conformance.oracle import (
    exact_shortest_counterexample,
    model_from_dict,
)

FIXTURES = Path(
    "research/studies/004-finite-state-conformance/data/oracle_fixtures_v1.json"
)


def _fixture_data() -> list[dict]:
    data = json.loads(FIXTURES.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    assert data["action_order"] == ["a0", "a1", "a2"]
    assert len(data["fixtures"]) == 10
    return data["fixtures"]


def test_frozen_fixture_gate() -> None:
    for fixture in _fixture_data():
        reference = model_from_dict(fixture["reference"])
        implementation = model_from_dict(fixture["implementation"])
        result = exact_shortest_counterexample(reference, implementation)
        assert result.equivalent is fixture["expected_equivalent"], fixture["fixture_id"]
        expected = fixture["expected_shortest_trace"]
        assert result.shortest_trace == (
            None if expected is None else tuple(expected)
        ), fixture["fixture_id"]
        assert result.visited_pairs <= reference.state_count * implementation.state_count


def test_oracle_is_deterministic_on_frozen_fixtures() -> None:
    for fixture in _fixture_data():
        reference = model_from_dict(fixture["reference"])
        implementation = model_from_dict(fixture["implementation"])
        assert exact_shortest_counterexample(
            reference, implementation
        ) == exact_shortest_counterexample(reference, implementation)


def test_oracle_source_has_no_method_reducer_execution_or_corpus_import() -> None:
    path = (
        Path(__file__).parents[1]
        / "src"
        / "templex_zero"
        / "finite_state_conformance"
        / "oracle.py"
    )
    tree = ast.parse(path.read_text(encoding="utf-8"))
    imported: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module)
    forbidden_suffixes = ("methods", "reducer", "execution", "corpus")
    assert not any(name.endswith(forbidden_suffixes) for name in imported)
