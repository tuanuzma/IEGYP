import re
def validate_pan(pan):
    # Regular expression to match the PAN format
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    # Check if the PAN matches the pattern
    if re.match(pattern, pan):
        return "Valid PAN Number"
    else:
        return "Invalid PAN Number"
# Input the PAN number
pan_number = input().strip()
# Validate the PAN number
result = validate_pan(pan_number)
# Output the result
print(result)