import pandas as pd
import joblib

model = joblib.load("models/sales_forecast_model.pkl")

new_data = pd.read_csv("data/processed_sales.csv")

predictions = model.predict(new_data)

new_data["Forecast"] = predictions

new_data.to_csv("outputs/predictions.csv", index=False)

print("Predictions generated successfully.")
