# Import the Hall class from Hall.py
from Hall import Hall

# Get user input for the start date, end date, and cost per day
print("Enter Start time")
start_date = input()
print("Enter the End time")
end_date = input()
print("Enter the cost per day")
cost_per_day = int(input())

# Create a Hall object with the input data
hall_booking = Hall(start_date, end_date, cost_per_day)

# Call the no_days method to calculate and display the results
hall_booking.no_days()
