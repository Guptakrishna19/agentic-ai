from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
from tools import calculator, current_datetime

load_dotenv()
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

agent = create_agent(
    model=llm,
    tools=[
        calculator,
        current_datetime
    ]
)

while True:

    query = input("\nAsk: ")

    if query.lower() == "exit":
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    print("\nResponse:")

    print(
        response["messages"][-1].content
    )