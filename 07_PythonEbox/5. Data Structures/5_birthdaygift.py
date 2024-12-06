# Input number of schools
n = int(input())

# Input number of students in each school
students = [int(input()) for _ in range(n)]

# Input price of a book
price_per_book = int(input())

# Calculate total number of books required
total_books = sum(students)

# Calculate total cost
total_cost = total_books * price_per_book

# Output the result with a space after the colon to match the expected format
print(f"Total number of books required : {total_books}")
print(f"Total cost : {total_cost}")
