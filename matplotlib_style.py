"""
Style plots using a Matplotlib style sheet. See the matplotlib-style.mplstyle
style sheet file for the styles in this example. Requires Matplotlib v1.4 or
higher.

More info about style sheets provided by the Matplotlib documentation:
http://matplotlib.org/users/style_sheets.html
"""

import numpy as np
import matplotlib.pyplot as py

# Create example data for plot
# ------------------------------------------------------------------------------

x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Plot using style sheet
# ------------------------------------------------------------------------------

py.close('all')
py.ion()

# use style sheet in current working directory or you can add the file to
# the ~/.matplotlib/stylelib folder (create the directory if it doesn't exist)
py.style.use('./matplotlib-style.mplstyle')

py.figure(1)
py.plot(x, y)
py.ylim(-1.1, 1.1)
py.title('Plot Title')
py.ylabel('Y label')
py.xlabel('X label')

