from src.ai.startAiAPI import lucy_db

def getRevelantInfo(embedded_query):
    results = lucy_db.query(query_embeddings=[embedded_query], n_results=10)
    relevant_summary = ""
    for result in results["documents"][0]:
        relevant_summary += result + "\n"
    return relevant_summary