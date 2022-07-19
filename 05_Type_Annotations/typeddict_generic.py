import typing


T = typing.TypeVar('T')

class Node(typing.TypedDict, typing.Generic[T]):
    label: T
    neighbors: list[T]


n = Node(label='Acme', neighbors=['anvil', 'magnet', 'bird seed'])


# statements that generate mypy errors
n['label'] = 100
n['neighbors'].append(100)
