"""
A basic example of a random walk function and plotting the results.
"""

import numpy as np
import matplotlib.pyplot as py

# Random walk function
#------------------------------------------------------------------------------

def randomWalkb(length):
    x, y = 0, 0
    walkx, walky = [x], [y]
    
    for i in range(length):
        new = np.random.randint(1, 5)
        if new == 1:
            x += 1
        elif new == 2:
            y += 1
        elif new ==3:
            x += -1
        else:
            y += -1
        walkx.append(x)
        walky.append(y)
    
    return [walkx, walky]

# Plot 
#------------------------------------------------------------------------------

walk = randomWalkb(1000)

py.close('all')
py.ion()

py.figure(1)
py.plot(walk[0], walk[1], lw=2)

py.figure(2)
py.scatter(walk[0], walk[1], s=50)

