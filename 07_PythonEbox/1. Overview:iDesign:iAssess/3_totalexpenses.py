# Function to calculate percentage
def calculate_percentage(part, total):
    return (part / total) * 100
# Input expenses for the event
branding_expenses = int(input("Enter branding expenses"))
travel_expenses = int(input("Enter travel expenses"))
food_expenses = int(input("Enter food expenses"))
logistics_expenses = int(input("Enter logistics expenses"))
# Calculate total expenses
total_expenses = branding_expenses + travel_expenses + food_expenses + logistics_expenses
# Calculate percentage of each expense
branding_percentage = calculate_percentage(branding_expenses, total_expenses)
travel_percentage = calculate_percentage(travel_expenses, total_expenses)
food_percentage = calculate_percentage(food_expenses, total_expenses)
logistics_percentage = calculate_percentage(logistics_expenses, total_expenses)
# Display total expenses and percentages
print(f"Total expenses : Rs.{total_expenses:.2f}")
print(f"Branding expenses percentage : {branding_percentage:.2f}%")
print(f"Travel expenses percentage : {travel_percentage:.2f}%")
print(f"Food expenses percentage : {food_percentage:.2f}%")
print(f"Logistics expenses percentage : {logistics_percentage:.2f}%")