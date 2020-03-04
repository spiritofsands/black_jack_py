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

    def game_loop(self):
        while True:
            self.single_game()

            print('\nGame finished')

            for player in self.players:
                if player.budget < 2:
                    print(f'Out of budget, {player.name}. Bye!')
                    self.players.remove(player)

            if not self.players:
                break

            print('\nContinue?')
            if get_answer() == 'n':
                break

    def single_game(self):
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

    def prepare_deck(self, count):
        self.deck = Deck(count)
        self.deck.shuffle()

    def make_bets(self):
        for player in self.players:
            player.make_bet()

    def deal_start_cards(self):
        for player in self.players:
            player.cards.extend(self.deck.get(exposed=2))
        self.dealer.cards.extend(self.deck.get(exposed=1, hidden=1))

    def print_participants_cards(self):
        for number, player in enumerate(self.players + [self.dealer]):
            player.print_summary()
            print('\n')

    def each_player_makes_move(self):
        for player in self.players:
            while player.determine_points() <= 21:
                action = player.make_move()
                if action == 'stand':
                    break
                player.cards.extend(self.deck.get(exposed=1))
                player.print_summary()

    def dealer_makes_move(self):
        while self.dealer.determine_points() < 17:
            self.dealer.cards.extend(self.deck.get(exposed=1))
            self.dealer.print_summary()

    def _win(self, player, multiplier=1):
        amount = player.current_bet * multiplier
        player.budget += amount
        self.dealer.budget -= amount
        print(f'\n{player.name} wins this time! (${amount})\n')

    def _lose(self, player):
        amount = player.current_bet
        player.budget -= amount
        self.dealer.budget += amount
        print(f'\n{player.name} loses this time. (${amount})\n')

    def determine_winner(self):
        dealer_points = self.dealer.determine_points()
        for player in self.players:
            player_points = player.determine_points()
            if player_points == 21 and dealer_points != 21:
                self._win(player, 2)
            elif dealer_points > 21 and player_points <= 21:
                self._win(player)
            elif player_points > 21:
                self._lose(player)
            elif player_points > dealer_points:
                self._win(player)
            elif player_points < dealer_points:
                self._lose(player)
            else:
                print(f'Push! No loses for {player.name}')
