from cards.card_hand import CardHand

#player that participates in a card game
class CardPlayer:
    def __init__(self, card_hand: CardHand = CardHand()):
        super().__init__()
        self.card_hand = card_hand

    def deal_hand(self, card_hand):
        self.card_hand.add_cards(card_hand)