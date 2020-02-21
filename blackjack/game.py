from typing import List

from blackjack.deck import Deck
from blackjack.cli import get_answer, print_header


class Game:
    deck: Deck

    def __init__(self, players, dealer):
        self.players = players
        self.dealer = dealer

    def clean_cards(self):
        for player in self.players:
            player.cards = []
        self.dealer.cards = []

    def start_game(self):
        print_header('Make your bets')
        self.make_bets()

        print_header('Preparing the deck')
        self.prepare_deck(1)

        print_header('Dealing cards')
        self.clean_cards()
        self.deal_start_cards()

        self.print_participants_cards()

        print_header('Make your moves')
        self.each_player_makes_move()

        self.print_participants_cards()

        print_header('Dealer exposes cards')
        self.dealer.expose_cards()

        self.print_participants_cards()

        self.dealer_makes_move()

        print_header('Game end state:')
        self.print_participants_cards()

        print_header('Winners')
        self.determine_winner()

        # TODO actual code

    def prepare_deck(self, count):
        self.deck = Deck(count)
        self.deck.shuffle()

    def make_bets(self):
        for player in self.players:
            player.make_bet()

    def deal_start_cards(self):
        for player in self.players:
            player.add_cards(self.deck.get(exposed=2))
        self.dealer.add_cards(self.deck.get(exposed=1, hidden=1))

    def print_participants_cards(self):
        for number, player in enumerate(self.players + [self.dealer]):
            player.print_summary()
            print('\n')

    def each_player_makes_move(self):
        for player in self.players:
            while player.determine_points() <= 21:
                action = get_answer(['hit', 'stand'])
                if action == 'stand':
                    break
                player.add_cards(self.deck.get(exposed=1))
                player.print_summary()

    def dealer_makes_move(self):
        while self.dealer.determine_points() < 17:
            self.dealer.add_cards(self.deck.get(exposed=1))
            self.dealer.print_summary()

    def determine_winner(self):
        dealer_points = self.dealer.determine_points()
        for player in self.players:
            player_points = player.determine_points()
            # TODO: refine
            if 21 >= player_points > dealer_points:
                amount = player.current_bet * 2
                print(f'\n{player.name} wins ${amount}!\n')
            else:
                amount = -player.current_bet
                print(f'\n{player.name} loses, ${amount}.\n')

            player.budget += amount
