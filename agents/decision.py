from crewai import Agent
from tools.maintenance import MaintenanceSchedulingTool

class DecisionAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Decision Agent",
            goal="Schedule maintenance based on predictions",
            backstory="I make decisions on maintenance scheduling.",
            tools=[MaintenanceSchedulingTool()],
            verbose=True
        )