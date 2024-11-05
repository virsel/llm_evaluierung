import os
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

model = "qwen2.5:3b"
model_url = "http://localhost:11434"

def call_api(prompt, options, context):
    # Initialize Llama model via Ollama
    chat = ChatOllama(
        model=model,
        base_url=model_url,
        temperature=0
    )
    message = HumanMessage(content=prompt)
    response = chat([message])
    
    # Evaluate response
    
    return {
        "output": response.content,
    }