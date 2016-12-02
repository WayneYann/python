# Use a carriage return to replace the previous line. Instead of ending with a
# new line character \n at the end of the line, the carriage return \r goes
# back to the beginning of the line.

import time

for i in range(1, 11):
    print('Item is {} out of 10'.format(i), end='\r')
    time.sleep(1)


