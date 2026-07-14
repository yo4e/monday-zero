from monday_zero.agents import random_agent
from monday_zero.games import relay
from monday_zero.match import play


def test_initial_state_has_legal_moves():
    assert relay.legal_moves(relay.initial_state())


def test_all_initial_moves_preserve_friendly_connectivity():
    state = relay.initial_state()
    for move in relay.legal_moves(state):
        next_state = relay.apply_move(state, move)
        assert relay._connected_by_king_steps(next_state.board, 0)


def test_random_games_terminate_under_fixed_seeds():
    for seed in range(25):
        result = play(random_agent, random_agent, seed)
        assert result.winner in (0, 1, None)
        assert result.plies <= 200
