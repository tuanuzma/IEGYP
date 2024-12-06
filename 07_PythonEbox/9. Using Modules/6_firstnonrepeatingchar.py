def first_non_repeating_character(s):
    # Create a dictionary to count occurrences of each character
    char_count = {}
    # Count each character's frequency
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    # If no non-repeating character is found, return '#'
    return '#'
# Main program
input_string = input()
result = first_non_repeating_character(input_string)
print(result)   