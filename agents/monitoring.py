from crewai import Agent
from tools.anomaly import AnomalyDetectionTool

class MonitoringAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Monitoring Agent",
            goal="Detect anomalies in sensor data",
            backstory="I monitor sensor readings to identify unusual patterns.",
            tools=[AnomalyDetectionTool()],
            verbose=True
        )