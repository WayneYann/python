"""
Example of raising a ValueError exception in Python.
"""

def rey(x):
    """input a value representing a number"""
    num = x
    if num < 6:
        raise ValueError('Number is less than 6')
    else:
        return num


Rey1 = rey(10)  # will not raise an error

print('Rey1 = ', Rey1)

Rey2 = rey(4)   # will raise an error in the terminal

print('Rey2 = ', Rey2)

