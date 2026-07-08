from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = "Give me a creative name for a futuristic coffee shop."

temperatures = [0.2, 0.7, 1.2]

for temp in temperatures:
    print(f"\n{'='*50}")
    print(f"Temperature: {temp}")
    print(f"{'='*50}")

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        temperature=temp
    )

    print(response.output_text)