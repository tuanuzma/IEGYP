# Input the number of adults, kids, and the number of legs counted
C, D, L = map(int, input().split())

# Maximum possible legs (no kids are riding on adults)
max_legs = 2 * C + 2 * D

# Minimum possible legs (as many kids as possible are riding on adults)
min_legs = 2 * C + 2 * max(0, D - 2 * C)

# Check if the counted legs are within the valid range and is even
if L % 2 == 0 and min_legs <= L <= max_legs:
    print("yes")
else:
    print("no")
       