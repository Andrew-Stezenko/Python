from numpy import *
import matplotlib.pyplot as plt
x = linspace(0, 10, 51)
y = x**cos(x**2)
plt.plot(x, y, "f-.", lable= "x^cos(x^2)")
plt.axis([0, 10, 0, 10])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Лабораторна робота №7")
plt.legend()
plt.grid()
plt.show()