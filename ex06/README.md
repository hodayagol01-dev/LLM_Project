# Assignment 06: Multimedia Vibe Coding with ShoreStep AI

## Project Overview

This GitHub project, "Assignment 06: Multimedia Vibe Coding with ShoreStep AI," demonstrates the power of AI agents in generating multimedia code and comprehensive documentation. The core concept revolves around **ShoreStep AI**, a fictional product designed to transform an overwhelming academic assignment into a calm, structured action plan for students. The project uses a 60-second Remotion video to tell this story.

## Project Concept: ShoreStep AI

Imagine a student feeling anxious in front of a complex academic assignment. Our video narrative unfolds as follows:
1.  **Anxiety:** The student is overwhelmed by the assignment's scope.
2.  **Escape & Calm:** She imagines herself at a serene beach, finding mental clarity and calm.
3.  **ShoreStep AI Introduction:** The student discovers ShoreStep AI, an innovative tool.
4.  **Structured Planning:** ShoreStep AI helps her break down the assignment into manageable components: a Product Requirements Document (PRD), a detailed Project Plan, a TODO list, specific AI prompts, structured JSON scenes, and a GitHub-ready workflow.
5.  **Clarity & Action:** The student regains control, feeling empowered and ready to tackle her assignment with a clear plan.

This project embodies the principle of **Vibe Coding**: transforming human intent and emotional states into structured AI prompts, generated code, and ultimately, a rendered multimedia output that reflects the initial "vibe."

## Core Course Requirements & Deliverables

This assignment adheres strictly to the following academic and technical requirements:

### Required Deliverables:

1.  **60-second Remotion Video:** A dynamically animated video showcasing the ShoreStep AI narrative. (Output: `output/final-video.mp4`)
2.  **Detailed README.md:** This document, serving as a comprehensive report of the assignment.
3.  **Markdown Planning Files:**
    *   `docs/PRD.md`: Product Requirements Document for ShoreStep AI.
    *   `docs/PLAN.md`: Detailed project plan.
    *   `docs/TODO.md`: Remaining tasks and action items.
4.  **Full Prompt Documentation:** `docs/PROMPTS.md` — documenting all prompts used for code and multimedia generation.
5.  **Token and Cost Awareness:** `docs/TOKEN_COST_REPORT.md` — detailing LLM usage, token estimates, and cost estimations.
6.  **QA and Rubric Mapping:** `docs/QA_REPORT.md` — outlining quality assurance checks and mapping to assignment rubric points.
7.  **Full Script:** `script/script.fountain` — the video script in Fountain format.
8.  **Structured Scenes JSON:** `script/scenes.json` — a machine-readable JSON file describing video scenes.
9.  **Music and Sound Prompt Documentation:** `script/music_prompt.md` — prompts for generating background music and sound effects.
10. **Skill/Instruction File for Coding Agent:** `skills/remotion_video_skill.md` — a specialized instruction set for AI to generate Remotion code.
11. **Remotion Codebase:** `src/` — the complete Remotion project files.
12. **Screenshots:** `assets/screenshots/` — visual proof of the project running.
13. **Final Video Output:** `output/final-video.mp4` — the rendered 60-second video.

### Important Course Requirements Highlighted:

*   **Detailed README:** This file serves as the primary report, summarizing all aspects of the project.
*   **Screenshots for Execution Proof:** `README.md` will include screenshots from `assets/screenshots/`.
*   **GitHub Folder Structure:** `PRD.md`, `PLAN.md`, and `TODO.md` are included under the `docs/` directory.
*   **Prompt Documentation:** All prompts used throughout the generation process are thoroughly documented in `docs/PROMPTS.md`.
*   **LLM Usage, Token & Cost Estimation:** The project details the specific LLM used (assumed to be Gemini for this project), provides estimates for token usage, and calculates approximate costs in `docs/TOKEN_COST_REPORT.md`.
*   **Prompt Injection Risks & Basic QA:** `docs/QA_REPORT.md` addresses prompt injection considerations and outlines basic quality assurance checks.
*   **Vibe Coding Demonstration:** The entire workflow, from initial human intent to AI-generated assets and final multimedia output, exemplifies the Vibe Coding methodology: **Human Intent → AI Prompts → Structured JSON/Script → Generated Code → Rendered Multimedia Output.**

## Bilingual Awareness (Hebrew/RTL)

While the primary language for documentation and code is English, the project acknowledges the potential for bilingual (e.g., Hebrew) and Right-to-Left (RTL) content in multimedia applications. Future enhancements or specific prompts could explore RTL layout considerations within Remotion components, ensuring the AI agent is capable of generating code that accommodates such requirements.

---

## Final Video

**Video title:** ShoreStep AI — From Assignment Anxiety to Clarity

The final rendered video is available at:

`output/final-video.mp4`

The video presents a 60-second multimedia Vibe Coding story about a student who feels overwhelmed by a complex academic assignment, imagines a calming beach environment, and uses ShoreStep AI to transform assignment chaos into a structured workflow.

## Execution Proof

The project was successfully previewed in Remotion Studio.

A screenshot proving local execution and preview is included at:

`assets/screenshots/remotion_studio_running.png`

## Run Instructions

Install dependencies:

```bash
npm install

```

Preview the Remotion project:

```bash
npm run start
```

Render the final video:

```bash
npm run build
```

The render command outputs the final video to:

`output/final-video.mp4`

## Technical Refinement Note

During development, direct local video playback caused browser media playback errors in Remotion Preview. To improve reliability, the project was adapted to use extracted still frames from the video assets with animated Ken Burns motion, gradient overlays, smooth transitions, and product UI cards. This preserved the cinematic concept while making the Remotion preview and final render stable.

## Submission Status

- PRD, PLAN, and TODO files are included under `docs/`.
- Prompt documentation is included in `docs/PROMPTS.md`.
- Token and cost awareness is included in `docs/TOKEN_COST_REPORT.md`.
- QA and rubric mapping are included in `docs/QA_REPORT.md`.
- The Remotion implementation is included under `src/`.
- Execution proof is included under `assets/screenshots/`.
- The final rendered video is included under `output/final-video.mp4`.
