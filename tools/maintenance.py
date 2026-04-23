from crewai.tools import BaseTool

class MaintenanceSchedulingTool(BaseTool):
    name: str = "Maintenance Scheduling Tool"
    description: str = "Schedules maintenance based on predictions."

    def _run(self, anomaly_result: str, rul_result: str) -> str:
        if "Anomaly detected" in anomaly_result or "RUL" in rul_result and float(rul_result.split(": ")[1].split()[0]) < 100:
            return "Schedule maintenance immediately."
        else:
            return "No maintenance needed at this time."