# Input: First line is the string, second line is the index (n)
name = input().strip()  # Taking input for the string
n = int(input().strip())  # Taking input for the integer (index)

# Remove the character at index n
# Create a new string without the nth character
result = name[:n-1] + name[n:]

# Output the resulting string
print(result)
