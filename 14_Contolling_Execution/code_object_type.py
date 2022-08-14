def g(x):
    print('g', x)

code_object = g.__code__

def f(x):
    pass

f.__code__ = code_object
f(23)     # prints: g 23
