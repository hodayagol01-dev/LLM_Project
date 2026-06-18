import React from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, interpolate, useVideoConfig } from "remotion";

// Represents the student, hunched and stressed
const Student: React.FC<{ frame: number }> = ({ frame }) => {
  const { fps } = useVideoConfig();

  // Simple animation for student posture - slight sway or slump
  const sway = interpolate(frame, [0, fps * 2], [0, 5], { extrapolateRight: "clamp" });

  return (
    <div
      style={{
        width: 200,
        height: 300,
        backgroundColor: "#a0a0a0", // Grey for a figure
        borderRadius: "10px",
        position: "absolute",
        bottom: 50,
        left: "35%",
        transform: `translateY(${sway}px) rotate(-5deg)`,
        // Simple representation of hunched posture
        clipPath: "polygon(10% 0%, 90% 0%, 100% 80%, 0% 80%)",
      }}
    >
      {/* Head */} <div style={{ width: 60, height: 60, backgroundColor: "#c0c0c0", borderRadius: "50%", position: "absolute", top: -30, left: "50%", transform: "translateX(-50%)" }}></div>
      {/* Body */} <div style={{ width: 180, height: 220, backgroundColor: "#a0a0a0", position: "absolute", bottom: 0, left: "50%", transform: "translateX(-50%)", borderRadius: "5px" }}></div>
    </div>
  );
};

// Represents the laptop screen with the assignment brief
const LaptopScreen: React.FC<{ frame: number }> = ({ frame }) => {
  const { fps } = useVideoConfig();

  // Fade in the screen content
  const opacity = interpolate(frame, [fps * 2, fps * 4], [0, 1], { extrapolateRight: "clamp" });

  return (
    <div
      style={{
        width: 400,
        height: 250,
        backgroundColor: "#222",
        borderRadius: "8px",
        position: "absolute",
        top: "20%",
        left: "50%",
        transform: "translateX(-50%) rotate(5deg)",
        boxShadow: "0 0 20px rgba(0,0,0,0.5)",
        opacity,
      }}
    >
      <div style={{ padding: 20, color: "#fff", fontSize: 24, fontFamily: "sans-serif" }}>
        <p><strong>Assignment Brief</strong></p>
        <p style={{ fontSize: 16, marginTop: 10 }}>Complex Academic Task Requirements:</p>
        <ul style={{ fontSize: 12, marginTop: 5, paddingLeft: 20 }}>
          <li>Analyze historical data trends...</li>
          <li>Develop a predictive model...</li>
          <li>Write a comprehensive report...</li>
        </ul>
      </div>
    </div>
  );
};

// Represents scattered papers and textbooks
const Clutter: React.FC<{ frame: number }> = ({ frame }) => {
  const { fps } = useVideoConfig();
  const frameOffset = fps * 0.5; // Offset for clutter elements

  // Simple animation for clutter to appear/settle
  const opacity = interpolate(frame, [frameOffset, frameOffset + fps * 2], [0, 1], { extrapolateRight: "clamp" });
  const scale = interpolate(frame, [frameOffset, frameOffset + fps * 2], [0.8, 1], { extrapolateRight: "clamp" });

  return (
    <>
      {/* Textbook 1 */}
      <div
        style={{
          width: 120,
          height: 180,
          backgroundColor: "#8B4513", // Brown
          borderRadius: "4px",
          position: "absolute",
          bottom: "10%",
          left: "15%",
          transform: `scale(${scale}) skewX(-10deg)`,
          opacity,
        }}
      ></div>
      {/* Papers 1 */}
      <div
        style={{
          width: 150,
          height: 100,
          backgroundColor: "#f0f0f0", // Off-white
          borderRadius: "2px",
          position: "absolute",
          bottom: "25%",
          left: "25%",
          transform: `scale(${scale}) rotate(15deg)`,
          opacity,
        }}
      ></div>
      {/* Textbook 2 */}
      <div
        style={{
          width: 100,
          height: 140,
          backgroundColor: "#D2B48C", // Tan
          borderRadius: "3px",
          position: "absolute",
          bottom: "15%",
          right: "20%",
          transform: `scale(${scale}) rotate(-20deg)`,
          opacity,
        }}
      ></div>
    </>
  );
};

export const AnxietyApartmentNightScene: React.FC = () => {
  const { fps } = useVideoConfig();
  const frame = useCurrentFrame();

  // Vibe Coding: Map data to visual elements and animations
  // Scene: anxiety_apartment_night
  // Time: 0-10 seconds (0 to 300 frames at 30 fps)
  // Visuals: Overwhelmed student, cluttered room, dim lighting.
  // Audio: Tense music, frantic typing, narrator V.O.

  // Overall scene opacity/transition - starts at 0, fades in to 1 over first 2 seconds
  const sceneOpacity = interpolate(frame, [0, fps * 2], [0, 1], { extrapolateRight: "clamp" });

  // Subtle blur effect to indicate stress/overwhelm
  const blur = interpolate(frame, [0, fps * 5], [0, 3], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ backgroundColor: "#1a1a2e", opacity: sceneOpacity }}>
      {/* Apply blur to the whole scene or specific elements if needed */}
      <div style={{ filter: `blur(${blur}px)`, width: "100%", height: "100%" }}>
        {/* Student Representation */}
        <Student frame={frame} />

        {/* Laptop Representation */}
        <LaptopScreen frame={frame} />

        {/* Clutter Representation */}
        <Clutter frame={frame} />
      </div>

      {/* Narrator V.O. - appears after initial setup */}
      <Sequence from={fps * 3} duration={fps * 7}> {/* Appears from frame 90 to 210 */}
        <div style={{ position: "absolute", top: "70%", left: "50%", transform: "translateX(-50%)", color: "#f0f0f0", fontSize: 36, fontFamily: "sans-serif", fontWeight: "bold", textAlign: "center", textShadow: "2px 2px 8px rgba(0,0,0,0.5)" }}>
          Feeling overwhelmed by a mountain of assignments?
        </div>
      </Sequence>
    </AbsoluteFill>
  );
};
