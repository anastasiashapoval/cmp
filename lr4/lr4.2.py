import numpy as np

A = np.matrix([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])
B = np.dot(A, A)

print(A)
print("A^2:", "\n", B)