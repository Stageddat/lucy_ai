from src.ai.getRelevantInfo import getRevelantInfo
from src.ai.getRecentHistory import retrieveRecentHistory

def genPrompt(query, embedded_query):
    relevant_info = getRevelantInfo(embedded_query)
    prompt = f"""
    RELEVANT SUMMARY/INFORMATION: '{relevant_info}'
    Last 20 chat messages: '{retrieveRecentHistory()}'
    New message: '{query}'
    """

    return prompt