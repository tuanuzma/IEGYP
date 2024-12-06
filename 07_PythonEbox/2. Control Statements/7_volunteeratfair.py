# Input section
N, M, K = map(int, input().split())

# Calculate the initial difference between the two groups
initial_difference = abs(N - M)

# Calculate the minimum possible difference after adding K volunteers
min_difference = max(initial_difference - K, 0)

# Output the result
print(min_difference)   