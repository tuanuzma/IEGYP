# Input the coordinates of the two points
x1 = int(input("Enter x1\n"))
y1 = int(input("Enter y1\n"))
x2 = int(input("Enter x2\n"))
y2 = int(input("Enter y2\n"))

# Calculate the midpoint
x_mid = (x1 + x2) / 2
y_mid = (y1 + y2) / 2

# Output the result with formatting to 1 decimal place
print(f"Resort is located at ({x_mid:.1f}, {y_mid:.1f})")   