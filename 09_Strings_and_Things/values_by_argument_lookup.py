"""
>>> 'First: {} second: {}'.format(1, 'two')
'First: 1 second: two'

>>> 'Second: {1}, first: {0}'.format(42, 'two')
'Second: two, first: 42'

>>> 'a: {a}, 1st: {}, 2nd: {}, a again: {a}'.format(1, 'two', a=3)
'a: 3, 1st: 1, 2nd: two, a again: 3'
>>> 'a: {a} first:{0} second: {1} first: {0}'.format(1, 'two', a=3)
'a: 3 first:1 second: two first: 1'

>>> 'p0[1]: {[1]} p1[0]: {[0]}'.format(('zero', 'one'), ('two', 'three'))
'p0[1]: one p1[0]: two'
>>> 'p1[0]: {1[0]} p0[1]: {0[1]}'.format(('zero', 'one'), ('two', 'three'))
'p1[0]: two p0[1]: one'
>>> '{} {} {a[2]}'.format(1, 2, a=(5, 4, 3))
'1 2 3'

>>> 'First r: {.real} Second i: {a.imag}'.format(1+2j, a=3+4j)
'First r: 1.0 Second i: 4.0'
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
