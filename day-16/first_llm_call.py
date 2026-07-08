from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Initialize client
client = OpenAI(api_key=api_key)

# Send prompt
response = client.responses.create(
    model="gpt-4o-mini",
    input="Hello, explain what you do in 2 sentences."
)

# Print response
print("Response:")
print(response.output_text)