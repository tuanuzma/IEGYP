# Function to calculate gross salary based on basic salary
def calculate_gross_salary(basic_salary):
    # Initialize HRA and DA
    if basic_salary < 15000:
        HRA = 0.15 * basic_salary  # 15% of basic salary
        DA = 0.90 * basic_salary   # 90% of basic salary
    else:
        HRA = 5000                  # Fixed HRA of Rs. 5000
        DA = 0.98 * basic_salary    # 98% of basic salar
    # Calculate gross salary
    gross_salary = basic_salary + HRA + DA
    return gross_salary
# Input from user
basic_salary = int(input())
# Calculate and output the gross salary
gross_salary = calculate_gross_salary(basic_salary)
print(f"{gross_salary:.2f}")