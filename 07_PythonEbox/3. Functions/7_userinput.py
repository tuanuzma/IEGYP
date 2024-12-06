# Function definition
def multiVarFunc():
    # Taking inputs
    department = input("Enter department name:\n").strip()
    total_students = int(input("Enter the number of total students:\n").strip())
    total_faculty = int(input("Enter the number of total faculties:\n").strip())
    # Returning multiple values
    return department, total_students, total_faculty

# Main program
# Function call to get values
department, total_students, total_faculty = multiVarFunc()

# Displaying the details
print("Details:")
print(f"Department:{department}")
print(f"Total students:{total_students}")
print(f"Total faculties:{total_faculty}")   