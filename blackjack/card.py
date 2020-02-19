class Card:
    def __init__(self, name, values, suit, exposed=False):
        self._name = name
        self._values = values

        self._selected_value = None
        if len(self._values) == 1:
            self._selected_value = self._values[0]
        # else user-determined

        self._suit = suit
        self.exposed = exposed

    def __str__(self):
        return (f'{self.name} of {self.suit} [{self.value}]' if self.exposed
                else '***')

    @property
    def name(self):
        return self._name if self.exposed else '*'

    @property
    def value(self):
        if self._selected_value:
            value = self._selected_value
        else:
            if len(self._values) > 1:
                value = ' or '.join(map(str, self._values))
            else:
                value = self._values

        return value if self.exposed else '*'

    @value.setter
    def value(self, value):
        if value not in self._values:
            raise Exception('Wrong value')
        self._selected_value = value

    @property
    def suit(self):
        return self._suit if self.exposed else '*'

    @property
    def possible_values(self):
        return self._values if self.exposed else '*'

    def expose(self):
        self.exposed = True
        return self

    @property
    def no_value_selected(self):
        return not self._selected_value
