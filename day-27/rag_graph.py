from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma


load_dotenv()

# ======================================================
# Load LLM
# ======================================================

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

embeddings = OpenAIEmbeddings()


# ======================================================
# Load Documents
# ======================================================

loader = TextLoader("documents/company_handbook.txt")

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings
)

retriever = vectorstore.as_retriever()


# ======================================================
# Graph State
# ======================================================

class GraphState(TypedDict):
    question: str
    route: str
    documents: list
    answer: str


# ======================================================
# Node 1
# classify_question
# ======================================================

def classify_question(state):

    question = state["question"].lower()

    factual_keywords = [
    "langgraph",
    "langchain",
    "leave",
    "employee",
    "company",
    "working hours",
    "office",
    "aws",
    "cloud",
    "embedding",
    "vector",
    "database",
    "password",
    "budget",
    "performance review",
    "scrum",
    "sprint",
    "remote work",
    "handbook"
]
    if any(word in question for word in factual_keywords):
        print("\nRoute Selected : RAG\n")
        return "factual"

    print("\nRoute Selected : Direct LLM\n")
    return "chitchat"


# ======================================================
# Node 2
# retrieve_docs
# ======================================================

def retrieve_docs(state):

    docs = retriever.invoke(state["question"])

    print("Retrieved Documents\n")

    for i, doc in enumerate(docs, start=1):
        print(f"Document {i}")
        print(doc.page_content[:200])
        print("-" * 60)

    return {
        "documents": docs
    }


# ======================================================
# Node 3
# generate_answer
# ======================================================

def generate_answer(state):

    if state.get("documents"):

        context = "\n\n".join(
            [doc.page_content for doc in state["documents"]]
        )

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{state['question']}
"""

    else:

        prompt = state["question"]

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


# ======================================================
# Build Graph
# ======================================================

graph = StateGraph(GraphState)

graph.add_node(
    "retrieve_docs",
    retrieve_docs
)

graph.add_node(
    "generate_answer",
    generate_answer)


graph.set_conditional_entry_point(
    classify_question,
    {
        "factual": "retrieve_docs",
        "chitchat": "generate_answer"
    }
)

graph.add_edge(
    "retrieve_docs",
    "generate_answer"
)

graph.add_edge(
    "generate_answer",
    END
)

app = graph.compile()

# ======================================================
# Chat Loop
# ======================================================

trace = open(
    "graph-traces.md",
    "a",
    encoding="utf-8"
)

print("Type 'exit' to quit.\n")

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        break

    print("=" * 80)

    result = app.invoke(
        {
            "question": question
        }
    )

    answer = result["answer"]

    print("\nAssistant:\n")
    print(answer)

    # Determine execution path
    route = classify_question({"question": question})

    if route == "factual":
        path = """
START
↓
classify_question
↓
retrieve_docs
↓
generate_answer
↓
END
"""
    else:
        path = """
START
↓
classify_question
↓
generate_answer
↓
END
"""

    trace.write(f"## Question\n\n{question}\n\n")
    trace.write("Execution Path\n")
    trace.write(path)
    trace.write("\n")
    trace.write("Answer\n\n")
    trace.write(answer)
    trace.write("\n\n---\n")

trace.close()

print("\nConversation ended.")