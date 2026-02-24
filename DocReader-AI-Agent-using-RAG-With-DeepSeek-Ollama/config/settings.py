# ✅ Updated imports
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama


PDF_STORAGE_PATH = 'data/pdfs/'
PROMPT_TEMPLATE = """
You are an expert research assistant. Use the provided context to answer the query. 
If unsure, state that you don't know. Be concise and factual (max 3 sentences).

Query: {user_query} 
Context: {document_context} 
Answer:
"""

EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
LANGUAGE_MODEL = Ollama(model="deepseek-r1:1.5b")

