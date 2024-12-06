# Function to calculate final scores after N turns
def calculate_final_score(A, B, N):
    # Initialize scores for Richie and Riya
    richie_score = A
    riya_score = B
    # Iterate through the number of turns
    for turn in range(N):
        if turn % 2 == 0:  # Richie’s turn (even turns)
            richie_score *= 2
        else:               # Riya’s turn (odd turns)
            riya_score *= 2
    # Calculate the final score as the sum of both scores
    final_score = richie_score + riya_score
    return final_score
# Input from user
A, B, N = map(int, input().split())
# Calculate and output the final score
final_score = calculate_final_score(A, B, N)
print(final_score)