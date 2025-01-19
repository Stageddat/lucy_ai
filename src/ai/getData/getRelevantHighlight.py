from src.ai.startAiAPI import lucyHighlightDb

def getRelevantHighlight(embedded_query):
    results = lucyHighlightDb.query(query_embeddings=[embedded_query], n_results=5)
    relevantHighlights = ""
    for result in results["documents"][0]:
        relevantHighlights += result + "\n"
    return relevantHighlights