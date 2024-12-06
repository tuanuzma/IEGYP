# Function to calculate the average word length
def calculate_average_word_length(filename):
    try:
        # Open the file
        with open(filename, 'r') as file:
            # Read the entire file contents
            text = file.read()
            
            # Split the text into words
            words = text.split()
            
            # Calculate the total number of words
            total_words = len(words)
            
            # Calculate the sum of the lengths of all words
            total_length = sum(len(word) for word in words)
            
            # Calculate the average word length
            if total_words == 0:
                return 0  # Avoid division by zero if there are no words
            average_length = total_length // total_words
            
            # Return the average word length as an integer
            return average_length
    except FileNotFoundError:
        return "File not found."

# File name
filename = 'averageLength.txt'

# Calculate and print the average word length
average_length = calculate_average_word_length(filename)
print(average_length)