"""
Animate scatter plot using animation package of Matplotlib
"""

import numpy as np
import matplotlib.pyplot as py
from matplotlib import animation

# Data for scatter plot
#------------------------------------------------------------------------------

x = np.random.rand(1000)
y = np.random.rand(1000)

# Plot scatter
# ------------------------------------------------------------------------------

py.close('all')
py.ion()

py.figure(1)
py.scatter(x, y, s=100)
py.axis([0, 1, 0, 1])

# Animation of a scatter plot using x, y from above
#------------------------------------------------------------------------------

fig = py.figure(2)
ax = py.axes(xlim=(0, 1), ylim=(0, 1))
scat = ax.scatter([], [], alpha=0.4, s=100)

def init():
    scat.set_offsets([])
    return scat

def animate(i):
    data = np.hstack((x[:i,np.newaxis], y[:i, np.newaxis]))
    scat.set_offsets(data)
    return scat

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(x)+1, interval=10, blit=False, repeat=False)

