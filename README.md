# PLM Agentic AI System (Predictive Maintenance)

A multi-agent AI system using CrewAI for predictive maintenance with sensor data, machine learning, and decision automation.

## Features

- **Multi-Agent System**: Monitoring, Analytics, Decision, and Orchestrator agents
- **Machine Learning**: Anomaly detection with Isolation Forest, RUL prediction with regression
- **RAG Memory**: ChromaDB for engineering knowledge storage and retrieval
- **FastAPI Backend**: REST API for predictions
- **Streamlit UI**: Interactive dashboard for predictions
- **Docker Support**: Containerized deployment

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the ML models:
   ```bash
   python ml/train.py
   ```
4. Run the backend:
   ```bash
   uvicorn backend.main:app --reload
   ```
5. Run the UI:
   ```bash
   streamlit run ui/app.py
   ```

## API Usage

POST /predict with JSON:
```json
{
  "temperature": 85,
  "vibration": 4.5,
  "cycle": 500
}
```

## Docker

Build and run:
```bash
docker-compose up --build
```

## Project Structure

- `backend/`: FastAPI application
- `agents/`: CrewAI agents
- `tasks/`: Task definitions
- `tools/`: Custom tools
- `ml/`: Machine learning models and training
- `rag/`: Vector database setup
- `ui/`: Streamlit dashboard
- `data/`: Sample datasets