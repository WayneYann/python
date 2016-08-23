"""
Solve system of ODEs using SciPy ODE solvers with fixed or variable time-step.
"""

import numpy as np
import matplotlib.pyplot as py
import scipy.integrate as sp

#---- close all previous plot windows
py.close('all')
py.ion()

#---- Example 1, fixed time-step
# http://nbviewer.ipython.org/gist/dpsanders/d417c1ffbb76f13f678c

a = 2

def f(y, t):
    return a*y
    
y0 = 1

t_output = np.arange(0, 6, 0.1)

y_result = sp.odeint(f, y0, t_output)
y_result = y_result[:, 0]

# plot

py.figure(1)
py.plot(t_output, y_result, 'ro')
py.plot(t_output, y0 * np.exp(a * t_output), 'b-')
py.title('Example 1: fixed time-step')
py.xlabel('time (s)')
py.ylabel('y')

#---- Example 2a, fixed time-step

def ff(vec, t):
    y1, y2, y3, y4 = vec
    
    T = 773
    
    A1 = 1.3e8;     E1 = 140
    A2 = 2e8;       E2 = 133
    A3 = 1.08e7;    E3 = 121
    A4 = 4.28e6;    E4 = 108
    A5 = 1e6;       E5 = 108
    R = 0.008314
    
    K1 = A1*np.exp(-E1/(R*T))
    K2 = A2*np.exp(-E2/(R*T))
    K3 = A3*np.exp(-E3/(R*T))
    K4 = A4*np.exp(-E4/(R*T))
    K5 = A5*np.exp(-E5/(R*T))
        
    return [-(K1+K2+K3)*y1, K1*y1+K4*y3, K2*y1-(K4+K5)*y3, K3*y1+K5*y3]
    
y0 = [700, 0, 0, 0]

t_output = np.arange(0, 25, 0.1)

y_result = sp.odeint(ff, y0, t_output)

# plot

py.figure(2)
py.plot(t_output, y_result)
py.title('Example 2a: fixed time-step')
py.xlabel('time (s)')
py.ylabel('density (kg/m^3)')

#---- Example 2b, fixed time-step

def fff(vec, t):
    y1 = vec[0]
    #y2 = vec[1]
    y3 = vec[2]
    #y4 = vec[3]
    
    T = 773
    
    A1 = 1.3e8;     E1 = 140
    A2 = 2e8;       E2 = 133
    A3 = 1.08e7;    E3 = 121
    A4 = 4.28e6;    E4 = 108
    A5 = 1e6;       E5 = 108
    R = 0.008314
    
    K1 = A1*np.exp(-E1/(R*T))
    K2 = A2*np.exp(-E2/(R*T))
    K3 = A3*np.exp(-E3/(R*T))
    K4 = A4*np.exp(-E4/(R*T))
    K5 = A5*np.exp(-E5/(R*T))
    
    c1 = -(K1+K2+K3)*y1
    c2 = K1*y1+K4*y3
    c3 = K2*y1-(K4+K5)*y3
    c4 = K3*y1+K5*y3
        
    return [c1, c2, c3, c4]
    
y0 = [700, 0, 0, 0]

t_output = np.arange(0, 25, 0.1)

y_result = sp.odeint(fff, y0, t_output)

# plot

py.figure(3)
py.plot(t_output, y_result)
py.title('Example 2b: fixed time-step')
py.xlabel('time (s)')
py.ylabel('density (kg/m^3)')

#---- Example 3, variable time-step
# http://stackoverflow.com/questions/12926393/using-adaptive-step-sizes-with-scipy-integrate-ode
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html

import warnings

def logistic(t, y, r):
    return r * y * (1.0 - y)

r = .01
t0 = 0
y0 = 1e-5
t1 = 5000.0

#backend = 'vode'
backend = 'dopri5'
#backend = 'dop853'

solver = sp.ode(logistic).set_integrator(backend, nsteps=1)
solver.set_initial_value(y0, t0).set_f_params(r)
# suppress Fortran-printed warning
solver._integrator.iwork[2] = -1

sol = []
warnings.filterwarnings("ignore", category=UserWarning)
while solver.t < t1:
    solver.integrate(t1, step=True)
    sol.append([solver.t, solver.y])
warnings.resetwarnings()
sol = np.array(sol)

# plot

py.figure(4)
py.plot(sol[:,0], sol[:,1], 'bo-')
py.title('Example 3: variable time-step')
py.xlabel('time (s)')
py.ylabel('y')

#---- Example 4, variable time-step
# http://stackoverflow.com/questions/12926393/using-adaptive-step-sizes-with-scipy-integrate-ode
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html

import warnings

def ffff(t, y):
    y1 = y[0]
    #y2 = y[1]
    y3 = y[2]
    #y4 = y[3]
    
    T = 773
    
    A1 = 1.3e8;     E1 = 140
    A2 = 2e8;       E2 = 133
    A3 = 1.08e7;    E3 = 121
    A4 = 4.28e6;    E4 = 108
    A5 = 1e6;       E5 = 108
    R = 0.008314
    
    K1 = A1*np.exp(-E1/(R*T))
    K2 = A2*np.exp(-E2/(R*T))
    K3 = A3*np.exp(-E3/(R*T))
    K4 = A4*np.exp(-E4/(R*T))
    K5 = A5*np.exp(-E5/(R*T))
    
    c1 = -(K1+K2+K3)*y1
    c2 = K1*y1+K4*y3
    c3 = K2*y1-(K4+K5)*y3
    c4 = K3*y1+K5*y3
    
    return [c1, c2, c3, c4]

t0 = 0
t1 = 25
y0 = [700, 0, 0, 0]

# integrators to use
backend = ['vode', 'zvode', 'lsoda', 'dopri5', 'dop853']

# select integrator: vode = 0, zvode = 1, lsoda = 2, dopri5 = 3, dop853 = 4
n = 0   

solver = sp.ode(ffff).set_integrator(backend[n], nsteps=1)
solver.set_initial_value(y0, t0)
# suppress Fortran-printed warning
solver._integrator.iwork[2] = -1

sol = []
warnings.filterwarnings("ignore", category=UserWarning)
while solver.t < t1:
    solver.integrate(t1, step=True)
    sol.append([solver.t, solver.y[0], solver.y[1], solver.y[2], solver.y[3]])
warnings.resetwarnings()
sol = np.array(sol)

# plot

py.figure(5)
py.plot(sol[:,0], sol[:, 1:], 'o-')
py.title('ode using ' + backend[n])
py.title('Example 4: variable time-step')
py.xlabel('time (s)')
py.ylabel('density (kg/m^3)')

