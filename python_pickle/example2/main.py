"""
Example of creating a class instance by loading a pickle file.
"""

# Import the Vehicle class which uses a class method to initialize from a
# pickle file.

from vehicle import Vehicle

# Create a Vehicle class instance by loading a pickle file.
# This example uses the pickle files saved in example1.

car = Vehicle.load('example1/car.pickle')
truck = Vehicle.load('example1/truck.pickle')

# Print results

print(f'car is {car.name} {car.year}')
print(f'truck is {truck.name} {truck.year}')

