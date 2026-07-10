import sys
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Reconfigure stdout to use UTF-8 to prevent UnicodeEncodeError in Windows terminals
sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Chain 1: Summary Chain
summary_prompt = ChatPromptTemplate.from_template(
    """
    Generate exactly 3 concise bullet points about the following topic:
    Topic: {topic}
    """
)
parser = StrOutputParser()
summary_chain = summary_prompt | llm | parser

# Chain 2: Translation Chain
translate_prompt = ChatPromptTemplate.from_template(
    """
    Translate the following English text into Hindi. Do not include any prefix or labels in the translation output:
    {text}
    """
)
translate_chain = translate_prompt | llm | parser

print("--- Running Summary Chain ---")
topic = "Artificial Intelligence"
summary_result = summary_chain.invoke({"topic": topic})
print(f"Topic: {topic}")
print(summary_result)
print()

print("--- Running Translation Chain ---")
english_text = "I think you are fine"
translation_result = translate_chain.invoke({"text": english_text})
print(f"English: {english_text}")
print(f"Hindi Translation: {translation_result}")
