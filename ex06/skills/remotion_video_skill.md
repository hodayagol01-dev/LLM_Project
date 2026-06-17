# Remotion Video Skill: Instructions for AI Coding Agent

## 1. Skill Overview

This skill provides a comprehensive set of instructions and best practices for an AI coding agent to generate Remotion video code. The goal is to enable the agent to translate a detailed script (`script/script.fountain`) and structured scene data (`script/scenes.json`) into a functional, visually appealing, and well-structured Remotion project. The agent should prioritize modularity, animation quality, and adherence to Remotion/React/TypeScript conventions.

## 2. Core Directives for Remotion Code Generation

### 2.1. Project Structure

*   **Root Components:** Create `src/Composition.tsx` as the main composition file and `src/Video.tsx` to define the overall video structure (duration, FPS, width, height).
*   **Scene Components:** Each distinct scene in `script/scenes.json` (e.g., `anxiety_apartment_night`, `serene_beach_day`) must correspond to its own React component file (e.g., `src/scenes/AnxietyScene.tsx`, `src/scenes/BeachScene.tsx`).
*   **Shared Components:** Create a `src/components/` directory for reusable UI elements (e.g., `TextReveal.tsx`, `FadeTransition.tsx`, `ShoreStepLogo.tsx`).
*   **Utilities:** Create a `src/utils/` directory for helper functions (e.g., timing calculations, animation helpers).
*   **Styling:** Use inline styles or CSS modules within Remotion components for maximum control. Avoid global stylesheets unless explicitly required.

### 2.2. Data Integration

*   **Scene Data as Prop:** Each scene component (`src/scenes/*.tsx`) should accept its corresponding data from `script/scenes.json` as a prop. This allows for data-driven video generation.
*   **Text Integration:** Dynamically render text content (dialogue, on-screen text) from the `scenes.json` data. Avoid hardcoding text directly into components.
*   **Asset Paths:** When integrating visual (placeholders) or audio assets, ensure paths are relative and correct within the Remotion project structure (e.g., `assets/images/`, `assets/audio/`).

### 2.3. Animations & Transitions

*   **Remotion Primitives:** Utilize Remotion's built-in animation primitives (e.g., `interpolate`, `spring`, `Sequence`, `AbsoluteFill`, `Still`) for smooth and performant animations.
*   **Keyframing:** Animate elements (position, opacity, scale, rotation, blur) based on frame numbers derived from `startTimeSeconds` and `durationSeconds` in `scenes.json`.
*   **Scene Transitions:** Implement smooth transitions between scenes. Common patterns include cross-fades, slides, or custom animated wipes. The `Sequence` component should be used to manage scene timings.
*   **Text Animations:** Employ engaging text reveal animations (e.g., typewriter effect, character-by-character fade-in, word-by-word slide-up) for dialogue and on-screen text.

### 2.4. Styling & Visuals

*   **Consistency:** Maintain a consistent visual style throughout the video, aligning with the "anxiety" and "calm" vibes.
    *   **Anxiety Vibe:** Use darker, muted colors, slightly frantic animations, subtle blurs, and potentially a more angular aesthetic.
    *   **Calm Vibe:** Use brighter, softer colors, smooth, flowing animations, gentle gradients, and an open, spacious aesthetic (e.g., beach scene).
*   **Responsiveness:** Design components to adapt to varying video resolutions (though 1920x1080 is standard for this project, consider scalable elements).
*   **Placeholders:** For visual assets (student character, ShoreStep AI UI), create programmatic placeholders (e.g., `div` elements with colors/gradients, simple SVG shapes) or use readily available royalty-free icons until actual assets are integrated.

### 2.5. Accessibility & Internationalization

*   **Bilingual/RTL Support:** If `scenes.json` contains Hebrew or other RTL content, the agent *must* implement appropriate CSS properties (e.g., `direction: 'rtl'`, `text-align: 'right'`) within the Remotion text components to ensure correct rendering. Consider using fonts that support Hebrew characters.

## 3. Best Practices & Quality Assurance

*   **Modularity:** Break down complex scenes or animations into smaller, manageable components.
*   **Readability:** Generate clean, well-commented, and easily understandable TypeScript/React code.
*   **Performance:** Optimize animations for smooth playback (e.g., prefer `transform` properties over `left`/`top` for movement).
*   **Error Handling:** Implement basic error boundaries or checks where appropriate (e.g., for missing data props).
*   **Testing:** While direct unit testing of Remotion components by AI is complex, the agent should structure code in a way that *facilitates* manual visual testing and review during the integration phase.

## 4. Example Code Snippets (Illustrative)

### 4.1. Basic Remotion Component Structure

'''typescript
import React from 'react';
import { AbsoluteFill, Sequence, useCurrentFrame, useVideoConfig } from 'remotion';

interface MySceneProps {
  title: string;
  durationInFrames: number;
}

export const MyScene: React.FC<MySceneProps> = ({ title, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Example: Simple text fade-in animation
  const opacity = Math.min(1, frame / (fps * 1)); // Fades in over 1 second

  return (
    <AbsoluteFill style={{ backgroundColor: '#f0f8ff' }}>
      <h1 style={{ opacity, textAlign: 'center', fontSize: 80, color: '#333' }}>
        {title}
      </h1>
    </AbsoluteFill>
  );
};
'''

### 4.2. Handling RTL Text (Example)

'''typescript
import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';

interface RtlTextSceneProps {
  text: string;
}

export const RtlTextScene: React.FC<RtlTextSceneProps> = ({ text }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 30], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', backgroundColor: '#fff' }}>
      <p style={{
        fontFamily: 'Arial, sans-serif',
        fontSize: 60,
        color: '#000',
        direction: 'rtl', // Key for RTL
        textAlign: 'right', // Key for RTL
        paddingRight: 50, // Adjust as needed
        opacity,
      }}>
        {text}
      </p>
    </AbsoluteFill>
  );
};
'''

## 5. Iterative Development Flow

The AI agent should follow an iterative process:
1.  **Generate Core Structure:** Start with `Video.tsx` and `Composition.tsx`.
2.  **Generate Scene Components:** Create empty or basic scene components based on `scenes.json`.
3.  **Implement Content & Styling:** Populate scene components with text, basic visuals, and styling.
4.  **Add Animations:** Implement animations and transitions for each scene.
5.  **Integrate Audio:** Add audio sequences and synchronize with visuals.
6.  **Refine:** Review outputs, identify discrepancies with script/JSON, and refine code through targeted prompts.

By adhering to these instructions, the AI coding agent will effectively generate the Remotion video project for Assignment 06.