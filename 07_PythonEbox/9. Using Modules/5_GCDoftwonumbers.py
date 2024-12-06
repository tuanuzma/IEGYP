def gcd(a, b):
    # Using the Euclidean algorithm to find GCD
    while b:
        a, b = b, a % b
    return a
# Main program
try:
    print("Enter the two positive numbers")
    num1 = int(input())
    num2 = int(input())
    # Ensure both numbers are positive
    if num1 <= 0 or num2 <= 0:
        print("Please enter positive integers only.")
    else:
        result = gcd(num1, num2)
        print(f"GCD: {result}")
except ValueError:
    print("Please enter valid integers.")   