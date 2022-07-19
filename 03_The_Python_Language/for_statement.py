"""
for target in iterable:
    statement(s)
"""

for letter in 'ciao':
    print(f'give me a {letter}...')


d = {'a': 0, 'b': 1, 'c': 2}
for key, value in d.items():
    if key and value:             # print only truish keys and values
        print(key, value)


prototype = [1, 'placeholder', 3]
for prototype[1] in 'xyz':
    print(prototype)
# prints [1, 'x', 3], then [1, 'y', 3], then [1, 'z', 3]


someseq = [1, 2, 3]
def process(i):
    print("?" * i)

for x in someseq:
    process(x)
print(f'Last item processed was {x}')  # potential NameError if someseq is empty