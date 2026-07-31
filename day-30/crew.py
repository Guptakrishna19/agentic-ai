import sys
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

news_agent = Agent(
    role="AI News Reporter",
    goal="Summarize the latest AI news",
    backstory="An experienced technology journalist.",
    verbose=True
)

task = Task(
    description="Summarize the latest AI news in 5 concise bullet points.",
    expected_output="A concise AI news summary.",
    agent=news_agent
)

crew = Crew(
    agents=[news_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()

print(result)