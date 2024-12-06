from math import gcd

def printValue(numerator, denominator):
    # Simplify the fraction
    common_divisor = gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor
    
    # Check if it can be a whole number
    if numerator % denominator == 0:
        print(numerator // denominator)
    else:
        # If it's a mixed fraction
        whole_number = numerator // denominator
        remaining_numerator = numerator % denominator
        
        if whole_number > 0:
            print(f"{whole_number} {remaining_numerator}/{denominator}")
        else:
            print(f"{remaining_numerator}/{denominator}")

# Input values
numerator = int(input().strip())
denominator = int(input().strip())

# Function call
printValue(numerator, denominator)   