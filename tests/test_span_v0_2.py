import pytest

from templex_zero.games import span, span_v0_2 as game


def make_state(
    *,
    black=(),
    white=(),
    participant=0,
    participant_colors=(0, 1),
    swap_available=False,
    ply=0,
    placements=0,
):
    board = [game.EMPTY] * (game.BOARD_SIZE**2)
    for row, column in black:
        board[span._index(row, column)] = 0
    for row, column in white:
        board[span._index(row, column)] = 1
    return game.State(
        tuple(board),
        participant,
        participant_colors,
        swap_available,
        ply,
        placements,
    )


def placement_destinations(state):
    return tuple(
        action.destination
        for action in game.legal_actions(state)
        if not action.is_swap
    )


def test_initial_state_preserves_v01_setup_and_legal_black_placements():
    state = game.initial_state()
    baseline = span.initial_state()
    assert state.board == baseline.board
    assert state.participant == 0
    assert state.participant_colors == (0, 1)
    assert game.current_color(state) == 0
    assert not state.swap_available
    assert game.SWAP not in game.legal_actions(state)
    assert placement_destinations(state) == span.legal_moves(baseline)


def test_swap_is_available_only_after_first_black_placement():
    state = game.apply_action(game.initial_state(), game.Action((1, 2)))
    assert state.participant == 1
    assert game.current_color(state) == 1
    assert state.swap_available
    assert state.placements == 1
    assert state.ply == 1
    assert game.SWAP in game.legal_actions(state)


def test_swap_preserves_board_and_exchanges_participant_color_ownership():
    after_opening = game.apply_action(game.initial_state(), game.Action((1, 2)))
    after_swap = game.apply_action(after_opening, game.SWAP)
    assert after_swap.board == after_opening.board
    assert after_swap.participant_colors == (1, 0)
    assert after_swap.participant == 0
    assert game.current_color(after_swap) == 1
    assert after_swap.placements == 1
    assert after_swap.ply == 2
    assert not after_swap.swap_available
    assert game.SWAP not in game.legal_actions(after_swap)


def test_normal_white_response_expires_swap_without_changing_ownership():
    after_opening = game.apply_action(game.initial_state(), game.Action((1, 2)))
    response = game.Action((1, 0))
    assert response in game.legal_actions(after_opening)
    after_response = game.apply_action(after_opening, response)
    assert after_response.participant_colors == (0, 1)
    assert after_response.participant == 0
    assert game.current_color(after_response) == 0
    assert after_response.placements == 2
    assert after_response.ply == 2
    assert not after_response.swap_available
    assert game.SWAP not in game.legal_actions(after_response)


def test_swap_is_illegal_initially_and_cannot_be_repeated():
    with pytest.raises(ValueError, match="Illegal Span v0.2 action"):
        game.apply_action(game.initial_state(), game.SWAP)

    after_opening = game.apply_action(game.initial_state(), game.Action((1, 2)))
    after_swap = game.apply_action(after_opening, game.SWAP)
    with pytest.raises(ValueError, match="Illegal Span v0.2 action"):
        game.apply_action(after_swap, game.SWAP)


def test_v01_legality_is_preserved_on_normal_no_swap_path():
    v01 = span.initial_state()
    v02 = game.initial_state()

    for move in ((1, 2), (1, 0), (2, 2)):
        assert placement_destinations(v02) == span.legal_moves(v01)
        v01 = span.apply_move(v01, move)
        v02 = game.apply_action(v02, game.Action(move))

    assert v02.board == v01.board
    assert game.current_color(v02) == v01.player


def test_connection_winner_is_reported_by_color_and_participant_after_swap():
    state = make_state(
        black=((0, 2), (1, 2), (2, 2), (3, 2), (4, 2)),
        white=((2, 0), (2, 4)),
        participant=0,
        participant_colors=(1, 0),
        ply=9,
        placements=9,
    )
    assert game.winning_color(state) == 0
    assert game.winner(state) == 1


def test_immobilization_winner_is_mapped_to_participant_after_swap():
    state = make_state(
        black=((2, 2),),
        white=((1, 2), (2, 1), (2, 3), (3, 2)),
        participant=1,
        participant_colors=(1, 0),
        ply=8,
        placements=8,
    )
    assert game.current_color(state) == 0
    assert game.legal_actions(state) == ()
    assert game.winning_color(state) == 1
    assert game.winner(state) == 0


@pytest.mark.parametrize(
    ("black", "white", "participant", "expected_move", "expected_legal"),
    (
        (((1, 1), (1, 2), (2, 1)), (), 0, (3, 1), True),
        (((1, 1), (1, 2), (2, 1)), (), 0, (2, 2), False),
        (((2, 1), (2, 3)), (), 0, (2, 2), True),
        (((2, 2),), (), 0, (0, 0), False),
        ((), ((2, 1), (2, 3)), 1, (2, 2), True),
    ),
)
def test_representative_v01_placement_rules_are_unchanged(
    black, white, participant, expected_move, expected_legal
):
    state = make_state(
        black=black,
        white=white,
        participant=participant,
        participant_colors=(0, 1),
        placements=len(black) + len(white),
    )
    assert (expected_move in game.legal_placement_moves(state)) is expected_legal
    assert game.legal_placement_moves(state) == span._legal_moves(
        state.board, game.current_color(state)
    )


def test_render_preserves_board_and_shows_participant_ownership():
    state = game.initial_state()
    rendered = game.render(state)
    assert rendered.startswith(span.render(span.initial_state()))
    assert "Participant 1: Black" in rendered
    assert "Participant 2: White" in rendered
    assert "To move: Participant 1 (Black)" in rendered
    assert "Swap available: no" in rendered
