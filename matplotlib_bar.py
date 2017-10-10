"""
Simple bar chart using Matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

# Prepare for plotting

plt.ion()
plt.close('all')

# Example 1

items = np.array([1, 2, 3, 4, 5])
data = np.array([10, 8, 5, 7, 9])
data2 = np.array([8, 9, 6, 8, 7])

plt.figure(1)
plt.bar(items, data, color='g', width=0.4, align='center', alpha=0.5)
plt.bar(items + 0.4, data2, color='b', width=0.4, align='center', alpha=0.5)
plt.xticks(items + 0.2, ['aaa', 'bbb', 'ccc', 'ddd', 'eee'])

# Example 2

data3 = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}

plt.figure(2)
plt.bar(data3.keys(), data3.values())

