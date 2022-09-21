
# slow
big_string = ''
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    piece = letter*10
    big_string += piece

# fast
temp_list = [letter*10 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
big_string = ''.join(temp_list)


# string formatting

x, y, k = "scrambled two juicy".split()
# slow (and hard to read)
oneway = str(x) + ' eggs and ' + str(y) + ' slices of ' + k + ' ham'

# faster
another = '{} eggs and {} slices of {} ham'.format(x, y, k)
yetanother = f'{x} eggs and {y} slices of {k} ham'


print(oneway)
print(another)
print(yetanother)