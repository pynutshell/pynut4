import typing


class HouseListingDict(typing.TypedDict):
    address: str
    list_price: int
    square_footage: int
    condition: str



listing1 = HouseListingDict(
    address='123 Main',
    list_price=100_000,
    square_footage=2400,
    condition='Good',
)

print(listing1['address'])  # prints 123 Main
print(type(listing1))  # prints <class 'dict'>

# statements that generate mypy errors
listing2 = HouseListingDict(
    address='124 Main',
    list_price=110_000,
)
