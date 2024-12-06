def count_words(input_string):
    # Split the input string into words
    words = input_string.split()
    # Initialize a dictionary to store word counts
    word_count = {}
    # Count occurrences of each word
    for word in words:
        # Convert to lowercase to ensure case insensitivity
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
# Main program
input_string = input("Enter the String")
word_counts = count_words(input_string)
# Output the counts in the specified format
for word, count in sorted(word_counts.items()):
    print(f"{word}-{count}")   