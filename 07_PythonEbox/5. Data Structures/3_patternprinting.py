def print_pattern(n):
    # Constructing the single line pattern
    line_pattern = '/' * n + '\\' * n + '/' * n + '\\' * n
    
    # Print the pattern for 4 lines
    for _ in range(4):
        print(line_pattern)

# Example usage:
if __name__== "__main__":
    # Sample Input
    n = int(input())
    print_pattern(n)