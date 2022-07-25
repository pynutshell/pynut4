"""
for x in c:
    statement(s)

is exactly equivalent to:

_temporary_iterator = iter(c)
while True:
    try:
	    x = next(_temporary_iterator)
    except StopIteration:
	    break
    statement(s)
"""

"""
>>> iterable = [1, 2]
>>> for i in iterable:
...     for j in iterable:
...         print(i, j)
...
1 1
1 2
2 1
2 2

>>> iterator = iter([1, 2])
>>> for i in iterator:
...     for j in iterator:
...         print(i, j)
...
1 2
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod()
