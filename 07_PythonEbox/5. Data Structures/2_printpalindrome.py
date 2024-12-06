word=input().strip()
length=len(word)

firstHalf=word[:length//2+(length%2)] 


if length %2==0:
    palindrome=firstHalf+firstHalf[::-1]
else: 
    palindrome=firstHalf+firstHalf[-2::-1]

print(palindrome)