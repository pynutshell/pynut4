import pdb

def f(x):
    pdb.set_trace()
    if x > 100:
        q = x**2
    else:
        q = x
    return q

f(10)
