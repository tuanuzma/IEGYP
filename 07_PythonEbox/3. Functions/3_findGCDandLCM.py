def GCD(n1, n2):
    """Function to calculate GCD of two numbers."""
    while n2:
        n1, n2 = n2, n1 % n2
    return n1
def LCM(n1, n2):
    """Function to calculate LCM of two numbers."""
    return abs(n1 * n2) // GCD(n1, n2)
# Input from user
print("Enter two integers:")
num1 = int(input())
num2 = int(input())
# Calculate GCD and LCM
gcd_value = GCD(num1, num2)
lcm_value = LCM(num1, num2)
# Output the results
print(f"Greatest common divisor of {num1} and {num2} = {gcd_value}")
print(f"Least common multiple of {num1} and {num2} = {lcm_value}")
