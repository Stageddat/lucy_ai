from src.ai.startAiAPI import lucyNoteDb

def getRevelantNotes(embedded_query):
    results = lucyNoteDb.query(query_embeddings=[embedded_query], n_results=10)
    relevantNotes = ""
    for result in results["documents"][0]:
        relevantNotes += result + "\n"
    return relevantNotes