"""Deterministic Study 002 candidate-manifest generation.

This module performs static tuple generation, canonicalization, seeded ordering,
schema validation, and rule-text generation only. It does not enumerate game
states, solve candidates, or run approximate play.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
from typing import Any, Iterable, Mapping

from . import grammar
from .schema import (
    FirstMoveScope,
    GameSpec,
    GoalKind,
    GoalRule,
    LineDirections,
    MechanismFamily,
    Neighborhood,
    NoMoveOutcome,
    PlacementKind,
    PlacementRule,
)

MANIFEST_VERSION = 1
FAMILY_CODES = {
    MechanismFamily.ADJACENCY_GROWTH: "AG",
    MechanismFamily.COMPONENT_EXPANSION: "CE",
    MechanismFamily.LOCAL_BLOCK_PATTERN: "LB",
}


class ManifestGenerationError(RuntimeError):
    """Raised when the frozen grammar cannot produce its committed manifest."""


@dataclass(frozen=True)
class SelectedCandidate:
    candidate_id: str
    manifest_index: int
    cell_rank: int
    rank: str
    canonical: dict[str, Any]
    canonical_json: str
    rule_text: str
    word_count: int
    spec: GameSpec


def _compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def canonical_json(candidate: Mapping[str, Any]) -> str:
    """Serialize one already normalized candidate in frozen insertion order."""

    return _compact_json(dict(candidate))


def seeded_rank(candidate: Mapping[str, Any]) -> str:
    payload = (
        f"{grammar.GENERATION_SEED}|{candidate['board_size']}|"
        f"{candidate['family']}|{canonical_json(candidate)}"
    )
    return sha256(payload.encode("utf-8")).hexdigest()


def _common_prefix(
    board_size: int,
    family: MechanismFamily,
    neighborhood: str,
    first_move_scope: str,
) -> dict[str, Any]:
    return {
        "board_size": board_size,
        "family": family.value,
        "neighborhood": neighborhood,
        "first_move_scope": first_move_scope,
    }


def _goal_fields(board_size: int, goal: str, neighborhood: str) -> dict[str, Any]:
    if goal == "connect_edges":
        return {
            "goal_kind": GoalKind.CONNECT_EDGES.value,
            "goal_neighborhood": neighborhood,
            "goal_threshold": 1,
        }
    if goal == "component_size_board":
        return {
            "goal_kind": GoalKind.COMPONENT_SIZE.value,
            "goal_neighborhood": neighborhood,
            "goal_threshold": board_size,
        }
    raise AssertionError(f"unknown goal option: {goal}")


def _finish(candidate: dict[str, Any]) -> dict[str, Any]:
    candidate["no_move_outcome"] = NoMoveOutcome.PREVIOUS_PLAYER_WINS.value
    candidate["intended_symmetric"] = True
    return candidate


def _raw_adjacency(board_size: int) -> Iterable[dict[str, Any]]:
    options = grammar.ADJACENCY_GROWTH_OPTIONS
    keys = ("neighborhood", "first_move_scope", "friendly_requirement", "goal")
    for neighborhood, first_scope, requirement, goal in product(*(options[key] for key in keys)):
        friendly_min, friendly_max = {
            "at_least_one": (1, None),
            "exactly_one": (1, 1),
            "at_least_two": (2, None),
        }[requirement]
        candidate = _common_prefix(
            board_size,
            MechanismFamily.ADJACENCY_GROWTH,
            neighborhood,
            first_scope,
        )
        candidate["placement_kind"] = PlacementKind.FRIENDLY_ADJACENCY.value
        candidate["friendly_min"] = friendly_min
        candidate["friendly_max"] = friendly_max
        candidate.update(_goal_fields(board_size, goal, neighborhood))
        yield _finish(candidate)


def _raw_component(board_size: int) -> Iterable[dict[str, Any]]:
    options = grammar.COMPONENT_EXPANSION_OPTIONS
    keys = ("neighborhood", "first_move_scope", "expansion_policy", "goal")
    for neighborhood, first_scope, policy, goal in product(*(options[key] for key in keys)):
        allow_expand, allow_merge = {
            "expand_only": (True, False),
            "merge_only": (False, True),
            "expand_or_merge": (True, True),
        }[policy]
        candidate = _common_prefix(
            board_size,
            MechanismFamily.COMPONENT_EXPANSION,
            neighborhood,
            first_scope,
        )
        candidate["placement_kind"] = PlacementKind.EXPAND_OR_MERGE.value
        candidate["allow_expand"] = allow_expand
        candidate["allow_merge"] = allow_merge
        candidate.update(_goal_fields(board_size, goal, neighborhood))
        yield _finish(candidate)


def _raw_local_block(board_size: int) -> Iterable[dict[str, Any]]:
    options = grammar.LOCAL_BLOCK_PATTERN_OPTIONS
    keys = ("neighborhood", "first_move_scope", "enemy_neighbor_max", "line_directions")
    for neighborhood, first_scope, enemy_max, directions in product(*(options[key] for key in keys)):
        candidate = _common_prefix(
            board_size,
            MechanismFamily.LOCAL_BLOCK_PATTERN,
            neighborhood,
            first_scope,
        )
        candidate["placement_kind"] = PlacementKind.ENEMY_LIMIT.value
        candidate["friendly_min"] = 0
        candidate["enemy_max"] = enemy_max
        candidate["goal_kind"] = GoalKind.LINE.value
        candidate["goal_threshold"] = board_size
        candidate["line_directions"] = directions
        yield _finish(candidate)


def _generated_for_cell(
    board_size: int, family: MechanismFamily
) -> tuple[dict[str, Any], ...]:
    if board_size not in grammar.BOARD_SIZES:
        raise ValueError("board size is outside the frozen grammar")
    generators = {
        MechanismFamily.ADJACENCY_GROWTH: _raw_adjacency,
        MechanismFamily.COMPONENT_EXPANSION: _raw_component,
        MechanismFamily.LOCAL_BLOCK_PATTERN: _raw_local_block,
    }
    try:
        return tuple(generators[family](board_size))
    except KeyError as exc:
        raise ValueError("family is outside the frozen grammar") from exc


def normalized_candidates(
    board_size: int, family: MechanismFamily
) -> tuple[dict[str, Any], ...]:
    generated = _generated_for_cell(board_size, family)
    unique: dict[str, dict[str, Any]] = {}
    for candidate in generated:
        unique.setdefault(canonical_json(candidate), candidate)
    return tuple(unique[key] for key in sorted(unique))


def _first_move_text(scope: str) -> str:
    if scope == FirstMoveScope.ANY.value:
        return "A player's first stone may be placed on any empty cell."
    if scope == FirstMoveScope.HOME_EDGE.value:
        return (
            "Player 0's first stone must be on the top row; Player 1's first "
            "stone must be on the left column."
        )
    raise AssertionError(f"unhandled first-move scope: {scope}")


def _near_relation(value: str) -> str:
    return (
        "orthogonally adjacent to"
        if value == Neighborhood.ORTHOGONAL.value
        else "within one king move of"
    )


def _connected_group(value: str) -> str:
    return (
        "orthogonally connected group"
        if value == Neighborhood.ORTHOGONAL.value
        else "group connected through king-move adjacency"
    )


def _goal_text(candidate: Mapping[str, Any]) -> str:
    if candidate["goal_kind"] == GoalKind.CONNECT_EDGES.value:
        group = _connected_group(candidate["goal_neighborhood"])
        return (
            f"Player 0 wins by connecting the top and bottom edges with one {group}; "
            f"Player 1 wins by connecting the left and right edges with one {group}."
        )
    if candidate["goal_kind"] == GoalKind.COMPONENT_SIZE.value:
        group = _connected_group(candidate["goal_neighborhood"])
        threshold = candidate["goal_threshold"]
        return (
            f"A player wins when one friendly {group} contains at least {threshold} stones."
        )
    directions = candidate["line_directions"]
    allowed = (
        "horizontal or vertical"
        if directions == LineDirections.ORTHOGONAL.value
        else "horizontal, vertical, or diagonal"
    )
    return (
        f"A player wins by completing a straight {allowed} line of "
        f"{candidate['goal_threshold']} friendly stones."
    )


def generate_rule_text(candidate: Mapping[str, Any]) -> str:
    board_size = candidate["board_size"]
    opening = _first_move_text(candidate["first_move_scope"])
    relation = _near_relation(candidate["neighborhood"])
    if candidate["family"] == MechanismFamily.ADJACENCY_GROWTH.value:
        minimum = candidate["friendly_min"]
        maximum = candidate["friendly_max"]
        quantity = f"exactly {minimum}" if maximum == minimum else f"at least {minimum}"
        noun = "stone" if quantity.endswith(" 1") else "stones"
        placement = (
            f"After that player's first stone, every new stone must be {relation} "
            f"{quantity} friendly {noun}."
        )
    elif candidate["family"] == MechanismFamily.COMPONENT_EXPANSION.value:
        clauses = []
        if candidate["allow_expand"]:
            clauses.append(
                "it lies outside the pre-move bounding rectangle of at least one such component"
            )
        if candidate["allow_merge"]:
            clauses.append(
                "it is adjacent to at least two distinct friendly components under that relation"
            )
        joined = clauses[0] if len(clauses) == 1 else "either " + " or ".join(clauses)
        placement = (
            f"After that player's first stone, a placement is legal only if it is "
            f"{relation} a friendly component and {joined}."
        )
    else:
        placement = (
            f"Every placement may have at most {candidate['enemy_max']} enemy stones "
            f"{relation} it."
        )
    goal = _goal_text(candidate)
    return (
        f"Setup: use every cell of an empty {board_size}×{board_size} board. Player 0 "
        f"moves first; turns alternate, and each move places one stone on an empty cell. "
        f"{opening} {placement} {goal} If the next player has no legal placement and "
        f"the previous move did not win, the previous player wins."
    )


def count_rule_words(text: str) -> int:
    return len(text.split())


def candidate_to_spec(
    candidate: Mapping[str, Any], *, name: str, word_count: int
) -> GameSpec:
    neighborhood = Neighborhood(candidate["neighborhood"])
    first_scope = FirstMoveScope(candidate["first_move_scope"])
    family = MechanismFamily(candidate["family"])
    kind = PlacementKind(candidate["placement_kind"])
    placement = PlacementRule(
        kind=kind,
        neighborhood=neighborhood,
        first_move_scope=first_scope,
        friendly_min=int(candidate.get("friendly_min", 0)),
        friendly_max=candidate.get("friendly_max"),
        enemy_max=candidate.get("enemy_max"),
        allow_expand=bool(candidate.get("allow_expand", False)),
        allow_merge=bool(candidate.get("allow_merge", False)),
    )
    goal_kind = GoalKind(candidate["goal_kind"])
    goal = GoalRule(
        kind=goal_kind,
        neighborhood=Neighborhood(candidate.get("goal_neighborhood", "orthogonal")),
        threshold=int(candidate["goal_threshold"]),
        line_directions=LineDirections(candidate.get("line_directions", "orthogonal")),
    )
    return GameSpec(
        name=name,
        board_size=int(candidate["board_size"]),
        family=family,
        placement=placement,
        goal=goal,
        no_move_outcome=NoMoveOutcome(candidate["no_move_outcome"]),
        intended_symmetric=bool(candidate["intended_symmetric"]),
        core_rule_words=word_count,
    )


def _valid_ranked_cell(
    board_size: int, family: MechanismFamily
) -> list[tuple[str, str, dict[str, Any], str, int, GameSpec]]:
    ranked = []
    for candidate in normalized_candidates(board_size, family):
        canonical = canonical_json(candidate)
        rank = seeded_rank(candidate)
        text = generate_rule_text(candidate)
        words = count_rule_words(text)
        try:
            spec = candidate_to_spec(candidate, name="static_validation", word_count=words)
        except (TypeError, ValueError):
            continue
        if words <= 250:
            ranked.append((rank, canonical, candidate, text, words, spec))
    ranked.sort(key=lambda item: (item[0], item[1]))
    return ranked


def selected_candidates() -> tuple[SelectedCandidate, ...]:
    selected: list[SelectedCandidate] = []
    manifest_index = 1
    for board_size, family in grammar.cell_order():
        ranked = _valid_ranked_cell(board_size, family)
        if len(ranked) < grammar.CANDIDATES_PER_CELL:
            raise ManifestGenerationError(
                f"{board_size}x{board_size} {family.value} produced only {len(ranked)} valid candidates"
            )
        for cell_rank, (rank, canonical, candidate, text, words, _) in enumerate(
            ranked[: grammar.CANDIDATES_PER_CELL], start=1
        ):
            candidate_id = (
                f"S2-{board_size}-{FAMILY_CODES[family]}-{cell_rank:02d}"
            )
            spec = candidate_to_spec(candidate, name=candidate_id, word_count=words)
            selected.append(
                SelectedCandidate(
                    candidate_id=candidate_id,
                    manifest_index=manifest_index,
                    cell_rank=cell_rank,
                    rank=rank,
                    canonical=dict(candidate),
                    canonical_json=canonical,
                    rule_text=text,
                    word_count=words,
                    spec=spec,
                )
            )
            manifest_index += 1
    if len(selected) != grammar.TOTAL_CANDIDATES:
        raise ManifestGenerationError("manifest size differs from the frozen total")
    return tuple(selected)


def manifest_object() -> dict[str, Any]:
    entries = []
    for item in selected_candidates():
        candidate = item.canonical
        entries.append(
            {
                "id": item.candidate_id,
                "manifest_index": item.manifest_index,
                "cell_rank": item.cell_rank,
                "board_size": candidate["board_size"],
                "family": candidate["family"],
                "rank": item.rank,
                "canonical": candidate,
                "canonical_json": item.canonical_json,
                "rule_text": item.rule_text,
                "word_count": item.word_count,
                "validation": {
                    "schema_valid": True,
                    "word_limit_valid": item.word_count <= 250,
                    "full_board": len(item.spec.playable_cells)
                    == item.spec.board_size**2,
                    "intended_symmetric": item.spec.intended_symmetric,
                },
            }
        )
    entries_sha = sha256(_compact_json(entries).encode("utf-8")).hexdigest()
    cells = []
    for board_size, family in grammar.cell_order():
        selected_ids = [
            entry["id"]
            for entry in entries
            if entry["board_size"] == board_size and entry["family"] == family.value
        ]
        cells.append(
            {
                "board_size": board_size,
                "family": family.value,
                "raw_count": len(_generated_for_cell(board_size, family)),
                "canonical_unique_count": len(normalized_candidates(board_size, family)),
                "statically_valid_count": len(_valid_ranked_cell(board_size, family)),
                "selected_ids": selected_ids,
            }
        )
    return {
        "manifest_version": MANIFEST_VERSION,
        "generation_seed": grammar.GENERATION_SEED,
        "selection": {
            "cell_order": [
                {"board_size": size, "family": family.value}
                for size, family in grammar.cell_order()
            ],
            "candidates_per_cell": grammar.CANDIDATES_PER_CELL,
            "ranking": "sha256(seed|board_size|family|canonical_json)",
            "manual_ranking": False,
        },
        "entry_count": len(entries),
        "entries_sha256": entries_sha,
        "cells": cells,
        "entries": entries,
    }


def manifest_json() -> str:
    return json.dumps(manifest_object(), ensure_ascii=False, indent=2) + "\n"


def manifest_markdown() -> str:
    manifest = manifest_object()
    lines = [
        "# Study 002 Frozen Candidate Manifest",
        "",
        "_Generated deterministically before exact, random, or shallow candidate evaluation._",
        "",
        f"- Generation seed: `{manifest['generation_seed']}`",
        f"- Entry count: `{manifest['entry_count']}`",
        f"- Entries SHA-256: `{manifest['entries_sha256']}`",
        "- Selection: first three statically valid candidates in seeded SHA-256 order for each frozen cell",
        "- Manual ranking or replacement: none",
        "",
        "| Index | ID | Board | Family | Cell rank | Words | Seeded rank |",
        "|---:|---|---:|---|---:|---:|---|",
    ]
    for entry in manifest["entries"]:
        lines.append(
            f"| {entry['manifest_index']} | `{entry['id']}` | {entry['board_size']}×{entry['board_size']} "
            f"| `{entry['family']}` | {entry['cell_rank']} | {entry['word_count']} "
            f"| `{entry['rank']}` |"
        )
    for entry in manifest["entries"]:
        lines.extend(
            [
                "",
                f"## {entry['id']}",
                "",
                entry["rule_text"],
                "",
                f"- Word count: `{entry['word_count']}`",
                f"- Seeded rank: `{entry['rank']}`",
                f"- Canonical JSON: `{entry['canonical_json']}`",
                "- Static validation: schema valid, full board, intended symmetry, word limit valid",
            ]
        )
    lines.append("")
    return "\n".join(lines)
