import pandas as pd

child = pd.read_csv('DHS-testing\childrecode.csv')
house = pd.read_csv('DHS-testing\householdrecode.csv')

# create set of column names for each dataframe
set1 = set(child.columns)
set2 = set(house.columns)

# find unique columns in each set
unique_cols_child = set1 - set2
unique_cols_household = set2 - set1

# print number of unique columns in each set
print("Number of columns in child dataframe:", len(set1))
print("Number of unique columns in child dataframe:", len(unique_cols_child))
print("Number of unique columns in household dataframe:", len(unique_cols_household))
