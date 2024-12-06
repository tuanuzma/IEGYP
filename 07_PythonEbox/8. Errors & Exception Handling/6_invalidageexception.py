# Custom Exception Class
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
# Function to check voting eligibility
def check_voter_eligibility():
    try:
        # Prompt user for name
        name = input("Enter the Name\n")
        # Prompt user for age
        age = int(input("Enter the age\n"))
        # Check if age is valid for voting
        if age < 18:
            raise CustomError("CustomException: InvalidAgeRangeException")
        # If eligible, print voter details
        print(f"Voter name: {name}")
        print(f"Voter age: {age}")
    except CustomError as e:
        print(e)
# Call the function to execute the program
check_voter_eligibility()