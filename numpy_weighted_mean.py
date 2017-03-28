"""
Compare mean and weighted mean using manual calculation and NumPy approach. See
article on WikiPedia for more details about weighted mean,
https://en.wikipedia.org/wiki/Weighted_arithmetic_mean
"""

import numpy as np

# Calculate Mean and Weighted Mean
# -----------------------------------------------------------------------------

# several data points and their mean value
x1 = 81                     # data point 1
x2 = 98                     # data point 2
x3 = 92                     # data point 3
ms = np.mean([x1, x2, x3])  # mean for collection of data points

# weights used for each data point and their weighted mean
wt1 = 11                                        # weight for class 1
wt2 = 42                                        # weight for class 2
wt3 = 25                                        # weight for class 3
wt_sum = wt1 + wt2 + wt3                        # sum of weights
wt_ms = ((wt1*x1)+(wt2*x2)+(wt3*x3)) / wt_sum   # weighted mean for data points

# weighted mean for the data points using NumPy approach
a = [x1, x2, x3]                            # list of data points
wts = [wt1, wt2, wt3]                       # list of weights
wt_numpy_ms = np.average(a, weights=wts)    # weighted mean for data points

# Print Results
# -----------------------------------------------------------------------------

print('mean \n', ms)
print('weighted mean \n', wt_ms)
print('weighted mean numpy \n', wt_numpy_ms)
