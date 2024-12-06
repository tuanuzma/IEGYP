def calculate_batting_average():
    try:
        # Prompt user for the number of matches
        n = int(input("Enter the number of matches\n"))
        # Initialize a list to store scores
        scores = []
        # Prompt user for scores
        print("Enter the scores")
        for _ in range(n):
            score = input()  # Read input as string
            scores.append(int(score))  # Convert to integer and append to the list
        # Calculate batting average
        average = sum(scores) / n
        # Print the batting average rounded to two decimal places
        print(f"Batting average: {average:.2f}")
    except ValueError:
        print("Type Error Exception")
# Call the function to execute the program
calculate_batting_average()   