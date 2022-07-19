def f(a, b, c=23, d=42, *x):
    print(a, b, c, d, x)
f(1,2,3,4,5,6)  # prints 1 2 3 4 (5, 6)


def f(a, b, *x, c=23, d=42):
    print(a, b, x, c, d)
f(1,2,3,4,5,6)  # prints 1 2 (3, 4, 5, 6) 23 42


def divide(divisor, dividend=94):
    return dividend // divisor
print(divide(12))                            # prints: 7
print(divide(12, 94))                        # prints: 7
print(divide(dividend=94, divisor=12))       # prints: 7


print(divide(divisor=12))                    # prints: 7


def f(middle, begin='init', end='finis'):
    return begin+middle+end
print(f('tini', end=''))                   # prints: inittini


print(f('a', 'c', 't'))                      # prints: cat


def sum_sequence(*numbers):
    return sum(numbers)

d = {'a': 1, 'b': 100, 'c': 1000}
print(sum_sequence(*d.values()))


