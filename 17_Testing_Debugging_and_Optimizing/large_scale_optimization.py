import time

def slow(it):
    result = []
    for item in it:
        result.insert(0, item)
    return result

def fast(it):
    result = []
    for item in it:
        result.append(item)
    result.reverse()
    return result

def fastest(it):
    result = list(it)
    return result


biggie = range(10 * 1000)
n_times = range(50)

def timit(afunc):
    lobi = biggie
    start = time.perf_counter()
    for x in n_times:
        afunc(lobi)
    stend = time.perf_counter()
    return '{:<10}: {:.4f}'.format(afunc.__name__, stend - start)

for fn in slow, fast, fastest, fastest, fast, slow:
    print(timit(fn))
