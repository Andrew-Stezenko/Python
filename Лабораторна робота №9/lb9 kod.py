import matplotlib.pyplot as plt
import numpy as np
import math

x= [0.101,0.111,0.121,0.131,0.141,0.151]
y= [1.2618,1.2912,1.3213,1.3520,1.3835,1.4157]
h = x[1] - x[0]

def f(y,j):
  m1 = []
  for i in range(len(y)):
     m1.append(y[i] - y[i-1])
  m1.pop(0)
  if j == 1:
    return m1
  else:
    j-=1
    return f(m1,j)

  
xa1 = 0.112
xa2 = 0.145
q1 = (xa1-x[0])/h
q2 = (xa2 - x[5])/h
N1 = y[0] + q1*f(y,1)[0] + ((q1*(q1-1))/math.factorial(2)) * f(y,2)[0] + ((q1*(q1-1)*(q1-2))/math.factorial(3))*f(y,3)[0] + ((q1*(q1-1)*(q1-2)*(q1-3))/math.factorial(4)) * f(y,4)[0] + ((q1*(q1-1)*(q1-2)*(q1-3)*(q1-4))/math.factorial(5)) * f(y,5)[0]
N2 = y[5] + q2*f(y,1)[4] + ((q2*(q2+1))/math.factorial(2) )*f(y,2)[3] + ((q2*(q2+1)*(q2+2))/math.factorial(3))*f(y,3)[2] + ((q2*(q2+1)*(q2+2)*(q2+3))/math.factorial(4))*f(y,4)[1] + ((q2*(q2+1)*(q2+2)*(q2+3)*(q2+4))/math.factorial(5))*f(y,5)[0]
print("N1=", N1)
print("N2=", N2)

nX = [0.112, 0.145]
nY = [N1,N2]

plt.plot(x, y, 'g--' )  
plt.plot(nX, nY, 'ro')
plt.plot(x, y, 'bo')
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('') 
plt.legend()
plt.grid() 
plt.show()