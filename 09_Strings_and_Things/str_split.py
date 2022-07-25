"""
>>> x = 'a  b'  # two spaces between a and b
>>> x.split()   # or x.split(None)
['a', 'b']
>>> x.split(' ')
['a', '', 'b']
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod()
