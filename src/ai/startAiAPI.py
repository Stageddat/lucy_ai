import google.generativeai as genai
import chromadb
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_AI_API")
genai.configure(api_key=GOOGLE_API_KEY)

chromaClient = chromadb.PersistentClient(path="./db/chroma_db")

lucyNoteDb = chromaClient.get_or_create_collection(name="lucyNote")
lucySummaryDb = chromaClient.get_or_create_collection(name="lucySummary")
lucyHighlightDb = chromaClient.get_or_create_collection(name="lucyHighlight")