class College:
    def display(self, *args):
        if len(args) == 5:
            college_id, college_name, city, state, pincode = args
            # Returning formatted details, each on a new line
            return f"id : {college_id}\nName : {college_name}\nCity : {city}\nState : {state}\nPincode : {pincode}\n"
        elif len(args) == 3:
            college_name, contact_number, email = args
            return f"Name : {college_name}\nContact Number : {contact_number}\nEmail : {email}\n"
        else:
            return "Invalid number of arguments!\n"

def main():
    college = College()

    # Display the menu only once
    print("1. Enter College address and Display\n2. Enter  the contact details and Display\n3. exit")

    while True:
        choice = int(input("Enter your choice\n"))

        if choice == 1:
            college_id = input("Enter the College id\n")
            college_name = input("Enter the College name\n")
            city = input("Enter the City\n")
            state = input("Enter the State\n")
            pincode = input("Enter the Pincode\n")
            print(college.display(college_id, college_name, city, state, pincode))

        elif choice == 2:
            college_name = input("Enter the name of the College\n")
            contact_number = input("Enter the contact number\n")
            email = input("Enter the email id\n")
            print(college.display(college_name, contact_number, email))

        elif choice == 3:
            break

        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()   