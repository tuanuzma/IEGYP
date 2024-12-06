import datetime

# Input the year
year = int(input())

# Create a date object for January 1st of the given year
date = datetime.date(year, 1, 1)

# Get the day of the week as an integer (0=Monday, 1=Tuesday, ..., 6=Sunday)
day_of_week = date.weekday()

# Map the integer to the corresponding day name
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Output the result
print(days[day_of_week])   