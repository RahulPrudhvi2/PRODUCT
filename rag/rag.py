import chromadb
from sentence_transformers import SentenceTransformer

class RAGSystem:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(name="engineering_knowledge")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def add_knowledge(self, documents):
        embeddings = self.model.encode(documents)
        ids = [f"doc_{i}" for i in range(len(documents))]
        self.collection.add(
            embeddings=embeddings.tolist(),
            documents=documents,
            ids=ids
        )

    def retrieve_context(self, query, n_results=3):
        query_embedding = self.model.encode([query])
        results = self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=n_results
        )
        return results['documents'][0] if results['documents'] else []

# Initialize and add some knowledge
rag = RAGSystem()
knowledge = [
    "High temperature above 90°C indicates potential overheating.",
    "Vibration levels above 5.0 suggest mechanical wear.",
    "Maintenance should be scheduled when RUL drops below 50 cycles.",
    "Anomaly detection helps identify unusual sensor readings."
]
rag.add_knowledge(knowledge)