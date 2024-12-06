import pandas as pd

# Load the CSV file as a DataFrame
df = pd.read_csv('iris_with_header.csv')

# Print the original column names
print("Column Names")
print(df.columns)

# Rename the column 'species_type' to 'SpeciesType'
df.rename(columns={'species_type': 'SpeciesType'}, inplace=True)

# Print the column names after renaming
print("\nColumn Names after renaming")
print(df.columns)

# Print the entire contents of the DataFrame
print("\nDataFrame")
print(df)
