from card_games.card_game import CardGame
from card_games.game_state import GameStateEnum
from cards.card_deck import CardDeck
from cards.card_enums import DeckFormat
from cards.card import PlayingCard
from cards.card_enums import Suit, Rank


class Bisca(CardGame):
    point_dict = {
        Rank.ACE.value: 11,
        Rank.SEVEN.value: 10,
        Rank.KING.value: 4,
        Rank.JACK.value: 3,
        Rank.QUEEN.value: 2
    }
    # played_cards saves a tuple (player_key, card)
    COLUMN_PLAYER_KEY = 0
    COLUMN_CARD = 1

    def __init__(self, players: dict, current_suit: Suit = Suit.JOKER,
                 trump_suit: Suit = Suit.JOKER,
                 current_round: int = 1, card_deck: CardDeck = None,
                 player_order: [] = None, played_cards: [] = None, game_state: GameStateEnum = GameStateEnum.CREATED):

        if len(players) != 2:
            raise Exception("Must have 2 players to start game")

        super().__init__(cards_per_player=7, card_deck=card_deck, players=players, game_state=game_state,
                         player_order=player_order, played_cards=played_cards
                         )

        self.current_suit = current_suit
        self.trump_suit = trump_suit
        self.current_round = current_round

    # override
   # def start_game(self):
    #    CardGame.start_game(self)
     #   self.current_round = 1

    def set_card_deck(self, card_deck: CardDeck):
        if card_deck is None:
            self.card_deck = CardDeck(DeckFormat.FORTY)
        else:
            self.card_deck = card_deck

    def play_card(self, player_key, card: PlayingCard):
        player = self.players[player_key]

        if not player.is_playing():
            raise Exception(f'Player {player_key} cant play')
        if self.player_order[0] != player_key:
            raise Exception(f"It's not {player_key}'s turn")
        if not player.has_card(card):
            raise Exception(f"Player {player_key} doesn't own card {card}")
        if card.suit != self.current_suit:
            if (self.current_suit == Suit.JOKER):
                self.current_suit = card.suit
            elif player.contains_card_of_suit(self.current_suit):
                raise Exception(
                    f"Player {player_key} must play card of current round suit {self.current_suit}")

        player.play_card(card)
        self.add_played_card(player_key=player_key, card=card)
        player.pass_turn()
        self.rotate_player_order()
        if self.end_round():
            self.end_game()

    def end_round(self) -> bool:
        if self.exists_players_playing():
            return False

        winner = self.get_round_winner(self.current_round)
        self.players[winner].add_points(
            self.get_round_points(self.current_round))

        if self.player_order[0] != winner:
            winner_index = self.player_order.index(
                winner, 1, len(self.player_order))
            self.rotate_player_order_n_times(winner_index)
        self.current_round += 1
        self.set_all_players_playing()
        if self.card_deck.list_size() > 0:
            for player in self.players:
                self.deal_n_cards_to_player(player_key=player, nCards=1)

        self.current_suit = Suit.JOKER
        return True

    def end_game(self) -> bool:
        if self.current_round == 21:
            self.game_state = GameStateEnum.GAME_END

    # method assumes played cards array is ordered
    def get_round_winner(self, current_round):
        plays = self.get_plays_from_round(current_round)
        best_play = plays[0]
        round_suit = best_play[Bisca.COLUMN_CARD].suit
        for play in plays[1:]:
            card1 = best_play[Bisca.COLUMN_CARD]
            card2 = play[Bisca.COLUMN_CARD]
            if self.compare_cards(card1=card1, card2=card2, round_suit=round_suit) == card2:
                best_play = play

        return best_play[Bisca.COLUMN_PLAYER_KEY]

    def get_round_points(self, current_round) -> int:
        plays = self.get_plays_from_round(current_round)
        points = 0
        for play in plays:
            if Bisca.point_dict.keys().__contains__(play[Bisca.COLUMN_CARD].rank.value):
                points += Bisca.point_dict[play[Bisca.COLUMN_CARD].rank.value]

        return points

    def get_plays_from_round(self, current_round: int):
        nPlayers = len(self.players)
        starting_index = nPlayers * (current_round - 1)
        ending_index = starting_index + nPlayers
        cards_played_len = len(self.played_cards)
        if ending_index > cards_played_len:
            ending_index = cards_played_len
        if starting_index >= cards_played_len:
            raise Exception(f"Round wasn't reached yet")
        plays_from_round = self.played_cards[starting_index:ending_index]
        return plays_from_round

    def compare_cards(self, card1: PlayingCard, card2: PlayingCard, round_suit: Suit) -> PlayingCard:
        if card1.suit == card2.suit:
            return Bisca.rank_comparison(card1, card2)
        elif card1.suit == self.trump_suit:
            return card1
        elif card2.suit == self.trump_suit:
            return card2
        elif card1.suit == round_suit:
            return card1
        elif card2.suit == round_suit:
            return card2
        else:
            return None

    @staticmethod
    def rank_comparison(card1: PlayingCard, card2: PlayingCard) -> PlayingCard:
        rank1 = card1.rank
        rank2 = card2.rank
        if rank1 == rank2:
            return None
        elif Bisca.point_dict.keys().__contains__(rank1.value):
            if Bisca.point_dict.keys().__contains__(rank2.value)\
               and Bisca.point_dict[rank1.value] < Bisca.point_dict[rank2.value]:
                return card2
            else:
                return card1

        elif (Bisca.point_dict.keys().__contains__(rank2.value)):
            return card2
        else:
            if rank1 > rank2:
                return card1
            else:
                return card2
