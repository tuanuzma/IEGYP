# Function to generate the series
def generate_series(n):
    series = []  # Initialize an empty list to store the series
    for i in range(1, n + 1):
        if i == 1:
            term = 20  # The first term is 20
        else:
            term = 20 + (i - 1) * 40 + ((i - 1) * (i - 2) // 2) * 4
        series.append(term)  # Append the term to the series
    
    return " ".join(map(str, series))  # Convert the series list to a space-separated string

# Input: Read the number of terms (N)
n = int(input())

# Output: Print the series till Nth term
print(generate_series(n))