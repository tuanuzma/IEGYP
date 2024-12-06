import numpy as np
# Get the size of the 1-D array from the user
print("Enter the size of 1-D array")
size = int(input())
# Create a 1-D array using the range function
one_d_array = np.arange(size)
# Print the 1-D array
print("1-D Array")
print(one_d_array)
# Get m and n values from the user
print("Enter m value")
m = int(input())
print("Enter n value")
n = int(input())
# Reshape the 1-D array to a 2-D array with m rows and n columns
two_d_array = one_d_array.reshape(m, n)
# Print the resulting 2-D array
print("2-D Array")
print(two_d_array)   