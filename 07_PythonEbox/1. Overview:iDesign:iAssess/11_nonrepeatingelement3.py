def findNonRepeatingElement(arr, n):
    ones = 0
    twos = 0

    for i in range(n):
        # Update `twos` with the bits that have appeared twice
        twos |= (ones & arr[i])
        
        # Update `ones` with the bits that have appeared once
        ones ^= arr[i]
        
        # Find bits which have appeared three times and reset them in `ones` and `twos`
        common_bit_mask = ~(ones & twos)
        
        ones &= common_bit_mask
        twos &= common_bit_mask
    
    return ones  # The remaining value in `ones` will be the non-repeating element

# Input
n = int(input())  # First input: size of the array

arr = list(map(int, input().split()))  # Read next `n` integers

# Find and output the non-repeating element
result = findNonRepeatingElement(arr, n)
print(result)