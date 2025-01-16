from src.ai.startAiAPI import lucy_db
from datetime import datetime
import random
import string
from src.ai.embedGenerator import generate_embedding


def save_summary(summary):
    actual_time = datetime.now()
    formatted_date = actual_time.strftime("%Y-%m-%d")
    formatted_time = actual_time.strftime("%H:%M:%S")
    hour_24 = actual_time.hour
    embedded_summary = generate_embedding(summary)

    lucy_db.add(
        documents=[summary],
        embeddings=[embedded_summary],
        ids=["".join(random.choices(string.ascii_letters, k=20))],
        metadatas=[
            {
                "author": "summary",
                "date": formatted_date,
                "time": formatted_time,
                "hour_24": hour_24,
            }
        ],
    )
