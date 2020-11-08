from player import CardPlayer
from cards.card_deck import CardDeck
from cards.card_enums import DeckFormat
from game_state import GameStateMachine
from cards.card import PlayingCard


class CardGame(GameStateMachine):

    # rounds are
    def __init__(self, cards_per_player: int, players: dict = {},
                 card_deck: CardDeck = CardDeck(DeckFormat.FIFTY_TWO),
                 player_order: [] = []):
        self.players = players
        self.card_deck = card_deck
        self.cards_per_player = cards_per_player
        self.player_order = player_order
        self.played_cards = {}

    # reusable methods
    def number_of_playing_players(self):
        count = 0
        for player in self.players.values():
            if player.is_playing():
                count += 1
        return count

    def deal_cards(self):
        for player in self.players.values():
            player.deal_cards(
                self.card_deck.deal_n_cards(self.cards_per_player))

    def set_player_order(self, ordered_player_keys: []):
        self.player_order = ordered_player_keys

    def rotate_player_order(self):
        self.rotate_player_order_n_times(1)

    def rotate_player_order_n_times(self, n: int):
        if n >= len(self.player_order):
            n = len(self.player_order) % n
        self.player_order = self.player_order[n:] + self.player_order[:n]

    def inverse_rotate_player_order(self):
        self.inverse_rotate_player_order_n_times(1)

    def inverse_rotate_player_order_n_times(self, n):
        size = len(self.player_order)
        if n >= size:
            n = size % n
        rotate = size-n
        self.player_order = self.player_order[rotate:] + \
            self.player_order[:rotate]

    def deal_n_cards_to_player(self, player_key, nCards: int):
        hand = self.card_deck.deal_n_cards(nCards)
        self.players[player_key].deal_cards(hand)

    def player_exists(self, player_key) -> bool:
        return player_key in self.players

    # overridable methods
    def start_game(self):
        raise NotImplementedError(
            "Implement 'start_game' in class 'CardGame'")

    def play_card(self, player_key, card):
        raise NotImplementedError(
            "Implement 'play_card' in class 'CardGame'")

    def quit(self, player_key) -> bool:
        raise NotImplementedError(
            "Implement 'quit' in class 'CardGame'")

    def player_pass(self, player):
        raise NotImplementedError(
            "Implement 'player_pass' in class 'CardGame'")

    def bet(self, player, bet):
        raise NotImplementedError(
            "Implement 'bet' in class 'CardGame'")

    def is_round_over(self) -> bool:
        raise NotImplementedError(
            "Implement 'is_round_over' from class 'CardGame'")

    def is_game_over(self) -> bool:
        raise NotImplementedError(
            "Implement 'is_game_over' from class 'CardGame'")
