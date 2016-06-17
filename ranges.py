import numpy as np

# range examples using Python

r1 = range(10)
r2 = range(1, 10)
r3 = range(-2, 8)
r4 = range(0, 10, 2)

print('r1 is', list(r1))
print('r2 is', list(r2))
print('r3 is', list(r3))
print('r4 is', list(r4))

# arange examples using NumPy

ar1 = np.arange(10)
ar2 = np.arange(1, 10)
ar3 = np.arange(1, 10, 2)
ar4 = np.arange(0.2, 0.8, 0.1)

print('ar1 is', ar1)
print('ar2 is', ar2)
print('ar3 is', ar3)
print('ar4 is', ar4)

# linspace examples using NumPy

ln1 = np.linspace(1, 10)
ln2 = np.linspace(1, 10, 10)
ln3 = np.linspace(1, 10, 5)

print('ln1 is', ln1)
print('ln2 is', ln2)
print('ln3 is', ln3)

