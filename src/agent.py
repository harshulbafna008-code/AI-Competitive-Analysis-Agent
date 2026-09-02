import os
from crewai import LLM, Agent, Task, Crew, Process
from src.tools import web_search_tool

def get_llm():
    return LLM(
        model="gemini/gemini-flash-lite-latest",
        api_key=os.environ["GEMINI_API_KEY"]
    )

def build_crew(company_name: str):
    llm = get_llm()

    researcher = Agent(
        role="Market Researcher",
        goal="Find accurate, up-to-date information about a company and its competitors",
        backstory="You are a meticulous researcher who gathers real data from the web, never guessing or making up facts.",
        tools=[web_search_tool],
        llm=llm,
        verbose=True
    )

    analyst = Agent(
        role="Competitive Analyst",
        goal="Synthesize research into a clear, structured competitive analysis report",
        backstory="You are a sharp business analyst who turns raw research into SWOT-style insights for decision makers.",
        llm=llm,
        verbose=True
    )

    research_task = Task(
        description=f"""Research the company '{company_name}'. Find information on:
        - What they offer (products/services)
        - Their pricing
        - Recent news or updates
        - Main competitors
        Use the web search tool to find real, current data.""",
        expected_output="A detailed set of research notes with sources",
        agent=researcher
    )

    analysis_task = Task(
        description=f"""Using the research notes, write a structured competitive analysis of '{company_name}' with:
        1. Overview
        2. Key Products/Services
        3. Pricing Strategy
        4. Strengths
        5. Weaknesses
        6. Market Positioning
        7. Top 2-3 Competitors and how they compare""",
        expected_output="A well-formatted competitive analysis report in markdown",
        agent=analyst,
        context=[research_task]
    )

    return Crew(
        agents=[researcher, analyst],
        tasks=[research_task, analysis_task],
        process=Process.sequential,
        verbose=True
    )
def run_analysis(company_name: str) -> str:
    crew = build_crew(company_name)
    result = crew.kickoff()
    return str(result)