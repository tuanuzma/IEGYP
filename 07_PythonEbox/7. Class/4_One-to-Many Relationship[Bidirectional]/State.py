# Import the City class from City.py
from City import City

# State class
class State:
    def __init__(self, name, city_list=None):  # Correct constructor
        if city_list is None:
            city_list = []  # Initialize with an empty list if no cities are passed
        self.__name = name  # private attribute for state name
        self.__city_list = city_list  # list of cities in this state

    def __str__(self):  # Correct string representation method
        return f"{self.__name} has {len(self.__city_list)} cities"  # output format for state details

    @property
    def name(self):
        return self.__name

    @property
    def city_list(self):
        return self.__city_list

    @city_list.setter
    def city_list(self, city_list):
        self.__city_list = city_list

    def add_city(self, city):
        if isinstance(city, City) and city not in self.__city_list:
            self.__city_list.append(city)  # only add the city if it's not already in the list

    def get_city_count(self):
        return len(self.__city_list)
