import functools


def announce(f):
    @functools.wraps(f)
    def wrap(*a, **k):
        print(f'Calling {f.__name__}')
        return f(*a, **k)

    return wrap

@announce
def f1():
    print("f1 doing work")

f1()
