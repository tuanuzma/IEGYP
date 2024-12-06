# Function to calculate weekday and weekend hours based on total salary
def calculate_hours(total_salary):
    # Define the hourly rates
    weekday_rate = 80
    weekend_rate = 50
    # Let x be the number of weekend hours
    # Weekday hours will then be x + 10
    # Total salary equation: (80 * (x + 10)) + (50 * x) = total_salary
    # Rearranging gives us:
    # 80x + 800 + 50x = total_salary
    # 130x + 800 = total_salary
    # 130x = total_salary - 800
    # x = (total_salary - 800) / 130
    weekend_hours = (total_salary - 800) / 130
    weekday_hours = weekend_hours + 10
    return int(weekday_hours), int(weekend_hours)
# Input from user
total_salary = float(input("Enter the total salary paid"))
# Calculate hours worked
weekday_hours, weekend_hours = calculate_hours(total_salary)
# Output results
print(f"Number of weekday hours is {weekday_hours}")
print(f"Number of weekend hours is {weekend_hours}")