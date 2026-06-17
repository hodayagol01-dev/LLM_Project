# TODO: Assignment 06 - Multimedia Vibe Coding

This document outlines the remaining tasks for Assignment 06, following the initial documentation and planning phase.

## Phase 2: Scripting & Asset Prompting

*   [ ] **Refine `script/script.fountain`:** Review and finalize the Fountain script for the 60-second video, ensuring it aligns perfectly with the PRD and narrative flow.
*   [ ] **Generate `script/scenes.json`:** Create a detailed JSON representation of each scene, including elements, duration, transitions, and any specific visual/audio cues, derived directly from the Fountain script.
*   [ ] **Develop Music & Sound Prompts:** Craft precise prompts for an AI music/sound generator to create appropriate background music and sound effects (e.g., ocean waves, typing sounds, calm ambient music). Document these in `script/music_prompt.md`.
*   [ ] **Develop Visual Asset Prompts:** Create prompts for generating necessary visual assets (e.g., student character in different emotional states, a serene beach background, ShoreStep AI UI elements, assignment documents). *Note: This project will focus on programmatic generation or simple placeholders for visual assets within Remotion, rather than external image generation.*

## Phase 3: Remotion Code Generation

*   [ ] **Finalize `skills/remotion_video_skill.md`:** Ensure the skill file contains comprehensive and clear instructions for the AI coding agent to generate Remotion code.
*   [ ] **Prompt AI for Remotion Project Structure:** Use the AI agent (e.g., Gemini) to generate the basic Remotion project structure and core components (e.g., `src/Composition.tsx`, `src/Video.tsx`, utility files).
*   [ ] **Prompt AI for Scene-Specific Components:** For each scene defined in `script/scenes.json`, prompt the AI to generate corresponding Remotion components (e.g., `src/scenes/AnxietyScene.tsx`, `src/scenes/BeachScene.tsx`).
*   [ ] **Implement Transitions and Animations:** Guide the AI to create smooth transitions between scenes and dynamic animations for text, characters, and UI elements within each scene.
*   [ ] **Integrate Text and UI Elements:** Ensure all textual content from the script and simulated ShoreStep AI UI elements are correctly implemented and styled in Remotion components. *Address bilingual/RTL considerations if applicable.*
*   [ ] **Code Review and Refinement:** Manually review and refine the AI-generated Remotion code for quality, performance, and adherence to Remotion best practices.

## Phase 4: Integration, Rendering & Refinement

*   [ ] **Integrate Multimedia Assets:** Incorporate generated music, sound effects, and visual assets (even placeholders) into the Remotion project.
*   [ ] **Test Remotion Playback:** Run `npm start` (or equivalent) to preview the video locally and debug any playback, timing, or rendering issues.
*   [ ] **Render Final Video:** Use Remotion's rendering capabilities to generate the final `output/final-video.mp4`.
*   [ ] **Capture Screenshots:** Take clear screenshots of the Remotion project running locally (`npm start`) and save them to `assets/screenshots/`.
*   [ ] **Conduct QA:** Perform a thorough quality assurance check against `docs/QA_REPORT.md` and the assignment rubric.
*   [ ] **Update `docs/TOKEN_COST_REPORT.md`:** Populate with actual token usage and cost data from the code generation phase.
*   [ ] **Final `README.md` Update:** Add screenshots and any final project details to `README.md`.
*   [ ] **GitHub Submission:** Prepare the repository for submission, ensuring all required files are present and documentation is complete and accurate.
