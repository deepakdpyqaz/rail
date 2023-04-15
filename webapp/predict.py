import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

# Load data into a DataFrame
# df = pd.read_csv('data.csv')

# Select relevant features for the model
# features = ['distance', 'type']

# Encode categorical variables using one-hot encoding
# X = pd.get_dummies(df[features])

# Scale the data
# scaler = StandardScaler()
# scaler.fit(X)
# X_scaled = scaler.transform(X)

# y = df['duration']

# # Split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# # Train a random forest regression model
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = model.predict(X_test)

# # Display the mean absolute error of the model
# mae = round(abs(y_pred - y_test).mean(), 2)

# # Save the trained model to a file
# joblib.dump(model, 'trained_model.joblib')

# Load the trained model from file
model = joblib.load("trained_model.joblib")
le = joblib.load("label_encoder.joblib")


# Make predictions on a new dataset
def predict_duration(distance, train_type):
    # st.write('Mean absolute error:', mae)
    # Encode categorical variables using one-hot encoding
    train_data = pd.DataFrame({"distance": [distance], "type": [train_type]})
    train_data["type"] = le.transform(train_data["type"].copy())
    # Scale the input data
    # train_data_scaled = scaler.transform(train_data_encoded)
    # Make a prediction using the trained model
    duration = model.predict(train_data)[0]

    return duration
