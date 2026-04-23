from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Crew
from tasks.tasks import create_tasks
from rag.rag import RAGSystem

app = FastAPI(title="PLM Predictive Maintenance API")

class SensorData(BaseModel):
    temperature: float
    vibration: float
    cycle: int

rag_system = RAGSystem()

@app.post("/predict")
def predict_maintenance(data: SensorData):
    # Retrieve context from RAG
    query = f"Sensor data: temp={data.temperature}, vib={data.vibration}, cycle={data.cycle}"
    context = rag_system.retrieve_context(query)

    # Create crew and tasks
    tasks = create_tasks(data.dict())
    crew = Crew(
        agents=[],  # Agents are in tasks
        tasks=tasks,
        verbose=True
    )

    # Run the crew
    result = crew.kickoff()

    return {
        "prediction": str(result),
        "context": context
    }