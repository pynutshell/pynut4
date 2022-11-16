"""
>>> from fractions import Fraction
>>> from decimal import Decimal
>>> Fraction(1,10)
Fraction(1, 10)
>>> Fraction(Decimal('0.1'))
Fraction(1, 10)
>>> Fraction('0.1')
Fraction(1, 10)
>>> Fraction('1/10')
Fraction(1, 10)
>>> Fraction(0.1)
Fraction(3602879701896397, 36028797018963968)
>>> Fraction(-1, 10)
Fraction(-1, 10)
>>> Fraction(-1,-10)
Fraction(1, 10)
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
