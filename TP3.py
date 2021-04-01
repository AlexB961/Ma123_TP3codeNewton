# -*- coding: utf-8 -*-

"""
TP3Ma123_MethodeNewton
M.Laurent BLETZACKER

Alexandre Jean-Philippe BESSON
Antony ABDEL MALAK
1-PT1

"""

from math import sin
from math import cos
from math import tan
from math import exp
from math import log
from math import acos
from math import atan
from math import asin
from math import sqrt


def Newton(f, fder, x0, epsilon, Nitermax):
    n=0
    xold = x0
    erreur = -(f(xold)/(fder(xold)))

    while abs(erreur) > epsilon and n < Nitermax :
        xnew = xold - f(xold)/fder(xold)
        n += 1
        erreur = xnew - xold
        xold = xnew
        print(n,xnew)
    return xnew


#(fonction):x**4 + 3x = 9

def f1(x):
    return (x**4) + 3*x -9

def fder1(x):
    return 4 * (x**3) + 3

#(fonction):x = 3cos(x)-2

def f2(x):
    return x - 3 * cos(x) + 2

def fder2(x):
    return 1 + 3*sin(x)

#(fonction):x*e^x = 7

def f3(x):
    return x*exp(x)-7

def fder3(x):
    return exp(x) + x*exp(x)

#(fonction): e^x − x = 10

def f4(x):
    return exp(x) - x - 10

def fder4(x):
    return -1 + exp(x)
    
#(fonction): 2tan(x) = x + 5

def f5(x):
    return 2*tan(x) - x - 5

def fder5(x):
    return 1 + 2*tan(x)**2
    
#(fonction):e^x = x^2 + 3

def f6(x):
    return exp(x) - (x**2) - 3

def fder6(x):
    return -2*x + exp(x)

#(fonction):3x + 4 ln(x) = 7

def f7(x):
    return 3*x + 4*log(x) - 7

def fder7(x):
    return (4+3*x)/x
    
#(fonction):x^4 − 2x^2 + 4x = 17

def f8(x):
    return (x**4) - 2*(x**2) + 4*x - 17

def fder8(x):
    return 4 - 4*x + 4*(x**3)

#(fonction):e^x -2sin(x) =7

def f9(x):
    return exp(x) - 2*sin(x) - 7

def fder9(x):
    return -2*cos(x)+exp(x)

#(fonction): ln(x^2+4)*e^x =10 

def f10(x):
    return log((x**2)+4)*exp(x) - 10

def fder10(x):
    return (4*log(4+x**2)*exp(x)+2*x*exp(x)+(x**2)*log(4+x**2)*exp(x))/(4+x**2)

print (Newton(f10,fder10,1.5, 1e-10, 5e4))

