"""
Unpack the binary data in the data_ch04.dat file which was formatted as 4 byte
float and big-endian. Save the data to t105.csv which can be read in other
programs. Finally plot the data.

Documentation on using struct in Python to unpack binary data from buffer
https://docs.python.org/3.5/library/struct.html#module-struct
"""     

import struct
import csv
import matplotlib.pyplot as py

# Read entire binary data file
with open('data_ch04.dat', 'rb') as f:
    data = f.read()

# Convert to tuple of floats
lg = len(data)                      # length of the data
fmt = '>{}f'.format(lg//4)          # create format string based on 4 byte float
data = struct.unpack(fmt, data)     # unpack data based on format string

# Display some of the data
print(lg, 'total length of data')
print(lg//4, 'length of 4 byte data')
print(data[0], data[1], data[2], "...")

# Write data to CSV file as one column
with open('t105.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for row in data:
        writer.writerow([row])

# Read each row from CSV file and create list from data (to check the CSV)
datalist = []

with open('t105.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        datalist.append(row[0])
    
# Plot
py.ion()
py.close('all')
py.figure(1)
py.plot(data, 'o')

