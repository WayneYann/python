"""
Use the where() routine in NumPy to find index corresponding to values in an
array that meet a declared condition. Note that the return type is an array or
tuple of arrays.

Reference:
https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html#numpy.where
"""

import numpy as np

# Example 1
# ------------------------------------------------------------------------------

a = np.array([1, 2, 3, 4, 5, 6])
print('a is', a)

x = np.where(a > 4)     # returns a tuple containing array of indices
print('indices where values of a > 4 are:', x[0])

y = np.where(a == 3)
print('index where value of a = 3 is:', y[0])

# Example 2
# ------------------------------------------------------------------------------

b = np.array([1, 2, 3, 7, 7, 8, 9])
print('b is', b)

s = np.where(b > 7)
print('indices where b > 7 are:', s[0])

t = np.where(b >= 7)
print('indices where b >= 7 are:', t[0])

