import joblib
import numpy as np
from crewai.tools import BaseTool

class RULPredictionTool(BaseTool):
    name: str = "RUL Prediction Tool"
    description: str = "Predicts Remaining Useful Life (RUL) using regression model."

    def _run(self, temperature: float, vibration: float, cycle: int) -> str:
        model = joblib.load('../ml/models/rul_model.pkl')
        features = np.array([[temperature, vibration, cycle]])
        rul = model.predict(features)[0]
        return f"Predicted RUL: {rul:.2f} cycles."