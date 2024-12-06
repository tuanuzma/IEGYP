def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    """Return the sum of all primes from 1 to n."""
    return sum(i for i in range(2, n + 1) if is_prime(i))

def continuous_prime_sum(n, t):
    """Perform the sum of primes operation t times."""
    current_sum = sum_of_primes(n)
    for _ in range(t - 1):  # We already calculated the first sum
        current_sum = sum_of_primes(current_sum)
    return current_sum

def main():
    # Read the input values
    n = int(input())  # Last integer of prime series
    t = int(input())  # Number of times to perform the sum operation
    
    # Get the continuous prime sum result
    result = continuous_prime_sum(n, t)
    
    # Print the result in the required format
    print(f"Sum:{result}")

if __name__ == "__main__":
    main()   