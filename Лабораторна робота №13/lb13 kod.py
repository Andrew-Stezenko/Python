from scipy import integrate
from numpy import *

#Метод прямокутників
def f (x):
    return 1/sqrt(3*x+1)
def pr_int(f,a,b,n):
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        sum += f(a + i * h)
    return sum * h
print("The rectangle method=" ,pr_int(f,1.4,2.2,10))
v,err = integrate.quad(f, 1.4, 2.2)#Перевірка для методу прямокутників
print ("Check for the rectangle method=" ,v)

#Метод Сімпсона
def f1(x):
    return log(x**2+2)/x+1
v,err = integrate.quad(f1, 1.4, 2.2)
print ("Check for the Simpson method=" ,v)

#Метод трапецій
def f2 (x):
    return 1/sqrt(x**2+0.8)
def tr_int(f2,a,b,n):
    h = (b - a) / n
    sum = 0.5 * (f2(a) + f2(b))
    for i in range(1, n):
        sum += f2(a + i * h)
    return sum * h
print("Trapezoidal method=" ,tr_int(f2,0.6,1.6,20))
v,err = integrate.quad(f2, 0.6, 1.6)#Перевірка для методу трапецій
print("Check for trapezoidal method=" ,v)


