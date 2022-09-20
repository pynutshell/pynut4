# equivalent of itertools.dropwhile
def dropwhile(func, iterable):
    iterator = iter(iterable)
    for item in iterator:
        if not func(item):
            yield item
            break
    for item in iterator:
        yield item

