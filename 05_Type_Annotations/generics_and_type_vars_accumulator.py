import typing
T = typing.TypeVar('T')


class Accumulator(typing.Generic[T]):
    def __init__(self):
        self._contents: list[T] = []

    def update(self, *args: T) -> None:
        self._contents.extend(args)

    def undo(self) -> None:
        # remove last value added
        if self._contents:
            self._contents.pop()

    def __len__(self) -> int:
        return len(self._contents)

    def __iter__(self) -> typing.Iterator[T]:
        return iter(self._contents)


acc: Accumulator[int] = Accumulator()
acc.update(1, 2, 3)
print(sum(acc))  # prints 6
acc.undo()
print(sum(acc))  # prints 3


# statements that generate mypy errors
acc.update('A')
# error: Argument 1 to "update" of "Accumulator" has incompatible type "str"; expected "int"

print(''.join(acc))
# error: Argument 1 to "join" of "str" has incompatible type "Accumulator[int]"; expected "Iterable[str]"
