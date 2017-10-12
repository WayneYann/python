"""
Example of a function that accepts a scalar or array as an input.
"""

import numpy as np

def userinput(x):
    """ x input can be scalar or array """
    x = np.asarray(x)

    if x.ndim == 0:
        print('scalar input')
        x = x[None]
    else:
        print('array input')

    return x


print('Example where x = 12')
x1 = userinput(12)
print('x1 is', x1)

print('\nExample where x = 12.95')
x2 = userinput(12.95)
print('x2 is', x2)

print('\nExample where x = [7, 8, 9]')
x3 = userinput([7, 8, 9])
print('x3 is', x3)

print('\nExample where x = np.array([4, 5, 6])')
x4 = userinput(np.array([4, 5, 6]))
print('x4 is', x4)

print('\nExample where np.array([[3, 4], [5, 6]])')
x5 = userinput(np.array([[3, 4], [5, 6]]))
print('x5 is', x5)

