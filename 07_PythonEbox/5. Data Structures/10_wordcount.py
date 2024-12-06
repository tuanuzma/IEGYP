# Input: Read a sentence from the user
sentence = input()

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store the count of each word
word_count = {}

# Iterate over the words and count the occurrences
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Output the word count dictionary
print(word_count)
   