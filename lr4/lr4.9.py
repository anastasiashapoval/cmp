import numpy as np

N = int(input("Кількість рядків: "))
M = int(input("Кількість стовпчиків: "))

A = np.random.randint(low = 0, high = 20, size = (N, M))

def min_avg(matrix):
    row_avg = np.mean(matrix, axis=1) # середні значення по рядкам
    m_a = np.min(row_avg) # найменше середнє значення
    return m_a

min_average = min_avg(A)

print(A)
print("Найменше середнє значення серед рядків: ", min_average)

