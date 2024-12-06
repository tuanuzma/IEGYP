def write_blood_donor_details():
    # Taking inputs from the user
    name = input("Enter the recipient name\n")
    blood_group = input("Enter the blood group\n")
    age = input("Enter the age\n")
    gender = input("Enter the gender\n")
    
    # Prepare the data in the required format
    donor_details = f"{name},{blood_group},{age},{gender}"
    
    # Write the details to the file CAfile2.txt instead of file.txt
    with open("CAfile2.txt", "w") as file:
        file.write(donor_details)
    
    # Inform the user that the data has been stored
    print("Data has been stored")

# Call the function
write_blood_donor_details()