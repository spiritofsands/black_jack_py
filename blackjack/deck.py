from typing import List
from random import shuffle

from blackjack.card import Card

class Deck:
    cards: List[Card]

    def __init__(self, decks):
        self.cards = []
        for _ in range(decks):
            self.cards += self.get_full_deck()

    @staticmethod
    def get_full_deck():
        """ Returns whole deck """

        cards = [
            {'name': 'Ace', 'value': [1, 11]},
            {'name': 'Two', 'value': [2]},
            {'name': 'Three', 'value': [3]},
            {'name': 'Four', 'value': [4]},
            {'name': 'Five', 'value': [5]},
            {'name': 'Six', 'value': [6]},
            {'name': 'Seven', 'value': [7]},
            {'name': 'Eight', 'value': [8]},
            {'name': 'Nine', 'value': [9]},
            {'name': 'Ten', 'value': [10]},
            {'name': 'Jack', 'value': [10]},
            {'name': 'Queen', 'value': [10]},
            {'name': 'King', 'value': [10]},
        ]
        suits = ['♣', '♦', '♥', '♠']

        return [Card(card['name'], card['value'], suit)
                for card in cards for suit in suits]

    def shuffle(self):
        shuffle(self.cards)

    def get(self, exposed=0, hidden=0):
        exposed_cards = [self.cards.pop().expose() for _ in range(exposed)]
        hidden_cards = [self.cards.pop() for _ in range(hidden)]
        return exposed_cards + hidden_cards
