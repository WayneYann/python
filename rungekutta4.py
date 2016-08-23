"""
Example of the fourth-order Runge-Kutta method.
See book "Numerical Methods in Engineering with Python 3", pg. 254, Example 7.4
"""

import numpy as np
import matplotlib.pyplot as py

# Book Approach
# ------------------------------------------------------------------------------

# runge-kutta fourth-order method

def integrate(F, x, y, xStop, h):
    
    def run_kut4(F, x, y, h):
        K0 = h*F(x, y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
        
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h, xStop-x)
        y = y + run_kut4(F, x, y, h)
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
h = 0.1

X, Y = integrate(F, x, y, xStop, h)

yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)

py.close('all')
py.ion()

py.figure(1)
py.plot(X, Y[:, 0], 'o')
py.plot(X, yExact)
py.xlabel('x')
py.ylabel('y')
py.legend(('runge-kutta', 'exact'), loc='best', numpoints=1)
py.title('Runge-Kutta Method (book approach) \n h = %s' % h)
py.grid()

# My Approach
# ------------------------------------------------------------------------------

# runge-kutta fourth-order method

def run_kut4(F, x, y, h):
        K0 = h*F(x, y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0

def rungekutta(F, x, y, h):    
    Y = []
    for x in X:
        Y.append(y)
        y = y + run_kut4(F, x, y, h)
    return np.array(Y)

# function array

def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1]-x
    return F
    
xi = 0.0
xf = 2.0
y = np.array([0.0, 1.0])
h = 0.1

X = np.arange(xi, xf+h, h)

Y = rungekutta(F, X, y, h)

yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)

py.figure(2)
py.plot(X, Y[:, 0], 'o')
py.plot(X, yExact)
py.xlabel('x')
py.ylabel('y')
py.legend(('runge-kutta', 'exact'), loc='best', numpoints=1)
py.title('Runge-Kutta Method (my approach) \n h = %s' % h)
py.grid()

