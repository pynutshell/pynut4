# equivalent of itertools.islice
def islice(iterable, start, stop, step=1):
    en = enumerate(iterable)
    n = stop
    for n, item in en:
        if n>=start:
            break
    while n<stop:
        yield item
        for x in range(step):
            n, item = next(en)
