"""
Simple bar chart using Matplotlib
"""

import matplotlib.pyplot as py
import numpy as np

# parameters
items = np.array([1, 2, 3, 4, 5])

data = np.array([10, 8, 5, 7, 9])
data2 = np.array([8, 9, 6, 8, 7])

# bar plot
py.ion()
py.close('all')
py.figure(1)
py.bar(items, data, color='g', width=0.4, align='center', alpha=0.5)
py.bar(items + 0.4, data2, color='b', width=0.4, align='center', alpha=0.5)
py.xticks(items + 0.2, ['aaa', 'bbb', 'ccc', 'ddd', 'eee'])
