from ai.getData.getRelevantNotes import getRevelantNotes
from ai.getData.getRelevantSummary import getRevelantSummary
from ai.getData.getRelevantHighlight import getRelevantHighlight
from src.ai.getData.getRecentHistory import retrieveRecentHistory

def genPrompt(query, embedded_query):
    relevantSummaries = getRevelantSummary(embedded_query)
    relevantNotes = getRevelantNotes(embedded_query)
    relevantHighlight = getRelevantHighlight(embedded_query)

    prompt = f"""
    RELEVANT HIGHLIGHTS: '{relevantHighlight}'
    RELEVANT NOTES: '{relevantNotes}'
    RELEVANT OLD CHAT SUMMARIES: '{relevantSummaries}'
    notes are extra data to help in certain contexts, summaries are summaries of old chat messages and highlights are useful information extracted from the chat
    use notes, summaries and highlight if required, you can also search more if required
    Last 20 chat messages history: '{retrieveRecentHistory()}'
    New message: '{query}'
    """

    with open('debug_prompt.txt', 'w', encoding="utf-8") as f:
        f.write(prompt)

    return prompt