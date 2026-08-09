import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Load the encoder
encoder = joblib.load("encoder.pkl")

# User input
food = input("Enter food type: ")
quantity = float(input("Enter quantity (kg): "))

# Convert food name into number
food_encoded = encoder.transform([food])[0]

# Predict meals
prediction = model.predict([[food_encoded, quantity]])

print(f"\nEstimated Meals: {int(prediction[0])}")