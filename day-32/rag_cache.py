import sys
import time
from typing import TypedDict

import redis
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

# -----------------------------------
# Redis Connection
# -----------------------------------

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# -----------------------------------
# LLM
# -----------------------------------

llm = ChatOpenAI(model="gpt-5-mini")

# -----------------------------------
# Read Company Handbook
# -----------------------------------

with open("company_handbook.txt", "r", encoding="utf-8") as f:
    handbook = f.read()

# -----------------------------------
# Graph State
# -----------------------------------

class CompanyState(TypedDict):
    question: str
    answer: str

# -----------------------------------
# LangGraph Node
# -----------------------------------

def answer_question(state: CompanyState):

    question = state["question"].strip()

    cache_key = f"company:{question.lower()}"

    # Check Redis
    cached_answer = redis_client.get(cache_key)

    if cached_answer:
        print("=" * 50)
        print("✅ CACHE HIT")
        print(f"Key: {cache_key}")
        print(f"TTL: {redis_client.ttl(cache_key)} sec")
        print("=" * 50)

        return {"answer": cached_answer}

    print("=" * 50)
    print("❌ CACHE MISS")
    print("Calling GPT...")
    print("=" * 50)

    prompt = f"""
You are a helpful HR assistant.

Answer ONLY using the company handbook below.

If the answer is not present in the handbook,
reply exactly:

"I couldn't find that information in the company handbook."

------------------------
Company Handbook
------------------------

{handbook}

------------------------
Question
------------------------

{question}
"""

    response = llm.invoke(prompt)

    answer = response.content

    # Cache for 1 hour
    redis_client.set(
        cache_key,
        answer,
        ex=3600
    )

    print("\nStored in Redis")
    print(f"TTL: {redis_client.ttl(cache_key)} seconds\n")

    return {"answer": answer}

# -----------------------------------
# Build Graph
# -----------------------------------

graph = StateGraph(CompanyState)

graph.add_node("answer_question", answer_question)

graph.set_entry_point("answer_question")

graph.add_edge("answer_question", END)

app = graph.compile()

# -----------------------------------
# User Question
# -----------------------------------

question = input("Ask a question about the company handbook:\n> ")

# -----------------------------------
# Benchmark
# -----------------------------------

start = time.perf_counter()

result = app.invoke({"question": question})

end = time.perf_counter()

print("\nAnswer:\n")
print(result["answer"])

print("\nResponse Time:", round(end - start, 3), "seconds")