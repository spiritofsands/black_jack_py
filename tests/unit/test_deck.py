from unittest.mock import patch
from unittest import TestCase

from blackjack.deck import Deck
from blackjack.card import Card

_ = None

class TestDeck(TestCase):
    one_deck = 52

    def test_get_full_deck(self):

        deck = Deck.get_full_deck()
        self.assertEqual(len(deck), self.one_deck)
        for card in deck:
            self.assertIsInstance(card, Card)

    def test_get_n_decks(self):
        number = 3

        deck = Deck(number)

        self.assertEqual(len(deck.cards), self.one_deck * number)

    @patch(f'blackjack.deck.shuffle', autospec=True)
    def test_shuffle(self, shuffle_mock):
        number = 1

        deck = Deck(number)
        deck.shuffle()

        shuffle_mock.assert_called_with(deck.cards)

    def test_get_exposed(self):
        number = 1
        exposed_cards = 5

        deck = Deck(number)
        cards = deck.get(exposed=exposed_cards)

        for card in cards:
            self.assertTrue(card.exposed)

    def test_get_hidden(self):
        number = 1
        hidden_cards = 5

        deck = Deck(number)
        cards = deck.get(hidden=hidden_cards)

        for card in cards:
            self.assertFalse(card.exposed)
