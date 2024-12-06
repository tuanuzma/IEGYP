import re
def check_phone_number(phone_number):
    # Regular expression pattern to match valid phone numbers
    pattern = r'^\+91-\d{10}$'
    # Check if the phone number matches the pattern
    if re.match(pattern, phone_number):
        return "Not a Spam Call"
    else:
        return "Spam Call"
def main():
    # Read input
    phone_number = input().strip()
    # Check the phone number and print the result
    result = check_phone_number(phone_number)
    print(result)
# Call the main function to execute the program
if __name__ == "__main__":
    main()