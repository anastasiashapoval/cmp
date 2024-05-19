import numpy as np

A = np.matrix([[1, -1, 3, 4], [0, -1, 2, 1], 
              [1, 1, -1, 2], [2, 3, -5, 3]])
rank = np.linalg.matrix_rank(A)
print("Ранг матриці:")
print(rank)