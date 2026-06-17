# Prompt Documentation: Assignment 06 - Multimedia Vibe Coding

## 1. Introduction to Prompt Engineering for Vibe Coding

This document outlines the strategy and principles behind the prompts used in Assignment 06 to demonstrate "Vibe Coding." Vibe Coding involves translating high-level human intent, including emotional states and creative concepts, into structured AI inputs that generate code and multimedia outputs. The prompts are designed to be clear, specific, and iterative, allowing for refinement and alignment with the desired "vibe."

## 2. General Prompting Strategy

Our prompting strategy follows a hierarchical and iterative approach:

1.  **High-Level Vision to Structured Data:** Start with broad creative vision (e.g., student anxiety to calm beach) and use prompts to break it down into structured formats like scripts (Fountain) and scene data (JSON).
2.  **Structured Data to Code/Assets:** Use the generated structured data as context for subsequent prompts that generate specific code (Remotion components) or multimedia assets (music, sound effects).
3.  **Iterative Refinement:** Each generation step is followed by a review and refinement process, where prompts are adjusted based on the output to better match the original intent.

## 3. Categories of Prompts

The prompts used in this project fall into several key categories:

### 3.1. Documentation & Planning Prompts

*   **Purpose:** To generate the initial project documentation (README, PRD, PLAN, TODO) based on the assignment brief.
*   **Characteristics:** Focus on clarity, academic rigor, and adherence to specific markdown formats and content requirements.
*   **Example Context:** "Given the project concept of ShoreStep AI and the assignment deliverables, generate a detailed `README.md` that covers..."

### 3.2. Scripting Prompts (Fountain & JSON)

*   **Purpose:** To translate the core narrative into a screenplay format and then into a machine-readable scene structure.
*   **Characteristics:** Emphasize narrative flow, character actions, emotional beats, scene transitions, and strict adherence to Fountain syntax and JSON schema.
*   **Example Context:** "Based on the ShoreStep AI concept, write a 60-second video script in Fountain format, focusing on a student's journey from anxiety to calm. Ensure it includes scenes for..."
*   **Example Context (JSON):** "Given the following Fountain script, extract each scene and represent it as a JSON object with properties like `sceneId`, `durationSeconds`, `description`, `visualElements`, `audioElements`, and `dialogue`. Ensure logical transitions."

### 3.3. Multimedia Asset Prompts (Music & Sound)

*   **Purpose:** To generate prompts for external AI tools (not directly within this project's scope, but documented) that would create music and sound effects.
*   **Characteristics:** Focus on mood, tempo, instrumentation, emotional progression, and specific sound events. Avoid ambiguous terms.
*   **Example Context:** "Generate a prompt for an AI music composer for a 20-second track: 'Start with tense, slightly dissonant piano chords, transitioning to a calming, flowing synth pad with gentle ocean wave sounds after 10 seconds.'"

### 3.4. Remotion Code Generation Prompts

*   **Purpose:** To instruct the AI coding agent to produce functional Remotion components and animations.
*   **Characteristics:** Highly specific, include existing code context, reference the `skills/remotion_video_skill.md` for guidelines, adhere to TypeScript/React best practices, and specify desired animations, styling, and data integration.
*   **Example Context:** "Using the `remotion_video_skill.md` as guidance, generate a Remotion React component `AnxietyScene.tsx` that displays a student character looking stressed, with a rapidly blinking cursor animation. Integrate text from `script/scenes.json` for this scene."
*   **Bilingual/RTL Consideration:** Prompts for text rendering will include instructions for handling Hebrew/RTL content, such as `direction: 'rtl'`, `text-align: 'right'`, and appropriate font selections if necessary.

## 4. Prompt Injection Risks & Mitigation

Awareness of prompt injection is crucial. While this project focuses on generation rather than adversarial interaction, the principles apply:

*   **Clear Delimitation:** Using clear delimiters (e.g., triple backticks, XML tags) for user-provided or dynamic content within prompts helps the LLM distinguish instructions from data.
*   **Input Validation (Conceptual):** In a production ShoreStep AI, any user input intended for AI processing would undergo rigorous validation and sanitization to prevent malicious instructions from being interpreted as commands.
*   **Role-Based Instructions:** Explicitly defining the AI's role and expected output format in the system prompt reduces the likelihood of it deviating from the intended task.
*   **Monitoring and Review:** For code generation, human review of AI-generated code is a critical last line of defense against unexpected or harmful outputs, including those from subtle prompt injections.

## 5. LLM Used

The primary Large Language Model assumed for prompt generation and code synthesis in this project is **Gemini**.
