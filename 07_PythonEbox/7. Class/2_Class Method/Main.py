from Person import Person

# Creating object using __init__ method
print("Creating object using __init__ method")
name = input("Enter name\n")
age = int(input("Enter age\n"))
person1 = Person(name, age)
print("Person Details")
print(person1)

# Creating object using class method
print("Creating object using class method")
person_str = input("Enter name and age in comma separated format\n")
person2 = Person.from_string(person_str)
print("Person Details")
print(person2)
