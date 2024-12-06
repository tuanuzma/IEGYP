def search_donor():
    # Taking input for the blood group to search
    blood_group_to_search = input("Enter blood group to search\n")
    
    # Open the file 'file.txt' for reading
    try:
        with open("file.txt", "r") as file:
            donor_details = file.readlines()
        
        # List to store donors that match the given blood group
        matching_donors = []
        
        # Loop through each line (donor details) in the file
        for donor in donor_details:
            name, blood_group, location = donor.strip().split(',')
            if blood_group == blood_group_to_search:
                matching_donors.append((name, blood_group, location))
        
        # If matching donors are found, display their details
        if matching_donors:
            print("Donor details")
            for index, donor in enumerate(matching_donors, 1):
                name, blood_group, location = donor
                print(f"Donor {index}")
                print(f"Donor name : {name}")
                print(f"Blood group : {blood_group}")
                print(f"Donor location : {location}")
        else:
            print(f"No donor found for the blood group {blood_group_to_search}")
    
    except FileNotFoundError:
        print("The file 'file.txt' does not exist.")

# Call the function
search_donor()