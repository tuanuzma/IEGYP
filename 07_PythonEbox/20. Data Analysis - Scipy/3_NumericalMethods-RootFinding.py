from scipy.optimize import root

# Define the equation whose root is to be found
def equation(x):
    return x**3 - 2*x - 5

# Get the initial guess from the user
x0 = float(input("Enter initial guess: "))

# Find the root using the root function from scipy.optimize
sol = root(equation, x0)

# Print the result in the expected format
# Ensure the result is printed with brackets and the required precision
root_value = sol.x[0]  # Extract the root from the solution object
print(f"Root: [{root_value:.8f}]")  # Format the root value to match the expected output
