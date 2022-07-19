import fileinput
for line in fileinput.input(inplace=True):
    print(line.replace('foo', 'bar'), end='')


with fileinput.input('file1.txt', 'file2.txt') as fin:
    dostuff(fin)
