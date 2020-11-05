
from card_list import CardList
from card_enums import DeckFormat
from default_deck_builder import DeckBuilder


class CardDeck(CardList):

    def __init__(self, deck_format: DeckFormat):
        super().__init__()
        self.deck_format = deck_format
        self.build_deck()
        self.shuffle()

    def build_deck(self):
        self.add_cards(DeckBuilder.build_deck(self.deck_format))

            
deck = CardDeck(DeckFormat.QUARENTA)
deck.__print_list__()

# print('dealt cards: ')
# for card in deck.dean_n_cards(3):
#     print(card)

# print('deck: ')
# deck.__print_deck__()