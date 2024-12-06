from prettytable import PrettyTable

# Mock data for testing purposes, simulating the database records
rows = [
    (1, "Food", 50000.0, 10000.0),
    (2, "Electronics", 85000.0, 15000.0),
    (3, "Fashion", 36000.0, 8000.0),
    (4, "Grooming", 15000.0, 5000.0),
    (5, "Books", 20000.0, 7500.0)
]

# Create an instance of PrettyTable to display the data in a table format
table = PrettyTable()

# Add column names based on the expected schema
table.field_names = ["ID", "Name", "Deposit", "Cost per day"]

# Iterate through the rows and add each row to the PrettyTable
for row in rows:
    table.add_row(row)

# Print the final table
print(table)