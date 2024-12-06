# Main program
input_values = input("Enter the values:\n")
# Convert the input string into a list of integers
numbers = list(map(int, input_values.split()))
# Calculate maximum and minimum using built-in functions
maximum_value = max(numbers)
minimum_value = min(numbers)
# Output the results
print(f"The maximum value is : {maximum_value}")
print(f"The minimum value is : {minimum_value}")   