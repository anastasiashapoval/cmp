import numpy as np

A = np.matrix([[1, 1, 1, 1], [1, 1, -1, -1], 
              [1, -1, 1, -1], [1, -1, -1, 1]])
A_inv = np.linalg.inv(A)
print("Обернена матриця:")
print(A_inv)