from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END


# Load environment variables
load_dotenv()


# Create LLM
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# -------------------------
# NODE
# -------------------------

def chatbot(state: MessagesState):

    response = model.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# -------------------------
# BUILD GRAPH
# -------------------------

builder = StateGraph(MessagesState)


# Add node
builder.add_node(
    "chatbot",
    chatbot
)


# Add edges
builder.add_edge(
    START,
    "chatbot"
)

builder.add_edge(
    "chatbot",
    END
)


# Compile graph
graph = builder.compile()


# -------------------------
# RUN CHATBOT
# -------------------------

while True:

    user_input = input(
        "You: "
    )

    if user_input.lower() in [
        "exit",
        "quit"
    ]:
        break

    result = graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }
    )

    print(
        "AI:",
        result["messages"][-1].content
    )