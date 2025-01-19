import google.generativeai as genai

def genSummary():
    with open("db/messageLog.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) < 20:
        return None

    conversation_snippet = "".join(lines[-20:]).strip()

    print("Generating summary...")
    prompt = f"Summarize the following conversation in a clear and concise paragraph.:\n\n{conversation_snippet}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    parsed_response = response.text.strip()
    print(f"Summary generated:\n{parsed_response}")
    return parsed_response