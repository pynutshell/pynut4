# equivalent of functools.reduce
def reduce_equiv(func,seq,init=None):
    seq = iter(seq)
    if init is None:
        init = next(seq)
    for item in seq:
        init = func(init,item)
    return init

