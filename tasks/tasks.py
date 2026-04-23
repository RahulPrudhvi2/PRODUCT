from crewai import Task
from agents.monitoring import MonitoringAgent
from agents.analytics import AnalyticsAgent
from agents.decision import DecisionAgent
from agents.orchestrator import OrchestratorAgent

monitoring_agent = MonitoringAgent()
analytics_agent = AnalyticsAgent()
decision_agent = DecisionAgent()
orchestrator_agent = OrchestratorAgent()

def create_tasks(sensor_data):
    temperature = sensor_data['temperature']
    vibration = sensor_data['vibration']
    cycle = sensor_data['cycle']

    monitor_task = Task(
        description=f"Monitor sensor data: temperature={temperature}, vibration={vibration}",
        agent=monitoring_agent,
        expected_output="Anomaly detection result"
    )

    analytics_task = Task(
        description=f"Predict RUL for cycle={cycle}, temperature={temperature}, vibration={vibration}",
        agent=analytics_agent,
        expected_output="RUL prediction result"
    )

    decision_task = Task(
        description="Schedule maintenance based on monitoring and analytics results",
        agent=decision_agent,
        expected_output="Maintenance decision",
        context=[monitor_task, analytics_task]
    )

    return [monitor_task, analytics_task, decision_task]