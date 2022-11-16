"""
>>> import math
>>> math.atan(-1./-1.)
0.7853981633974483
>>> math.atan2(-1., -1.)
-2.356194490192345
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
