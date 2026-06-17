# Assignment 05: Academic Research Assistant CrewAI

## Project Overview
The Academic Research Assistant is a multi-agent system built using CrewAI and Google's Gemini 2.5 Flash Lite. The system automates the generation of comprehensive academic research reports by orchestrating four specialized agents in a sequential workflow. From initial planning to final QA, the crew ensures that the research is well-structured, objectively summarized, critically analyzed, and professionally polished.

## How it satisfies Assignment 05
- **CrewAI Framework:** Utilizes `Agent`, `Task`, `Crew`, and `Process` classes.
- **Sequential Workflow:** Implements a strict 4-agent sequence where each agent builds on the previous one's output.
- **4 Specialized Agents:**
    - Research Planner
    - Academic Summary Writer
    - Critical Analyst
    - Submission Reviewer
- **Context Passing:** Uses the `context` parameter in tasks to ensure seamless information flow.
- **Gemini LLM:** Powered by `gemini/gemini-2.5-flash-lite` via `GOOGLE_API_KEY`.
- **Complete Documentation:** Includes PRD, PLAN, TODO, and detailed README.
- **Output & Logs:** Saves final results to `output/` and execution history to `logs/`.

## 4-Agent Architecture

| Agent | Role | Goal | Backstory |
| :--- | :--- | :--- | :--- |
| **Research Planner** | Research Planner | Define research question, scope, and structure. | Expert in academic methodology and research design. |
| **Academic Summary** | Academic Summary Writer | Synthesize the research plan into a cohesive summary. | Experienced writer expert in complex information synthesis. |
| **Critical Analyst** | Critical Analyst | Provide critical analysis and diverse perspectives. | Scholar known for rigorous critical thinking and evaluating tensions. |
| **Submission QA** | Submission Reviewer | Polish and format the final report for submission. | Senior journal editor ensuring clarity and academic rigor. |

## Context Flow Explanation
1.  **Task 1 (Plan):** Generates the roadmap for the research.
2.  **Task 2 (Summary):** Receives the Plan as context to ensure the summary covers all planned subtopics.
3.  **Task 3 (Analysis):** Receives the Summary as context to identify specific areas for critical evaluation.
4.  **Task 4 (QA):** Receives context from all previous tasks (Plan, Summary, Analysis) to compile, polish, and finalize the comprehensive report.

## Installation Instructions
1.  Clone the repository.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## .env Setup
Create a `.env` file in the root directory (refer to `.env.example`) and add your Google API key:
```env
GOOGLE_API_KEY=your-google-api-key-here
CREWAI_DISABLE_TELEMETRY=true
```

## Run Command
Run the system with a single command:
```bash
python src/main.py
```

## Output and Logs Explanation
- **Output:** The final polished academic report is saved to `output/academic_research_report.md`.
- **Logs:** A detailed log of each run, including the topic and the final result, is appended to `logs/run_log.md`.

## Proof of Run
*(Note: After running the script, you will see a structured Markdown report in the output folder. The verbose output in the terminal will show the step-by-step reasoning of each agent.)*

## Repository Structure
```
ex05/
├── .env.example
├── PRD.md
├── PLAN.md
├── TODO.md
├── README.md
├── requirements.txt
├── logs/
│   └── run_log.md
├── output/
│   └── academic_research_report.md
└── src/
    └── main.py
```

## Security Note
The `.env` file is used to manage sensitive API keys and should never be committed to the repository. The `.gitignore` file (if present) should include `.env`. This project uses environment variables exclusively to handle credentials.
