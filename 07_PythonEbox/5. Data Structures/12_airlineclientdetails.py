def find_client_details():
    # Step 1: Read the number of clients
    num_clients = int(input("Enter the number of clients\n"))
    
    # Step 2: Create an empty dictionary to store client details
    clients_dict = {}
    
    # Step 3: Input client details and store them in the dictionary
    for i in range(1, num_clients + 1):
        print(f"Enter the details of the client {i}")
        name = input()
        email = input()
        passport_number = input()
        
        # Store the details in the dictionary, with passport number as key
        clients_dict[passport_number] = f"{name}--{email}--{passport_number}"
    
    # Step 4: Search for a passport number
    passport_search = input("Enter the passport number of the client to be searched\n")
    
    # Step 5: Check if the passport number exists in the dictionary
    if passport_search in clients_dict:
        print("Client Details")
        print(clients_dict[passport_search])
    else:
        print("Client not found")

# Call the function to execute the program
find_client_details()