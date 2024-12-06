# Main.py

# Import the Person class from the Person.py file
from Person import Person

# Input name and age from the user
name = input("Enter name\n")
age = input("Enter age\n")

# Create an instance of Person
person = Person(name, age)

# Display the person's details
print("Person Details")
print(person.name)
print(person.age)
