def min_notes(N):
    # List of available denominations in descending order
    denominations = [100, 50, 10, 5, 2, 1]
    note_count = 0  # To store the total number of notes used

    for denom in denominations:
        # Calculate how many notes of this denomination can be used
        count = N // denom
        note_count += count
        # Update N to the remaining amount
        N %= denom
    
    return note_count

# Input
N = int(input())  # Input the amount of change to be given

# Output
print(min_notes(N))