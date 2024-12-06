# Custom Exception Class
class NotEligibleException(Exception):
    pass
# Student Class
class Student:
    def __init__(self, marks):
        self.marks = marks
    def check_marks(self):
        if self.marks >= 90:
            return True
        else:
            raise NotEligibleException("Not Eligible")
# Main program to test the Student class
try:
    # Input from user
    marks = int(input("Enter marks of student\n"))
    # Create a Student object
    student = Student(marks)
    # Check eligibility
    if student.check_marks():
        print("Eligible")
except (NotEligibleException, ValueError) as e:
    if isinstance(e, NotEligibleException):
        print(f"Inside Except Block : {e}")
    else:
        print("Invalid Value")