# Function to determine the grade of the ride based on its factors
def determine_ride_grade(hurl_factor, spin_factor, speed_factor):
    # Initialize condition flags
    hurl_condition = hurl_factor > 50
    spin_condition = spin_factor > 60
    speed_condition = speed_factor > 100
    # Count the number of conditions met
    conditions_met = sum([hurl_condition, spin_condition, speed_condition])
    # Determine the grade based on the conditions met
    if conditions_met == 3:
        return 10
    elif conditions_met == 2:
        if hurl_condition and spin_condition:
            return 9  # Hurl and Spin
        elif spin_condition and speed_condition:
            return 8  # Spin and Speed
        elif hurl_condition and speed_condition:
            return 7  # Hurl and Speed
    elif conditions_met == 1:
        return 6
    else:
        return 5
# Input from user
hurl_factor, spin_factor, speed_factor = map(int, input().split())
# Calculate and output the grade of the ride
ride_grade = determine_ride_grade(hurl_factor, spin_factor, speed_factor)
print(ride_grade)