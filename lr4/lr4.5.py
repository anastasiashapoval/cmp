import numpy as np

A = np.matrix([[2, 3, 4, 1], [1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]])
a_det = np.linalg.det(A)
print("Визначник:")
print(a_det)