import numpy as np
import matplotlib.pyplot as py

y1 = np.random.rand(50)
y2 = np.random.rand(50)
y3 = np.random.rand(50)

x = np.linspace(1, 50)

# Interactive mode is OFF
# -----------------------

# py.figure(1)
# py.plot(x, y1, lw=2)
# py.title('Plot 1')
# py.grid()
# py.show()

# py.figure(2)
# py.plot(x, y2, lw=2)
# py.title('Plot 2')
# py.grid()
# py.show()

# py.figure(3)
# py.plot(x, y3, lw=2)
# py.title('Plot 3')
# py.grid()
# py.show()

# Interactive mode is ON
# ----------------------

py.ion()

py.figure(1)
py.plot(x, y1, lw=2)
py.title('Plot 1')
py.grid()

py.figure(2)
py.plot(x, y2, lw=2)
py.title('Plot 2')
py.grid()

py.figure(3)
py.plot(x, y3, lw=2)
py.title('Plot 3')
py.grid()
