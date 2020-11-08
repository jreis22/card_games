import unittest
import sys
sys.path.insert(
    1, '/Users/joao reis/Documents/projects/python_projects/card_games/src')
from cards.card_deck import CardDeck
from cards.card import PlayingCard
from cards.card_enums import Rank, Suit, DeckFormat
from cards.card_hand import CardHand
from player import CardPlayer
from card_game import CardGame

class CardPlayerTest(unittest.TestCase):

    def setUp(self):
        players_dict = {1: CardPlayer(card_hand=CardHand()),
                        2: CardPlayer(card_hand=CardHand()),
                        3: CardPlayer(card_hand=CardHand()),
                        4: CardPlayer(card_hand=CardHand())}
        player_order = [1, 2, 3, 4]

        self.game = CardGame(cards_per_player=7, players=players_dict,
                             player_order=player_order, card_deck=CardDeck(DeckFormat.FIFTY_TWO))

    def test_CardGame_constructor(self):
        self.assertTrue(self.game.cards_per_player == 7)
        self.assertTrue(len(self.game.players) == 4)
        self.assertTrue(self.game.card_deck.list_size() == 52)

    def test_deal_cards(self):
        self.game.deal_cards()

        # loop players
        for player in self.game.players:
            # assert right numer of cards for player
            self.assertTrue(
                self.game.players[player].card_hand.list_size() == self.game.cards_per_player)

            # loop player cards
            for card in self.game.players[player].card_hand.show_cards():
                # assert card isnt in game deck
                self.assertFalse(self.game.card_deck.contains_card(card))

                # check if other players dont have same cards
                for player2 in self.game.players:
                    if player2 != player:
                        self.assertFalse(
                            self.game.players[player2].card_hand.contains_card(card))

        # assert number of cards left in deck
        self.assertTrue(self.game.card_deck.list_size() == 52 -
                        (len(self.game.players)*self.game.cards_per_player))

    def test_rotate_player_order(self):
        self.game.rotate_player_order()
        expected = [2, 3, 4, 1]
        self.assertEqual(self.game.player_order, expected)

        self.game.inverse_rotate_player_order()
        expected = [1, 2, 3, 4]
        self.assertEqual(self.game.player_order, expected)

    def test_rotate_player_order_n_times(self):
        self.game.rotate_player_order_n_times(2)
        expected = [3, 4, 1, 2]
        self.assertEqual(self.game.player_order, expected)

        self.game.inverse_rotate_player_order_n_times(3)        
        expected = [4, 1, 2, 3]
        self.assertEqual(self.game.player_order, expected)
        self.game.inverse_rotate_player_order_n_times(1)
        expected = [3, 4, 1, 2]
        self.assertEqual(self.game.player_order, expected)

        self.game.rotate_player_order_n_times(4)
        self.assertEqual(self.game.player_order, expected)
        

if __name__ == '__main__':
    unittest.main()
