import pandas as pd

# Load the CSV file as a DataFrame
df = pd.read_csv('iris_with_header.csv')

# Display the entire contents of the DataFrame
print("Dataframe")
print(df)

# Display the shape of the DataFrame
print("Shape")
print(df.shape)

# Display the data types of the different columns in the DataFrame
print("Data Types")
print(df.dtypes)

# Display the number of columns under each data type in the DataFrame
print("Column Count under each dtype")
print(df.groupby(df.dtypes, axis=1).size())

# Display the Summary Statistics of the DataFrame
print("Summary Statistics")
print(df.describe())
