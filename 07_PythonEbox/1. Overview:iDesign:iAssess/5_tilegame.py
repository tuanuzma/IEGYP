# Input the side of a square tile
side = int(input("Enter the side in cm of a square tile\n"))
# Input the number of square tiles available
tiles = int(input("Enter the number of square tiles available\n"))
# Find the largest number A such that A^2 <= tiles
A = int(tiles ** 0.5)
# Calculate the area of the largest possible square
largest_square_area = (side ** 2) * (A ** 2)
# Output the result
print(f"Area of the largest possible square is {largest_square_area}sqcm")