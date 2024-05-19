import numpy as np

#Матричний метод
def matrix_method(coefficients, constants):
 inverse_matrix = np.linalg.inv(coefficients)
 return np.dot(inverse_matrix, constants)

#Метод Крамера
def cramer_method(coefficients, constants):
 det_coefficients = np.linalg.det(coefficients)
 solutions = []
 for i in range(len(coefficients)):
  modified_coefficients = np.copy(coefficients)
  modified_coefficients[:, i] = constants
  solutions.append(round(np.linalg.det(modified_coefficients) / det_coefficients, 1)) 
 return solutions

#Метод Гауса
def gauss_method(a, b):
 n = len(b)
 for k in range(0, n-1):
  for i in range(k+1, n):
   if a[i, k] != 0.0:
    lam = a[i, k] / a[k, k]
    a[i, k+1:n] = a[i, k+1:n] - lam * a[k, k+1:n]
    b[i] = b[i] - lam * b[k]
 x = np.zeros(n)
 for k in range(n-1, -1, -1):
  x[k] = (b[k] - np.dot(a[k, k+1:n], x[k+1:n])) / a[k, k]
 return x
def main():
 A = np.array([[2, -1, 1],
              [3, 4, -2],
              [1, -3, 1]])
 B = np.array([5, -3, 4])
 
 # Матричний метод
 X_matrix = matrix_method(A, B)
 print("Матричний метод:", X_matrix)
 
 # Метод Крамера
 X_cramer = cramer_method(A, B)
 print("Метод Крамера:", X_cramer)
 
 # Метод Гауса
 X_gauss = gauss_method(A, B)
 print("Метод Гауса:", X_gauss)

 # Перевірка solve():
 X_solve = np.linalg.solve(A, B)
 print("Перевірка з solve():", X_solve)

if __name__ == "__main__":
 main()

