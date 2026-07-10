from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain


load_dotenv()

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Memory
memory = ConversationBufferMemory()

# Conversation Chain
chatbot = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chatbot.predict(input=user_input)

    print("Bot:", response)