from scipy.stats import linregress
# Input the values of x and y
x_input = input("Enter the values of x separated by spaces: ")
y_input = input("Enter the values of y separated by spaces: ")
# Convert the input strings into lists of floating-point numbers
x = [float(i) for i in x_input.split()]
y = [float(i) for i in y_input.split()]
# Perform linear regression using the input data
slope, intercept, r_value, p_value, std_err = linregress(x, y)
# Print the statistical results
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
print(f"p-value: {p_value}")
print(f"Standard error: {std_err}")   