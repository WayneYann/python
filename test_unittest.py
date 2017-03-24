"""
Example of using the unittest framework for writing unit tests in Python.

To perform the tests, enter `python test_unittest.py` at the command line.

References:
1) https://docs.python.org/3/library/unittest.html
2) http://pythontesting.net/framework/unittest/unittest-introduction/
3) http://docs.python-guide.org/en/latest/writing/tests/
"""

import unittest
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

class MyTest(unittest.TestCase):
    """ test class """

    def test_inc1(self):
        """ test inc function """
        self.assertEqual(inc(3), 5)

    def test_inc2(self):
        """ test inc function again """
        self.assertEqual(inc(3), 4)

    def test_npsum(self):
        """ test numpy sum function """
        s = npsum([1, 2, 3, 4])
        self.assertEqual(s, 10)


if __name__ == '__main__':
    unittest.main()

