import itertools as it
import operator
def set2dict(aset):
    first = operator.itemgetter(0)
    words = sorted(aset, key=first)
    adict = {}
    for initial, group in it.groupby(words, key=first):
        adict[initial] = max(group, key=len)
    return adict


word_set = set("tomorrow and tomorrow and tomorrow creeps in this petty pace from day to day".split())
print(set2dict(word_set))
