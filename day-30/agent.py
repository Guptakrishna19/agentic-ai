import sys
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini")


class NewsState(TypedDict):
    topic: str
    summary: str


def summarize(state: NewsState):
    response = llm.invoke(
        f"Summarize the latest AI news about {state['topic']} in 5 bullet points."
    )
    return {"summary": response.content}


graph = StateGraph(NewsState)

graph.add_node("summarize", summarize)

graph.set_entry_point("summarize")
graph.add_edge("summarize", END)

app = graph.compile()

result = app.invoke({"topic": "Artificial Intelligence"})

print(result["summary"])