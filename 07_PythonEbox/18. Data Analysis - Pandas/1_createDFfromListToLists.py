import pandas as pd

# List of lists (with species types)
data = [
    [5.1, 3.5, 1.4, 0.2, 'IrisSentosa'],
    [4.9, 3.0, 1.4, 0.2, 'IrisSentosa'],
    [4.9, 3.0, 1.4, 0.2, 'IrisVersicolor'],
    [6.4, 3.2, 4.5, 1.5, 'IrisVersicolor'],
    [6.3, 3.3, 6.0, 2.5, 'IrisVirginica'],
    [5.8, 2.7, 5.1, 1.9, 'IrisVirginica']
]

# Column names
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_type']

# Creating the DataFrame
df = pd.DataFrame(data, columns=columns)

# Printing the DataFrame
print(df)
