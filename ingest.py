import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Constants
CHROMA_PATH = "db"
model = "llama3.2:latest"
model_url = "http://localhost:11434"
dir_docs = "docs"

# Initialize text splitter and embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
embeddings = OllamaEmbeddings(model=model, base_url=model_url)
all_chunks = []

# Ensure the document directory exists
if not os.path.isdir(dir_docs):
    raise ValueError(f"The directory {dir_docs} does not exist.")

# Process each PDF file in the directory
for pdf_file in os.listdir(dir_docs):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(dir_docs, pdf_file)
        print(f"Ingesting {pdf_file} from {pdf_path}...")

        # Load PDF document from the local file
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()

        # Split the document into chunks
        chunks = text_splitter.split_documents(pages)
        all_chunks.extend(chunks)

# Embed all chunks and load them into the database
print("Embedding and saving chunks to Chroma database...")
db_chroma = Chroma.from_documents(all_chunks, embeddings, persist_directory=CHROMA_PATH)
print("Embedding complete.")