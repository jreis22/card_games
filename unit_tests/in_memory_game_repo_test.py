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
from core.repositories.in_memory_game_repo import InMemoryGameRepo

class InMemomoryGameRepoTest(unittest.TestCase):

    def setUp(self):
        players_dict = [CardPlayer(1),
                        CardPlayer(2),
                        CardPlayer(3),
                        CardPlayer(4)]
        player_order = [1, 2, 3, 4]

        self.game = CardGame(cards_per_player=7, players=players_dict,
                             player_order=player_order, card_deck=CardDeck(DeckFormat.FIFTY_TWO))
        self.game.card_deck.build_deck()
        self.repo = InMemoryGameRepo()

    def test_insert(self):
        self.assertEqual(len(self.repo.games), 0)
        self.repo.insert(self.game)

        self.assertEqual(len(self.repo.games), 1)
        self.assertEqual(self.game, list(self.repo.games.values())[0])
        self.assertEqual(self.game.game_id, list(self.repo.games.keys())[0])

        self.assertTrue(self.repo.has(self.game.game_id))
    
    def test_get_by_id(self):
        self.repo.insert(self.game)
        self.assertTrue(not self.game.game_id is None)
        game_id = self.game.game_id
        game = self.repo.get_by_id(game_id)
        self.assertNotEqual(self.game, game)

if __name__ == '__main__':
    unittest.main()
