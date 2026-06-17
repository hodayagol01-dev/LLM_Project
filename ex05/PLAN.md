# Development Plan - Academic Research Assistant

## Step-by-Step Development Plan
1.  **Environment Setup:**
    *   Create `.env.example` and `requirements.txt`.
    *   Initialize project structure (`src/`, `output/`, `logs/`).
2.  **Documentation:**
    *   Draft PRD, PLAN, TODO, and README.
3.  **Agent & Task Definition:**
    *   Define Research Planner Agent and its task.
    *   Define Academic Summary Agent and its task.
    *   Define Critical Analysis Agent and its task.
    *   Define Submission QA Agent and its task.
4.  **Core Implementation:**
    *   Implement `src/main.py` with CrewAI and Gemini LLM.
    *   Set up sequential process and context passing.
    *   Implement input handling and file saving logic.
5.  **Testing & Validation:**
    *   Run the script with the default topic.
    *   Verify output files and logs.
    *   Check for error handling (e.g., missing API key).
6.  **Final Polish:**
    *   Update TODO list.
    *   Finalize README with run proof.

## Architecture
The system follows a sequential multi-agent architecture using the CrewAI framework.
*   **LLM:** Google Gemini 2.5 Flash Lite.
*   **Workflow:** Sequential (Task 1 -> Task 2 -> Task 3 -> Task 4).
*   **Context:** Each subsequent task receives the output of previous tasks as context.

## Agent Pipeline
1.  **Research Planner:** Input topic -> Research Structure.
2.  **Academic Summary:** Research Structure -> Literature Review/Summary.
3.  **Critical Analysis:** Summary -> Analysis of Tensions/Risks.
4.  **Submission QA:** Full Content -> Polished Academic Report.

## Testing Plan
*   **Unit Test:** Ensure each agent initializes correctly with the Gemini LLM.
*   **Integration Test:** Run the full crew with the "ADHD" topic and verify `output/academic_research_report.md` exists and is coherent.
*   **Environment Test:** Delete the API key from `.env` and verify the script stops with a clear error message.

## Submission Readiness Checklist
- [x] Sequential workflow with 4 agents.
- [x] Agents have role, goal, backstory, tools, verbose=True.
- [x] Tasks have expected outputs and context.
- [x] Gemini 2.5 Flash Lite used via CrewAI LLM.
- [x] .env handling with `python-dotenv`.
- [x] Output saved to `output/` and logs to `logs/`.
- [x] README, PRD, PLAN, TODO completed.
