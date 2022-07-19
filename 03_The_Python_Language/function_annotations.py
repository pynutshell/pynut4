"""
>>> def f(a:'foo', b)->'bar': pass
...
>>> f.__annotations__
{'a': 'foo', 'return': 'bar'}
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    import sys
    doctest.testsource(sys.modules["__main__"], "__main__")
