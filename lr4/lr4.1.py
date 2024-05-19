import numpy as np

A = np.matrix([[2, 3, 1], [-1, 1, 0], [1, 2, -1]])
B = np.matrix([[1, 2, 1], [0, 1, 2], [3, 1, 1]])
AB = np.dot(A, B)
BA = np.dot(B, A)
C = np.subtract(AB, BA)

print("A:", "\n", A, "\n")
print("B:", "\n", B, "\n")
print("C = AB - BA = ", "\n", C)

