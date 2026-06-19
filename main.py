import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

# Example Agent Definition
search_agent = Agent(
    role='Medical Search Expert',
    goal='Retrieve authoritative medical research from PubMed',
    backstory='You are a veteran medical researcher specialized in finding high-impact clinical trials.',
    verbose=True,
    allow_delegation=False
)

# Example Task
research_task = Task(
    description='Find latest treatment approaches for Type 2 Diabetes.',
    expected_output='A summary of 3-5 major clinical findings with citations.',
    agent=search_agent
)

# Initialize Crew
medical_crew = Crew(
    agents=[search_agent],
    tasks=[research_task],
    verbose=True
)

if __name__ == "__main__":
    result = medical_crew.kickoff()
    print(result)
