def generate_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fibonacci_series = []
    # Handle cases for n = 0 or n = 1
    if n <= 0:
        return fibonacci_series
    elif n == 1:
        fibonacci_series.append(0)
        return fibonacci_series
    elif n == 2:
        fibonacci_series.extend([0, 1])
        return fibonacci_series
    # Start with the first two numbers
    fibonacci_series.append(0)
    fibonacci_series.append(1)
    # Generate Fibonacci series up to n terms
    for i in range(2, n):
        next_number = fibonacci_series[i - 1] + fibonacci_series[i - 2]
        fibonacci_series.append(next_number)
    return fibonacci_series
# Main program
try:
    n = int(input())
    # Generate and print Fibonacci series
    result = generate_fibonacci(n)
    print(" ".join(map(str, result)))
except ValueError:
    print("Please enter a valid integer.")   