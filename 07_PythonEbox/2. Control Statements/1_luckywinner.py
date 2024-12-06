# Function to determine if the ticket number is a lucky winner
def check_lucky_winner(ticket_number):
    # Get the last digit of the ticket number
    last_digit = ticket_number % 10
    # Check if the last digit is 3 or 8
    if last_digit == 3 or last_digit == 8:
        return "Lucky Winner"
    else:
        return "Not a Lucky Winner"
# Input from user
ticket_number = int(input())
# Check and output the result
result = check_lucky_winner(ticket_number)
print(result)