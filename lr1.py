import numpy as np
x1 = np.sqrt(75) # Точне число sqrt(x1)
x2 = 51 / 11 # Точне число x2
x1_1 = 8.66 # Наближене число x1
x2_2 = 4.64 # Наближене число x2
def f(x, y):
 return np.abs(x - y) / np.abs(x) # формула граничної відносної похибки
rel_error_x1 = f(x1, x1_1) # обчислення відносної похибки для першої рівності
rel_error_x2 = f(x2, x2_2) # обчислення відносної похибки для другої рівності
if rel_error_x1 < rel_error_x2:
 print("Перша рівність точніше з відносною похибкою:", round(rel_error_x1, 5))
elif rel_error_x2 < rel_error_x1:
 print("Друга рівність точніше з відносною похибкою:", round(rel_error_x2,5))
else:
 print("Обидві рівності мають однакову точність з відносною похибкою:", round(rel_error_x2, 5))