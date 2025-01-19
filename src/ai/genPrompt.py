from src.ai.getData.getRelevantInfo import getRevelantInfo
from src.ai.getData.getRecentHistory import retrieveRecentHistory

def genPrompt(query, embedded_query):
    relevant_info = getRevelantInfo(embedded_query)
    prompt = f"""
    RELEVANT SUMMARY/INFORMATION: '{relevant_info}'
    Last 20 chat messages: '{retrieveRecentHistory()}'
    New message: '{query}'
    """
    with open('debug_prompt.txt', 'w', encoding="utf-8") as f:
        f.write(prompt)
    return prompt