import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

def main():
    # 1. Load environment variables
    load_dotenv()
    
    google_api_key = os.getenv("GOOGLE_API_KEY")
    
    if not google_api_key:
        print("\n[ERROR] GOOGLE_API_KEY is missing in the .env file.")
        print("Please create a .env file with GOOGLE_API_KEY=your_key_here")
        sys.exit(1)
        
    # Set environment variables for CrewAI/LiteLLM
    os.environ["GOOGLE_API_KEY"] = google_api_key
    os.environ["GEMINI_API_KEY"] = google_api_key
    
    # 2. Configure LLM
    # Using Gemini 2.5 Flash Lite as requested
    llm = LLM(
        model="gemini/gemini-2.5-flash-lite",
        api_key=google_api_key,
        verbose=True
    )
    
    # 3. Get User Input
    print("--- Academic Research Assistant Crew ---")
    default_topic = "ADHD as a neurocognitive disorder versus social construction and overdiagnosis"
    user_input = input(f"Enter an academic research topic (default: {default_topic}): ").strip()
    
    topic = user_input if user_input else default_topic
    print(f"\nProcessing Topic: {topic}\n")
    
    # 4. Define Agents
    planner = Agent(
        role="Research Planner",
        goal="Define the research question, scope, subtopics, and report structure for the topic: {topic}",
        backstory="You are an expert in academic methodology and research design. You know how to break down complex topics into manageable and logical research structures.",
        llm=llm,
        tools=[],
        verbose=True,
        allow_delegation=False
    )
    
    summarizer = Agent(
        role="Academic Summary Writer",
        goal="Write a clear academic summary based on the research planner output for the topic: {topic}",
        backstory="You are an experienced academic writer with expertise in synthesizing complex information from research plans into cohesive summaries.",
        llm=llm,
        tools=[],
        verbose=True,
        allow_delegation=False
    )
    
    analyst = Agent(
        role="Critical Analyst",
        goal="Add critical analysis to the academic summary, including competing perspectives, limitations, risks, and tensions for the topic: {topic}",
        backstory="You are a scholar known for rigorous critical thinking. You excel at identifying gaps in research and evaluating diverse, often conflicting, viewpoints.",
        llm=llm,
        tools=[],
        verbose=True,
        allow_delegation=False
    )
    
    qa_reviewer = Agent(
        role="Submission Reviewer",
        goal="Review the full research report as a strict academic reviewer and produce a final polished Markdown report for the topic: {topic}",
        backstory="You are a senior editor for a prestigious academic journal. Your job is to ensure the final report meets the highest standards of clarity, structure, and academic rigor.",
        llm=llm,
        tools=[],
        verbose=True,
        allow_delegation=False
    )
    
    # 5. Define Tasks
    task_plan = Task(
        description=(
            "1. Analyze the topic: {topic}.\n"
            "2. Define a clear research question.\n"
            "3. Outline the scope and key subtopics.\n"
            "4. Provide a structured table of contents for the research report."
        ),
        expected_output="A comprehensive research plan including research question, scope, and structure.",
        agent=planner
    )
    
    task_summary = Task(
        description=(
            "Based on the research plan provided, write a 3-5 paragraph academic summary of the topic: {topic}.\n"
            "Ensure the summary is objective and follows the structure defined in the plan."
        ),
        expected_output="A well-structured academic summary of the research topic.",
        agent=summarizer,
        context=[task_plan]
    )
    
    task_analysis = Task(
        description=(
            "Review the academic summary and add a critical analysis section.\n"
            "Include competing perspectives (e.g., medical vs. social models), potential limitations of current research, and risks of overdiagnosis or underdiagnosis.\n"
            "Ensure the analysis is balanced and rigorous."
        ),
        expected_output="A critical analysis section that complements the academic summary.",
        agent=analyst,
        context=[task_summary]
    )
    
    task_qa = Task(
        description=(
            "Review the entire compiled report (Plan, Summary, and Analysis).\n"
            "1. Fix any stylistic inconsistencies.\n"
            "2. Ensure the tone is academic and formal.\n"
            "3. Format the final output as a clean, professional Markdown report.\n"
            "4. Add a conclusion that synthesizes the findings."
        ),
        expected_output="A final, polished academic research report in Markdown format.",
        agent=qa_reviewer,
        context=[task_plan, task_summary, task_analysis]
    )
    
    # 6. Create Crew
    crew = Crew(
        agents=[planner, summarizer, analyst, qa_reviewer],
        tasks=[task_plan, task_summary, task_analysis, task_qa],
        process=Process.sequential,
        verbose=True
    )
    
    # 7. Kickoff
    result = crew.kickoff(inputs={'topic': topic})
    
    # 8. Save Outputs
    os.makedirs("output", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    report_path = "output/academic_research_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(str(result))
        
    log_path = "logs/run_log.md"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n--- Run on {datetime.now()} ---\n")
        f.write(f"Topic: {topic}\n")
        f.write(f"Result:\n{str(result)}\n")
        
    print(f"\nFinal report saved to: {report_path}")
    print(f"Run log saved to: {log_path}")

if __name__ == "__main__":
    main()
