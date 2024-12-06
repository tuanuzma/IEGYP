import pandas as pd
# Load the CSV file and import only the 'sepal_length' and 'sepal_width' columns
df = pd.read_csv('iris_with_header.csv', usecols=['sepal_length', 'sepal_width'])
# Print the DataFrame with the specified columns
print(df)
