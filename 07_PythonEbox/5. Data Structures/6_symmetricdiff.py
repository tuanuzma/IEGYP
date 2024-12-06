# Input the first set
set1 = set(map(int, input().split(',')))

# Input the second set
set2 = set(map(int, input().split(',')))

# Check if the sets are equal
if set1 == set2:
    print("invalid set")
else:
    # Find the symmetric difference and print it in sorted order
    sym_diff = sorted(set1.symmetric_difference(set2))
    print(f"{{{', '.join(map(str, sym_diff))}}}")
