from player import CardPlayer
from cards.card_deck import CardDeck
from cards.card_enums import DeckFormat


class CardGame:

    def __init__(self, cards_per_player: int, players: dict = None, card_deck: CardDeck = CardDeck(DeckFormat.CINQUENTA_DUAS)):
        self.players = players
        self.card_deck = card_deck
        self.cards_per_player = cards_per_player

    def play(self):
        pass

    def deal_cards(self):
        for player in self.players:
            player.deal_hand(self.card_deck.dean_n_cards(self.cards_per_player))


    def deal_n_cards_to_player(self, player, nCards: int):
        hand = self.card_deck.deal_n_cards(nCards)
        return hand
