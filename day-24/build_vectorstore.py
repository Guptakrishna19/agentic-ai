import os
import shutil

from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


load_dotenv()

# -----------------------------
# 1. Load documents
# -----------------------------

loader = DirectoryLoader(
    "documents",
    glob="**/*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

print(f"Loaded {len(documents)} documents")


# -----------------------------
# 2. Split into chunks
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")


# Add chunk number to metadata
for i, chunk in enumerate(chunks):
    chunk.metadata["chunk_id"] = i + 1


# -----------------------------
# 3. Create embedding model
# -----------------------------

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# -----------------------------
# 4. Remove old vector database
# -----------------------------

if os.path.exists("./chroma_db"):
    shutil.rmtree("./chroma_db")


# -----------------------------
# 5. Create Chroma vector store
# -----------------------------

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Vector store created successfully!")