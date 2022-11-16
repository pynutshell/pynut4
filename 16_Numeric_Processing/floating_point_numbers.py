"""
>>> f = 1.1 + 2.2 - 3.3  # f should be equal to 0
>>> f
4.440892098500626e-16

>>> f = 2**53
>>> f
9007199254740992
>>> # integer arithmetic is not bounded
>>> f + 1
9007199254740993
>>> # conversion to float loses integer precision at 2**53
>>> f + 1.0
9007199254740992.0
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
