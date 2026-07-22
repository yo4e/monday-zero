"""Study 004 finite-state conformance corpus schema.

This module defines deterministic Mealy-machine and mutant records plus
canonical JSON serialization. It contains no testing method, reducer, oracle,
or observational-equivalence classification.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from typing import Any, Iterable

ACTIONS: tuple[str, ...] = ("a0", "a1", "a2")
OUTPUTS: tuple[str, ...] = ("o0", "o1", "o2")
FAMILIES: tuple[str, ...] = ("reset-chain", "clustered", "cyclic")
STATE_SIZES: tuple[int, ...] = (4, 8)
MUTATION_OPERATORS: tuple[str, ...] = (
    "transition-target-substitution",
    "output-label-substitution",
    "action-column-swap",
    "state-row-transplant",
    "self-loop-injection",
    "paired-transition-mutation",
)


def canonical_bytes(value: Any) -> bytes:
    """Return canonical UTF-8 JSON bytes with one trailing newline."""
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def sha256_hex(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


@dataclass(frozen=True)
class Transition:
    target: int
    output: str

    def __post_init__(self) -> None:
        if self.target < 0:
            raise ValueError("transition target must be non-negative")
        if self.output not in OUTPUTS:
            raise ValueError(f"unknown output label: {self.output}")

    def to_dict(self) -> dict[str, Any]:
        return {"target": self.target, "output": self.output}


@dataclass(frozen=True)
class MealyModel:
    model_id: str
    family: str
    state_count: int
    variant: int
    transitions: tuple[tuple[Transition, ...], ...]
    reset_state: int = 0

    def __post_init__(self) -> None:
        if not self.model_id:
            raise ValueError("model_id must be non-empty")
        if self.family not in FAMILIES:
            raise ValueError(f"unknown family: {self.family}")
        if self.state_count not in STATE_SIZES:
            raise ValueError(f"unsupported state count: {self.state_count}")
        if self.variant not in (1, 2, 3, 4):
            raise ValueError("variant must be 1..4")
        if self.reset_state != 0:
            raise ValueError("frozen reset state is 0")
        if len(self.transitions) != self.state_count:
            raise ValueError("row count must equal state_count")
        for row in self.transitions:
            if len(row) != len(ACTIONS):
                raise ValueError("each row must contain exactly three actions")
            for transition in row:
                if transition.target >= self.state_count:
                    raise ValueError("transition target outside model")

    def to_dict(self) -> dict[str, Any]:
        return {
            "model_id": self.model_id,
            "family": self.family,
            "state_count": self.state_count,
            "variant": self.variant,
            "reset_state": self.reset_state,
            "actions": list(ACTIONS),
            "outputs": list(OUTPUTS),
            "transitions": [
                [[transition.target, transition.output] for transition in row]
                for row in self.transitions
            ],
        }

    @property
    def digest(self) -> str:
        return sha256_hex(canonical_bytes(self.to_dict()))


@dataclass(frozen=True)
class MutationRecord:
    mutant_id: str
    source_model_id: str
    source_model_digest: str
    operator: str
    selection_digest: str
    mutation: dict[str, Any]
    model: MealyModel

    def __post_init__(self) -> None:
        if self.operator not in MUTATION_OPERATORS:
            raise ValueError(f"unknown mutation operator: {self.operator}")
        if self.model.model_id != self.mutant_id:
            raise ValueError("mutant model id mismatch")
        if len(self.selection_digest) != 64:
            raise ValueError("selection_digest must be SHA-256 hex")

    def to_dict(self) -> dict[str, Any]:
        return {
            "mutant_id": self.mutant_id,
            "source_model_id": self.source_model_id,
            "operator": self.operator,
            "mutant_model_digest": self.model.digest,
        }


@dataclass(frozen=True)
class Corpus:
    schema_version: int
    proposal_path: str
    proposal_blob_sha: str
    seed: int
    models: tuple[MealyModel, ...]
    mutants: tuple[MutationRecord, ...]

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported schema version")
        if len(self.models) != 24:
            raise ValueError("frozen corpus requires exactly 24 models")
        if len(self.mutants) != 144:
            raise ValueError("frozen corpus requires exactly 144 mutants")
        if len({model.model_id for model in self.models}) != len(self.models):
            raise ValueError("model ids must be unique")
        if len({record.mutant_id for record in self.mutants}) != len(self.mutants):
            raise ValueError("mutant ids must be unique")

    def payload_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "proposal_path": self.proposal_path,
            "proposal_blob_sha": self.proposal_blob_sha,
            "seed": self.seed,
            "actions": list(ACTIONS),
            "outputs": list(OUTPUTS),
            "families": list(FAMILIES),
            "state_sizes": list(STATE_SIZES),
            "mutation_operators": list(MUTATION_OPERATORS),
            "counts": {
                "models": len(self.models),
                "mutants": len(self.mutants),
                "mutants_per_model": len(MUTATION_OPERATORS),
            },
            "models": [model.to_dict() for model in self.models],
            "mutants": [record.to_dict() for record in self.mutants],
        }

    @property
    def payload_sha256(self) -> str:
        return sha256_hex(canonical_bytes(self.payload_dict()))

    def to_dict(self) -> dict[str, Any]:
        result = self.payload_dict()
        result["payload_sha256"] = self.payload_sha256
        return result

    def to_bytes(self) -> bytes:
        return canonical_bytes(self.to_dict())


def replace_transition(
    transitions: tuple[tuple[Transition, ...], ...],
    state: int,
    action: int,
    replacement: Transition,
) -> tuple[tuple[Transition, ...], ...]:
    rows = [list(row) for row in transitions]
    rows[state][action] = replacement
    return tuple(tuple(row) for row in rows)


def replace_row(
    transitions: tuple[tuple[Transition, ...], ...],
    state: int,
    replacement: Iterable[Transition],
) -> tuple[tuple[Transition, ...], ...]:
    rows = [tuple(row) for row in transitions]
    rows[state] = tuple(replacement)
    return tuple(rows)
