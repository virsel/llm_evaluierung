import os
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.schema import Document

# Constants
CHROMA_PATH = "db_focus_qanda"
model = "llama3.2:latest"
model_url = "http://localhost:11434"
DATA_PATH = "data/GermanQuAD.csv"

# Initialize text splitter and embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
embeddings = OllamaEmbeddings(model=model, base_url=model_url)

# Check if the CSV file exists
if not os.path.exists(DATA_PATH):
    raise ValueError(f"The file {DATA_PATH} does not exist.")

print(f"Loading data from {DATA_PATH}...")

# Read the CSV file
df = pd.read_csv(DATA_PATH)

# Convert the context column into documents
documents = []
for i, row in df.iterrows():
    doc = Document(
        page_content=row['context'],
        metadata={'source': f'row_{i}'}  # You can add more metadata fields if needed
    )
    documents.append(doc)

print(f"Processing {len(documents)} documents...")

# Split the documents into chunks
chunks = text_splitter.split_documents(documents)

# Embed chunks and load them into the database
print("Embedding and saving chunks to Chroma database...")
db_chroma = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)
print(f"Embedding complete. Processed {len(chunks)} chunks.")