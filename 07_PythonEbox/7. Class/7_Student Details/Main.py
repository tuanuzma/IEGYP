# Import the Student class from Student.py
from Student import Student

# Collecting student details from user input
print("Enter the student id")
_id = int(input())
print("Enter the student's username")
_username = input()
print("Enter the password")
_password = input()
print("Enter the name of the student")
_name = input()
print("Enter the address")
_address = input()
print("Enter the city")
_city = input()
print("Enter the pincode")
_pincode = int(input())
print("Enter the contact number")
_contact_number = int(input())
print("Enter the email id")
_email = input()

# Creating an instance of Student with the collected details
student = Student(_id, _username, _password, _name, _address, _city, _pincode, _contact_number, _email)

# Display the student details using the overridden __str__ method
print(student)
