"""
>>> s = 'a string'
>>> '{:^12s}'.format(s)
'  a string  '
>>> '{:.>12s}'.format(s)
'....a string'

>>> '{:.>{}s}'.format(s, 20)
'............a string'

"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    import sys
    doctest.testsource(sys.modules["__main__"], "__main__")
