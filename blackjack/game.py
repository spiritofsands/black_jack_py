from typing import List

from blackjack.deck import Deck
from blackjack.player import Player, Dealer


class Game:
    deck: Deck
    players: List[Player]
    dealer: Dealer

    def __init__(self):
        decks = 1
        self.deck = Deck(decks)
        self.deck.shuffle()

        self.players = [Player('Bob', 500)]
        self.dealer = Dealer('Dealer', 5000)

    @property
    def all_participants(self):
        return self.players + [self.dealer]

    def start_game(self):
        self.make_bets()

        self.deal_cards()

        self.print_players_cards()

        # TODO actual code

    def make_bets(self):
        for player in self.players:
            player.make_bet()

    def deal_cards(self):
        for player in self.players:
            player.add_cards(self.deck.get(exposed=2))
        self.dealer.add_cards(self.deck.get(exposed=1, hidden=1))

    def print_players_cards(self):
        for number, player in enumerate(self.all_participants):
            print(f'{number}:===================================')
            player.print_summary()
            print('\n')
