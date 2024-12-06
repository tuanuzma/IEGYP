import numpy as np
# Get input for first array
print("Enter the size of 1st array")
size1 = int(input())
print("Enter the elements of first array")
arr1 = np.array([float(input()) for _ in range(size1)])
# Get input for second array
print("Enter the size of 2nd array")
size2 = int(input())
print("Enter the elements of second array")
arr2 = np.array([float(input()) for _ in range(size2)])
# Perform set operations
union_arr = np.unique(np.concatenate((arr1, arr2)))
intersection_arr = np.intersect1d(arr1, arr2)
difference_arr = np.setdiff1d(arr1, arr2)
# Print results
print("Union Array")
print(union_arr)
print("Intersection Array")
print(intersection_arr)
print("Difference Array")
print(difference_arr)   