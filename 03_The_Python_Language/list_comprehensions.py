"""
[ expression for target in iterable lc-clauses ]

lc-clauses is a series of zero or more clauses, each with one of the two forms:
    for target in iterable
or
    if expression
"""

some_sequence = [10, 20, 30]
listoflists = [[1, 2, 3], [4, 5, 6], [90, 91, 92]]

result = [x+1 for x in some_sequence]

result = []
for x in some_sequence:
    result.append(x+1)


result = [x+1 for x in some_sequence if x > 23]

result = []
for x in some_sequence:
    if x>23:
        result.append(x+1)


result = [x for sublist in listoflists for x in sublist]

result = []
for sublist in listoflists:
    for x in sublist:
        result.append(x)
