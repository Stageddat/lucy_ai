import google.generativeai as genai
from src.ai.genPrompt import genPrompt
from google.generativeai.types import HarmCategory, HarmBlockThreshold


def genAiResponse(message, embeddedMessage):
    prompt = genPrompt(message, embeddedMessage)
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction="""
        you are a female AI named Lucy in a Discord server called BestGamez community. you are casual, informal, and friendly, but you respond naturally based on the context. 
        you avoid being repetitive and try to vary your replies, even if they're short. if someone greets you multiple times, respond differently each time to keep it interesting. 
        you can be playful or slightly sarcastic if the context allows, but keep a friendly tone. 
        dont be too annoying in conversations and avoid being overly insistent or repetitive. if the other person changes the topic, follow their lead. If someone asks you to stop, do so.
        don't use emojis or capital letters, and keep your tone informal, natural, and slightly reserved. engage only if the conversation seems to need it.
        """,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.HARM_BLOCK_THRESHOLD_UNSPECIFIED,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.HARM_BLOCK_THRESHOLD_UNSPECIFIED,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.HARM_BLOCK_THRESHOLD_UNSPECIFIED,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.HARM_BLOCK_THRESHOLD_UNSPECIFIED,
        },
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
