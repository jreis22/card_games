import unittest
import sys
sys.path.insert(
    1, '/Users/joao reis/Documents/projects/python_projects/card_games/src')
from card_game import CardGame
from player import CardPlayer
from cards.card_hand import CardHand
from cards.card_enums import Rank, Suit, DeckFormat
from cards.card import PlayingCard
from cards.card_deck import CardDeck


class CardPlayerTest(unittest.TestCase):

    def setUp(self):
        players_dict = {1: CardPlayer(card_hand=CardHand()),
                  2: CardPlayer(card_hand=CardHand()),
                  3: CardPlayer(card_hand=CardHand()),
                  4: CardPlayer(card_hand=CardHand())}
        
        self.game = CardGame(cards_per_player=7, players=players_dict, card_deck=CardDeck(DeckFormat.FIFTY_TWO))

    def test_CardGame_constructor(self):
        self.assertTrue(self.game.cards_per_player == 7)
        self.assertTrue(len(self.game.players) == 4)
        self.assertTrue(self.game.card_deck.list_size() == 52)

    def test_deal_cards(self):
        self.game.deal_cards()
        self.assertTrue(self.game.players[1].card_hand.list_size() == self.game.cards_per_player)

if __name__ == '__main__':
    unittest.main()
