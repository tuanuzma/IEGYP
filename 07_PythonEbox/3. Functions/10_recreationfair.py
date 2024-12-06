def findValue(f1, f2):
    # Function to calculate GCD using the Euclidean algorithm
    while f2 != 0:
        f1, f2 = f2, f1 % f2
    return f1

# Input values
f1 = int(input().strip())  # Number of cards Gary has
f2 = int(input().strip())  # Number of cards Dory has

# Output the maximum stack size
print(findValue(f1, f2))   