import math
import numpy as np
y = np.array([3.526, 3.782, 3.945, 4.043, 4.104, 4.155])
x = np.array([2.4, 2.6, 2.8, 3.0, 3.2, 3.4])
def f(y):
    m1=[]
    for i in range(len(y)):
        m1.append(y[i]-y[i-1]) 
    m1.pop(0)      
    return m1  
print (f(y))

y = np.array([3.526, 3.782, 3.945, 4.043, 4.104, 4.155])
x = np.array([2.4, 2.6, 2.8, 3.0, 3.2, 3.4])
h = x[1]-x[0]
def f(y,j):
    m1=[]
    for i in range(len(y)):
        m1.append(y[i]-y[i-1]) 
    m1.pop(0)
    if j ==1:
        return m1
    else:
        j-=1          
        return f(m1,j) 
yx1=1/h*f(y,1)[1]-f(y, 2)[1]/2+f(y, 3)[1]/3-f(y, 4)[1]/4
print (yx1)
yx2=1/h**2*f(y, 2)[1]-f(y, 3)[1]+11/12*f(y,4)[1]
print (yx2)