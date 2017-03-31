"""
Example import package from parent directory.
"""

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pack as pc

car1 = pc.mt
car2 = pc.cm

print('car 1 is', car1)
print('car 2 is', car2)

truck1 = pc.bc
truck2 = pc.tm

print('truck 1 is', truck1)
print('truck 2 is', truck2)

