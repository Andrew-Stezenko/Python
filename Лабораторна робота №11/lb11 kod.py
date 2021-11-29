import matplotlib.pyplot as plt
from numpy import *
import sympy as sp
from math import *

def taylor(x):
  y = 0
  d1 = sp.diff(f, x)
  d2 = sp.diff(d1, x)
  d3 = sp.diff(d2, x)
  print("d1=", d1, "\n" "d2=", d2, "\n" "d3=", d3)
  y += f + d1*x + d2*(x-0)**2/2 + d3*(x-0)**3/6
  print("y=", y)
  return y

x = sp.symbols("x")
y = sp.symbols("y")
f = sp.cos(x)*5
p1 = sp.plot(f, taylor(x), (x, -5, 5), label="Taylor")
plt.ledend()
plt.grid()
plt.show()
