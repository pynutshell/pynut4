import numpy as np

np.array([1, 2, 3, 4])  # from a Python list
# array([1, 2, 3, 4])

# a common error: passing items separately (they
# must be passed as a sequence, e.g. a list)
np.array(5, 6, 7)

s = 'alph', 'abet'  # a tuple of two strings
np.array(s)
# array(['alph', 'abet'], dtype='<U4')

t = [(1, 2), (3, 4), (0, 1)]  # a list of tuples
np.array(t, dtype='float64')  # explicit type designation
# array([[1., 2.],
#        [3., 4.],
#        [0., 1.]]

x = np.array(1.2, dtype=np.float16)  # a scalar
x.shape
# ()
x.max()
# 1.2

np.zeros(3)  # shape defaults to a vector
# array([0., 0., 0.])

np.ones((2, 2))  # with shape specified
# array([[1., 1.],
#        [1., 1.]])

np.empty(9)  # arbitrary float64s
# array([4.94065646e-324, 9.88131292e-324, 1.48219694e-323,
#        1.97626258e-323, 2.47032823e-323, 2.96439388e-323,
#        3.45845952e-323, 3.95252517e-323, 4.44659081e-323])

np.indices((3, 3))
# array([[[0, 0, 0],
#         [1, 1, 1],
#         [2, 2, 2]],
#
#        [[0, 1, 2],
#         [0, 1, 2],
#         [0, 1, 2]]])

np.arange(0, 10, 2)  # upper bound excluded
# array([0, 2, 4, 6, 8])

np.linspace(0, 1, 5)  # default: endpoint included
# array([0., 0.25, 0.5, 0.75, 1.])

np.linspace(0, 1, 5, endpoint=False)  # endpoint not included
# array([0., 0.2, 0.4, 0.6, 0.8])

import io

np.genfromtxt(io.BytesIO(b'1 2 3\n4 5 6'))  # using a pseudo-file
# array([[1., 2., 3.],
#        [4., 5., 6.]])

with io.open('x.csv', 'wb') as f:
    f.write(b'2,4,6\n1,3,5')
np.genfromtxt('x.csv', delimiter=',')  # using an actual CSV file
# array([[2., 4., 6.],
#        [1., 3., 5.]])
