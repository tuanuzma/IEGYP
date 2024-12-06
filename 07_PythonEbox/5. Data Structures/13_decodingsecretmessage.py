# Step 1: Read input values
secret_message = input("Enter Secret Message\n")
start_range = int(input("Enter Starting Range\n"))
end_range = int(input("Enter Ending Range\n"))

# Step 2: Reverse the secret message
reversed_message = secret_message[::-1]

# Step 3: Extract the substring from the reversed message
substring = reversed_message[start_range:end_range + 1]

# Step 4: Get the ASCII values of the first two characters of the original string
ascii_values = str(ord(secret_message[0])) + str(ord(secret_message[1]))

# Step 5: Construct the password
password = substring + ascii_values

# Step 6: Output the password
print(f"Password: {password}")   