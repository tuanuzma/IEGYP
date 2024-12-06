# Input the total number of attendance sheets
n = int(input("Enter total Number of sheets:\n"))

# List to store each sheet's register numbers as tuples
attendance_sheets = []

# Set to collect unique register numbers from all sheets
unique_registers = set()

# Process each attendance sheet
for _ in range(n):
    # Input the register numbers for the current sheet
    register_numbers = tuple(map(int, input().split()))
    
    # Add the current sheet (with or without duplicates) to the attendance sheets list
    attendance_sheets.append(register_numbers)
    
    # Add all unique register numbers from this sheet to the unique set
    unique_registers.update(register_numbers)

# Display the initial attendance sheets
print(f"Attendance Sheets with Register Number: {tuple(attendance_sheets)}")

# Convert the unique registers set to a sorted list for the final sheet
final_sheet = tuple(sorted(unique_registers))

# Display the final sheet with unique register numbers
print(f"Final sheet: {final_sheet}")
   