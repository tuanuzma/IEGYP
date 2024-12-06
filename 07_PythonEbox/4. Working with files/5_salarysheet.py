import csv
def read_and_print_salaries(filename):
    try:
        # Open the CSV file for reading
        with open(filename, mode='r', newline='') as csvfile:
            # Create a CSV reader object
            reader = csv.reader(csvfile)
            # Read each row from the CSV file
            for row in reader:
                # Join the elements of the row with a semicolon and print
                print(';'.join(row))
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Specify the input filename
input_filename = "SalariesDataSet.csv"
# Call the function to read and print salaries
read_and_print_salaries(input_filename)   