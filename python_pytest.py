"""
Example of using the pytest framework for writing unit tests in Python.

To perform the tests, enter `pytest` at the command line within the same
directory as this file.

References:
1) Pytest documentation at http://pytest.org
2) https://jacobian.org/writing/getting-started-with-pytest/
"""

import numpy as np

# Functions
# ------------------------------------------------------------------------------

def inc(x):
    """ increment function """
    return x + 1


def npsum(x):
    """ summation of list items """
    s = np.sum(x)
    return s


# Tests
# ------------------------------------------------------------------------------

def test_inc1():
    """ test inc function """
    assert inc(3) == 5


def test_inc2():
    """ test inc function again """
    assert inc(3) == 4


def test_npsum():
    """ test numpy sum function """
    s = npsum([1, 2, 3, 4])
    assert s == 10


