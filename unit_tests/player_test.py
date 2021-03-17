import unittest
import sys
sys.path.insert(
    1, '/Users/joao reis/Documents/projects/python_projects/card_games/src')
from core.cards.card_deck import CardDeck
from core.cards.card import PlayingCard
from core.cards.card_enums import Rank, Suit, DeckFormat
from core.cards.card_hand import CardHand
from core.player import CardPlayer
from core.card_games.card_game import CardGame

class CardGameTest(unittest.TestCase):

    def setUp(self):
        self.player = CardPlayer(player_id=1,card_hand=CardHand())

        self.card_list = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]

    def test_number_of_cards_left(self):
        self.player.deal_cards(self.card_list)
        self.assertTrue(self.player.number_of_cards_left() == 3)

if __name__ == '__main__':
    unittest.main()
