# equivalent of itertools.takewhile
def takewhile(func, iterable):
    for item in iterable:
        if func(item):
            yield item
        else:
            break
