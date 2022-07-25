"""
>>> A = 100
>>> Α = 200  # this variable is GREEK CAPITAL LETTER ALPHA
>>> print(A, Α)
100 200
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
