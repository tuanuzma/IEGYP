import pandas as pd
# Load the CSV file
df = pd.read_csv('cars.csv')
# Calculate the mean, variance, and standard deviation of the column 'cyl'
mean_value = df['cyl'].mean()
variance_value = df['cyl'].var()
std_deviation_value = df['cyl'].std()
# Print the values with 2 decimal precision
print(f"{mean_value:.2f}")
print(f"{variance_value:.2f}")
print(f"{std_deviation_value:.2f}")   