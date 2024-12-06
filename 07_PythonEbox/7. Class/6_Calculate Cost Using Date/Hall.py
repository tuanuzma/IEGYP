from datetime import datetime

# Hall class
class Hall:
    def __init__(self, start_date, end_date, cost_per_day):  # Corrected constructor method
        # If the start_date and end_date are not already datetime objects, convert them
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, "%b %d %Y")  # Convert string to datetime object
        else:
            self.start_date = start_date

        if isinstance(end_date, str):
            self.end_date = datetime.strptime(end_date, "%b %d %Y")  # Convert string to datetime object
        else:
            self.end_date = end_date

        self.cost_per_day = cost_per_day

    # Method to calculate the number of days between start_date and end_date
    def no_days(self):
        num_days = (self.end_date - self.start_date).days  # Calculate number of days
        self.cost(num_days)  # Call cost method
        return num_days

    # Method to calculate the total cost
    def cost(self, d):
        total_cost = d * self.cost_per_day
        print(f"Total number of days {d}")
        print(f"Total cost {total_cost}")
