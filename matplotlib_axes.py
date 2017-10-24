"""
Remove top and right axes from plot figures.
"""

import matplotlib.pyplot as plt

x = [1, 4, 5, 9, 7, 15, 27]

# Example 1
# ------------------------

plt.figure(1)
plt.plot(x, lw=3)
plt.grid()

ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.tick_params(bottom='off', top='off', left='off', right='off')

plt.show()

# Example 2
# ------------------------

import matplotlib as mpl

mpl.rcParams["axes.spines.right"] = False
mpl.rcParams["axes.spines.top"] = False

plt.figure(2)
plt.plot([1, 3, 2, 6, 7, 5, 9], lw=2)
plt.grid()
plt.show()

