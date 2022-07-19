"""
identifier: type_specification

type_specifier[type_parameter, ...]
"""
import typing

# an int
count: int

# a list of ints, with a default value
counts: list[int] = []

# a dict with str keys, and values which are tuples containing 2 ints and a str
employee_data: dict[str, tuple[int, int, str]]

# a callable taking a single str or bytes argument and returning a bool
str_predicate_function: typing.Callable[[str | bytes], bool]

# a dict with str keys, whose values are functions that take and return an int
str_function_map: dict[str, typing.Callable[[int], int]] = {
    'square': lambda x: x * x,
    'cube': lambda x: x * x * x,
}


"""
def identifier(argument, ...) -> type_specification :

identifier: type_specification = default_value
"""

def pad(a: list[str], minimum_len: int = 1, padstr: str = ' ') -> list[str]:
    """
    Given a list of strings and a minimum length, return a copy of the list
    extended with empty strings to be at least the minimum length.
    """
    return a + ([padstr] * (minimum_len - len(a)))

print(pad(["A", "B"], minimum_len=4))