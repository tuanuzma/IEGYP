def daysInYear(year, is_leap=False):
    # Determine if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
    # Print the result based on the leap year status
    if is_leap:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
# Input from user
year = int(input())
daysInYear(year)   