def f(x, y):
    x = 23
    y.append(42)

a = 77
b = [99]
f(a, b)
print(a, b)             # prints: 77 [99, 42]
