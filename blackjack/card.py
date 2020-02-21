class Card:
    _value = None
    possible_values = None

    def __init__(self, name, values, suit, exposed=False):
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

    @property
    def name(self):
        return self._name if self.exposed else '*'

    @property
    def value(self):
        return self._value if self.exposed else '*'

    @value.setter
    def value(self, value):
        if value not in self.possible_values:
            raise Exception('Wrong value')
        self._value = value

    @property
    def suit(self):
        return self._suit if self.exposed else '*'

    def expose(self):
        self.exposed = True
        return self
