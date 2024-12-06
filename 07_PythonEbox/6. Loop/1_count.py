# Function to count even and odd registration codes
def count_even_odd_registration_codes(N, registration_codes):
    even_count = 0
    odd_count = 0
    # Iterate through the registration codes to count evens and odds
    for code in registration_codes:
        if code % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
# Input from user
N = int(input())
registration_codes = []
# Collecting the registration codes
for _ in range(N):
    code = int(input())
    registration_codes.append(code)
# Calculate counts of even and odd registration codes
even_count, odd_count = count_even_odd_registration_codes(N, registration_codes)
# Output the result
print(even_count, odd_count)