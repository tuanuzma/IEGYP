# Function to compute BMI
def computeBMI(weight, height_cm):
    height_m = height_cm / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)  # Calculate BMI
    return bmi

# Input section
weight = float(input("Enter weight\n"))  # Input weight in kg
height = float(input("Enter height\n"))  # Input height in cm
age = int(input("Enter age\n"))  # Input age in years

# Compute BMI
bmi = computeBMI(weight, height)

# Compute BFP using the formula
bfp = 1.20 * bmi + 0.23 * age - 16.2

# Output the result with formatting to 2 decimal places
print(f"BFP is {bfp:.2f}")   