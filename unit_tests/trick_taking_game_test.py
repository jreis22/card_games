import unittest
import sys
sys.path.insert(
    1, '/Users/joao reis/Documents/projects/python_projects/card_games/src')
from core.cards.card_enums import Rank, Suit, DeckFormat
from core.card_games.trick_taking_game import TrickTakingGame
from core.cards.card import PlayingCard
from core.cards.card_hand import CardHand
from core.player import CardPlayer
from core.cards.card_deck import CardDeck
from core.card_games.game_state import GameStateEnum
from core.card_games.played_card import PlayedCard


class TrickTakingGameTest(unittest.TestCase):

    def setUp(self):
        players_dict = [CardPlayer(1),
                        CardPlayer(2)]
        player_order = [1, 2]

        self.game = TrickTakingGame(cards_per_player= 7, players=players_dict,
                          player_order=player_order,
                          current_suit=Suit.JOKER, trump_suit=Suit.DIAMONDS, current_round=1)
        self.game.card_deck.build_deck()
        self.game.card_deck.sort_by_suit()
        for i in range(0, 7):
            for player in self.game.players:
                self.game.deal_n_cards_to_player(player, 1)
        self.game.game_state = GameStateEnum.STARTED

        self.game.trump_suit = Suit.DIAMONDS
        self.game.current_suit = Suit.HEARTS

    def test_constructor(self):
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.card_deck.deck_format, DeckFormat.FIFTY_TWO)
        self.assertEqual(self.game.card_deck.list_size(), 38)

        expected_player_1_cards = [
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.ACE),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.THREE),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.FIVE),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.SEVEN),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.NINE),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.JACK),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.KING)
        ]
        expected_player1_hand = CardHand(expected_player_1_cards)
        self.assertEqual(
            self.game.players[1].card_hand, expected_player1_hand)

        expected_player_1_cards = [
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TWO),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.SIX),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.EIGHT),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TEN),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.QUEEN),
            PlayingCard(suit=Suit.CLUBS, rank=Rank.ACE)
        ]
        expected_player1_hand = CardHand(expected_player_1_cards)
        self.assertEqual(
            self.game.players[2].card_hand, expected_player1_hand)

    def test_rank_comparison(self):
        cards = [
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TWO),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.SEVEN),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.JACK),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.QUEEN),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.KING),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.ACE)
        ]

        card42 = PlayingCard(suit=Suit.CLUBS, rank=Rank.FOUR)

        # teste for card1
        self.assertTrue(self.game.rank_comparison(card1=cards[1], card2=card42) is None)
        for i in range(1, 7):
            card1 = cards[i]
            for j in range(0, i):
                card2 = cards[j]
                result = self.game.rank_comparison(card1, card2)
                self.assertTrue(result == card1)

        # test for card2
        for i in range(5, -1, -1):
            card1 = cards[i]
            for j in range(6, i, -1):
                card2 = cards[j]
                result = self.game.rank_comparison(card1, card2)
                self.assertTrue(result == card2)

    def test_compare_cards(self):
        self.game.trump_suit = Suit.DIAMONDS
        self.game.current_suit = Suit.HEARTS

        cards = [
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.FOUR),
            PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TWO),
            PlayingCard(suit=Suit.HEARTS, rank=Rank.QUEEN),
            PlayingCard(suit=Suit.CLUBS, rank=Rank.JACK),
        ]

        cardA = PlayingCard(suit=Suit.SPADES, rank=Rank.ACE)

        self.assertTrue(self.game.compare_cards(cards[3], cardA, round_suit=self.game.current_suit) is None)
        for i in range(0, 3):
            card1 = cards[i]
            for j in range(i+1, 4):
                card2 = cards[j]
                result = self.game.compare_cards(card1=card1, card2=card2, round_suit=self.game.current_suit)
                self.assertTrue(result == card1)

        # test for card2
        for i in range(3, 0, -1):
            card1 = cards[i]
            for j in range(0, i):
                card2 = cards[j]
                result = self.game.compare_cards(card1=card1, card2=card2, round_suit=self.game.current_suit)
                self.assertTrue(result == card2)

    def test_get_plays_from_round(self):
        self.game.add_played_card(player_key=1, card=PlayingCard(suit=Suit.HEARTS, rank=Rank.FOUR), round=1)
        self.game.add_played_card(player_key=2, card=PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TWO), round=1)
        self.game.add_played_card(player_key=1, card=PlayingCard(suit=Suit.SPADES, rank=Rank.QUEEN), round=2)
        self.game.add_played_card(player_key=2, card=PlayingCard(suit=Suit.CLUBS, rank=Rank.JACK), round=2)

        result = self.game.get_plays_from_round(1)
        expected = [
            PlayedCard(player_key=1, card=PlayingCard(suit=Suit.HEARTS, rank=Rank.FOUR), round=1),
            PlayedCard(player_key=2, card=PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TWO), round=1),
        ]
        self.assertEqual(result, expected)

    def test_get_round_points(self):
        self.game.add_played_card(player_key=1, card=PlayingCard(suit=Suit.HEARTS, rank=Rank.FOUR), round=1)
        self.game.add_played_card(player_key=2, card=PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TWO), round=1)
        
        #necessary to add extra cards
        self.game.current_round = 2
        self.game.add_played_card(player_key=1, card=PlayingCard(suit=Suit.SPADES, rank=Rank.QUEEN), round=2)
        self.game.add_played_card(player_key=2, card=PlayingCard(suit=Suit.CLUBS, rank=Rank.JACK), round=2)
        

        result = self.game.get_round_points(1)
        expected = 0
        self.assertEqual(result, expected)

        result = self.game.get_round_points(2)
        expected = 5
        self.assertEqual(result, expected)

    def test_get_round_winner(self):
        self.game.add_played_card(player_key=1, card=PlayingCard(suit=Suit.HEARTS, rank=Rank.FOUR), round=1)
        self.game.add_played_card(player_key=2, card=PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TWO), round=1)
        self.game.current_round=2
        self.game.add_played_card(player_key=1, card=PlayingCard(suit=Suit.SPADES, rank=Rank.QUEEN), round=2)
        self.game.add_played_card(player_key=2, card=PlayingCard(suit=Suit.CLUBS, rank=Rank.JACK), round=2)
        

        result = self.game.get_round_winner(1)
        #because its trump suit
        expected = 2
        self.assertEqual(result, expected)
        self.assertEqual(len(self.game.get_plays_from_round(1)), 2)
        #player 1 winds because of round suit
        self.assertEqual(self.game.get_round_winner(2), 1)
    
    def test_end_round(self):
        self.game.add_played_card(player_key=1, card=PlayingCard(suit=Suit.HEARTS, rank=Rank.FOUR), round=1)
        
        self.assertFalse(self.game.end_round())

        self.game.add_played_card(player_key=2, card=PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TWO), round=1)
        #falso pois ha jogadores a jogar
        self.assertFalse(self.game.end_round())
        self.game.players[1].pass_turn()
        self.game.players[2].pass_turn()
        self.assertEqual(self.game.players[1].number_of_cards_left(), 7)
        self.assertEqual(self.game.players[2].number_of_cards_left(), 7)
        self.assertEqual(self.game.card_deck.list_size(), 38)
        self.assertTrue(self.game.end_round())
        self.assertTrue(self.game.current_round == 2)
        
        for player in self.game.players.values():
            self.assertTrue(player.is_playing())
            self.assertEqual(player.number_of_cards_left(), 8)
        
        self.assertEqual(self.game.card_deck.list_size(), 36)
        self.assertTrue(self.game.current_suit == Suit.JOKER)

    def test_play_card(self):
        self.game.current_suit = Suit.JOKER
        card1 = PlayingCard(suit=Suit.DIAMONDS, rank=Rank.ACE)
        self.assertTrue(self.game.players[1].has_card(card1))
        self.assertEqual(len(self.game.played_cards), 0)
        self.assertEqual(self.game.current_suit, Suit.JOKER)
        self.game.play_card(1, card1)
        self.assertEqual(self.game.current_suit, Suit.DIAMONDS)
        self.assertFalse(self.game.players[1].has_card(card1))
        self.assertEqual(len(self.game.played_cards), 1)
        self.assertFalse(self.game.players[1].is_playing())
        try:
            self.game.play_card(2, card1)
        except Exception:
            pass
        else:
            self.fail("game.play_card player2 shouldnt own card")
        
        card2 = PlayingCard(suit=Suit.CLUBS, rank=Rank.TWO)

        try:
            self.game.play_card(2, card2)
        except Exception:
            pass
        else:
            self.fail("game.play_card player2 shouldnt be able to play card of different suit")

        card3 = PlayingCard(suit=Suit.DIAMONDS, rank=Rank.TWO)
        self.assertEqual(self.game.player_order[0], 2)
        
        self.game.play_card(2, card3)

        self.assertEqual(len(self.game.played_cards), 2)
        self.assertEqual(self.game.current_round, 2)
        self.assertEqual(self.game.current_suit, Suit.JOKER)
        self.assertEqual(self.game.player_order[0], 1)
        self.assertEqual(self.game.player_order[1], 2)
        self.assertEqual(self.game.players[1].points, 11)
        self.assertEqual(self.game.players[2].points, 0)
        

if __name__ == '__main__':
    unittest.main()
