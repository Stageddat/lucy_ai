import google.generativeai as genai

def generate_embedding(text):
    response = genai.embed_content(model="models/text-embedding-004", content=text)
    embedding = response["embedding"]
    return embedding
