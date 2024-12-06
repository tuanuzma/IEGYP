# Step 1: Read the number of employees
n = int(input())

# Step 2: Create an empty dictionary to store employee data
employee_data = {}

# Step 3: Read the employee data and store it in the dictionary
for _ in range(n):
    # Read employee name and salary components
    data = input().split()
    name = data[0]
    salary = float(data[1])
    pf = float(data[2])
    health_insurance = float(data[3])
    
    # Store the data in the dictionary
    employee_data[name] = [salary, pf, health_insurance]

# Step 4: Read the employee name to calculate the average salary
employee_name = input()

# Step 5: Retrieve the salary data for the employee and calculate the average
salary_details = employee_data[employee_name]
total_salary = sum(salary_details)  # sum the salary, PF, and health insurance
average_salary = total_salary / 3  # compute the average salary

# Step 6: Output the average salary formatted to two decimal places
print(f"{average_salary:.2f}")   