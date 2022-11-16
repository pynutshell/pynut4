"""
>>> import math
>>> f = 1.1 + 2.2 - 3.3  # f is intuitively equal to 0

>>> f==0
False
>>> f
4.440892098500626e-16
>>> # default tolerance is fine for this comparison
>>> math.isclose(-1, f-1)
True

>>> # near-0 comparison with default tolerances
>>> math.isclose(0, f)
False
>>> # must use abs_tol for comparison with 0
>>> math.isclose(0, f, abs_tol=1e-15)
True
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)

