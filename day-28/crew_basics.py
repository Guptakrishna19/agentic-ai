from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# Agents
# -------------------------

researcher = Agent(
    role="Researcher",
    goal="Research the given topic thoroughly",
    backstory="You are an experienced researcher.",
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Write a high-quality article",
    backstory="You are a professional content writer.",
    verbose=True
)

editor = Agent(
    role="Editor",
    goal="Review and improve the article",
    backstory="You are a senior editor who ensures clarity, grammar, and accuracy.",
    verbose=True
)

# -------------------------
# Tasks
# -------------------------

research_task = Task(
    description="Research the benefits of renewable energy.",
    expected_output="Research notes.",
    agent=researcher
)

writing_task = Task(
    description="Write an article based on the research.",
    expected_output="Article on renewable energy.",
    agent=writer
)

editing_task = Task(
    description="Review the article, correct grammar, improve readability, and ensure factual accuracy.",
    expected_output="A polished and publication-ready article.",
    agent=editor
)

# -------------------------
# Crew
# -------------------------

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\nFinal Output:\n")
print(result)