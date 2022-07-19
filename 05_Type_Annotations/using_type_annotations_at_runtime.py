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
