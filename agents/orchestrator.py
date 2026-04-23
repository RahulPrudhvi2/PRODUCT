from crewai import Agent

class OrchestratorAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Orchestrator Agent",
            goal="Manage the workflow of the predictive maintenance system",
            backstory="I coordinate the activities of all agents.",
            verbose=True
        )