"""
Various methods to calculate execuation time of code.
"""

import time
import timeit

# Function
# ------------------------------------------------------------------------------

def procedure():
    time.sleep(2.8) # pause for 2.8 seconds

# Measure process time, use this for benchmarking code or algorithms
# ------------------------------------------------------------------------------

ti = time.clock()
procedure()
tf = time.clock()
print(tf-ti, 'seconds time.clock()')

# Measure wall time
# ------------------------------------------------------------------------------

ti = time.time()
procedure()
tf = time.time()
print(tf-ti, 'seconds time.time()')

# Measure with timeit
# ------------------------------------------------------------------------------

ti = timeit.default_timer()
procedure()
tf = timeit.default_timer()
print(tf-ti, 'seconds timeit.default_timer()')

# Measure with process_time
# ------------------------------------------------------------------------------

ti = time.process_time()
procedure()
tf = time.process_time()
print(tf-ti, 'seconds time.process_time()')

# Measure with perf_counter
# ------------------------------------------------------------------------------

ti = time.perf_counter()
procedure()
tf = time.perf_counter()
print(tf-ti, 'seconds time.perf_counter()')

# so it looks like the following are similar:
#   time.clock() <-> process_time()         is cpu clock time
#   time.time()  <-> time.perf_counter()    is wall time

