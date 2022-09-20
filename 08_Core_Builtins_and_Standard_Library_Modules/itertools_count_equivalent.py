# equivalent of itertools.count
def count(start=0, step=1):
    while True:
        yield start
        start += step
