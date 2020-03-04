from unittest.mock import patch
from unittest import TestCase

from blackjack.cli import get_answer, print_header

from utils import Substr, SubstrList

_ = None
# TARGET = 'blackjack.cli'

class TestCli(TestCase):
    @patch(f'builtins.input', autospec=True)
    @patch(f'builtins.print', autospec=True)
    def test_get_answer_default(self, _print_mock, input_mock):
        positive = 'y'
        negative = 'n'
        input_mock.return_value = positive

        answer = get_answer()

        self.assertEqual(answer, positive)
        input_mock.assert_called_with(SubstrList([positive, negative]))

    @patch(f'builtins.input', autospec=True)
    @patch(f'builtins.print', autospec=True)
    def test_get_answer_custom(self, _print_mock, input_mock):
        first = 1
        last = 9
        last_str = str(last)
        first_str = str(first)
        answers = range(1, last + 1)
        input_mock.return_value = first_str

        answer = get_answer(answers)

        self.assertEqual(answer, first_str)
        input_mock.assert_called_with(SubstrList([first_str, last_str]))

    @patch(f'builtins.print', autospec=True)
    def test_print_header(self, print_mock):
        text = 'some text'

        print_header(text)

        print_mock.assert_called_with(Substr(text))
