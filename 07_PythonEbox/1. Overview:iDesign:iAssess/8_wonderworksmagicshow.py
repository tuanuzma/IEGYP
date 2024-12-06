# Taking inputs
print("Enter the number of people who watched show 1")
people1 = int(input().strip())
print("Enter the average rating for show 1")
rating1 = float(input().strip())

print("Enter the number of people who watched show 2")
people2 = int(input().strip())
print("Enter the average rating for show 2")
rating2 = float(input().strip())

print("Enter the number of people who watched show 3")
people3 = int(input().strip())
print("Enter the average rating for show 3")
rating3 = float(input().strip())

# Calculating weighted average
total_people = people1 + people2 + people3
overall_average_rating = (people1 * rating1 + people2 * rating2 + people3 * rating3) / total_people

# Displaying result with 2 decimal places
print(f"The overall average rating for the show is {overall_average_rating:.2f}")