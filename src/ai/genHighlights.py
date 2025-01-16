from datetime import datetime
import google.generativeai as genai

# REMINDER ADD USING JSON RESPONSE SHIT BRO :V
def genHighlights():
    with open("db/messageLog.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) < 20:
        return None

    conversation_snippet = "".join(lines[-20:]).strip()

    print("Generating highlights...")
    prompt = f"""
    Analyze the following conversation and extract the most important points in a concise bullet list:
    {conversation_snippet}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    highlights = response.text.strip().split("\n")
    print(f"Highlights generated:\n{highlights}")
    return highlights

genHighlights()