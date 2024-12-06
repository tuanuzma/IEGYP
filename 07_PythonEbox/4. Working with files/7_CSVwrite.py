def write_csv():
    # Take input for the number of persons
    n = int(input())
    
    # Open the file in write mode
    file_name = "salaryData.csv"
    with open(file_name, 'w') as file:
        for _ in range(n):
            # Take name and salary as input
            name = input().strip()
            salary = input().strip()
            
            # Write to the file in the format: name,salary
            file.write(f"{name},{salary}\n")
    
    # Read and print the file content
    with open(file_name, 'r') as file:
        print(file.read().strip())

# Call the function
write_csv()