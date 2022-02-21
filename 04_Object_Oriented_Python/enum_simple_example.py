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


import dataclasses


@dataclasses.dataclass
class Apparel:
    size: Size
    color: Color

shirt = Apparel(Size.S, Color.RED)

# fails type check
coat = Apparel(Color.BLUE, Size.XS)

coat = Apparel(Size.XS, Color.BLUE)

class Customer:
    def __init__(self, size: Size, favorite_color: Color):
        self.size = size
        self.favorite_color = favorite_color

    def can_wear(self, item: Apparel) -> bool:
        return item.size is self.size and item.color is self.favorite_color

    def could_buy(self, inventory: list[Apparel]) -> list[Apparel]:
        return [item for item in inventory if self.can_wear(item)]


def available_colors(inventory: list[Apparel]) -> set[Color]:
    return set(item.color for item in inventory)

# fails type check
z: set[int] = available_colors([shirt, coat])
