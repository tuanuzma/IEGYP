from Person import Person

def main():
    # Input for the first name, last name, and age
    first_name = input("Enter first name\n")
    last_name = input("Enter last name\n")
    age = input("Enter age\n")
    
    # Create an object of the Person class
    person = Person(first_name, last_name, age)
    
    # Print the full name
    print(f"Full name of the person is {person.fullname()}")
    
    # Print the person details using the __str__ method
    print("Person Details")
    print(person)

if __name__ == "__main__":
    main()