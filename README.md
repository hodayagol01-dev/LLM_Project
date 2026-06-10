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

### Assignment 04: Agentic PDF Generation

This assignment focuses on agentic PDF generation using LaTeX, LuaLaTeX, a custom CLS template, Skills, and QA orchestration.

The `ex04` directory includes the following components:
- `PRD.md`
- `PLAN.md`
- `TODO.md`
- `README.md`
- `main.tex`
- `custom-academic-template.cls`
- `references.bib`
- `skills/`
- `src/`
- `logs/`
- `assets/`
- `screenshots/`

Key functionalities include:
- `qa_check.py`: Validates the presence of required files and folders for the assignment.
- `compile_pdf.py`: Prepares and compiles the PDF using LuaLaTeX.

**Note:** Local compilation currently requires LuaLaTeX to be installed on the machine.

This project builds upon previous feedback by incorporating clearer setup instructions, comprehensive QA logs, and detailed documentation.

---


## Notes

The assignments are separated into different folders so each submission can be reviewed independently.

- `ex02` contains the translation-chain assignment.
- `ex03` contains the meeting-scheduler assignment with MCP architecture.

Sensitive local files such as credentials, tokens, and environment files should not be committed to GitHub.