import numpy as np
import csv
def read_csv_to_numpy(file_name):
    # Open and read the CSV file
    with open(file_name, mode='r') as file:
        # Use the CSV reader to read the contents of the file
        reader = csv.reader(file)
        data_list = list(reader)  # Convert the reader object to a list of rows
    # Convert the list of rows to a NumPy array
    data_array = np.array(data_list)
    # Print the NumPy array
    print(data_array)
def main():
    # Define the file name (already available in the environment)
    file_name = 'sample_data.csv'
    # Read and print the CSV content as a NumPy array
    read_csv_to_numpy(file_name)
# Ensure that the main function is executed
if __name__ == "__main__":
    main()