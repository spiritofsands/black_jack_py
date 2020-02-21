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
        current_bet_str = (f', bet: ${self.current_bet}' if self.current_bet
                           else '')
        print(f'{self.name} (${self.budget}){current_bet_str}:')
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

    def make_move(self):
        return get_answer(['hit', 'stand'])


class AiPlayer(Player):
    current_bet: int = 0

    def _ask_points(self, card):
        points = sum(card.value for card in self.cards if card not in
                     self.undetermined_cards)
        max_possible_points = max(card.possible_values)
        possible_points = points + max_possible_points
        if 17 >= possible_points <= 21:
            value = max_possible_points
        else:
            value = min(card.possible_values)
        card.value = value

    def make_bet(self):
        self.current_bet = (2 + self.budget) // 2

    def make_move(self):
        return choice(['hit', 'stand'])
