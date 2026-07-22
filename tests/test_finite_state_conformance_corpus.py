from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from templex_zero.finite_state_conformance.corpus import generate_corpus, validate_family
from templex_zero.finite_state_conformance.schema import (
    ACTIONS,
    FAMILIES,
    MUTATION_OPERATORS,
    STATE_SIZES,
)

BUNDLE = Path("research/studies/004-finite-state-conformance/data/corpus_v1.json")
MODELS_BUNDLE = Path("research/studies/004-finite-state-conformance/data/models_v1.json")


def _cell_differences(source, mutant):
    differences = []
    for state, (source_row, mutant_row) in enumerate(zip(source.transitions, mutant.transitions)):
        for action, (source_transition, mutant_transition) in enumerate(zip(source_row, mutant_row)):
            if source_transition != mutant_transition:
                differences.append((state, action, source_transition, mutant_transition))
    return differences


def test_frozen_inventory_and_cell_balance() -> None:
    corpus = generate_corpus()
    assert len(corpus.models) == 24
    assert len(corpus.mutants) == 144
    assert Counter((model.state_count, model.family) for model in corpus.models) == {
        (size, family): 4 for size in STATE_SIZES for family in FAMILIES
    }
    assert Counter(record.operator for record in corpus.mutants) == {
        operator: 24 for operator in MUTATION_OPERATORS
    }
    assert Counter(record.source_model_id for record in corpus.mutants) == {
        model.model_id: 6 for model in corpus.models
    }


def test_models_are_total_and_match_frozen_family_rules() -> None:
    for model in generate_corpus().models:
        validate_family(model)
        assert len(model.transitions) == model.state_count
        for row in model.transitions:
            assert len(row) == len(ACTIONS)
            assert all(0 <= transition.target < model.state_count for transition in row)


def test_model_and_mutant_ids_and_digests_are_unique() -> None:
    corpus = generate_corpus()
    assert len({model.model_id for model in corpus.models}) == 24
    assert len({model.digest for model in corpus.models}) == 24
    assert len({record.mutant_id for record in corpus.mutants}) == 144
    assert all(len(record.selection_digest) == 64 for record in corpus.mutants)
    by_id = {model.model_id: model for model in corpus.models}
    assert all(record.source_model_digest == by_id[record.source_model_id].digest for record in corpus.mutants)


def test_every_mutation_changes_structure_without_replacement() -> None:
    corpus = generate_corpus()
    by_id = {model.model_id: model for model in corpus.models}
    for record in corpus.mutants:
        source = by_id[record.source_model_id]
        differences = _cell_differences(source, record.model)
        assert differences
        if record.operator in {
            "transition-target-substitution",
            "output-label-substitution",
            "self-loop-injection",
        }:
            assert len(differences) == 1
        elif record.operator == "action-column-swap":
            assert len({state for state, *_ in differences}) == 1
            assert len(differences) == 2
        elif record.operator == "state-row-transplant":
            assert len({state for state, *_ in differences}) == 1
        elif record.operator == "paired-transition-mutation":
            assert len(differences) == 2
            assert len({state for state, *_ in differences}) == 2


def test_mutation_specific_fields_are_preserved() -> None:
    corpus = generate_corpus()
    by_id = {model.model_id: model for model in corpus.models}
    for record in corpus.mutants:
        source = by_id[record.source_model_id]
        differences = _cell_differences(source, record.model)
        if record.operator in {
            "transition-target-substitution",
            "self-loop-injection",
            "paired-transition-mutation",
        }:
            assert all(old.output == new.output for _, _, old, new in differences)
            assert all(old.target != new.target for _, _, old, new in differences)
        elif record.operator == "output-label-substitution":
            assert all(old.target == new.target for _, _, old, new in differences)
            assert all(old.output != new.output for _, _, old, new in differences)


def test_generation_is_byte_deterministic() -> None:
    first = generate_corpus()
    second = generate_corpus()
    assert first.to_bytes() == second.to_bytes()
    assert first.models_to_bytes() == second.models_to_bytes()
    assert first.payload_sha256 == second.payload_sha256
    assert first.model_payload_sha256 == second.model_payload_sha256


def test_checked_in_bundle_matches_regeneration() -> None:
    generated = generate_corpus()
    checked_in = BUNDLE.read_bytes()
    assert checked_in == generated.to_bytes()
    parsed = json.loads(checked_in)
    models_checked_in = MODELS_BUNDLE.read_bytes()
    assert models_checked_in == generated.models_to_bytes()
    models_parsed = json.loads(models_checked_in)
    assert models_parsed["payload_sha256"] == generated.model_payload_sha256
    assert parsed["models_bundle"]["payload_sha256"] == generated.model_payload_sha256
    assert parsed["counts"] == {
        "models": 24,
        "mutants": 144,
        "mutants_per_model": 6,
    }
    assert parsed["payload_sha256"] == generated.payload_sha256


def test_cycle_one_bundle_contains_no_oracle_or_benchmark_results() -> None:
    parsed = json.loads(generate_corpus().to_bytes())
    forbidden = {
        "equivalent",
        "distinguishable",
        "shortest_trace",
        "detected",
        "detection_rate",
        "oracle_result",
        "benchmark_result",
    }
    assert forbidden.isdisjoint(parsed.keys())
    text = json.dumps(parsed, sort_keys=True)
    assert '"equivalent"' not in text
    assert '"shortest_trace"' not in text
    assert '"detected"' not in text
