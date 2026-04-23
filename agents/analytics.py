from crewai import Agent
from tools.rul import RULPredictionTool

class AnalyticsAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Analytics Agent",
            goal="Predict Remaining Useful Life (RUL)",
            backstory="I analyze data to predict equipment failure.",
            tools=[RULPredictionTool()],
            verbose=True
        )