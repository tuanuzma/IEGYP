import numpy as np
def main():
    # Prompt for the size of the list
    print("Enter the size of the list")
    size = int(input().strip())
    # Prompt for the elements in the list
    print("Enter the elements in the list")
    elements = []
    for _ in range(size):
        elements.append(int(input().strip()))
    # Convert the list to a NumPy array
    arr = np.array(elements)
    # Print the type of the NumPy array
    print(f"class '{arr.__class__.__module__}.{arr.__class__.__name__}'")
    # Print the NumPy array
    print(arr)
if __name__ == "__main__":
    main()   