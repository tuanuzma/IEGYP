def calculate_sum_of_integers():
    try:
        # Open the input file
        with open("sample.txt", "r") as file:
            # Read the contents of the file
            lines = file.readlines()
        # Initialize the sum
        total_sum = 0
        # Iterate through each line and convert it to an integer
        for line in lines:
            num = int(line.strip())
            total_sum += num
        # Print the result
        print(f"The sum of the integers in the file sample.txt is:{total_sum}")
    except FileNotFoundError:
        print("Error: File 'sample.txt' not found.")
    except ValueError:
        print("Error: Invalid integer format in the file.")
    except Exception as e:
        print(f"Error: {e}")
# Call the function to calculate the sum of integers
calculate_sum_of_integers()   