# Input the log string
s = input().strip()

# Initialize the expected order: 'C' -> 'E' -> 'S'
current_stage = 'C'

# Iterate through the string to check if it follows the correct order
for activity in s:
    if activity == 'C':
        if current_stage in ['E', 'S']:
            print("no")
            break
    elif activity == 'E':
        if current_stage == 'S':
            print("no")
            break
        current_stage = 'E'
    elif activity == 'S':
        current_stage = 'S'
else:
    print("yes")   