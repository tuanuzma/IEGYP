# City class
class City:
    def __init__(self, name, state):  # Correct constructor
        self.__name = name  # private attribute for city name
        self.__state = state  # private attribute for state (type State)

    def __str__(self):  # Correct string representation method
        return f"{self.__name} is in state {self.__state.name}"  # output format for city details

    @property
    def name(self):
        return self.__name

    @property
    def state(self):
        return self.__state
