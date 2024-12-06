from datetime import datetime

# Input the first date
date1_str = input().strip()

# Input the second date
date2_str = input().strip()

# Define the format of the input dates
date_format = "%b %d %Y %I:%M%p"

# Convert input strings to datetime objects
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)

# Calculate the difference between the two dates
time_difference = date2 - date1

# Extract the days, seconds, hours, and minutes from the difference
days = time_difference.days
seconds = time_difference.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

# Print the output in the required format
print(f"{days} days, {hours}:{minutes:02}:{remaining_seconds:02}")
   