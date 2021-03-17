from core.card_games.game_state import GameStateEnum
from core.card_games.trick_taking_game import TrickTakingGame
from core.card_games.card_values_enum import CardValuesEnum
from core.cards.card_deck import CardDeck
from core.cards.card_enums import DeckFormat
from core.cards.card_enums import Suit


class Bisca(TrickTakingGame):

    def __init__(self, players: dict, current_suit: Suit = Suit.JOKER,
                 trump_suit: Suit = Suit.JOKER,
                 current_round: int = 1, card_deck: CardDeck = None,
                 player_order: [] = None, played_cards: [] = None, game_state: GameStateEnum = GameStateEnum.CREATED):

        if len(players) != 2:
            raise Exception("Must have 2 players to start game")

        super().__init__(cards_per_player=7, card_deck=card_deck, current_round=current_round, players=players, game_state=game_state,
                         player_order=player_order, played_cards=played_cards)

        self.current_suit = current_suit
        self.trump_suit = trump_suit

    # override
   # def start_game(self):
    #    CardGame.start_game(self)
     #   self.current_round = 1

    def get_deck_format(self) -> DeckFormat:
        return DeckFormat.FORTY

    def get_rank_dictionary(self) -> CardValuesEnum:
        return CardValuesEnum.ACE_SEVEN.value
