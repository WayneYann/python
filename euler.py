"""
Euler method as described in the book Numerical Methods in Engineering with
Python 3 on page 251 in Example 7.2
"""

import numpy as np
import matplotlib.pyplot as py

# Book Approach
# ------------------------------------------------------------------------------

# euler method
def integrate(F, x, y, xStop, h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h, xStop-x)
        y = y + h*F(x, y)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

# function array
def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1]-x
    return F
    
x = 0.0
xStop = 2.0
y = np.array([0.0, 1.0])
h = 0.05

X, Y = integrate(F, x, y, xStop, h)

yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)

py.close('all')
py.ion()

py.figure(1)
py.plot(X, Y[:, 0], 'o')
py.plot(X, yExact)
py.xlabel('x')
py.ylabel('y')
py.legend(('euler', 'exact'), loc='best', numpoints=1)
py.title('Euler Method (book approach) \n h = %s' % h)
py.grid()

# My Approach
# ------------------------------------------------------------------------------

def euler(F, X, y, h):
    Y = []
    for x in X:
        Y.append(y)
        y = y + h*F(x, y)
    return np.array(Y)


def Func(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1]-x
    return F

xi = 0.0
xf = 2.0
y = np.array([0.0, 1.0])
h = 0.05

X = np.arange(xi, xf+h, h)

Y = euler(Func, X, y, h)

yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)

py.figure(2)
py.plot(X, Y[:, 0], 'o')
py.plot(X, yExact)
py.xlabel('x')
py.ylabel('y')
py.legend(('euler', 'exact'), loc='best', numpoints=1)
py.title('Euler Method (my approach) \n h = %s' % h)
py.grid()

