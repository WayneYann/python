"""
Example of reading json from a file.
"""

import json

# open json file and assign its data to a variable as a dictionary
# file is automatically closed when with block is complete

with open('vehicles.json', 'r') as vfile:
    vdata = json.load(vfile)

# pretty print the parsed json to the console

print(json.dumps(vdata, indent=2))

# print various values from the parsed json

print('Make is', vdata['vehicles'][0]['make'])
print('Model is', vdata['vehicles'][0]['model'])

print('Make is', vdata['vehicles'][1]['make'])
print('Miles are', vdata['vehicles'][1]['miles'])

# loop through json array and print values

for v in vdata['vehicles']:
    print('Make is', v['make'])

