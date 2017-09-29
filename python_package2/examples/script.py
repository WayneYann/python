"""
Example import package from parent directory.
"""

# add parent directory to python path
import sys
sys.path.append('..')

# import the modules from the pack package
import pack as pc

# examples of using the modules
car1 = pc.mt
car2 = pc.cm

print('car 1 is', car1)
print('car 2 is', car2)

truck1 = pc.bc
truck2 = pc.tm

print('truck 1 is', truck1)
print('truck 2 is', truck2)

