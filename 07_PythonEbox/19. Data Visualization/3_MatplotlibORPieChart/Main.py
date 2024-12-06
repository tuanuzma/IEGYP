import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv('Medals.csv')

# Calculate the total medals for Gold, Silver, and Bronze
total_gold = df['Gold'].sum()
total_silver = df['Silver'].sum()
total_bronze = df['Bronze'].sum()

# Create the pie chart
plt.figure()

# Data for the pie chart
medals = [total_gold, total_silver, total_bronze]
labels = ['Gold', 'Silver', 'Bronze']

# Create the pie chart
plt.pie(medals, labels=labels, autopct='%1.1f%%')

# Set the axis to be equal
plt.axis('equal')

# Add a title to the plot
plt.title('Medals data')

# Add legend at the specified location
plt.legend(loc='lower right')

# Save the plot to a file
plt.savefig('plot7.png')

# Show the plot (optional, remove if running in a headless environment)
# plt.show()
