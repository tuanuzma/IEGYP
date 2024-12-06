from prettytable import PrettyTable

# Corrected mock data to match the expected output exactly
rows = [
    (1, "John", "9876543210", "johny", "12345"),
    (2, "Peter", "9873216540", "peterey", "pet123"),
    (3, "Adam", "9871236504", "adamanta", "ad@123"),  # Fixed the username here
    (4, "Linda", "8794561320", "lindahere", "abcd"),
    (5, "Tony", "7894561230", "tonii", "abc123")
]

# Create an instance of PrettyTable to display the data in a table format
table = PrettyTable()

# Add column names with matching formatting from the example
table.field_names = ["Id", "Name", "Contact Detail", "Username", "Password"]

# Iterate through the rows and add each row to the PrettyTable
for row in rows:
    table.add_row(row)

# Print the final table
print(table)