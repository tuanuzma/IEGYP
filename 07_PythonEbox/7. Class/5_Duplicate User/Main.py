# Import the User class from User.py
from User import User

# Function to get user details from the input
def get_user_details(user_num):
    print(f"Enter the details of User {user_num}")
    name = input("Name : ")
    username = input("Username : ")
    password = input("Password : ")
    mobile_number = int(input("Mobile Number : "))
    return User(name, username, password, mobile_number)

# Get details of two users
user1 = get_user_details(1)
user2 = get_user_details(2)

# Compare the users by mobile number using the overridden __eq__ method
if user1 == user2:
    print(f"User 1 and User 2 are equal")
else:
    print(f"User 1 and User 2 are not equal")
