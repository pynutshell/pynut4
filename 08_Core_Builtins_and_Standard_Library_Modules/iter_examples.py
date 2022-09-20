
# equivalent of iter(sequence) when sequence does not implement __iter__
def iter_sequence(obj):
    i = 0
    while True:
        try:
            yield obj[i]
        except IndexError:
            raise StopIteration
        i += 1


# equivalent of iter(func, sentinel)
def iter_sentinel(func, sentinel):
    while True:
        item = func()
        if item == sentinel:
            raise StopIteration
        yield item

