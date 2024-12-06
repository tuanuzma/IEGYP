def decode_message(message, split_char):
    """Decode the message by splitting it with the given character and capitalizing the first letter of each word."""
    # Split the message using the split character
    words = message.split(split_char)
    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words if word]  # Ignore empty words if any
    return capitalized_words

def main():
    # Input the encoded message and the split character
    message = input().strip()
    split_char = input().strip()
    
    # Decode the message
    decoded_message = decode_message(message, split_char)
    
    # Output the results
    print("Strings after splitting")
    for word in decoded_message:
        print(word)

if __name__ == "__main__":
    main()