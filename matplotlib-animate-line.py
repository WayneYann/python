"""
Animate line plot using animation package of Matplotlib
"""

import numpy as np
import matplotlib.pyplot as py
from matplotlib import animation

# Data to plot
# ------------------------------------------------------------------------------

x = np.random.rand(40)
y = np.random.rand(40)

# Plot line
# ------------------------------------------------------------------------------
py.close('all')
py.ion()

py.figure(1)
py.plot(x, y, lw=2)
py.axis([0, 1, 0, 1])

# Animation of the same random line plot
#------------------------------------------------------------------------------

fig = py.figure(2)
ax = py.axes(xlim=(0, 1), ylim=(0, 1))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,
    
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,
    
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(x)+1, 
                               interval=200, blit=False, repeat=False)

