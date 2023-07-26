# This is a sample Python script.
import dataclasses
import random
from dataclasses import dataclass


@dataclass
class Features:
    # all of these should be from 0 to 100
    buzzword_score: int
    connections: int
    years_of_experience: int
    education_level: int
    number_of_endorsements: int
    languages: int


@dataclass
class Card:
    name: str
    features: Features


def two_player_card_battle(cards: list[Card]) -> (int, int):
    player1_wins = 0
    player2_wins = 0

    cards = cards.copy()
    random.shuffle(cards)

    feature_names = [f.name for f in dataclasses.fields(Features)]
    i = 0
    while len(cards) >= 2:
        i += 1
        print(f"round{i}!")
        player1_card = cards.pop()
        player2_card = cards.pop()
        feature = random.choice(feature_names)
        player1_value = getattr(player1_card.features, feature)
        player2_value = getattr(player2_card.features, feature)
        print(f"player 1's {player1_card.name} VS. player 2's {player2_card.name}!!!")
        print(f"{player2_card.name} has {player2_value} for {feature}")
        print(f"and {player1_card.name} has {player1_value} for {feature}!")
        if player1_value == player2_value:
            pass
        elif player1_value > player2_value:
            player1_wins += 1
        else:
            player2_wins += 1
        print()
    print("GAME OVER")
    if player1_wins > player2_wins:
        print("player one wins!")

    elif player1_wins < player2_wins:
        print("player two wins!")
    else:
        print("DRAW!!")
    return player1_wins, player2_wins


def get_raw_user_data(user_id: str):
    pass


def get_cards(user_ids: list[str]) -> list[Card]:
    cards = []
    for user_id in user_ids:
        raw_data = get_raw_user_data(user_id)
        cards.append(Card(
            name=user_id,

        ))


def extract_features(raw_data_source: str) -> Features:
    """Might be better to produce scores and then generate card where the score reflects the percentile"""
    ...


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from data import EXAMPLE_CARDS
    print(two_player_card_battle(EXAMPLE_CARDS))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
