from cards.card_hand import CardHand
from player_state import PlayerStateEnum
from cards.card import PlayingCard
from cards.card_enums import Rank, Suit

# player that participates in a card game


class CardPlayer:
    def __init__(self, card_hand: CardHand = CardHand(), player_state: PlayerStateEnum = PlayerStateEnum.PLAYING, points: int = 0):
        super().__init__()
        self.card_hand = card_hand
        self.player_state = player_state
        self.points = points

    def deal_cards(self, card_hand: [PlayingCard]):
        self.card_hand.add_cards(card_hand)

    def add_points(self, points) -> int:
        self.points += points
        return self.points

    def subtract_points(self, points) -> int:
        self.points -= points
        return self.points

    def current_points(self) -> int:
        return self.points

    def quit(self):
        self.player_state = PlayerStateEnum.QUIT

    def play_card(self, card: PlayingCard) -> bool:
        return self.card_hand.remove_card(card)

    def has_card(self, card: PlayingCard) -> bool:
        return self.card_hand.contains_card(card)

    def contains_card_of_suit(self, suit: Suit) -> bool:
        return self.card_hand.contains_card_of_suit(suit)

    def contains_card_of_rank(self, rank: Rank) -> bool:
        return self.card_hand.contains_card_of_rank(rank)

    def is_playing(self) -> bool:
        return self.player_state == PlayerStateEnum.PLAYING

    def pass_turn(self):
        self.player_state = PlayerStateEnum.PASS
