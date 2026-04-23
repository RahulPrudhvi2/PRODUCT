import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

# Load data
data = pd.read_csv('../data/sample_data.csv')

# Features for anomaly detection
features_anomaly = ['temperature', 'vibration']
X_anomaly = data[features_anomaly]

# Train Isolation Forest
iso_forest = IsolationForest(contamination=0.1, random_state=42)
iso_forest.fit(X_anomaly)

# Save model
joblib.dump(iso_forest, 'models/anomaly_model.pkl')

# For RUL prediction, assume target is remaining cycles (simplified)
# In real scenario, RUL is calculated based on historical data
data['rul'] = 500 - data['cycle']  # Simplified RUL

features_rul = ['temperature', 'vibration', 'cycle']
X_rul = data[features_rul]
y_rul = data['rul']

X_train, X_test, y_train, y_test = train_test_split(X_rul, y_rul, test_size=0.2, random_state=42)

# Train Random Forest Regressor
rul_model = RandomForestRegressor(n_estimators=100, random_state=42)
rul_model.fit(X_train, y_train)

# Evaluate
y_pred = rul_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'RUL Model MSE: {mse}')

# Save model
joblib.dump(rul_model, 'models/rul_model.pkl')

print('Models trained and saved.')