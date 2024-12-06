# Taking input for the 3 cards
card1 = input().strip().split()
card2 = input().strip().split()
card3 = input().strip().split()

# Extracting card types and numbers
type1, num1 = card1[0], card1[1]
type2, num2 = card2[0], card2[1]
type3, num3 = card3[0], card3[1]

# Checking for Double Bonanza
if type1 == type2 == type3 and num1 == num2 == num3:
    print("Double Bonanza")
# Checking for Bonanza (same type or same number)
elif type1 == type2 == type3 or num1 == num2 == num3:
    print("Bonanza")
# No Bonanza
else:
    print("No Bonanza")