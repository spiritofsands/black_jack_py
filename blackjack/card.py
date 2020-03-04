from typing import List


class Card:
    _value = None
    possible_values = None

    def __init__(self, name, values: List[int], suit, exposed=False):
        self._name = name
        if len(values) == 1:
            self._value = values[0]
        else:
            self.possible_values = values

        self._suit = suit
        self.exposed = exposed

    def __str__(self):
        if not self.value:
            value = ' or '.join(map(str, self.possible_values))
        else:
            value = self.value

        return (f'{self.name} of {self.suit} [{value}]' if self.exposed
                else '***')

    def __eq__(self, rhs):
        return (isinstance(rhs, Card) and
                self.exposed == rhs.exposed and
                self.name == rhs.name and
                self.value == rhs.value and
                self.suit == rhs.suit)

    @property
    def name(self):
        return self._name if self.exposed else '*'

    @property
    def value(self):
        return self._value if self.exposed else '*'

    @value.setter
    def value(self, value):
        if self.possible_values:
            if value not in self.possible_values:
                raise RuntimeError(f'Wrong value: {value} of '
                                   f'{self.possible_values}')
        self._value = value

    @property
    def suit(self):
        return self._suit if self.exposed else '*'

    def expose(self):
        self.exposed = True
        return self
