"""
SciPy ode solver for system of kinetic reactions for biomass pyrolysis. Solution
based on reaction rates function, for example dp/dt = K*p. Kinetic scheme from
Papadikis 2010 which uses parameters from Chan 1985, Liden 1988, and Blasi 1993.

Requirements: Python 3, Numpy, Matplotlib

References:
Papadikis, Gu, Bridgwater, 2010. Fuel Processing Technology, 91(1), pp.68–79.
Chan, Kelbon, Krieger, 1985. Fuel, 64(11), pp.1505–1513.
Liden, Berruti, Scott, 1988. Chemical Engineering Communications, 65, pp.207–221.
Blasi, 1993. Combustion Science and Technology, 90, pp.315–340.
"""

import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as py

# Function for SciPy ode solver for wood, gas, tar, char reaction rates
# ------------------------------------------------------------------------------

def dpdt(t, rho, T):
    """
    Function for SciPy odeint solver as a system of ODEs dy/dt = f(y,t).
    INPUTS:
    t = time vector, s
    rho = concentrations array, kg/m^3
    T = temperature, K
    OUTPUTS:
    rw = wood reaction rate, rho/s or kg/(m^3 s)
    rg = gas reaction rate, rho/s or kg/(m^3 s)
    rt = tar reaction rate, rho/s or kg/(m^3 s)
    rc = char reaction rate, rho/s or kg/(m^3 s)
    """
    pw = rho[0]     # wood concentration as density, kg/m^3
    pt = rho[2]     # tar concentration as density, kg/m^3
    R = 0.008314    # universal gas constant, kJ/mol*K

    # Kinetic parameters from Chan 1985 (1-3), Liden 1988 (4), Blasi 1993 (5)
    # A = pre-factor (1/s) and E = activation energy (kJ/mol)
    A1 = 1.3e8;     E1 = 140    # wood -> gas
    A2 = 2e8;       E2 = 133    # wood -> tar
    A3 = 1.08e7;    E3 = 121    # wood -> char
    A4 = 4.28e6;    E4 = 108    # tar -> gas
    A5 = 1e6;       E5 = 108    # tar -> char

    # reaction rate constant for each reaction, 1/s
    K1 = A1 * np.exp(-E1 / (R * T))  # wood -> gas
    K2 = A2 * np.exp(-E2 / (R * T))  # wood -> tar
    K3 = A3 * np.exp(-E3 / (R * T))  # wood -> char
    K4 = A4 * np.exp(-E4 / (R * T))  # tar -> gas
    K5 = A5 * np.exp(-E5 / (R * T))  # tar -> char

    # reaction rates where r = dp/dt, rho/s or kg/(m^3 s)
    rw = -(K1+K2+K3)*pw          # wood rw = dpw/dt
    rg = K1*pw + K4*pt           # gas rg = dpg/dt
    rt = K2*pw - K4*pt - K5*pt   # tar rt = dpt/dt
    rc = K3*pw + K5*pt           # char rc = dpc/dt

    # return wood, gas, tar, char reaction rates, rho/s or kg/(m^3 s)
    return [rw, rg, rt, rc]


# Parameters from Papadikis 2010a
# ------------------------------------------------------------------------------

rhow = 700  # density of wood, kg/m^3
Tinf = 773  # ambient temp, K

# Initial Calculations
# ------------------------------------------------------------------------------

dt = 0.01                               # time step, delta t
tmax = 25                               # max time, s
t = np.linspace(0, tmax, num=tmax/dt)   # time vector

pw = np.zeros(len(t))   # wood array
pg = np.zeros(len(t))   # gas array
pt = np.zeros(len(t))   # tar array
pc = np.zeros(len(t))   # char array

pw[:] = rhow # initial wood density

# SciPy ode solver
# ------------------------------------------------------------------------------

# temperature at which reactions are evaluated
T = Tinf

# setup the ode integrator where 'dopri5' is Runge-Kutta 4th order with 'bdf'
# for backward differentiation formula
r = sp.ode(dpdt).set_integrator('dopri5', method='bdf')
r.set_f_params(T)
r.set_initial_value([rhow, 0, 0, 0], 0)

# integrate the odes for each time step then store the results
k = 1
while r.successful() and r.t < tmax-dt:
    r.integrate(r.t+dt)
    pw[k] = r.y[0]
    pg[k] = r.y[1]
    pt[k] = r.y[2]
    pc[k] = r.y[3]
    k += 1

# Plot Results
# ------------------------------------------------------------------------------

py.ion()
py.close('all')

py.figure(4)
py.plot(t, pw, label='wood', lw=2)
py.plot(t, pg, label='gas', lw=2)
py.plot(t, pt, label='tar', lw=2)
py.plot(t, pc, label='char', lw=2)
py.title('SciPy ode solver, reactions at T = %.f K' % Tinf)
py.xlabel('Time (s)')
py.ylabel('Concentration ($kg/m^3$)')
py.legend(loc='best', numpoints=1)
py.grid()

