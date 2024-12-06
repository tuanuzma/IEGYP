# Input section
n = int(input())  # Total number of marbles
x = int(input())  # Number of red marbles
y = int(input())  # Number of blue marbles

# Calculate the probabilities
prob_red = x / n
prob_blue = y / n
prob_red_after_blue = x / (n - 1)  # After one blue marble is picked

# Output the results formatted to 2 decimal places
print(f"{prob_red:.2f}")
print(f"{prob_blue:.2f}")
print(f"{prob_red_after_blue:.2f}")
