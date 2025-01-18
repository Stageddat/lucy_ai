import google.generativeai as genai
import typing_extensions as typing
import json

# import os

# GOOGLE_API_KEY = os.getenv("GOOGLE_AI_API")
# genai.configure(api_key=GOOGLE_API_KEY)


class highlightType(typing.TypedDict):
    highlights: list[str]


def gen_highlights():
    try:
        with open("db/messageLog.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        if len(lines) < 20:
            print(
                "no enough conversation for highlights"
            )
            return None

        conversation_snippet = "".join(lines[-20:]).strip()

        print("Generating highlights...")
        prompt = f"""
        Analyze the following conversation and extract the most important points in a concise sentence for each. For each point, include the participants, what was discussed, any relevant context, and if a decision or question was raised. Keep each point to a single sentence.

        Conversation snippet:
        {conversation_snippet}
        """

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=list[highlightType],
            ),
        )
        raw_response = response.text
        print(raw_response)
        data = json.loads(raw_response)

        if data and len(data) > 0 and "highlights" in data[0]:
            highlights = data[0]["highlights"]
            print("Highlights:")
            for point in highlights:
                print(f"- {point}")
            return highlights
        else:
            print("no highlights found")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


gen_highlights()
