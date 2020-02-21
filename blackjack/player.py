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

    def add_card(self, card):
        self.cards.append(card)

    def add_cards(self, cards):
        self.cards += cards

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, new_budget):
        if new_budget < 0:
            Exception('Can not go below zero budget')
        self._budget = new_budget

    def print_summary(self):
        print(f'{self.name} (${self.budget}), bet: ${self.current_bet}:')
        self.print_cards()

    def print_cards(self):
        print(f'Cards___________:')
        for card in self.cards:
            print(card)

    @property
    def undetermined_cards(self):
        return [card for card in self.cards if not card.value]

    def _ask_points(self, card):
        print(f'+--{self.name}, please determine your ace point--+')
        value = int(get_answer(card.possible_values))
        card.value = value

    def make_bet(self):
        print(f'+--{self.name}, please make your bet:--+')
        self.current_bet = int(get_answer(range(2, self.budget + 1)))

    def determine_points(self):
        undetermined_cards = self.undetermined_cards
        for card in undetermined_cards:
            self._ask_points(card)

        return sum([card.value for card in self.cards])

    def expose_cards(self):
        for card in self.cards:
            card.expose()

class Dealer(Player):
    current_bet: int = 100

    def _ask_points(self, card):
        # TODO: add logic
        value = choice(card.possible_values)
        card.value = value

    def print_summary(self):
        print(f'{self.name} (${self.budget}):')
        self.print_cards()
