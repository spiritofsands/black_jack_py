from unittest.mock import patch
from unittest import TestCase

from blackjack.card import Card
from blackjack.player import AiPlayer, Player
from blackjack.game import Game

_ = None


class TestGameScenarios(TestCase):
    @patch('blackjack.game.Game.deal_start_cards', autospec=True)
    @patch('blackjack.player.Player.make_bet', autospec=True)
    @patch('blackjack.player.Player.make_move', autospec=True)
    @patch('blackjack.player.AiPlayer.make_move', autospec=True)
    @patch('builtins.print', autospec=True)
    def test_player_wins(self, _print_mock, ai_player_make_move_mock,
                         player_make_move_mock,
                         player_make_bet_mock, deal_start_cards_mock):

        player_cards = [
            Card('Ten', [10], '♣', exposed=True),
            Card('Ten', [10], '♦', exposed=True),
        ]
        dealer_cards = [
            Card('One', [1], '♣', exposed=True),
            Card('One', [1], '♦', exposed=False),
        ]

        def deal(self):
            for player in self.players:
                player.cards.extend(player_cards)
            self.dealer.cards.extend(dealer_cards)

        deal_start_cards_mock.side_effect = deal

        budget = 500
        player = Player('Bob', budget)
        players = [player]
        dealer = AiPlayer('Dealer', 5000)

        bet = 100

        def make_bet(self):
            self.current_bet = bet
        player_make_bet_mock.side_effect = make_bet

        stand = 'stand'
        player_make_move_mock.return_value = stand
        ai_player_make_move_mock.return_value = stand

        game = Game(players, dealer)
        game.single_game()

        self.assertEqual(player.budget, budget + bet)

    @patch('blackjack.game.Game.deal_start_cards', autospec=True)
    @patch('blackjack.player.Player.make_bet', autospec=True)
    @patch('blackjack.player.Player.make_move', autospec=True)
    @patch('blackjack.player.AiPlayer.make_move', autospec=True)
    @patch('builtins.print', autospec=True)
    def test_player_loses(self, _print_mock,
                         ai_player_make_move_mock, player_make_move_mock,
                         player_make_bet_mock, deal_start_cards_mock):

        player_cards = [
            Card('One', [1], '♣', exposed=True),
            Card('One', [1], '♦', exposed=True),
        ]
        dealer_cards = [
            Card('Ten', [10], '♣', exposed=True),
            Card('Ten', [10], '♦', exposed=False),
        ]

        def deal(self):
            for player in self.players:
                player.cards.extend(player_cards)
            self.dealer.cards.extend(dealer_cards)

        deal_start_cards_mock.side_effect = deal

        budget = 500
        player = Player('Bob', budget)
        players = [player]
        dealer = AiPlayer('Dealer', 5000)

        bet = 100

        def make_bet(self):
            self.current_bet = bet
        player_make_bet_mock.side_effect = make_bet

        stand = 'stand'
        player_make_move_mock.return_value = stand
        ai_player_make_move_mock.return_value = stand

        game = Game(players, dealer)
        game.single_game()

        self.assertEqual(player.budget, budget - bet)

    @patch('blackjack.game.Game.deal_start_cards', autospec=True)
    @patch('blackjack.player.Player.make_bet', autospec=True)
    @patch('blackjack.player.Player.make_move', autospec=True)
    @patch('blackjack.player.AiPlayer.make_move', autospec=True)
    @patch('builtins.print', autospec=True)
    def test_player_push(self, _print_mock,
                         ai_player_make_move_mock, player_make_move_mock,
                         player_make_bet_mock, deal_start_cards_mock):

        player_cards = [
            Card('One', [10], '♣', exposed=True),
            Card('One', [10], '♦', exposed=True),
        ]
        dealer_cards = [
            Card('Ten', [10], '♣', exposed=True),
            Card('Ten', [10], '♦', exposed=False),
        ]

        def deal(self):
            for player in self.players:
                player.cards.extend(player_cards)
            self.dealer.cards.extend(dealer_cards)

        deal_start_cards_mock.side_effect = deal

        budget = 500
        player = Player('Bob', budget)
        players = [player]
        dealer = AiPlayer('Dealer', 5000)

        bet = 100

        def make_bet(self):
            self.current_bet = bet
        player_make_bet_mock.side_effect = make_bet

        stand = 'stand'
        player_make_move_mock.return_value = stand
        ai_player_make_move_mock.return_value = stand

        game = Game(players, dealer)
        game.single_game()

        self.assertEqual(player.budget, budget)

    @patch('blackjack.game.Game.single_game', autospec=True)
    @patch('builtins.print', autospec=True)
    def test_game_loop_out_of_budget(self, _print_mock,
                                     single_game_mock):
        budget = 500
        player = Player('Bob', budget)
        players = [player]
        dealer = AiPlayer('Dealer', 5000)

        def single_game(self):
            for player in self.players:
                player.budget = 0
        single_game_mock.side_effect = single_game

        game = Game(players, dealer)
        game.game_loop()

        self.assertFalse(game.players)

    @patch('blackjack.game.Game.single_game', autospec=True)
    @patch('blackjack.game.get_answer', autospec=True)
    @patch('builtins.print', autospec=True)
    def test_game_loop_no_continue(self, _print_mock,
                                   get_answer_mock,
                                   single_game_mock):
        budget = 500
        player = Player('Bob', budget)
        players = [player]
        dealer = AiPlayer('Dealer', 5000)

        def single_game(self):
            for player in self.players:
                player.budget = 0
        single_game_mock.side_effect = single_game
        get_answer_mock.return_value = 'n'

        game = Game(players, dealer)
        game.game_loop()

        self.assertFalse(game.players)
