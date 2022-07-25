"""
>>> for sequence in (["one", "two", "three"], range(2), range(6)):
...     match sequence:
...         case  (first, *vars, last): print(first, vars, last)
one ['two'] three
0 [] 1
0 [1, 2, 3, 4] 5
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
