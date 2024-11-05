from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

CHROMA_PATH = "db"
model = "llama3.2:latest"
model_url = "http://localhost:11434"

# Initialize embeddings and load the Chroma database
# Initialize Ollama embeddings
embeddings = OllamaEmbeddings(
    model=model,  # or the specific model you have
    base_url=model_url,  # default Ollama server URL
)
db_chroma = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)


def get_var(var_name, prompt, other_vars):
    question = other_vars["query"]
    k = other_vars.get("config", {}).get("topK", 5)
    docs_chroma = db_chroma.similarity_search_with_score(question, k=k)
    context_text = "\n\n".join([doc.page_content for doc, _score in docs_chroma])

    return {
        "output": context_text,
    }
