"""
>>> f = 1
>>> while f != 0:
...     f -= 0.2  # even though f started as int, it's now a float
...     if isinstance(f, float): break

>>> # This code shows why:
>>> 1 - 0.2 - 0.2 - 0.2 - 0.2 - 0.2  # should be 0, but...
5.551115123125783e-17


>>> f = 1
>>> count = 0
>>> while f > 0:
...     count += 1
...     f -= 0.2
>>>  # 1 time too many!
>>> print(count)
6

>>> import math
>>>
>>> f = 1
>>> count = 0
>>> while not math.isclose(0, f, abs_tol=1e-15):
...     count += 1
...     f -= 0.2
>>> # just right this time!
>>> print(count)
5
"""