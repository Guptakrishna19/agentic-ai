
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
You are a helpful AI assistant.

Follow the user's instructions carefully and provide accurate responses.
"""

def call_llm(user_prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.output_text


while True:
    print("\n=== Prompt Engineering Lab ===")
    print("1. Custom Prompt Testing")
    print("2. Few-Shot Sentiment Analysis")
    print("3. JSON Extraction")
    print("4. Exit")

    choice = input("\nSelect option: ")

    if choice == "1":
        print("\nEnter your prompt:")
        user_prompt = input("> ")

        output = call_llm(user_prompt)

        print("\n===== RESPONSE =====")
        print(output)

    elif choice == "2":
        few_shot_prompt = """
Classify the sentiment as Positive, Negative, or Neutral.

Example 1:
Text: This phone has excellent battery life and great performance.
Sentiment: Positive

Example 2:
Text: The service was slow and the staff were rude.
Sentiment: Negative

Now classify:

Text:
"""

        text = input("\nEnter text to classify:\n> ")

        output = call_llm(few_shot_prompt + text)

        print("\n===== RESPONSE =====")
        print(output)

    elif choice == "3":
        text = input("\nEnter text for JSON extraction:\n> ")

        extraction_prompt = f"""
Extract the following information and return ONLY valid JSON.

Schema:
{{
    "name": "",
    "email": "",
    "phone": "",
    "company": ""
}}

Text:
{text}
"""

        output = call_llm(extraction_prompt)

        print("\n===== RESPONSE =====")
        print(output)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")