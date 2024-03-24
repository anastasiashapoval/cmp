import math
import numpy as np
from scipy.misc import derivative
import numdifftools as nd

def f(x):
 return 4*pow(x, 4) + 4*pow(x,3) - 6*pow(x, 2) - 9*x - 1

eps=0.0001

def find_segments(): #відокремлюємо корені
 search_range = np.arange(-10, 10, 1)
 
 a = None
 previous_x = None
 current_x = None
 segments = []

 for x in search_range:
  x = round(x, 4)
  current_x = f(x)
  if previous_x != None and previous_x * current_x < 0:
   segments.append((a, x))
  a = x
  previous_x = current_x
 return segments

segments = find_segments()
for a, b in segments:
 print(f'Found segment: [{a}, {b}]')

def rec(a, b, eps): # метод половинного ділення
 while (abs(a - b) > eps):
  if f(a) * f((a + b) / 2) < 0:
   b = (a + b) / 2
  else:
   a = (a + b) / 2
  x = (a + b) / 2
 print('x= ', round(x, 5), ' - Half division method')

def hord(a, b, eps): # метод хорд
 derivative_f = nd.Derivative(f, n=1)
 if f(a) * derivative_f(a) > 0:
  x0 = a
  xi = b
 else:
  x0 = b
  xi = a
 xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
 while (abs(xi_1 - xi) > eps):
  xi = xi_1
  xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
 print('x= ', round(xi_1, 5), ' - Chord method')

a=-1 
b=0 
a1=1.
b1=2.

print (f'Solution of a nonlinear equation on a segment [{a}, {b}]')
rec (a,b,eps) 
hord (a,b,eps) 
print (f'Solution of a nonlinear equation on a segment [{a1}, {b1}]')
rec (a1,b1,eps) 
hord (a1,b1,eps)