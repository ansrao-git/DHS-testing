import pandas as pd

# Load the dataset
data = pd.read_stata('https://github.com/ansrao-git/DHS-testing/raw/main/ETKR70FL.DTA')

# Create binary target variable for stunting
data['stunting'] = data['HAZ_score'] < -2
data['stunting'] = data['stunting'].astype(int)

# Create binary target variable for wasting
data['wasting'] = data['WHZ_score'] < -2
data['wasting'] = data['wasting'].astype(int)

# Create binary target variable for underweight
data['underweight'] = data['WAZ_score'] < -2
data['underweight'] = data['underweight'].astype(int)

# Print the first five rows of the dataset with the new target variables
print(data[['stunting', 'wasting', 'underweight']].head())
