import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load data
df = pd.read_csv("your_data.csv", parse_dates=["arrival"])

# Preprocess data
df = df[["arrival", "number"]]
df = df.set_index("arrival")
df = df.resample("D").sum()
df = df.fillna(method="ffill")

# Split data
train_size = int(len(df) * 0.8)
train_data = df[:train_size]
test_data = df[train_size:]

# Train ARIMA model
model = ARIMA(train_data, order=(1, 0, 1))
model_fit = model.fit()

# Make predictions
predictions = model_fit.forecast(steps=len(test_data))

# Evaluate model
mae = np.mean(np.abs(predictions - test_data))
mse = np.mean(np.square(predictions - test_data))
rmse = np.sqrt(mse)

# Plot results
plt.plot(train_data, label="Training Data")
plt.plot(test_data, label="Testing Data")
plt.plot(predictions, label="Predictions")
plt.legend()
plt.show()
