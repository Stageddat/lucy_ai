from src.ai.startAiAPI import lucySummaryDb

def getRevelantSummary(embedded_query):
    results = lucySummaryDb.query(query_embeddings=[embedded_query], n_results=5)
    relevantSummaries = ""
    for result in results["documents"][0]:
        relevantSummaries += result + "\n"
    return relevantSummaries