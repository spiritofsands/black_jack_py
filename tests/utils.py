class ArgChecker:
    def __init__(self, checker):
        self._checker = checker

    def __eq__(self, rhs):
        return bool(self._checker(rhs))

class Substr(ArgChecker):
    """ Helper class to check that argument contains any specified values
    from the list """
    def __init__(self, str_):
        super().__init__(
            lambda arg: str_ in arg
        )
class SubstrList(ArgChecker):
    """ Helper class to check that argument contains any specified values
    from the list """
    def __init__(self, str_list):
        super().__init__(
            lambda arg: all(str_ in arg for str_ in str_list)
        )
