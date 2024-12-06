from sklearn import datasets
# Load the iris dataset
iris = datasets.load_iris()
# Extract the data part
X = iris.data
# Print the top 3 rows of the data part
print(X[:3])   
