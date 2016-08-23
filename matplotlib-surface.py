"""
Surface plot example using Matplotlib.

References:
- mplot3d tutorial
  http://matplotlib.org/1.3.1/mpl_toolkits/mplot3d/tutorial.html
- mplot3d example code: surface3d_demo.py
  http://matplotlib.org/examples/mplot3d/surface3d_demo.html
- color example code: colormaps_reference.py
  http://matplotlib.org/examples/color/colormaps_reference.html
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as py
import numpy as np

# Parameters
# ------------------------------------------------------------------------------

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)

r = np.sqrt(x**2 + y**2)
z = np.sin(r)

# Surface Plot
# ------------------------------------------------------------------------------

py.close('all')
py.ion()

fig = py.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='coolwarm', linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_zlabel('z label')
fig.colorbar(surf, shrink=0.5, aspect=5)

