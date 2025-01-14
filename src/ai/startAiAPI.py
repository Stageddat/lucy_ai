import google.generativeai as genai
import chromadb
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_AI_API")
genai.configure(api_key="GOOGLE_API_KEY")

chroma_client = chromadb.PersistentClient(path="./chroma_db")

summary_db = chroma_client.get_or_create_collection(name="lucy")