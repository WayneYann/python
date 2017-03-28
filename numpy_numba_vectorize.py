"""
Example of vectorizing for-loops to speed up computation time. Also attempts to
use Numba for further speed increases with autojit.

Uses the time.perf_counter() function for speed comparisons.

Change value of p to 6, 7, or 8 for best speed comparisons between the methods.
"""

import numpy as np
import numba as nb
import time

# Parameter
# ------------------------------------------------------------------------------

p = 7

# Loop Example
# ------------------------------------------------------------------------------

t1 = time.perf_counter()

A = []

for i in range(0, 10**p):
    A.append(i**3 + i**2)

t1end = time.perf_counter()

# Vectorized Array Example
# ------------------------------------------------------------------------------

t2 = time.perf_counter()

j = np.arange(0, 10**p)
B = j**3 + j**2

t2end = time.perf_counter()

# Vectorized Array Expanded Example
# ------------------------------------------------------------------------------ 

t3 = time.perf_counter()

k = np.arange(0, 10**p)
C = k*k*(k+1)

t3end = time.perf_counter()

# Vectorized Array Using Numba Example
# ------------------------------------------------------------------------------

# Note that Numba must "jit" the code during the first run, subsequent runs will
# be faster. The approach below includes the initial "jit-ing" of the code.
# Use %timeit in iPython to see the best of several runs of the function which 
# should be faster than the vectorized array examples above.

t4 = time.perf_counter()

@nb.jit
def func():
    n = np.arange(0, 10**p)
    a = n*n*(n+1)
    return a

D = func()

t4end = time.perf_counter()

# Print Speed Comparisons
# ------------------------------------------------------------------------------

print('--- p =', p, ' ---')
print('{:.4f} s, for-loop'.format(t1end-t1))
print('{:.4f} s, vectorized array'.format(t2end-t2))
print('{:.4f} s, vectorized array expanded'.format(t3end-t3))
print('{:.4f} s, vectorized array with numba'.format(t4end-t4))

