def greet(name, message="Welcome to Python Programming"):
    return f"Hello {name}, {message}"
# Display menu
print("Menu")
print(" 1. Name and Message")
print(" 2. Name")
# Get user choice
choice = int(input())
if choice == 1:
    # Get user name and message
    name = input("Enter the name\n")
    message = input("Enter the message\n")
    print(greet(name, message))
elif choice == 2:
    # Get user name only
    name = input("Enter the name\n")
    print(greet(name))
else:
    print("Invalid choice")   