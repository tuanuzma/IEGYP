# Main program to prompt for positive integers
while True:
    try:
        # Prompt user for input
        number = input("Enter a positive integer\n")
        # Attempt to convert input to an integer
        num = int(number)
        # Check if the number is positive
        if num > 0:
            print(f"Good! You entered {num}")
            break  # Exit the loop if a positive number is entered
        else:
            raise ValueError("You entered a negative number. Retry!")
    except ValueError as e:
        # Handle ValueError for negative numbers or invalid inputs
        print(e)   