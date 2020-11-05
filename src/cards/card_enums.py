from enum import Enum


class DeckFormat(Enum):
    FORTY = 40
    FIFTY_TWO = 52
    FIFTY_FOUR = 54
    FIFTY_THREE = 53


class Suit(Enum):
    JOKER = 0
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    @staticmethod
    def get_all():
        return [Suit.HEARTS, Suit.CLUBS, Suit.DIAMONDS, Suit.SPADES]

    def __eq__(self, other):
        if isinstance(other, Suit):
            return self.value == other.value
        return False


class Rank(Enum):

    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    JOKER = 100

    def __eq__(self, other):
        if isinstance(other, Rank):
            return self.value == other.value
        return False

    def __gt__(self, other):
        if isinstance(other, Rank):
            return self.value > other.value
        return False

    def __lt__(self, other):
        if isinstance(other, Rank):
            return self.value < other.value
        return False

    @staticmethod
    def get_pip_ranks():
        return [Rank.ACE, Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.SIX, Rank.SEVEN, Rank.EIGHT, Rank.NINE, Rank.TEN]

    @staticmethod
    def get_court_ranks():
        return [Rank.JACK, Rank.QUEEN, Rank.KING]
