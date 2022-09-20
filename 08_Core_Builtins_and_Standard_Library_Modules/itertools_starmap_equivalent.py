# equivalent of itertools.starmap
def starmap(func, iterable):
    for item in iterable:
        yield func(*item)
