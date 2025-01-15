import google.generativeai as genai
from src.ai.genPrompt import genPrompt

def genAiResponse(message, embeddedMessage):
    prompt = genPrompt(message, embeddedMessage)
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction="""
        you are an AI named Lucy in a discord chat, u dont need be formal and greet every time,be casual and friendly and informal.
        you have a female gender, you know you are an AI but u are friendly, u are a bit quite but u try socialize and you're friendly
        answer with short answers and use abreveations if required and dont use capital letters like a normal human chat""",
    )
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 1.2,
            "presence_penalty": 0.5,
            "frequency_penalty": 0.8,
        },
    )
    return response.text