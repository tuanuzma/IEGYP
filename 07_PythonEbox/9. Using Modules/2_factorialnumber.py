def calculate_factorial(n):
    # Initialize factorial to 1 (0! = 1)
    factorial = 1
    # Calculate factorial using a loop
    for i in range(1, n + 1):
        factorial *= i
    return factorial
# Main program
try:
    n = int(input())
    # Check for negative input
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = calculate_factorial(n)
        print(result)
except ValueError:
    print("Please enter a valid integer.")   