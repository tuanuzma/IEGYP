# Function definitions for each operation
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return "Division by zero is undefined"
    return n1 / n2

def modulus(n1, n2):
    if n2 == 0:
        return "Modulus by zero is undefined"
    return n1 % n2

# Main program
print("Select the operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")

# Taking user choice
choice = int(input("Enter the choice(1/2/3/4/5):\n"))

# Check if choice is valid
if choice in [1, 2, 3, 4, 5]:
    # Taking input for the two numbers
    n1 = int(input("Enter the first number\n"))
    n2 = int(input("Enter the second number\n"))

    # Performing the chosen operation
    if choice == 1:
        print(f"{n1} + {n2} = {addition(n1, n2)}")
    elif choice == 2:
        print(f"{n1} - {n2} = {subtraction(n1, n2)}")
    elif choice == 3:
        print(f"{n1} * {n2} = {multiplication(n1, n2)}")
    elif choice == 4:
        result = division(n1, n2)
        if isinstance(result, str):
            print(result)  # If division by zero
        else:
            print(f"{n1} / {n2} = {result}")
    elif choice == 5:
        result = modulus(n1, n2)
        if isinstance(result, str):
            print(result)  # If modulus by zero
        else:
            print(f"{n1} % {n2} = {result}")
else:
    print("Invalid Input")