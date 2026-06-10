# PRD — Assignment 04: Agentic PDF Generation with LaTeX

## 1. Product Overview

This project implements an agentic workflow for generating a professional academic PDF document using LaTeX, LuaLaTeX, and a custom CLS template.

The goal is to demonstrate how AI agents can generate, structure, validate, and compile a long-form PDF document in a repeatable and reproducible way.

## 2. Assignment Context

Assignment 04 focuses on the creation of a PDF document through a text-based workflow. The project is based on the concepts discussed in Lecture 07, including:

- LaTeX as a reliable document generation language
- LuaLaTeX for Hebrew, English, Unicode, and BiDi support
- CLS templates for reusable document styling
- Skills as reusable natural-language instructions for agents
- QA agents for checking structure, formatting, references, and compilation
- Agent orchestration for managing multi-step document generation

## 3. Main Objective

Build a documented GitHub project that includes:

- A LaTeX-based PDF generation workflow
- A custom CLS file
- A structured academic document
- Agent Skills for content generation and QA
- A reproducible compilation process
- Markdown planning files: PRD, PLAN, and TODO
- A detailed README report

## 4. Target Users

The target users are:

- Students in the LLM course
- Course instructors evaluating agentic workflows
- Developers learning how to use AI agents for document generation
- Teams that need repeatable academic or technical PDF generation

## 5. Functional Requirements

The system should:

1. Generate a structured academic PDF document.
2. Use LaTeX source files.
3. Compile the PDF using LuaLaTeX.
4. Use a custom CLS template for styling and consistency.
5. Include a table of contents.
6. Include chapters or sections.
7. Include references in IEEE-style format.
8. Include text, summaries, graphs, and images.
9. Include QA checks for document structure and compilation readiness.
10. Document the agent workflow through Skills and logs.

## 6. Non-Functional Requirements

The project should be:

- Reproducible
- Clearly documented
- Easy to run from the terminal
- Organized in a professional GitHub structure
- Extensible for future assignments
- Transparent about limitations and assumptions

## 7. Agent Roles

The project includes the following planned agents:

### 7.1 Orchestrator Agent
Coordinates the entire workflow and delegates tasks to specialized agents.

### 7.2 Content Writer Agent
Generates the academic content for the PDF document.

### 7.3 LaTeX Builder Agent
Transforms structured content into LaTeX code.

### 7.4 CLS Template Agent
Maintains consistent formatting through a reusable CLS file.

### 7.5 QA Structure Agent
Checks the document structure, required files, table of contents, and section organization.

### 7.6 QA BiDi Agent
Checks Hebrew-English directionality and mixed-language formatting.

### 7.7 QA References Agent
Checks the bibliography and citation consistency.

## 8. Expected Deliverables

The final submission should include:

- README.md in the repository root
- ex04/README.md
- ex04/PRD.md
- ex04/PLAN.md
- ex04/TODO.md
- main.tex
- custom CLS file
- references.bib
- final PDF output
- Skills folder
- Source code folder
- QA logs
- Screenshots as evidence

## 9. Success Criteria

The project is considered successful if:

- The repository is organized and understandable.
- The required Markdown files exist.
- The LaTeX source files exist.
- The PDF can be compiled using LuaLaTeX.
- The README explains setup, execution, output, and QA.
- The project demonstrates an agentic workflow rather than only a static document.
- The QA process addresses the feedback received in previous assignments.

## 10. Limitations

This project may use a simplified local workflow instead of a fully autonomous production-grade agent system. However, the repository will clearly document the agent roles, Skills, QA process, and reproducible workflow.
