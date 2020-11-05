from card_game import CardGame
from cards.card_deck import CardDeck
from cards.card_enums import DeckFormat


class Bisca(CardGame):
    def __init__(self, players: dict):
        super().__init__(cards_per_player=7, card_deck=CardDeck(
            deck_format=DeckFormat.FORTY), players=players)
