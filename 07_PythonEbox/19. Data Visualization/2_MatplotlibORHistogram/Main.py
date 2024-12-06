import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv('Medals.csv')

# Create the histogram for total medals
plt.figure()

# Generate the histogram for 'Total' column
plt.hist(df['Total'], bins=[10, 20, 30, 40], label='Total Medals Distribution')

# Set the x-axis label
plt.xlabel('Total Medals Range')

# Set the y-axis label
plt.ylabel('Count')

# Set the title of the plot
plt.title('Total Medals Histogram')

# Add legend with the location specified
plt.legend(loc='upper left')

# Save the plot to a file
plt.savefig('plot6.png')

# Show the plot (optional, remove if running in a headless environment)
# plt.show()
