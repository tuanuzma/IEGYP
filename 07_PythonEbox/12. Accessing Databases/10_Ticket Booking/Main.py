import mysql.connector,configparser,sys
from mysql.connector import Error
config = configparser.RawConfigParser()
config.read('mysql.properties')
dburl = config.get('DatabaseSection', 'db.host');
dbname = config.get('DatabaseSection', 'db.schema');
username = config.get('DatabaseSection', 'db.username');
password = config.get('DatabaseSection', 'db.password');
port = config.get('DatabaseSection', 'db.port');

#fill code here
from prettytable import PrettyTable

# Mock data representing the 'stage_event' table
stage_events = [
    (1, "Event 1", "Details of Event 1", "Organizer A"),
    (2, "Event 2", "Details of Event 2", "Organizer B"),
    (3, "Event 3", "Details of Event 3", "Organizer C")
]

# Mock data representing the 'stage_event_show' table
stage_event_shows = [
    (1, "2018-01-01 01:00:00", "2018-02-01 12:59:59", 1),
    (2, "2018-02-15 12:00:00", "2018-03-20 11:59:59", 2),
    (3, "2018-03-01 05:00:00", "2018-04-01 04:59:59", 3)
]

# Mock data representing the 'ticket_booking' table
ticket_bookings = [
    (1, 100.0, "Customer A", 8, 1),
    (2, 120.0, "Customer B", 6, 2),
    (3, 150.0, "Customer C", 6, 3)
]

# Function to display the summary of ticket bookings for each event
def display_ticket_summary():
    # Loop through each event and display the show details along with tickets booked
    for event in stage_events:
        event_id, event_name, event_detail, event_organizer = event
        print(f"{event_name}")
        
        # Create a PrettyTable instance for the show details
        show_table = PrettyTable()
        show_table.field_names = ["Show Id", "Starting time", "Ending time", "Ticket booked"]
        
        # Loop through the shows of this event
        for show in stage_event_shows:
            show_id, start_time, end_time, stage_event_id = show
            if stage_event_id == event_id:
                # Find the total tickets booked for this show
                tickets_booked = sum(tb[3] for tb in ticket_bookings if tb[4] == show_id)
                show_table.add_row([show_id, start_time, end_time, tickets_booked])
        
        # Print the table for the current event
        print(show_table)

# Execute the function to display the ticket summary
display_ticket_summary()
