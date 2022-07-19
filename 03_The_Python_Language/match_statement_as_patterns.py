"""
>>> match subject:
...     case ((0 | 1) as x) | 2: print(x)
...
Traceback (most recent call last):
  ...
SyntaxError: alternative patterns bind different names
>>> match subject:
...     case (2 | x): print(x)
...
Traceback (most recent call last):
  ...
SyntaxError: alternative patterns bind different names
>>> match 42:
...     case (1 | 2 | 42) as x: print(x)
42
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    import sys
    doctest.testsource(sys.modules["__main__"], "__main__")
