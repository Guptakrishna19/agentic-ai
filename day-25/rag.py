import os

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()


# Embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Vector store
vector_store = None


def index_document(text, filename):

    global vector_store

    # Split document into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.create_documents(
        [text],
        metadatas=[
            {
                "source": filename
            }
        ]
    )

    # Create/update vector store
    if vector_store is None:

        vector_store = FAISS.from_documents(
            chunks,
            embeddings
        )

    else:

        vector_store.add_documents(chunks)

    return len(chunks)


def ask_rag(question):

    if vector_store is None:

        return {
            "answer": "Please upload a document first.",
            "sources": []
        }

    # Retrieve relevant chunks
    docs = vector_store.similarity_search(
        question,
        k=3
    )

    # Combine retrieved context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # Create prompt
    prompt = f"""
You are a helpful RAG assistant.

Answer the question using ONLY the provided context.

If the answer cannot be found in the context,
say:

"I could not find this information in the uploaded documents."

Context:

{context}

Question:

{question}
"""

    # Ask LLM
    response = llm.invoke(prompt)

    # Extract sources
    sources = list(
        set(
            doc.metadata.get(
                "source",
                "Unknown"
            )
            for doc in docs
        )
    )

    return {
        "answer": response.content,
        "sources": sources
    }