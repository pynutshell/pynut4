def slower(anobject, ahugenumber):
    for i in range(ahugenumber):
        anobject.amethod(i)

# hoisting attribute lookup of method 'amethod' out of the loop
def faster(anobject, ahugenumber):
    themethod = anobject.amethod
    for i in range(ahugenumber):
        themethod(i)

def slightly_slower(asequence, adict):
    for x in asequence:
        adict[x] = hex(x)

# copying a global builtin to a local name
def slightly_faster(asequence, adict):
    myhex = hex
    for x in asequence:
        adict[x] = myhex(x)


# list comprehension compared to append and list(map(...))
import timeit, operator


def slow(asequence):
    result = []
    for x in asequence:
        result.append(-x)
    return result


def middling(asequence):
    return list(map(operator.neg, asequence))


def fast(asequence):
    return [-x for x in asequence]


for afunc in slow, middling, fast:
    timing = timeit.repeat('afunc(big_seq)',
                           setup='big_seq=range(500*1000)',
                           globals={'afunc': afunc},
                           repeat=5,
                           number=100)
    # print(f'{afunc.__name__:<10}: {timing}')
    for t in timing:
        print(f'{afunc.__name__},{t}')
