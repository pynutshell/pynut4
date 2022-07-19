import numpy as np

a = np.arange(6).reshape(2, 3)  # a 2-d matrix
b = np.arange(3)  # a vector

a
# array([[0, 1, 2],
#        [3, 4, 5]])

a + 1  # adding a scalar
# array([[1, 2, 3],
#        [4, 5, 6]])

a + b  # adding a vector
# array([[0, 2, 4],
#        [3, 5, 7]])

a * 2  # multiplying by a scalar
# array([[0, 2, 4],
#        [6, 8, 10]])

a * b  # multiplying by a vector
# array([[0, 1, 4],
#        [0, 4, 10]])

a @ b  # matrix-multiplying by vector
# array([5, 14])

c = (a * 2).reshape(3, 2)  # using scalar multiplication to create
c  # another matrix
# array([[0, 2],
#        [4, 6],
#        [8, 10]])

a @ c  # matrix multiplying two 2-d matrices
# array([[20, 26],
#        [56, 80]])
