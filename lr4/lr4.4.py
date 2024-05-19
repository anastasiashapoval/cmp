import numpy as np

A = np.matrix([[1, 5, -5], [4, 0, 3], [2, -10, 3]])
a_det = np.linalg.det(A)
print("Визначник:")
print(format(a_det,'.9g'))