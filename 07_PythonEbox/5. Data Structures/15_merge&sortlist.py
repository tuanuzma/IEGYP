# Step 1: Read the size of the lists (although both lists are of the same size, we just need to read one)
n = int(input("Enter the length of the list:\n"))

# Step 2: Read the elements for the first list
list1 = list(map(int, input("Enter the elements for first list:\n").split()))

# Step 3: Read the elements for the second list
list2 = list(map(int, input("Enter the elements for second list:\n").split()))

# Step 4: Merge the two lists
merged_list = list1 + list2

# Step 5: Sort the merged list
sorted_list = sorted(merged_list)

# Step 6: Output the results
print("Merging of two lists:")
print(merged_list)
print("Sorted list:")
print(sorted_list)