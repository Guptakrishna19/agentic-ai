from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------
# Tool
# -----------------------------------

search_tool = SerperDevTool()

# -----------------------------------
# Agents
# -----------------------------------

researcher = Agent(
    role="AI Research Specialist",
    goal="""
    Find the latest trends in Agentic AI using reliable online sources.
    Gather accurate and up-to-date information.
    """,
    backstory="""
    You are an experienced AI researcher with expertise in
    LLMs, AI Agents, LangChain, LangGraph, CrewAI,
    OpenAI Agents SDK, AutoGen and enterprise AI.
    You always verify facts before presenting them.
    """,
    tools=[search_tool],
    verbose=True
)

analyst = Agent(
    role="Technology Analyst",
    goal="""
    Analyze the research findings and identify
    important trends, opportunities, challenges,
    and future directions.
    """,
    backstory="""
    You are a senior technology analyst.
    Your job is to convert raw research into
    meaningful insights.
    """,
    verbose=True
)

writer = Agent(
    role="Technical Report Writer",
    goal="""
    Write a professional report in Markdown format.
    Make it clear, structured and easy to read.
    """,
    backstory="""
    You have written hundreds of industry reports.
    Your reports include headings, bullet points,
    summaries and conclusions.
    """,
    verbose=True
)

# -----------------------------------
# Tasks
# -----------------------------------

research_task = Task(
    description="""
    Research the latest trends in Agentic AI.

    Include:
    - Latest frameworks
    - New tools
    - Enterprise adoption
    - Real-world applications
    - Benefits
    - Challenges
    - Future outlook

    Use recent online information.
    """,
    expected_output="""
    Detailed research notes with reliable information.
    """,
    agent=researcher
)

analysis_task = Task(
    description="""
    Analyze the research.

    Identify:
    - Key trends
    - Emerging technologies
    - Opportunities
    - Challenges
    - Future predictions

    Produce insightful analysis.
    """,
    expected_output="""
    A detailed trend analysis.
    """,
    agent=analyst
)

writing_task = Task(
    description="""
    Create a professional Markdown report.

    Include:

    # Executive Summary

    # Latest Trends

    # Popular Frameworks

    # Enterprise Adoption

    # Challenges

    # Future Outlook

    # Conclusion

    Use proper Markdown headings and bullet points.
    """,
    expected_output="""
    A polished markdown report ready for publication.
    """,
    agent=writer
)

# -----------------------------------
# Crew
# -----------------------------------

crew = Crew(
    agents=[
        researcher,
        analyst,
        writer
    ],
    tasks=[
        research_task,
        analysis_task,
        writing_task
    ],
    process=Process.sequential,
    verbose=True
)

# -----------------------------------
# Run Crew
# -----------------------------------

print("\nStarting Research Crew...\n")

result = crew.kickoff()

print("\nFinal Report:\n")
print(result)

# -----------------------------------
# Save Report
# -----------------------------------

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
report_path = os.path.join(script_dir, "agentic_ai_report.md")

with open(report_path, "w", encoding="utf-8") as file:
    file.write(str(result))

print(f"\nReport saved as {report_path}")

# -----------------------------------
# Estimate API Usage
# -----------------------------------

estimated_llm_calls = 3
estimated_cost_per_call = 0.01  # Example only

estimated_cost = estimated_llm_calls * estimated_cost_per_call

print("\n----- API Usage Estimate -----")
print(f"Estimated LLM Calls : {estimated_llm_calls}")
print(f"Estimated Cost      : ${estimated_cost:.2f}")