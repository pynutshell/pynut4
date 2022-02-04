def showdoc(f):
    if f.__doc__:
        print(f'{f.__name__}: {f.__doc__}')
    else:
        print(f'{f.__name__}: No docstring!')
    return f


@showdoc
def f1():
    """a docstring"""  # prints: f1: a docstring


@showdoc
def f2():
    pass  # prints: f2: No docstring!

f1()
f2()
