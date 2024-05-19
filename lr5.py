import numpy as np
import matplotlib.pyplot as plt

x_min, x_max = -3, 3
y_min, y_max = -3, 3
step = 0.01

x, y = np.meshgrid(np.arange(x_min, x_max, step),
                   np.arange(y_min, y_max, step))

eq1 = np.sin(y + 2) - x - 1.5
eq2 = y + np.cos(x - 2) - 0.5

fig, ax = plt.subplots(figsize=(10, 10))

ax.contour(x, y, eq1, levels=[0], colors='red')

ax.contour(x, y, eq2, levels=[0], colors='blue')

ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Графік системи рівнянь')
plt.grid(True)

plt.show()

#Розв'язок системи рівнянь методом простої ітерації
import numpy as np
from scipy import optimize
from scipy.misc import derivative
import math

x0 = -1.7
y0 = 1.35
delta = 0.1

def f1(y):
    return math.sin(y + 2) - 1.5 #задаємо функції
def f2 (x):
    return 0.5 - math.cos(x - 2) #задаємо функції
 
def iter (x,y,e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print ('Проста ітерація:')
    print ('x=', xn, '\ny=',yn,'\nКількість ітерацій = ',n)
iter(x0,y0,0.0001)

def f3(x): #Задаємо функцію для перевірки
    return math.sin(x[0] + 2) - x[1] - 1.5, x[0] + math.cos(x[1] - 2) - 0.5
s = optimize.root(f3, [0.,0.], method = 'hybr') #Перевірка розв*язку      #Відповіді мають співпасти
print ('Перевірка: ',s.x)
