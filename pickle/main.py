"""
Example of using the pickle module to save and load a class object.
"""

import pickle

class Vehicle:

    def __init__(self, name, year):
        self.name = name
        self.year = year


# Create class objects
car = Vehicle('Mustang', 1974)
truck = Vehicle('Bronco', 1989)

# Save class objects
pickle.dump(car, open('car.pickle', 'wb'))
pickle.dump(truck, open('truck.pickle', 'wb'))

# Load saved class objects
car2 = pickle.load(open('car.pickle', 'rb'))
truck2 = pickle.load(open('truck.pickle', 'rb'))

# Print from loaded class objects
print('car2 is', car2.name, 'and', car2.year)
print('truck2 is', truck2.name, 'and', truck2.year)

