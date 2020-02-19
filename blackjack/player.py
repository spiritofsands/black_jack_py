from typing import List
from random import choice

from blackjack.card import Card
from blackjack.cli import get_answer

class Player:
    name: str
    cards: List[Card]
    _budget: int
    current_bet: int

    def __init__(self, name, budget):
        self.name = name
        self.cards = []
        self._budget = budget

    def add_cards(self, cards):
        self.cards += cards

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, deposit):
        if self.budget + deposit < 0:
            Exception('Can not go below zero budget')
        self.budget += deposit

    def print_summary(self):
        print(f'{self.name} (${self.budget}), bet: ${self.current_bet}):')
        self.print_cards()

    def print_cards(self):
        print(f'Cards___________:')
        for card in self.cards:
            print(card)

    def determine_ace_points(self):
        for ace in [card for card in self.cards if card.name == 'Ace']:
            print(f'+--{self.name}, please determine your ace point--+')
            value = int(get_answer(ace.possible_values))
            ace.value = value

    def make_bet(self):
        print(f'+--{self.name}, please make your bet:--+')
        self.current_bet = int(get_answer(range(2, self.budget + 1)))


class Dealer(Player):
    current_bet: int = 100

    def determine_ace_points(self):
        for ace in [card for card in self.cards if card.name == 'Ace']:
            value = choice(ace.possible_values)
            ace.value = value

    def print_summary(self):
        print(f'{self.name} (${self.budget}):')
        self.print_cards()
