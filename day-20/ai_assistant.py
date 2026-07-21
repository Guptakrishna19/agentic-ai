from tools import *
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
from langchain.agents import create_agent



# Load environment variables
load_dotenv()


# Create LLM
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Available tools
tools = [
    calculator,
    current_datetime
]


# Create agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
    You are a helpful CLI AI assistant.

    Use the calculator tool for mathematical calculations.
    Use the current_datetime tool for providing the current date and time in proper format.

    Answer other general questions normally.
    """
)


# Store conversation history
history = []


print("=" * 50)
print("         LangChain CLI AI Assistant")
print("=" * 50)

print("\nType 'exit' to stop the assistant.\n")


while True:
    print("Assistant: How can I help you today?\n")

    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("\nAssistant: Goodbye!")
        break

    if user_input.lower() == "help":
        print("""
                You can perform the following operations:
                1. Mathematical calculations
                2. Get the current date and time
                3. Ask general questions
                """)
        continue

    if not user_input:
        continue

    # Add user message
    history.append({
        "role": "user",
        "content": user_input
    })

    # Keep only last 5 messages
    history = history[-5:]

    try:

        # Send conversation to agent
        result = agent.invoke({
            "messages": history
        })

        # Get final assistant response
        answer = result["messages"][-1].content

        print(f"\nAssistant: {answer}\n")

        # Add assistant response to history
        history.append({
            "role": "assistant",
            "content": answer
        })

        # Again keep only last 5 messages
        history = history[-6:]

    except Exception as e:
        print(f"\nError: {e}\n")