# Input the coordinates
x1, y1, x2, y2 = map(int, input().split())

# Determine the direction
if x2 < x1 and y1 == y2:
    print("left")
elif x2 > x1 and y1 == y2:
    print("right")
elif y2 > y1 and x1 == x2:
    print("up")
elif y2 < y1 and x1 == x2:
    print("down")
else:
    print("sad")   