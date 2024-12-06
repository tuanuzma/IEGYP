class Address:
    def __init__(self, street, city, state):
        self._street = street
        self._city = city
        self._state = state

    def __str__(self):
        return f"{self._street}, {self._city}, {self._state}"
