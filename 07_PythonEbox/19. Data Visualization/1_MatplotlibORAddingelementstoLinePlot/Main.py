import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv('Medals.csv')

# Generate the plot
plt.figure()

# Plot the line with specifications
plt.plot(df['Team'], df['Total'], linestyle='--', color='red', marker='o', markerfacecolor='black', linewidth=3, label='Team-wise Total Medal Data')

# Set the x-axis label
plt.xlabel('Team Name')

# Set the y-axis label
plt.ylabel('Total Number of Medals')

# Set the title of the plot
plt.title('Team-wise Total Medal Data')

# Add legend with the location specified
plt.legend(loc='lower right')

# Save the plot to a file
plt.savefig('plot2.png')

# Show the plot (optional, remove if running in a headless environment)
# plt.show()
