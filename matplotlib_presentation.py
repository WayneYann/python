"""
Use a Matplotlib stylesheet to format a plot figure for a presentation slide.
For more information about Matplotlib stylesheets see the links below. On a
Mac, custom style sheets are stored at ~/.matplotlib/stylelib which may need to
be created.

http://matplotlib.org/users/style_sheets.html
http://matplotlib.org/users/customizing.html

Below is the contents of the presentation.mplstyle file used in this example.

axes.grid : False
figure.autolayout : True
figure.figsize : 6, 4
font.size : 16
legend.fontsize : medium
legend.frameon : False
legend.numpoints : 1
lines.linewidth : 3
lines.markersize : 10
xtick.major.pad : 5
ytick.major.pad : 5
"""

import matplotlib.pyplot as py

py.ion()
py.close('all')

py.style.use('presentation')

py.figure(1)
py.plot([1, 2, 3, 4, 5], [2, 5, 6, 8, 4], label='one')
py.plot([1, 2, 3, 4, 5], [1, 4, 5, 5, 7], label='two')
py.xlabel('Time (s)')
py.ylabel('Distance (m)')
py.legend(loc='best')

