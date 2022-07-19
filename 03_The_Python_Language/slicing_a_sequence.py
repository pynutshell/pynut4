x = [1, 2, 3, 4]
x[1:3]                 # [2, 3]
x[1:]                  # [2, 3, 4]
x[:2]                  # [1, 2]

y = list(range(10))  #  values from 0-9
y[-5:]               #  last five items
# [5, 6, 7, 8, 9]
y[::2]               #  every other item
# [0, 2, 4, 6, 8]
y[10:0:-2]           #  every other item, in reverse order
# [9, 7, 5, 3, 1]
y[:0:-2]             #  every other item, in reverse order (simpler)
# [9, 7, 5, 3, 1]
y[::-2]              #  every other item, in reverse order (best)
# [9, 7, 5, 3, 1]
