import random

import data
import main


def test_two_player_card_battle():
    """The thing works."""
    random.seed(0)
    result = main.two_player_card_battle(data.EXAMPLE_CARDS)
    assert result == (0, 1)
