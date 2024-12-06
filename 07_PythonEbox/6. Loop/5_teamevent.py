# Function to assign team based on registration code
def assign_team(N):
    # Convert the number to a string to access individual digits
    registration_code = str(N)
    # Check if the input is valid (has at least two digits)
    if len(registration_code) < 2:
        return "Invalid Input"
    # Get the first and last digits
    first_digit = int(registration_code[0])
    last_digit = int(registration_code[-1])
    # Calculate the absolute difference between the first and last digits
    team_number = abs(first_digit - last_digit)
    # Return the team number (1 to 9)
    return team_number
# Input from user
registration_code = int(input())
# Assign team and output the result
team = assign_team(registration_code)
print(team)