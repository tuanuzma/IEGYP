# Input Aayush's 5 subject scores as space-separated integers
scores = list(map(int, input().split()))

# Condition 1: No failures (i.e., no score should be 2)
no_failures = all(score != 2 for score in scores)

# Condition 2: At least one full score (i.e., at least one score should be 5)
at_least_one_full_score = any(score == 5 for score in scores)

# Condition 3: Average score should be at least 4.0
average_score = sum(scores) / 5

# Check if all conditions are satisfied
if no_failures and at_least_one_full_score and average_score >= 4.0:
    print("Yes")
else:
    print("No")   