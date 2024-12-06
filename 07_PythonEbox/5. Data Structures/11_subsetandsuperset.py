def subset_and_superset():
    # Read the input sets
    set1 = set(map(int, input().split(',')))  # Convert the input into a set of integers
    set2 = set(map(int, input().split(',')))  # Convert the input into a set of integers

    # Check if set1 is a subset of set2
    print(set1 <= set2)  # True if set1 is a subset of set2, False otherwise

    # Check if set2 is a subset of set1
    print(set2 <= set1)  # True if set2 is a subset of set1, False otherwise

    # Check if set1 is a superset of set2
    print(set1 >= set2)  # True if set1 is a superset of set2, False otherwise

    # Check if set2 is a superset of set1
    print(set2 >= set1)  # True if set2 is a superset of set1, False otherwise

# Call the function
subset_and_superset()