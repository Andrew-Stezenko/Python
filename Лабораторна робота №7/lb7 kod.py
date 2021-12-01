import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
x = [-2, -1, 0, 1]
y = [-7, 4, 1, 2]
spl = UnivariateSpline(x, y)
xs = linspace(-2, 2, 1000)
plt.plot(x,y, "ro", xs, spl(xs), "g")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Histogram")
plt.legend()
plt.grid()
plt.show()