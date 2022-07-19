def f(a, *, b, c=56):    # b and c are keyword-only
    return a, b, c
f(12,b=34)  # returns (12, 34, 56) – c's optional, since it has a default
f(12)       # raises a TypeError exception, since you didn’t pass `b`:
# error message is: missing 1 required keyword-only argument: 'b'


def g(x, *a, b=23, **k):   # b is keyword-only
    return x, a, b, k

print(g(1, 2, 3, c=99))  # returns (1, (2, 3), 23, {'c': 99})
