from core.cards.card_list import CardList
from core.cards.card import PlayingCard

class CardHand(CardList):

    def __init__(self, card_list: [PlayingCard] = None):
        super().__init__(card_list=card_list)

