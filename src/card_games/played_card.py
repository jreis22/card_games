from cards.card import PlayingCard


class PlayedCard:
    def __init__(self, player_key, card: PlayingCard, round: int):
        self.player_key = player_key
        self.card = card
        self.round = round

    def __eq__(self, other):
        if isinstance(other, PlayedCard):
            return other.player_key == self.player_key and self.card == other.card and self.round == other.round
        else:
            return False
