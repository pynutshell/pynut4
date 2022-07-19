import typing


class HouseListingTuple(typing.NamedTuple):
    address: str
    list_price: int
    square_footage: int = 0
    condition: str = 'Good'


listing1 = HouseListingTuple(
    address='123 Main',
    list_price=100_000,
    square_footage=2400,
    condition='Good',
)

print(listing1.address)  # prints 123 Main
print(type(listing1))  # prints <class 'HouseListingTuple'>


# statements that generate mypy errors
listing2 = HouseListingTuple(
    '123 Main',
)
# raises a runtime error TypeError: HouseListingTuple.__new__() missing 1 required positional argument: 'list_price'
