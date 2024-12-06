def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to √n
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(a, b):
    """Find and return prime numbers in the range [a, b]."""
    primes = []
    for num in range(a, b + 1):  # Iterate through the range
        if is_prime(num):  # Check if the number is prime
            primes.append(num)
    return primes

# Input: Two integers a and b
a = int(input())
b = int(input())

# Get the list of prime numbers in the range and print them
primes = prime_numbers_in_range(a, b)
print(" ".join(map(str, primes)))