import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tips = sns.load_dataset('tips', cache=True, data_home='/tmp')

# Generate the bar plot based on 'total_bill' and 'day'
sns.set(style="whitegrid")
sns.barplot(x="day", y="total_bill", data=tips, palette="PuRd", ci=None)

# Save the plot
plt.savefig('splot3.png')
