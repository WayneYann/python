"""
Solve a system of equations in the form of A*x = B where A is a tridiagonal
martix. Compare NumPy and SciPy solvers using timeit function.

Examples below use a coefficient matrix represented by the tridiagonal array
A = [1  2   0   0   0   0]
    [7  8   9   0   0   0]
    [0  7   8   9   0   0]
    [0  0   7   8   9   0]
    [0  0   0   7   8   9]
    [0  0   0   0   3   4]

and the right hand side is represented by the vector
B = [ 1 ]
    [ 2 ]
    [ 2 ]
    [ 2 ]
    [ 2 ]
    [ 3 ]
where B can be passed as a column or row vector to the solver.
"""

import numpy as np
import scipy.linalg as sp
import timeit

# Parameters
# ------------------------------------------------------------------------------

m = 20000  # large arrays for performance comparison, A = m x m and B = m x 1

#m = 6   # use small arrays to check matrix formation with print function

# NumPy approach
# ------------------------------------------------------------------------------

# build tridiagonal coefficient matrix A and column vector B

A = np.zeros((m, m))    # initialize array A

A[0, 0] = 1
A[0, 1] = 2

j = np.arange(0, m-2)   # m-1
i = np.arange(1, m-1)   # m
k = np.arange(2, m)     # m+1

A[i, j] = 7     # node-1
A[i, i] = 8     # node
A[i, k] = 9     # node+1

A[m-1, m-2] = 3
A[m-1, m-1] = 4

B = np.zeros(m)     # initialize vector B 
B[0] = 1
B[1:] = 2
B[-1] = 3

# solve using numpy.linalg.solve
ti_np = timeit.default_timer() # start timer
x_np = np.linalg.solve(A, B)   # solve A*x = B for x
tf_np = timeit.default_timer() # end timer

# SciPy approach
# ------------------------------------------------------------------------------

# create banded array ab that represents tridiagonal matrix A
ab = np.zeros((3, m))

# upper diagonal
ab[0, 1] = 2
ab[0, 2:] = 9

# center diagonal
ab[1, 0] = 1
ab[1, 1:m-1] = 8
ab[1, m-1] = 4

# lower diagonal
ab[2, 0:m-2] = 7
ab[2, m-2] = 3

# create row vector b
b = np.zeros(m)
b[0] = 1
b[1:] = 2
b[-1] = 3

# solve using scipy.sparse.linalg.lsqr
ti_sp = timeit.default_timer() # start timer
x_sp = sp.solve_banded((1, 1), ab, b) # solve A*x = B for x
tf_sp = timeit.default_timer() # stop timer

# Print Results
# ------------------------------------------------------------------------------

print('m is', m)

# numpy approach

if m < 7:
    print('A is\n', A)
    print('B is\n', B)
    print('x is\n', x_np)

print('NumPy time is', tf_np - ti_np, 'seconds')

# scipy approach

if m < 7:
    print('ab is\n', ab)
    print('b is\n', b)
    print('x is\n', x_sp)

print('SciPy time is', tf_sp - ti_sp, 'seconds')

