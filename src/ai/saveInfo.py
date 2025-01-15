from src.ai.startAiAPI import lucy_db
from datetime import datetime
import random
import string
from src.ai.embedGenerator import generate_embedding

def save_summary(summary):
    actual_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    embedded_summary = generate_embedding(summary)
    lucy_db.add(
        documents=[summary],
        embeddings=[embedded_summary],
        ids=[str(''.join(random.choices(string.ascii_letters, k=20)))],
        metadatas=[{"author": "summary", "date": actual_time}],
    )