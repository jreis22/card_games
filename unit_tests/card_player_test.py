import unittest
import sys
sys.path.insert(1, '/Users/joao reis/Documents/projects/python_projects/card_games/src')
sys.path.insert(1, '/Users/joao reis/Documents/projects/python_projects/card_games/src/cards')
from card import PlayingCard
from card_enums import Rank, Suit
from card_hand import CardHand
from player import CardPlayer



class CardPlayerTest(unittest.TestCase):

    def test_CardPlayer_constructor(self):
        card = PlayingCard(suit=Suit.SPADES, rank=Rank.SEVEN)
        cardh = CardHand()
        cardh.add_card(card)
        cardp = CardPlayer(card_hand=cardh)
        self.assertEqual(card, cardp.card_hand.show_cards()[0])


if __name__ == '__main__':
    unittest.main()
