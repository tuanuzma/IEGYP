import numpy as np
from scipy.integrate import dblquad
# Function to be integrated, which we will define dynamically
def dynamic_function(x, y):
    return eval(expression)
# Get the function from the user
expression = input("Enter the function to be integrated in terms of x and y: \n")
# Get the limits for x and y from the user
x_lower = float(input("Enter the lower limit for x: \n"))
x_upper = float(input("Enter the upper limit for x: \n"))
y_lower = float(input("Enter the lower limit for y: \n"))
y_upper = float(input("Enter the upper limit for y: \n"))
# Perform the double integration using dblquad
result, error = dblquad(lambda y, x: dynamic_function(x, y), x_lower, x_upper, lambda x: y_lower, lambda x: y_upper)
# Output the result and error estimate
print(f"Result of dblquad integration: {result}")
print(f"Error estimate: {error}")