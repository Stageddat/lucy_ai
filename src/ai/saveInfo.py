from src.ai.startAiAPI import lucySummaryDb
from datetime import datetime
import random
import string
from src.ai.embedGenerator import generate_embedding


def save_summary(summary):
    actual_time = datetime.now()
    formatted_date = actual_time.strftime("%Y-%m-%d")
    formatted_time = actual_time.strftime("%H:%M:%S")
    hour_24 = actual_time.hour
    year = actual_time.year
    day = actual_time.day
    hour = actual_time.hour
    minute = actual_time.minute

    embedded_summary = generate_embedding(summary)

    lucySummaryDb.add(
        documents=[summary],
        embeddings=[embedded_summary],
        ids=["".join(random.choices(string.ascii_letters, k=20))],
        metadatas=[
            {
                "author": "Summary Bot",
                "date": formatted_date,
                "time": formatted_time,
                "hour_24": hour_24,
                "year": year,
                "day": day,
                "hour": hour,
                "minute": minute,
            }
        ],
    )
