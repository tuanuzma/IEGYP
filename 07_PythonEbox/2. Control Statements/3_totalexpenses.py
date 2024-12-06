# Function to calculate total expenses
def calculate_total_expenses(ticket_cost, num_tickets):
    # Calculate the total cost without any discount
    total_cost = ticket_cost * num_tickets
    # Apply the appropriate discount based on the number of tickets
    if num_tickets < 50:
        discount_percent = 0
    elif num_tickets <= 100:
        discount_percent = 0.1
    elif num_tickets <= 200:
        discount_percent = 0.2
    elif num_tickets <= 400:
        discount_percent = 0.3
    elif num_tickets <= 500:
        discount_percent = 0.4
    else:
        discount_percent = 0.5
    # Calculate the discounted amount
    discount_amount = total_cost * discount_percent
    # Calculate the final total expenses
    final_total = total_cost - discount_amount
    return final_total
# Input from user
ticket_cost = float(input())
num_tickets = int(input())
# Calculate and output the total expenses
total_expenses = calculate_total_expenses(ticket_cost, num_tickets)
print(f"{total_expenses:.2f}")