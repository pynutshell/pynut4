import typing

T = typing.TypeVar('T')


@typing.runtime_checkable
class SupportsUpdateUndo(typing.Protocol):
    def update(self, *args: T) -> None:
        ...

    def undo(self) -> None:
        ...


from generics_and_type_vars_accumulator import Accumulator, acc

assert issubclass(Accumulator, SupportsUpdateUndo)
assert isinstance(acc, SupportsUpdateUndo)
