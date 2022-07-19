"""
>>> from decimal import Decimal
>>> df = Decimal(0.1)
>>> df
Decimal('0.1000000000000000055511151231257827021181583404541015625')

>>> ds = Decimal(str(0.1))  # or, directly, Decimal('0.1')
>>> ds
Decimal('0.1')

def dfs(x):
    return Decimal(str(x))

>>> dq = Decimal(0.1).quantize(Decimal('.00'))
>>> dq
Decimal('0.10')

>>> pidigits = (3, 1, 4, 1, 5)
>>> Decimal((1, pidigits, -4))
Decimal('-3.1415')

>>> import math
>>> a = 1.1
>>> d = Decimal('1.1')
>>> a == d
False
>>> math.isclose(a, d)
True
>>> a + d
Traceback (most recent call last):
  ...
TypeError: unsupported operand type(s) for +: 'float' and 'decimal.Decimal'
>>> d + Decimal(a) # new decimal constructed from a
Decimal('2.200000000000000088817841970')
>>> d + Decimal(str(a)) # convert a to decimal with str(a)
Decimal('2.2')
"""