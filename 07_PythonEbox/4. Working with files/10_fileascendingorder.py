def file_ascending_order():
    # Open the file 'sample.txt' in read mode
    try:
        with open("sample.txt", "r") as file:
            # Read all the lines from the file
            numbers = [int(line.strip()) for line in file.readlines()]
        
        # Sort the numbers in ascending order
        numbers.sort()
        
        # Display the sorted numbers
        print("Ascending Order of the file content is:")
        for number in numbers:
            print(number)
    
    except FileNotFoundError:
        print("The file 'sample.txt' does not exist.")

# Call the function
file_ascending_order()