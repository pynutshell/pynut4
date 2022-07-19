def f():
    print('in f, before 1/0')
    1/0    # raises a ZeroDivisionError exception
    print('in f, after 1/0')

def g():
    print('in g, before f()')
    f()
    print('in g, after f()')

def h():
    print('in h, before g()')
    try:
        g()
        print('in h, after g()')
    except ZeroDivisionError:
        print('ZD exception caught')
    print('function h ends')

# Calling the h function prints the following:
# in h, before g()
# in g, before f()
# in f, before 1/0
# ZD exception caught
# function h ends
h()
