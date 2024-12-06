from Address import Address

class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    def __str__(self):
        return f"{self._name} is a person who is {self._age} years old and lives in the following address: {self._address}"
