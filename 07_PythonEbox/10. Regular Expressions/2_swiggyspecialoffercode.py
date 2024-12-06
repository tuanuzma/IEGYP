def is_valid_offer_code(offer_code):
    # Check if the offer code contains all vowels
    vowels = set('aeiou')
    # If all vowels are present in the offer code, return 'Accepted'
    if vowels.issubset(set(offer_code)):
        return "Accepted"
    else:
        return "Not Accepted"
def main():
    # Take input for the offer code
    offer_code = input().strip()
    # Check if the offer code is valid
    result = is_valid_offer_code(offer_code)
    # Output the result
    print(result)
# Ensure that the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()