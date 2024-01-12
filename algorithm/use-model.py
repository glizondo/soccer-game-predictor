import joblib

model = joblib.load('liga_model.pkl')

result = [
    "Granada",  # Size in Square Feet
    "Malaga"  # Number of Bedrooms
]

results = [
    result
]

result_values = model.predict(results)

predicted_value = result_values[0]

print("Results details:")
print(f"- {result_values[1]} team")
print(f"- {result_values[2]} away team")
print(f"Estimated value: ${predicted_value}")