"""
>>> name = 'Dawn'
>>> print('{name!r} is {l} characters long'
...       .format(name=name, l=len(name)))
'Dawn' is 4 characters long

>>> print(f'{name!r} is {len(name)} characters long')
'Dawn' is 4 characters long

>>> for width in 8, 11:
...     for precision in 2, 3, 4, 5:
...         print(f'{3.14159:{width}.{precision}}')
...
     3.1
    3.14
   3.142
  3.1416
        3.1
       3.14
      3.142
     3.1416

>>> a = '*-'
>>> s = 12
>>> f'{a*s=}'
"a*s='*-*-*-*-*-*-*-*-*-*-*-*-'"
>>> f'{a*s = :30}'
'a*s = *-*-*-*-*-*-*-*-*-*-*-*-      '

"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    import sys
    doctest.testsource(sys.modules["__main__"], "__main__")
