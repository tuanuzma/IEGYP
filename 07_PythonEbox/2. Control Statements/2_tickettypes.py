# Function to determine the ticket type based on the input character
def get_ticket_type(ticket_char):
    ticket_types = {
        'E': "Early Bird Ticket",
        'e': "Early Bird Ticket",
        'D': "Discount Ticket",
        'd': "Discount Ticket",
        'V': "VIP Ticket",
        'v': "VIP Ticket",
        'S': "Standard Ticket",
        's': "Standard Ticket",
        'C': "Child Ticket",
        'c': "Child Ticket"
    }
    
    # Return the corresponding ticket type or a default message if not found
    return ticket_types.get(ticket_char, "Invalid ticket type")

# Input from user
ticket_char = input()

# Get and output the corresponding ticket type
ticket_type = get_ticket_type(ticket_char)
print(ticket_type)