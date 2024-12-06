# Function to filter numbers divisible by 13
def filter_divisible_by_thirteen():
    try:
        # Input for the size of the list
        n = int(input("Enter size of list\n"))
        # Check if n is greater than 0
        if n <= 0:
            print("Invalid input")
            return
        # Input for the elements in the list
        print("Enter the elements in list")
        elements = []
        for _ in range(n):
            element = int(input())
            elements.append(element)
        # Use lambda function to filter numbers divisible by 13
        divisible_by_thirteen = list(filter(lambda x: x % 13 == 0, elements))
        # Print the results
        print(" ".join(map(str, divisible_by_thirteen)))
    except ValueError:
        print("Invalid input")
# Call the function to execute the program
filter_divisible_by_thirteen()