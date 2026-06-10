# Ex04: LaTeX Document Generation

This repository contains the skeleton for a LaTeX document generation project. The goal is to programmatically generate a technical document using LaTeX, including academic references and custom styling.

## Repository Structure

-   `assets/`: Contains static assets like graphs and images.
    -   `assets/graphs/`
    -   `assets/images/`
-   `skills/`: Contains skills for various tasks related to document generation and quality assurance.
    -   `skills/content_writer_skill.md`
    -   `skills/latex_builder_skill.md`
    -   `skills/orchestrator_skill.md`
    -   `skills/qa_bidi_skill.md`
    -   `skills/qa_references_skill.md`
    -   `skills/qa_structure_skill.md`
-   `src/`: Contains the core Python scripts for orchestrating the document generation and QA processes.
    -   `src/compile_pdf.py`: Script for compiling the LaTeX document.
    -   `src/orchestrator.py`: Main script to manage the document generation workflow.
    -   `src/qa_check.py`: Script for performing quality assurance checks on the generated document.
-   `main.tex`: The main LaTeX file that defines the document structure and content.
-   `custom-academic-template.cls`: A custom class file for LaTeX, defining the document's appearance.
-   `references.bib`: BibTeX file containing bibliographic references.
-   `PLAN.md`, `PRD.md`, `TODO.md`: Project planning and documentation files.
-   `logs/`: Directory for generated logs.
    -   `logs/generation_log.md`: Logs detailing the document creation process.
    -   `logs/qa_report.md`: Report summarizing the results of quality assurance checks.
-   `screenshots/`: Directory for screenshots related to the project.

## Setup Instructions

1.  **Install Dependencies:**
    Ensure you have Python 3.x installed. Install the project dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Install LuaLaTeX:**
    Compilation of the LaTeX document requires a local installation of LuaLaTeX. Please follow the instructions for your operating system to install TeX Live or MiKTeX, which includes LuaLaTeX.

## How to Run QA

Quality Assurance checks can be performed using the `qa_check.py` script:
```bash
python src/qa_check.py
```
This script will validate various aspects of the generated document.

## Compiling with LuaLaTeX

To compile the LaTeX document into a PDF, navigate to the `ex04` directory and run the compilation script:
```bash
python src/compile_pdf.py
```
**Note:** This command requires LuaLaTeX to be installed and accessible in your system's PATH.

## Expected Output

The compilation process is expected to produce a PDF file (e.g., `document.pdf`) in the root of the `ex04` directory. This PDF will be formatted according to `custom-academic-template.cls` and will incorporate references from `references.bib`.

## Current Limitations

-   **LuaLaTeX Dependency:** Local PDF compilation is strictly dependent on a pre-installed LuaLaTeX environment. Users without this setup will not be able to generate the PDF locally.

## Future Improvements

-   Integrate alternative PDF compilation methods or provide clearer error messages for compilation failures.
-   Expand QA checks to cover more aspects of document quality and correctness.
-   Develop content generation capabilities using the skills defined in the `skills/` directory.
