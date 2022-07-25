"""
>>> import unicodedata
>>> unicodedata.name('⚀')
'DIE FACE-1'
>>> unicodedata.name('Ⅵ')
'ROMAN NUMERAL SIX'
>>> int('Ⅵ')
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'Ⅵ'
>>> unicodedata.numeric('Ⅵ')  # use unicodedata to get the numeric value
6.0
>>> unicodedata.lookup('RECYCLING SYMBOL FOR TYPE-1 PLASTICS')
'♳'

"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
