import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style
sns.set(style="whitegrid", rc={"grid.color": ".5", "grid.linestyle": ":"})

# Load the car crashes dataset
car_crashes = sns.load_dataset('car_crashes', cache=True, data_home='/tmp')

# Generate scatter plot
sns.scatterplot(x="speeding", y="alcohol", data=car_crashes)

# Save the plot
plt.savefig('splot1.png')
