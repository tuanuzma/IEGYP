import pandas as pd

# Load the CSV file as a DataFrame
df = pd.read_csv('iris_with_header.csv')

# Print the original DataFrame
print("Original DataFrame")
print(df)

# Sort rows based on 'sepal_length' in ascending order
df_sorted = df.sort_values(by='sepal_length')

# Print the sorted DataFrame
print("\nSorted DataFrame")
print(df_sorted)
