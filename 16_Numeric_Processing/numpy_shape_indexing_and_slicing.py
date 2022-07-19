import numpy as np

a = np.arange(8)
a
# array([0, 1, 2, 3, 4, 5, 6, 7])

a = a.reshape(2, 4)
a
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]])

print(a[1, 2])
# 6

a[:, :2]
# array([[0, 1],
#        [4, 5]])

for row in a:
    print(row)
# [0 1 2 3]
# [4 5 6 7]

for row in a:
    for col in row[:2]:  # first two items in each row
        print(col)
# 0
# 1
# 4
# 5
