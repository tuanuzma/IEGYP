# Student class definition
class Student:
    def __init__(self, _id, _username, _password, _name, _address, _city, _pincode, _contact_number, _email):
        self.__id = _id
        self.__username = _username
        self.__password = _password
        self.__name = _name
        self.__address = _address
        self.__city = _city
        self.__pincode = _pincode
        self.__contact_number = _contact_number
        self.__email = _email

    # Overriding the __str__ method to display the student details
    def __str__(self):
        return (f"Id : {self.__id}\n"
                f"User Name : {self.__username}\n"
                f"Password : {self.__password}\n"
                f"Name : {self.__name}\n"
                f"Address : {self.__address}\n"
                f"city : {self.__city}\n"
                f"Pincode : {self.__pincode}\n"
                f"Contact Number : {self.__contact_number}\n"
                f"email : {self.__email}")
