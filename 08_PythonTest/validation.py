def is_valid_isbn13(isbn):
    # Remove any hyphens or spaces
    isbn = isbn.replace('-', '').replace(' ', '')

    # Check that the ISBN is 13 digits long
    if len(isbn) != 13 or not isbn.isdigit():
        return False

    # Calculate checksum using the ISBN-13 validation algorithm
    total_sum = 0
    for i, digit in enumerate(isbn):
        digit = int(digit)
        # Multiply odd-positioned digits by 1, even-positioned digits by 3
        if i % 2 == 0:
            total_sum += digit
        else:
            total_sum += digit * 3

    # ISBN-13 is valid if total sum is divisible by 10
    return total_sum % 10 == 0

# Function to print validation result
def validate_isbn(isbn):
    if is_valid_isbn13(isbn):
        print(f"{isbn} is a valid ISBN-13 number.")
    else:
        print(f"{isbn} is not a valid ISBN-13 number.")

# Sample executions
validate_isbn("978-0-306-40615-7")
validate_isbn("978-0-262-13472-9")