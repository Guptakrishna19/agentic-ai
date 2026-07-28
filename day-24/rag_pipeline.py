import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


# -----------------------------
# 1. Load embedding model
# -----------------------------

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# -----------------------------
# 2. Load existing Chroma DB
# -----------------------------

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)


# -----------------------------
# 3. Create retriever
# -----------------------------

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


# -----------------------------
# 4. Create prompt
# -----------------------------

prompt = ChatPromptTemplate.from_template("""
You are a question-answering assistant.

Answer the question using only the provided context.

If the answer is not available in the context,
say "I don't know based on the provided documents."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
""")


# -----------------------------
# 5. Create LLM
# -----------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# -----------------------------
# 6. RAG function
# -----------------------------

def ask_question(question):

    # Retrieve relevant chunks
    docs = retriever.invoke(question)

    # Combine retrieved chunks into context
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # Create final prompt
    messages = prompt.invoke({
        "context": context,
        "question": question
    })

    # Ask LLM
    response = llm.invoke(messages)

    print("\nAnswer:")
    print(response.content)

    print("\nSources:")

    seen_sources = set()

    for doc in docs:

        source = os.path.basename(
            doc.metadata.get("source", "Unknown")
        )

        chunk_id = doc.metadata.get(
            "chunk_id",
            "Unknown"
        )

        citation = f"{source} - Chunk {chunk_id}"

        if citation not in seen_sources:
            print(f"- {citation}")
            seen_sources.add(citation)


# -----------------------------
# 7. Ask questions continuously
# -----------------------------

while True:

    question = input(
        "\nAsk a question (or type 'exit'): "
    )

    if question.lower() == "exit":
        break

    ask_question(question)