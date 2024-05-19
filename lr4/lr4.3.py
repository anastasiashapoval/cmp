import numpy as np

A = np.matrix([[3], [1], [-1], [5], [2]])
B = np.matrix([4, 0, -2, 3, 1])
C = np.dot(A, B)

print("Результат множення:", "\n", C)