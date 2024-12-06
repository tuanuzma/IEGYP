import pandas as pd

# Reading the CSV file into a DataFrame
df = pd.read_csv('iris_duplicates.csv')

# Printing the entire contents of the DataFrame before removing duplicates
print("Original DataFrame")
print(df)

# Removing duplicate rows
df_no_duplicates = df.drop_duplicates()

# Printing the DataFrame after removing duplicates
print("\nDataFrame after removing duplicates")
print(df_no_duplicates)		
