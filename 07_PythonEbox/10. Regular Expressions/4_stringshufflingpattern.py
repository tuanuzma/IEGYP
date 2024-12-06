def shuffle_strings(str1, str2):
    # Initialize an empty result string
    result = []
    # Find the lengths of both strings
    len1, len2 = len(str1), len(str2)
    # Iterate over the length of the longer string
    for i in range(max(len1, len2)):
        if i < len1:
            result.append(str1[i])  # Add character from str1
        if i < len2:
            result.append(str2[len2 - 1 - i])  # Add character from str2 (reversed order)
    # Join the list of characters into a string
    return ''.join(result)
def main():
    # Read the two input strings
    str1 = input().strip()
    str2 = input().strip()
    # Get the shuffled result
    result = shuffle_strings(str1, str2)
    # Output the result
    print(result)
# Ensure the main function is called when the script is executed
if __name__ == "__main__":
    main()   