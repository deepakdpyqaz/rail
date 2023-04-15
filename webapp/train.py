import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error
from sklearn.compose import ColumnTransformer


# Load data into a DataFrame
df = pd.read_csv("data.csv")
# Select relevant features for the model
features = ["distance", "type"]
X = df[features].copy()
y = df["duration"]
le = LabelEncoder()
X["type"] = le.fit_transform(X["type"].copy())
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
pipeline = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("model", RandomForestRegressor(n_estimators=100, random_state=42)),
    ]
)
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
mae = round(abs(y_pred - y_test).mean(), 2)
joblib.dump(pipeline, "trained_model.joblib")
joblib.dump(le, "label_encoder.joblib")
print(pipeline.score(X_test, y_test))
