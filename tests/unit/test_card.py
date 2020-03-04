from unittest import TestCase

from blackjack.card import Card

_ = None


class TestCard(TestCase):
    def test_card_attributes(self):
        name = 'Ten'
        value = 1
        values = [value]
        suit = 'Spades'
        exposed = True

        card = Card(name, values, suit, exposed)

        self.assertEqual(card.name, name)
        self.assertEqual(card.value, value)
        self.assertEqual(card.suit, suit)

    def test_card_multiple_values(self):
        first_value = 1
        values = [first_value, 2, 3]
        exposed = True

        card = Card(_, values, _, exposed)

        self.assertIsNone(card.value)
        self.assertEqual(card.possible_values, values)
        self.assertTrue(str(value) in str(card) for value in values)

        card.value = first_value
        self.assertEqual(card.value, first_value)


    def test_value_setter(self):
        initial_value = 1
        another_value = 2
        values = [initial_value]
        exposed = True

        card = Card(_, values, _, exposed)
        card.value = another_value

        self.assertEqual(card.value, another_value)

    def test_multiple_value_setter(self):
        first_value = 1
        second_value = 2
        values = [first_value, second_value, 3]
        exposed = True

        card = Card(_, values, _, exposed)
        card.value = second_value

        self.assertEqual(card.value, second_value)

    def test_multiple_value_setter_fail(self):
        first_value = 1
        unknown_value = 9
        values = [first_value, 2, 3]
        exposed = True

        card = Card(_, values, _, exposed)
        with self.assertRaises(RuntimeError):
            card.value = unknown_value

    def test_not_exposed(self):
        values = [_]
        exposed = False

        card = Card(_, values, _, exposed)

        hidden_str = '*'
        self.assertEqual(card.name, hidden_str)
        self.assertEqual(card.value, hidden_str)
        self.assertEqual(card.suit, hidden_str)
        self.assertIn(hidden_str, str(card))

    def test_equality(self):
        name = 'Ten'
        value = [10]
        values = [value]
        suit = 'Spades'
        exposed = True

        first_card = Card(name, values, suit, exposed)
        second_card = Card(name, values, suit, exposed)

        self.assertEqual(first_card, second_card)

    def test_equality_fail_not_card(self):
        values = [_]
        first_exposed = True
        second_exposed = False

        class Temp:
            exposed = None
            name = None
            value = None
            suit = None

            def __init__(self, *_, **__):
                pass

        first_card = Card(_, values, _, first_exposed)
        second_card = Temp(_, values, _, second_exposed)

        self.assertNotEqual(first_card, second_card)

    def test_equality_fail_exposed(self):
        values = [_]
        first_exposed = True
        second_exposed = False

        first_card = Card(_, values, _, first_exposed)
        second_card = Card(_, values, _, second_exposed)

        self.assertNotEqual(first_card, second_card)

    def test_equality_fail_name(self):
        values = [_]
        first_name = 'Ten'
        second_name = 'Nine'
        exposed = True

        first_card = Card(first_name, values, _, exposed)
        second_card = Card(second_name, values, _, exposed)

        self.assertNotEqual(first_card, second_card)

    def test_equality_fail_values(self):
        first_values = [10]
        second_values = [2]
        exposed = True

        first_card = Card(_, first_values, _, exposed)
        second_card = Card(_, second_values, _, exposed)

        self.assertNotEqual(first_card, second_card)

    def test_equality_fail_suit(self):
        values = [_]
        first_suit = 'Spades'
        second_suit = 'Hearts'
        exposed = True

        first_card = Card(_, values, first_suit, exposed)
        second_card = Card(_, values, second_suit, exposed)

        self.assertNotEqual(first_card, second_card)
