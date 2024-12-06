# Function definition with a default argument for argument2
def multiply(argument1, argument2=10):
    return argument1 * argument2

# Input values
a = int(input().strip())
b = int(input().strip())

# Function calls
result1 = multiply(a)                # Uses default value of argument2 (10)
result2 = multiply(a, b)             # Uses provided values a and b
result3 = multiply(a, argument2=9)   # Correctly specifies argument2 with 9

# Output the results
print(f"The result is {result1}")
print(f"The result is {result2}")
print(f"The result is {result3}")