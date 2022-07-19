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
>>> # use abs_tol for near-0 comparison
>>> math.isclose(0, f, abs_tol=1e-15)
True
"""