# Input number of students
n = int(input())

# Dictionary to store student names and their marks
students_marks = {}

# Input the student names and their respective marks
for _ in range(n):
    input_data = input().split()
    name = input_data[0]
    marks = list(map(int, input_data[1:]))
    students_marks[name] = marks

# Input the student's name for whom to find the second-highest mark
student_name = input().strip()

# Check if the student exists in the dictionary
if student_name in students_marks:
    marks = students_marks[student_name]
    # Check if all marks are the same
    if len(set(marks)) == 1:
        print(f"{student_name} scored same marks in all subjects: {marks[0]}")
    else:
        # Sort marks and find the second-highest mark
        unique_marks = sorted(set(marks), reverse=True)
        second_highest = unique_marks[1]
        print(f"Second Highest mark of {student_name}: {second_highest}")
else:
    print("Student doesn't exist")
   