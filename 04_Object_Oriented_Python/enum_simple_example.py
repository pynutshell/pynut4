from enum import Enum, auto


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    XS = auto()
    S = auto()
    M = auto()
    L = auto()


# these improper comparisons and expressions raise
# TypeError exceptions
print(Color.RED > Size.XS)
print(Size.L * Color.BLUE)
