# Main program
try:
    ascii_value = int(input("Enter the value :\n"))
    # Convert ASCII value to character
    character = chr(ascii_value)
    # Output the character
    print(f"Character of ASCII value {ascii_value} is {character}")
except ValueError:
    print("Please enter a valid integer.")   