# Tridiagonal Matrix

A system of equations can be represented in matrix form `A*x = B` where `A` is
the coefficient matrix, `x` and `B` are column vectors. The `A` matrix can take
the form of a sparse tridiagonal matrix.

Example of a tridiagonal (a.k.a. banded) matrix:

```
[[ 1  2  0  0  0  0]
 [ 7  8  9  0  0  0]
 [ 0  7  8  9  0  0]
 [ 0  0  7  8  9  0]
 [ 0  0  0  7  8  9]
 [ 0  0  0  0  3  4]]
```

The `numpy`, `scipy`, and `timeit` modules are used in these examples. See
comments in each file for more details. Code was executed on a MacBook Pro with
a 2.8 GHz processor and 8 GB of RAM.

## Computation Times

The following table lists the time (in seconds) for each method to create the
tridiagonal matrix `A` and solve the system of equations `A*x = B` for `x`. For
example, `m = 5` would be a system of 5 equations therefore `A` would be a
`5x5` matrix. The computation time was determined by using the
`timeit.default_timer()` function.

| Method | m = 1,000 | m = 10,000 | m = 20,000 |
| ------ | --------- | ---------- | ---------- |
| NumPy  | 0.024     | 9.71       | 82.09      |
| SciPy  | 0.00017   | 0.00056    | 0.049      |

As demonstrated in the table, the `scipy.linalg.solve_banded` was the fastest approach for all tests.

## Further Reading

Documentation on the solvers are available at the following links:  
NumPy documentation on [numpy.linalg.solve()](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html)  
SciPy documentation on [scipy.linalg.solve_banded()](http://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_banded.html)  

