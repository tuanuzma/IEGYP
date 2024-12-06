# Input values for X and Y
X = int(input("Enter the value of X"))  # X corresponds to the number of adult tickets more than children tickets
Y = int(input("Enter the value of Y"))  # Y corresponds to the total money made from ticket sales
# Solve for C (number of children tickets)
C = (Y - 5 * X) // 13  # Using the formula C = (Y - 5X) / 13
# Calculate the number of adult and senior tickets
A = C + X  # Number of adult tickets
S = 2 * C  # Number of senior tickets
# Output the results
print(f"Number of children tickets sold : {C}")
print(f"Number of adult tickets sold : {A}")
print(f"Number of senior tickets sold : {S}")