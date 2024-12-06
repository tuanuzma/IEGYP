from datetime import datetime, timedelta

# Step 1: Read the number of days
n = int(input())

# Step 2: Read the starting date
start_date_str = input()

# Step 3: Convert the input date string to a datetime object
start_date = datetime.strptime(start_date_str, "%d-%m-%Y")

# Step 4: Generate the next n-1 dates (i.e., start from the next day)
for i in range(1, n):  # Start from 1 to skip the first date
    current_date = start_date + timedelta(days=i)
    print(current_date.strftime("%d-%m-%Y"))