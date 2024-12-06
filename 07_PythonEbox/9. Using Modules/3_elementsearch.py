# Main program
try:
    # Read the number of balls
    n = int(input())
    # Initialize an empty list to store the balls
    balls = []
    # Read each ball number
    print()
    for _ in range(n):
        ball = int(input())
        balls.append(ball)
    # Read the number to search
    search_number = int(input())
    # Check if the searched number is in the list of balls
    if search_number in balls:
        print("Got It!")
    else:
        print("Sorry!")
except ValueError:
    print("Please enter valid integers.")   