import numpy as np
# Get the number of dice rolls from the user
print("Enter the number of dice rolls")
num_rolls = int(input())
# Get the values of each dice roll from the user
print("Enter the value of each dice roll")
dice_rolls = np.array([int(input()) for _ in range(num_rolls)])
# Count how many rolls are greater than 2
count_greater_than_2 = np.sum(dice_rolls > 2)
# Print the result
print("Dice rolls greater than 2")
print(count_greater_than_2)   