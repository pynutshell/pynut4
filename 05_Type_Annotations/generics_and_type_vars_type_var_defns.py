import typing
import collections.abc
from abc import ABC

class MyAbstractClass(ABC): pass


# T must be one of the types listed (int, float, complex, or str)
T = typing.TypeVar('T', int, float, complex, str)
# T must be a subclass of the class MyAbstractClass
T = typing.TypeVar('T', bound=MyAbstractClass)
# T must implement __len__ to be a valid subclass of the Sized protocol
T = typing.TypeVar('T', bound=collections.abc.Sized)
