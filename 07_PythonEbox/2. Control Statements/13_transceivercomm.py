import math

# Input the communication range R
R = int(input())

# Input the coordinates of the Event Coordinator, Security Chief, and Crowd Control Chief
x1, y1 = map(int, input().split())  # Event Coordinator
x2, y2 = map(int, input().split())  # Security Chief
x3, y3 = map(int, input().split())  # Crowd Control Chief

# Function to calculate the squared distance between two points
def squared_distance(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

# Compute the squared distances between each pair
dist1_2 = squared_distance(x1, y1, x2, y2)  # Event Coordinator to Security Chief
dist1_3 = squared_distance(x1, y1, x3, y3)  # Event Coordinator to Crowd Control Chief
dist2_3 = squared_distance(x2, y2, x3, y3)  # Security Chief to Crowd Control Chief

# Check if direct communication is possible using squared distances (to avoid floating-point precision issues)
R_squared = R ** 2
direct_1_2 = dist1_2 <= R_squared
direct_1_3 = dist1_3 <= R_squared
direct_2_3 = dist2_3 <= R_squared

# Condition to check if communication is possible (either directly or indirectly)
if (direct_1_2 and direct_1_3) or (direct_1_2 and direct_2_3) or (direct_1_3 and direct_2_3):
    print("Yes")
else:
    print("No")   