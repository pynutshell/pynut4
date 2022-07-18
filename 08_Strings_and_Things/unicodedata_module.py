'''
>>> import unicodedata
>>> unicodedata.name("🌈")
'RAINBOW'
>>> unicodedata.name("Ⅵ")
'ROMAN NUMERAL SIX'
>>> int("Ⅵ")
ValueError: invalid literal for int() with base 10: 'Ⅵ'
>>> unicodedata.numeric("Ⅵ")  # use unicodedata to get the numeric value
6.0
>>> unicodedata.lookup("MUSICAL SCORE")
'🎼'
'''


if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    import sys
    doctest.testsource(sys.modules["__main__"], "__main__")
