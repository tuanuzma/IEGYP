from Address import Address
from Person import Person

# Input for person details
name = input("Enter name\n")
age = int(input("Enter age\n"))

# Input for address details
print("Enter address")
street = input("Enter street\n")
city = input("Enter city\n")
state = input("Enter state\n")

# Creating an Address object
address = Address(street, city, state)

# Creating a Person object with the address
person = Person(name, age, address)

# Displaying person details
print("Person Details")
print(person)
