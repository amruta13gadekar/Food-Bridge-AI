import pandas as pd

# Read dataset
data = pd.read_csv("food_dataset.csv")

print("Food Bridge Dataset")
print(data)

print("\nFirst 5 Rows")
print(data.head())

print("\nDataset Information")
print(data.info())