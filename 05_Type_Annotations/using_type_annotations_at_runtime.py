"""
>>> def f(a:list[str], b) -> int:
...     pass
...
>>> f.__annotations__
{'a': list[str], 'return': <class 'int'>}
>>> class Customer:
...     name: str
...     reward_points: int = 0
...
>>> Customer.__annotations__
{'name': <class 'str'>, 'reward_points': <class 'int'>}
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
