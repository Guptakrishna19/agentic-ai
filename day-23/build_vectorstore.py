from dotenv import load_dotenv, find_dotenv

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
# pyrefly: ignore [missing-import]
from langchain_chroma import Chroma


# Load environment variables
load_dotenv(find_dotenv())


# -----------------------------------
# STEP 1: Load and chunk the document
# -----------------------------------

loader = DirectoryLoader("documents", glob="*.txt", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print("Total chunks:", len(chunks))


# -----------------------------------
# STEP 2: Generate embeddings
# -----------------------------------

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# print chunks before storing


print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Original Chunk {i} ---")
    print(chunk.page_content)
    
# -----------------------------------
# STEP 3: Store embeddings in Chroma
# -----------------------------------

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./chroma_db"
)

print("Embeddings stored successfully in Chroma!")


# -----------------------------------
# STEP 4: Similarity Search
# -----------------------------------

query = "What is the main topic?"

results = vector_store.similarity_search(
    query,
    k=3
)

print("\nTop 3 Matching Chunks:")

for i, doc in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content)