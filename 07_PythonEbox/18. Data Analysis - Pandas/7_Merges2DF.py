#Merge DataFrames, Change column order

import pandas as pd

df1 = pd.DataFrame([["Anitha",7.8,8.9], ["Baskar",5.6,6.9]], columns = ["student_name","sem1_cgpa", "sem2_cgpa"])
df2 = pd.DataFrame([["Anitha","CSE"], ["Baskar","IT"]], columns = ["student_name","department"])

# Printing the first DataFrame
print("DataFrame1")
print(df1)

# Printing the second DataFrame
print("\nDataFrame2")
print(df2)

# Merging the DataFrames
merged_df = pd.merge(df1, df2, on='student_name')

# Rearranging the columns
merged_df = merged_df[['student_name', 'department', 'sem1_cgpa', 'sem2_cgpa']]

# Printing the merged DataFrame
print("\nMerged DataFrame")
print(merged_df)