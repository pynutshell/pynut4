"""
>>> '{:,}'.format(12345678)
'12,345,678'

"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    import sys
    doctest.testsource(sys.modules["__main__"], "__main__")
