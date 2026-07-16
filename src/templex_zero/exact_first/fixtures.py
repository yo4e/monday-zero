"""Four hand-audited state graphs frozen before Study 002 candidate generation."""

from __future__ import annotations

from dataclasses import dataclass

from .schema import (
    FirstMoveScope,
    GameSpec,
    GoalKind,
    GoalRule,
    MechanismFamily,
    Neighborhood,
    NoMoveOutcome,
    PlacementKind,
    PlacementRule,
)


@dataclass(frozen=True)
class AuditedFixture:
    name: str
    spec: GameSpec
    expected_graph: dict[str, dict[str, object]]
    symmetry_claim: str | None = None


IMMEDIATE_COMPONENT_WIN = AuditedFixture(
    name="immediate_component_win",
    spec=GameSpec(
        name="fixture_immediate_component_win",
        board_size=1,
        family=MechanismFamily.FIXTURE,
        playable_cells=(0,),
        placement=PlacementRule(PlacementKind.ANY),
        goal=GoalRule(GoalKind.COMPONENT_SIZE, threshold=1),
        intended_symmetric=True,
    ),
    expected_graph={
        "p0:0:.": {"terminal": "ongoing", "actions": {"A1": "p1:1:X"}},
        "p1:1:X": {"terminal": "win:0", "actions": {}},
    },
    symmetry_claim="color-role symmetric",
)


SINGLE_CELL_DRAW = AuditedFixture(
    name="single_cell_draw",
    spec=GameSpec(
        name="fixture_single_cell_draw",
        board_size=1,
        family=MechanismFamily.FIXTURE,
        playable_cells=(0,),
        placement=PlacementRule(PlacementKind.ANY),
        goal=GoalRule(GoalKind.COMPONENT_SIZE, threshold=2),
        no_move_outcome=NoMoveOutcome.DRAW,
        intended_symmetric=True,
    ),
    expected_graph={
        "p0:0:.": {"terminal": "ongoing", "actions": {"A1": "p1:1:X"}},
        "p1:1:X": {"terminal": "draw", "actions": {}},
    },
    symmetry_claim="color-role symmetric",
)


BRANCHING_PATTERN = AuditedFixture(
    name="branching_pattern",
    spec=GameSpec(
        name="fixture_branching_pattern",
        board_size=2,
        family=MechanismFamily.FIXTURE,
        playable_cells=(0, 1),
        placement=PlacementRule(PlacementKind.ANY),
        goal=GoalRule(
            GoalKind.EXPLICIT_PATTERNS,
            explicit_patterns=(((0,),), ((1,),)),
        ),
        intended_symmetric=False,
    ),
    expected_graph={
        "p0:0:..##": {
            "terminal": "ongoing",
            "actions": {"A1": "p1:1:X.##", "B1": "p1:1:.X##"},
        },
        "p1:1:X.##": {"terminal": "win:0", "actions": {}},
        "p1:1:.X##": {
            "terminal": "ongoing",
            "actions": {"A1": "p0:2:OX##"},
        },
        "p0:2:OX##": {"terminal": "win:1", "actions": {}},
    },
)


ADJACENCY_CHAIN = AuditedFixture(
    name="adjacency_chain",
    spec=GameSpec(
        name="fixture_adjacency_chain",
        board_size=2,
        family=MechanismFamily.FIXTURE,
        playable_cells=(0, 1, 3),
        placement=PlacementRule(
            PlacementKind.FRIENDLY_ADJACENCY,
            neighborhood=Neighborhood.ORTHOGONAL,
            first_move_scope=FirstMoveScope.EXPLICIT,
            explicit_first_cells=((0,), (3,)),
            friendly_min=1,
            friendly_max=1,
        ),
        goal=GoalRule(
            GoalKind.EXPLICIT_PATTERNS,
            explicit_patterns=(((0, 1),), ((1, 3),)),
        ),
        intended_symmetric=True,
    ),
    expected_graph={
        "p0:0:..#.": {
            "terminal": "ongoing",
            "actions": {"A1": "p1:1:X.#."},
        },
        "p1:1:X.#.": {
            "terminal": "ongoing",
            "actions": {"B2": "p0:2:X.#O"},
        },
        "p0:2:X.#O": {
            "terminal": "ongoing",
            "actions": {"B1": "p1:3:XX#O"},
        },
        "p1:3:XX#O": {"terminal": "win:0", "actions": {}},
    },
    symmetry_claim="transpose plus player/color exchange",
)


AUDITED_FIXTURES = (
    IMMEDIATE_COMPONENT_WIN,
    SINGLE_CELL_DRAW,
    BRANCHING_PATTERN,
    ADJACENCY_CHAIN,
)
