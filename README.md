# LLM Course Project

This is the main README file for the LLM course.

Each assignment is organized in a separate folder in order to keep the projects clear, readable, and easy to evaluate.

---

## Repository Structure

```text
LLM_Project/
├── ex02/
├── ex03/
└── README.md
```

---

## Assignment 2 – Multi-Agent Translation Chain

Folder:

```text
ex02/
```

Assignment 2 implements a multi-agent translation chain.

The translation flow is:

```text
English → French → Hebrew → English
```

The project includes:

- Dedicated skill files for each translation step.
- An orchestrator script that manages the translation chain.
- Input and output text files.
- A semantic comparison report.
- Documentation explaining the workflow.

Main files:

```text
ex02/orchestrator_agent.py
ex02/source_english.txt
ex02/agent1_french_skill.md
ex02/agent2_hebrew_skill.md
ex02/agent3_english_skill.md
ex02/comparison_skill.md
ex02/comparison_report.txt
ex02/README.md
```

For details, see:

```text
ex02/README.md
```

---

## Assignment 3 – AI Meeting Scheduler Agent

Folder:

```text
ex03/
```

Assignment 3 implements an AI Meeting Scheduler Agent.

The project reads Gmail messages, identifies meeting requests, checks Google Calendar availability, creates calendar events when possible, and replies to the sender.

The project includes:

- MCP Server implementation.
- MCP Client Agent implementation.
- Gmail and Google Calendar integration.
- Prompt engineering and experiments documentation.
- Input/output examples and tested behavior documentation.

Main files:

```text
ex03/src/mcp_server.py
ex03/src/agent.py
ex03/main.py
ex03/requirements.txt
ex03/EXPERIMENTS.md
ex03/README.md
```

For details, see:

```text
ex03/README.md
```

---

---

## Assignment 04 – Agentic Academic PDF Generation

Folder:
```text
ex04/
```

Assignment 04 demonstrates the generation of a professional 31-page academic PDF using a sophisticated agentic architecture, LaTeX/LuaLaTeX, and a custom document class (`.cls`).

### Objectives
1. **Automation:** Implement an autonomous orchestration pipeline to generate high-quality academic documents.
2. **Reproducibility:** Ensure consistent document compilation using LaTeX/LuaLaTeX and a custom template.
3. **Quality Assurance:** Integrate automated structural, linguistic (BiDi), and bibliographic checks.

### Technology Stack
- **LaTeX/LuaLaTeX:** Used for advanced typesetting, superior layout control, and handling complex academic formatting.
- **Custom CLS Template:** Provides standardized structure, branding, and styling requirements.
- **Agentic Skills:** Reusable agent instructions (stored in `ex04/skills/`) that modularize writing, building, and validation tasks.

### Agentic Architecture
- **Orchestrator Agent:** Manages the overall lifecycle, from content planning to final compilation.
- **Content Writer Agent:** Generates academic text based on the PRD.
- **LaTeX Builder Agent:** Executes the transformation from markdown/source to LaTeX structures.
- **QA Structure Agent:** Validates document schema and section integrity.
- **QA BiDi Agent:** Ensures proper Bidirectional text rendering.
- **QA References Agent:** Verifies academic citation compliance.

### Documentation & Planning
All developmental stages are documented:
- `ex04/PRD.md`: Project Requirements Document.
- `ex04/PLAN.md`: Strategic execution plan.
- `ex04/TODO.md`: Task tracking and progress logs.

### Execution Instructions
**1. Run QA Validation:**
```bash
python3 ex04/src/qa_check.py
```

**2. Compile PDF:**
```bash
python3 ex04/src/compile_pdf.py
```

**3. Expected Output:**
- Generated PDF: `ex04/main.pdf`

### Improvements & Submission Quality
This submission addresses feedback from previous assignments by providing:
- **Stronger Documentation:** Comprehensive setup and architectural context.
- **Clear Setup Instructions:** Streamlined execution paths.
- **Automated Validation:** Dedicated `qa_check.py` for submission integrity.
- **Traceability:** Detailed logs in `ex04/logs/` and reproducible generation pipeline.

### Submission Checklist
- [x] `ex04/main.tex` (Source)
- [x] `ex04/custom-academic-template.cls` (Template)
- [x] `ex04/references.bib` (Bibliography)
- [x] `ex04/main.pdf` (Result)
- [x] `ex04/src/` (Scripts)
- [x] `ex04/skills/` (Reusable instructions)
- [x] `ex04/PRD.md`, `PLAN.md`, `TODO.md` (Planning)

---


## Notes

The assignments are separated into different folders so each submission can be reviewed independently.

- `ex02` contains the translation-chain assignment.
- `ex03` contains the meeting-scheduler assignment with MCP architecture.

Sensitive local files such as credentials, tokens, and environment files should not be committed to GitHub.