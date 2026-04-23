import joblib
import numpy as np
from crewai.tools import BaseTool

class AnomalyDetectionTool(BaseTool):
    name: str = "Anomaly Detection Tool"
    description: str = "Detects anomalies in sensor data using Isolation Forest."

    def _run(self, temperature: float, vibration: float) -> str:
        model = joblib.load('../ml/models/anomaly_model.pkl')
        features = np.array([[temperature, vibration]])
        prediction = model.predict(features)
        if prediction[0] == -1:
            return "Anomaly detected: Potential issue with sensor readings."
        else:
            return "No anomaly detected."