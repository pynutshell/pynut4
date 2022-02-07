def slower(anobject, ahugenumber):
    for i in range(ahugenumber): anobject.amethod(i)

# hoisting attribute lookup of method 'amethod' out of the loop
def faster(anobject, ahugenumber):
    themethod = anobject.amethod
    for i in range(ahugenumber): themethod(i)

def slightly_slower(asequence, adict):
    for x in asequence: adict[x] = hex(x)

# copying a global builtin to a local name
def slightly_faster(asequence, adict):
    myhex = hex
    for x in asequence: adict[x] = myhex(x)


# list comprehension compared to append and list(map(...))
import time, operator


def slow(asequence):
    result = []
    for x in asequence:
        result.append(-x)
    return result


def middling(asequence):
    return list(map(operator.neg, asequence))


def fast(asequence):
    return [-x for x in asequence]


biggie = range(500 * 1000)
n_times = [None] * 50


def timit(afunc):
    lobi = biggie
    start = time.perf_counter()
    for x in n_times: afunc(lobi)
    stend = time.perf_counter()
    return '{:<10}: {:.4f}'.format(afunc.__name__, stend - start)


for afunc in slow, middling, fast, fast, middling, slow:
    print(timit(afunc))
