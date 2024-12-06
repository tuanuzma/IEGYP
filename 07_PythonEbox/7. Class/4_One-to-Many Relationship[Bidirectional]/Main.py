# Import the necessary classes
from City import City
from State import State

# Initializing the state list with predefined states
state_list = ["Tamilnadu", "Andhra", "Karnataka", "Kerala"]
states = {state_name: State(state_name) for state_name in state_list}

# List to store all cities
cities = []

# Function to add cities to states
def add_city_to_state(city_name, state_name):
    if state_name in states:
        # Create a City object and add it to the corresponding state
        city = City(city_name, states[state_name])
        if city not in cities:
            states[state_name].add_city(city)
            cities.append(city)
    else:
        # If state is not in the list, add a new state and city
        new_state = State(state_name)
        states[state_name] = new_state
        city = City(city_name, new_state)
        if city not in cities:
            new_state.add_city(city)
            cities.append(city)

# Print "Enter City Details" only once
print("Enter City Details")

# User Input Loop
while True:
    # Directly ask for city and state name in subsequent iterations
    city_name = input("Enter city name\n")
    state_name = input("Enter state name\n")

    # Add the city to the corresponding state
    add_city_to_state(city_name, state_name)

    # Ask if the user wants to add another city
    add_more = input("Do you want to add another city? Type Yes / No\n")
    if add_more.lower() != 'yes':
        break

# Display City Details
print("\nCity Details")
for city in cities:
    print(city)

# Display State Details
print("\nState Details")
for state in states.values():
    print(state)
