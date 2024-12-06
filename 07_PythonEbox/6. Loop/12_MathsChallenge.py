def streak(n):
    k = 1
    while (n + k) % (k + 1) == 0:
        k += 1
    return k

def P(k, N):
    count = 0
    for n in range(2, N + 1):
        if streak(n) == k:
            count += 1
    return count

# Read the input values
k = int(input())  # the streak value to look for
N = int(input())  # the upper limit of n

# Call the function and print the result
print(P(k, N))   