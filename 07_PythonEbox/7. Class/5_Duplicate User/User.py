# User class
class User:
    def __init__(self, name, username, password, mobile_number):  # Correct constructor
        self.name = name
        self.username = username
        self.password = password
        self.mobile_number = mobile_number

    # Override the equality method to compare users by mobile number
    def __eq__(self, other):  # Correct equality method
        if isinstance(other, User):
            return self.mobile_number == other.mobile_number
        return False
