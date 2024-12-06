import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv('Medals.csv')

# Create the scatter plot
plt.figure()

# Scatter plot with Rank on X-axis and Rank_by_Total on Y-axis
plt.scatter(df['Rank'], df['Rank_by_Total'], label='Rank Comparison')

# Set the xlabel, ylabel, title, and legend
plt.xlabel('Rank')
plt.ylabel('Rank_by_Total')
plt.title('Rank Comparison')
plt.legend(loc='upper left')

# Save the figure as 'plot4.png'
plt.savefig('plot4.png')

# Optionally display the plot (remove if running in a non-GUI environment)
# plt.show()
