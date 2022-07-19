import heapq
from xml.etree import ElementTree as et


def cals_and_name():
    # memory-thrifty generator for (calories, name) pairs
    root = None
    for event, elem in et.iterparse('menu.xml', ['start', 'end']):
        if event == 'start':
            if root is None:
                root = elem
            continue
        if elem.tag != 'food':
            continue
        # just finished parsing a food, get calories and name
        cals = int(elem.find('calories').text)
        name = elem.find('name').text
        yield (cals, name)
        root.remove(elem)


lowest10 = heapq.nsmallest(10, cals_and_name())

for cals, name in lowest10:
    print(cals, name)


