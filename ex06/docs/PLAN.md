# Project Plan: Assignment 06 - Multimedia Vibe Coding

## 1. Project Phases & Deliverables

This project will be executed in a series of phases, each culminating in specific deliverables.

### Phase 1: Documentation & Planning (Current Phase)

**Goal:** Establish a comprehensive foundation of project documentation and planning before any code generation.

*   **Deliverables:**
    *   `README.md`: Project overview, concept, deliverables, and course requirements.
    *   `docs/PRD.md`: Product Requirements Document for ShoreStep AI.
    *   `docs/PLAN.md`: This project plan.
    *   `docs/TODO.md`: Initial list of remaining tasks.
    *   `docs/PROMPTS.md`: Documentation for all prompts.
    *   `docs/TOKEN_COST_REPORT.md`: LLM usage, token, and cost estimates.
    *   `docs/QA_REPORT.md`: QA and rubric mapping.
    *   `script/script.fountain`: Video script in Fountain format.
    *   `script/scenes.json`: Structured JSON for video scenes.
    *   `script/music_prompt.md`: Music and sound prompt documentation.
    *   `skills/remotion_video_skill.md`: Instructions for the Remotion coding agent.

### Phase 2: Scripting & Asset Prompting

**Goal:** Translate the PRD and project concept into a detailed video script and define prompts for multimedia assets.

*   **Tasks:**
    *   Refine `script/script.fountain` based on PRD.
    *   Generate `script/scenes.json` from the script, detailing each scene's elements and timing.
    *   Develop detailed prompts for music and sound effects, documented in `script/music_prompt.md`.
    *   Develop prompts for visual assets (e.g., beach background, UI elements for ShoreStep AI, student character states).

### Phase 3: Remotion Code Generation

**Goal:** Utilize AI agents to generate the Remotion video codebase based on the script, scene JSON, and skill instructions.

*   **Tasks:**
    *   Develop the `skills/remotion_video_skill.md` to guide the AI agent.
    *   Prompt the AI agent (e.g., using Gemini) to generate the Remotion project structure and components under `src/`.
    *   Iteratively refine prompts and generated code to match script and scene requirements.
    *   Ensure all visual and textual elements (including potential Hebrew/RTL content) are correctly rendered.

### Phase 4: Integration, Rendering & Refinement

**Goal:** Assemble all generated components, render the final video, and perform quality assurance.

*   **Tasks:**
    *   Integrate generated Remotion components with multimedia assets.
    *   Run Remotion previews and debug any issues.
    *   Render the final 60-second video (`output/final-video.mp4`).
    *   Capture screenshots of the running Remotion project (`assets/screenshots/`).
    *   Perform final QA based on `docs/QA_REPORT.md`.
    *   Review `docs/TOKEN_COST_REPORT.md` and update with actuals if possible.

## 2. Technology Stack

*   **AI Agent:** Gemini (assumed)
*   **Video Framework:** Remotion (React, TypeScript)
*   **Scripting:** Fountain Syntax
*   **Data Structuring:** JSON
*   **Documentation:** Markdown

## 3. Vibe Coding Methodology Integration

Each phase will emphasize the Vibe Coding workflow:

*   **Human Intent:** The initial concept of the overwhelmed student and the calming beach is the core human intent.
*   **AI Prompts:** This intent is translated into detailed prompts for script, scenes, assets, and code generation.
*   **Structured JSON/Script:** AI generates structured data (Fountain script, JSON scenes) that encapsulate the narrative.
*   **Generated Code:** AI uses the structured data and skill instructions to produce the Remotion codebase.
*   **Rendered Multimedia Output:** The final video visually and audibly represents the initial human intent and emotional journey.

## 4. Timeline (High-Level Estimation)

*   **Phase 1: Documentation & Planning:** 2-3 days
*   **Phase 2: Scripting & Asset Prompting:** 1-2 days
*   **Phase 3: Remotion Code Generation:** 3-5 days
*   **Phase 4: Integration, Rendering & Refinement:** 2-3 days

*Note: This timeline is an estimate and may adjust based on iterative AI interaction and refinement.*