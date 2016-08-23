"""
Fill between plot line using Matplotlib.
"""

import matplotlib.pyplot as py

# Parameters
# ------------------------------------------------------------------------------

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 8, 10, 14]
y2 = [1, 3, 6, 7, 8]

# Plot
# ------------------------------------------------------------------------------

py.close('all')
py.ion()

py.figure(1)
py.plot(x, y1, 'r-')
py.plot(x, y2, 'b-')
py.xlabel('x')
py.ylabel('y')
py.fill_between(x, y1, y2, facecolor='yellow', alpha=0.4)
py.grid()

