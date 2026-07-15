import pytest

from templex_zero.games import keystone


def make_state(*, black=(), white=(), reserves=(8, 8), player=0, ply=0):
    board = [keystone.EMPTY] * (keystone.BOARD_SIZE**2)
    for row, column in black:
        board[keystone._index(row, column)] = 0
    for row, column in white:
        board[keystone._index(row, column)] = 1
    board_tuple = tuple(board)
    key = keystone._position_key_parts(board_tuple, reserves, player)
    return keystone.State(board_tuple, reserves, player, ply, (key,))


def test_initial_state_offers_all_placements_and_no_shifts():
    state = keystone.initial_state()
    actions = keystone.legal_actions(state)
    assert len(actions) == 25
    assert all(action.is_placement for action in actions)
    assert all(action.capture is None for action in actions)
    assert state.reserves == (8, 8)


def test_placement_uses_reserve_and_switches_player():
    state = keystone.initial_state()
    next_state = keystone.apply_action(
        state, keystone.Action(None, (2, 2))
    )
    assert next_state.board[keystone.CENTER] == 0
    assert next_state.reserves == (7, 8)
    assert next_state.player == 1
    assert next_state.ply == 1


def test_shift_moves_one_step_orthogonally_without_using_reserve():
    state = make_state(black=((2, 2),), reserves=(0, 0))
    action = keystone.Action((2, 2), (2, 3))
    assert action in keystone.legal_actions(state)
    next_state = keystone.apply_action(state, action)
    assert next_state.board[keystone._index(2, 2)] == keystone.EMPTY
    assert next_state.board[keystone._index(2, 3)] == 0
    assert next_state.reserves == (0, 0)


def test_single_custodian_capture_is_mandatory_and_permanent():
    state = make_state(
        black=((2, 0),),
        white=((2, 1),),
        reserves=(7, 7),
    )
    required = keystone.Action(None, (2, 2), (2, 1))
    assert required in keystone.legal_actions(state)
    assert keystone.Action(None, (2, 2), None) not in keystone.legal_actions(state)
    with pytest.raises(ValueError, match="Illegal Keystone action"):
        keystone.apply_action(state, keystone.Action(None, (2, 2), None))

    next_state = keystone.apply_action(state, required)
    assert next_state.board[keystone._index(2, 1)] == keystone.EMPTY
    assert next_state.board[keystone._index(2, 2)] == 0
    assert next_state.reserves == (6, 7)


def test_multiple_brackets_create_one_action_per_capture_choice():
    state = make_state(
        black=((0, 2), (2, 0)),
        white=((1, 2), (2, 1)),
        reserves=(6, 6),
    )
    north = keystone.Action(None, (2, 2), (1, 2))
    west = keystone.Action(None, (2, 2), (2, 1))
    matching = [
        action
        for action in keystone.legal_actions(state)
        if action.source is None and action.destination == (2, 2)
    ]
    assert set(matching) == {north, west}

    next_state = keystone.apply_action(state, north)
    assert next_state.board[keystone._index(1, 2)] == keystone.EMPTY
    assert next_state.board[keystone._index(2, 1)] == 1


def test_center_component_with_two_distinct_edge_stones_wins():
    state = make_state(
        black=((0, 2), (1, 2), (2, 0), (2, 1)),
        reserves=(4, 8),
    )
    won = keystone.apply_action(state, keystone.Action(None, (2, 2)))
    assert keystone.winner(won) == 0


def test_corner_cannot_supply_two_edge_contacts_by_itself():
    center_and_corner = frozenset(
        {keystone.CENTER, keystone._index(0, 0)}
    )
    assert not keystone._component_has_required_edges(center_and_corner)

    with_second_edge_stone = center_and_corner | {
        keystone._index(0, 1)
    }
    assert keystone._component_has_required_edges(with_second_edge_stone)


def test_full_checkerboard_has_no_actions_and_current_player_loses():
    board = tuple(
        (row + column) % 2
        for row in range(keystone.BOARD_SIZE)
        for column in range(keystone.BOARD_SIZE)
    )
    key = keystone._position_key_parts(board, (0, 0), 0)
    state = keystone.State(board, (0, 0), 0, 21, (key,))
    assert not keystone._has_victory(board, 0)
    assert not keystone._has_victory(board, 1)
    assert keystone.legal_actions(state) == ()
    assert keystone.winner(state) == 1


def test_third_occurrence_of_complete_position_is_a_draw():
    state = make_state(
        black=((0, 0),),
        white=((4, 4),),
        reserves=(0, 0),
    )
    cycle = (
        keystone.Action((0, 0), (1, 0)),
        keystone.Action((4, 4), (3, 4)),
        keystone.Action((1, 0), (0, 0)),
        keystone.Action((3, 4), (4, 4)),
    )
    for _ in range(2):
        for action in cycle:
            state = keystone.apply_action(state, action)
    assert keystone._repetition_count(state) == 3
    assert keystone.winner(state) is None


def test_victory_precedes_repetition():
    board_state = make_state(
        black=((0, 2), (1, 2), (2, 0), (2, 1), (2, 2)),
        reserves=(3, 8),
        player=1,
    )
    key = keystone.position_key(board_state)
    repeated = keystone.State(
        board_state.board,
        board_state.reserves,
        board_state.player,
        board_state.ply,
        (key, key, key),
    )
    assert keystone.winner(repeated) == 0


def test_render_includes_coordinates_reserves_and_turn():
    assert keystone.render(keystone.initial_state()) == (
        "    A B C D E\n"
        " 1  . . . . .\n"
        " 2  . . . . .\n"
        " 3  . . . . .\n"
        " 4  . . . . .\n"
        " 5  . . . . .\n"
        "Black reserve: 8\n"
        "White reserve: 8\n"
        "To move: Black"
    )
