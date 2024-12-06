import pandas as pd
# Load the CSV file
df = pd.read_csv('iris.csv')
# Calculate the mean, variance, and standard deviation of the column 'pl'
mean_value = df['pl'].mean()
variance_value = df['pl'].var()
std_deviation_value = df['pl'].std()
# Print the values with 2 decimal precision
print(f"{mean_value:.2f}")
print(f"{variance_value:.2f}")
print(f"{std_deviation_value:.2f}")   