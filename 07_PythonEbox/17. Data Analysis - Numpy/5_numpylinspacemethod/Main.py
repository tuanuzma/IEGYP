import numpy as np
# Get the limit from the user
print("Enter the limit")
b = float(input())
# Get the number of points from the user
print("Enter the number of points")
a = int(input())
# Create the array using numpy.linspace
array = np.linspace(0, b, a)
# Print the resulting array
print(array)