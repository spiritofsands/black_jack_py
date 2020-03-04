from unittest.mock import call, patch
from unittest import TestCase

from blackjack.card import Card
from blackjack.player import AiPlayer, Player

_ = None


class TestPlayer(TestCase):
    def test_budget(self):
        budget = 500
        prize = 100

        player = Player(_, budget)
        player.budget += prize

        self.assertEqual(player.budget, budget + prize)

    def test_budget_below_zero(self):
        budget = 500
        debt = 1000

        player = Player(_, budget)
        with self.assertRaises(RuntimeError):
            player.budget -= debt

    def test_undetermined_cards(self):
        exposed = True
        values = [_]
        cards = [Card(_, values, _, exposed),
                 Card(_, values, _, exposed)]
        undetermined_values = [1, 2]
        undetermined_cards = [Card(_, undetermined_values, _, exposed),
                              Card(_, undetermined_values, _, exposed)]

        player = Player(_, _)
        player.cards.extend(cards + undetermined_cards)

        for card in undetermined_cards:
            self.assertTrue(all(card == undetermined_card for undetermined_card
                                in player.undetermined_cards))

    @patch('blackjack.player.get_answer', autospec=True)
    @patch(f'builtins.print', autospec=True)
    def test_make_bet(self, _print_mock, get_answer_mock):
        budget = 100
        bet = 20
        get_answer_mock.return_value = bet
        player = Player(_, budget)

        player.make_bet()

        get_answer_mock.assert_called()
        self.assertEqual(player.current_bet, bet)

    @patch('blackjack.player.get_answer', autospec=True)
    @patch(f'builtins.print', autospec=True)
    def test_determine_points(self, _print_mock, get_answer_mock):
        exposed = True
        first_values = [1, 2]
        second_values = [3, 4]
        cards = [Card(_, first_values, _, exposed),
                 Card(_, second_values, _, exposed)]

        def get_answer_select(value_list):
            return value_list[0]
        get_answer_mock.side_effect = get_answer_select

        player = Player(_, _)
        player.cards.extend(cards)

        player.determine_points()

        self.assertEqual(get_answer_mock.mock_calls,
                         [call(first_values), call(second_values)])

    def test_expose_cards(self):
        exposed = False
        first_values = [1, 2]
        second_values = [3, 4]
        hidden_cards = [Card(_, first_values, _, exposed),
                        Card(_, second_values, _, exposed)]
        exposed_cards = hidden_cards.copy()
        exposed_cards = [card.expose() for card in exposed_cards]

        player = Player(_, _)
        player.cards.extend(hidden_cards)

        player.expose_cards()

        self.assertEqual(player.cards, exposed_cards)

    @patch('blackjack.player.get_answer', autospec=True)
    @patch(f'builtins.print', autospec=True)
    def test_make_move(self, _print_mock, get_answer_mock):
        player = Player(_, _)

        hit = 'hit'
        stand = 'stand'

        get_answer_numbers = [0, 1]

        def get_answer_select(value_list):
            return value_list[get_answer_numbers.pop(0)]
        get_answer_mock.side_effect = get_answer_select

        moves = [player.make_move() for _ in range(2)]

        self.assertEqual(moves, [hit, stand])


class TestAiPlayer(TestCase):
    @patch(f'builtins.print', autospec=True)
    def test_make_bet(self, _print_mock):
        budget = 100

        ai_player = AiPlayer(_, budget)

        ai_player.make_bet()

        self.assertIn(ai_player.current_bet, range(2, budget + 1))

    @patch(f'builtins.print', autospec=True)
    def test_make_bet_whole_budget(self, _print_mock):
        budget = 2

        ai_player = AiPlayer(_, budget)

        ai_player.make_bet()

        self.assertEqual(ai_player.current_bet, budget)

    def test_make_move(self):
        hit = 'hit'
        stand = 'stand'
        moves = []

        ai_player = AiPlayer(_, _)

        value = 5
        ai_player.cards = [Card(_, [value], _, exposed=True)]
        moves.append(ai_player.make_move())

        value = 18
        ai_player.cards = [Card(_, [value], _, exposed=True)]
        moves.append(ai_player.make_move())

        self.assertEqual(moves, [hit, stand])
