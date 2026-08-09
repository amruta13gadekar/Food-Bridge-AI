import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("food_dataset.csv")

# Remove extra spaces
data["food_type"] = data["food_type"].str.strip()

# Encode food names
encoder = LabelEncoder()
data["food_encoded"] = encoder.fit_transform(data["food_type"])

# Input features
X = data[["food_encoded", "quantity_kg"]]

# Target
y = data["meals_served"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(encoder, "encoder.pkl")

print("Model trained successfully!")
print("Foods learned by model:")
print(list(encoder.classes_))