# Function to generate prime numbers up to the Nth term
def generate_prime_series(N):
    primes = []
    num = 2  # Start checking for prime from the first prime number
    while len(primes) < N:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # Check divisibility from 2 to sqrt(num)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1  # Move to the next number
    return primes
# Input from user
N = int(input())
# Generate and output the prime series
prime_series = generate_prime_series(N)
print(" ".join(map(str, prime_series)))