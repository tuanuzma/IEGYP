def count_character_frequency(file_name):
    try:
        # Open the file and read the content
        with open(file_name, 'r') as file:
            content = file.read()
        
        # Initialize a dictionary to store character frequencies
        frequency = {}
        
        # Count the frequency of each character
        for char in content.lower():  # Convert to lowercase for case insensitivity
            if char.isalpha():  # Consider only alphabetic characters
                frequency[char] = frequency.get(char, 0) + 1
        
        # Sort the dictionary by keys (alphabetically)
        sorted_frequency = dict(sorted(frequency.items()))
        
        # Print the result
        for char, count in sorted_frequency.items():
            print(f"{char}: {count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File name
file_name = "frequencyFile.txt"

# Call the function
count_character_frequency(file_name)   