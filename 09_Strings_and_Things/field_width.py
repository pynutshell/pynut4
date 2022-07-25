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
    doctest.testmod(verbose=True, exclude_empty=True)
