import re
# Function to extract the maximum number from the hint
def extract_max_number(hint):
    # Find all numbers in the hint using regex
    numbers = re.findall(r'\d+', hint)
    # If numbers were found, return the maximum number
    if numbers:
        max_number = max(map(int, numbers))  # Convert to int and find the max
        return str(max_number)
    else:
        # If no numbers are found, return 'No Password'
        return "No Password"
# Main function
def main():
    # Input reading
    hint = input().strip()
    # Extract the maximum number
    result = extract_max_number(hint)
    # Output the result
    print(result)
# Running the main function
if __name__ == "__main__":
    main()