"""
Contour plot examples using Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as py

# Parameters
# ------------------------------------------------------------------------------

xlist = np.linspace(-3, 3, 50)
ylist = np.linspace(-3, 3, 50)
x, y = np.meshgrid(xlist, ylist)

z = np.sqrt(x**2 + y**2)

print('xlist \n', xlist)
print('ylist \n', ylist)
print('x \n', x)
print('y \n', y)
print('z \n', z)

# Contour Plots
# ------------------------------------------------------------------------------

py.close('all')
py.ion()

py.figure(1)
cp =  py.contour(xlist, ylist, z)
py.clabel(cp, inline=True, fmt='%2.1f')

py.figure(2)
py.contourf(x, y, z)
py.colorbar()

