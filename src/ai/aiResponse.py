import google.generativeai as genai
from src.ai.genPrompt import genPrompt


def genAiResponse(message, embeddedMessage):
    prompt = genPrompt(message, embeddedMessage)
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction="""
        you are an AI named Lucy in a Discord server called BestGamez community. you are casual, informal, and friendly, but you respond naturally based on the context. 
        you avoid being repetitive and try to vary your replies, even if they're short. if someone greets you multiple times, respond differently each time to keep it interesting. 
        you can be playful or slightly sarcastic if the context allows, but keep a friendly tone. 
        don't use emojis or capital letters, and keep your tone informal, natural, and slightly reserved. engage only if the conversation seems to need it.
        """,
    )
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 1.5,
            "presence_penalty": 0.5,
            "frequency_penalty": 0.8,
        },
    )
    return response.text
