import typing

class RomanNumeral:
    """Class for representing Roman numerals and their integer values"""
    int_values = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}

    def __init__(self, label: str):
        self.label = label

    def __int__(self) -> int:
        return RomanNumeral.int_values[self.label]


movie_sequel = RomanNumeral('II')
print(int(movie_sequel))
assert issubclass(RomanNumeral, typing.SupportsInt)
assert isinstance(movie_sequel, typing.SupportsInt)
