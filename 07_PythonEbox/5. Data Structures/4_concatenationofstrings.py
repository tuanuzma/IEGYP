# Input the first string
string1 = input("Enter the first string: ").strip()

# Input the second string
string2 = input("Enter the second string: ").strip()

# Check if the first letters of both strings are the same
if string1[0].lower() == string2[0].lower():
    # Concatenate and print the result if they match
    print(f"{string1} {string2}")
else:
    # Print "Invalid Input" if they do not match
    print("Invalid Input")
