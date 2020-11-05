import unittest
import sys
sys.path.insert(
    1, '/Users/joao reis/Documents/projects/python_projects/card_games/src/cards')
from card_list import CardList
from card_enums import Rank, Suit
from card import PlayingCard


class CardListTest(unittest.TestCase):

    def test_card_list_constructor(self):
        cardL = CardList()
        self.assertEqual(len(cardL.show_cards()), 0)

        cardL = CardList([PlayingCard(suit=Suit.SPADES, rank=Rank.FIVE)])
        expected_list = [PlayingCard(suit=Suit.SPADES, rank=Rank.FIVE)]

        self.assertEqual(len(cardL.show_cards()), len(expected_list))
        self.assertEqual(cardL.show_cards()[0], expected_list[0])

    def test_show_cards(self):
        list1 = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        cardl = CardList(card_list=list1)
        size = 3
        for i in range(3):
            self.assertEqual(list1[i], cardl.show_cards()[i])

    def test_similar(self):
        list1 = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        list2 = [PlayingCard(suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(
            suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]

        cardl1 = CardList(list1)
        cardl2 = CardList(list2)

        self.assertTrue(cardl1.similar(cardl2))

        list2 = [PlayingCard(suit=Suit.HEARTS, rank=Rank.JACK), PlayingCard(
            suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        cardl2 = CardList(list2)
        self.assertFalse(cardl1.similar(cardl2))

    def test_eq(self):
        list1 = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        list2 = [PlayingCard(suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(
            suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]

        cardl1 = CardList(list1)
        cardl2 = CardList(list2)

        self.assertFalse(cardl1 == cardl2)

        list2 = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        cardl2 = CardList(list2)
        self.assertTrue(cardl1 == cardl2)

    def test_size(self):
        list1 = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        cardl1 = CardList(list1)
        expected = 3
        result = cardl1.list_size()

        self.assertEqual(expected, result)

    def test_contains_card(self):
        list1 = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        cardl1 = CardList(list1)
        card1 = PlayingCard(suit=Suit.SPADES, rank=Rank.TEN)

        self.assertTrue(cardl1.contains_card(card1))

        card1 = PlayingCard(suit=Suit.SPADES, rank=Rank.THREE)
        self.assertFalse(cardl1.contains_card(card1))

    def test_deal_card(self):
        list1 = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        cardl1 = CardList(list1)
        expected = PlayingCard(suit=Suit.SPADES, rank=Rank.TEN)
        result = cardl1.deal_card()
        self.assertEqual(result, expected)

        list2 = [PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        self.assertEqual(cardl1.show_cards(), list2)

    def test_deal_n_cards(self):
        list1 = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK), PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        cardl1 = CardList(list1)
        expected = [PlayingCard(suit=Suit.SPADES, rank=Rank.TEN), PlayingCard(
            suit=Suit.DIAMONDS, rank=Rank.JACK)]
        result = cardl1.dean_n_cards(2)

        self.assertEqual(result, expected)

        list2 = [PlayingCard(suit=Suit.CLUBS, rank=Rank.EIGHT)]
        self.assertEqual(cardl1.show_cards(), list2)

    def test_add_card(self):
        cardl1 = CardList()
        card = PlayingCard(suit=Suit.SPADES, rank=Rank.QUEEN)
        cardl1.add_card(card)

        self.assertTrue(cardl1.list_size() == 1)

    def test_add_cards(self):
        card = PlayingCard(suit=Suit.SPADES, rank=Rank.QUEEN)
        card2 = PlayingCard(suit=Suit.HEARTS, rank=Rank.FOUR)
        card3 = PlayingCard(suit=Suit.CLUBS, rank=Rank.KING)

        cardl1 = CardList()
        cardl1.add_cards([card, card2])
        expected = [card, card2]
        result = cardl1.show_cards()
        self.assertEqual(result, expected)

        cardl1 = CardList([card3])
        cardl1.add_cards([card, card2])
        result = cardl1.show_cards()
        self.assertNotEqual(result, expected)
        expected = [card3, card, card2]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
