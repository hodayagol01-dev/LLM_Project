import React from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, interpolate, useVideoConfig } from "remotion";

export const AnxietyEyesClosedTransitionScene: React.FC = () => {
  const { fps } = useVideoConfig();
  const frame = useCurrentFrame();

  // Vibe Coding: Map data to visual elements and animations
  // Scene: anxiety_eyes_closed_transition
  // Time: 10-20 seconds (300 to 600 frames at 30 fps)
  // Visuals: Student closes eyes, room blurs, warps, shifts to warm glow.
  // Audio: Music softens, narrator V.O.

  // Transition from dark/stressful background to a warm, soft glow
  const backgroundColor = interpolate(
    frame,
    [0, fps * 10], // Over 10 seconds (entire scene duration)
    ["#1a1a2e", "#FFCBA4"], // From dark anxiety to warm glow
    { extrapolateRight: "clamp" }
  );

  // Increase blur as the student closes eyes and transitions
  const blur = interpolate(
    frame,
    [0, fps * 5, fps * 10],
    [0, 5, 0], // Blur in, then fade out as scene transitions out
    { extrapolateRight: "clamp" }
  );

  // Slight warp/scale effect to indicate change
  const scale = interpolate(
    frame,
    [0, fps * 5, fps * 10],
    [1, 1.05, 1], // Zoom in slightly then back out
    { extrapolateRight: "clamp" }
  );

  // Opacity for the student figure - perhaps fades slightly or remains mostly visible
  const studentOpacity = interpolate(frame, [0, fps * 2], [1, 0.8], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ backgroundColor, transform: `scale(${scale})`, filter: `blur(${blur}px)` }}>
      {/* Simple Student figure - perhaps slightly more upright than before, eyes closed */}
      <div
        style={{
          width: 200,
          height: 300,
          backgroundColor: "#a0a0a0",
          borderRadius: "10px",
          position: "absolute",
          bottom: 50,
          left: "35%",
          opacity: studentOpacity,
          // Slightly more relaxed posture
          transform: "translateY(0px) rotate(-2deg)",
          clipPath: "polygon(10% 0%, 90% 0%, 100% 80%, 0% 80%)",
        }}
      >
        {/* Head with closed eyes hint */}
        <div style={{ width: 60, height: 60, backgroundColor: "#c0c0c0", borderRadius: "50%", position: "absolute", top: -30, left: "50%", transform: "translateX(-50%)" }}>
          <div style={{ width: 30, height: 2, backgroundColor: "#555", position: "absolute", top: 30, left: 15, borderRadius: "1px" }}></div> {/* Closed eye line */}
          <div style={{ width: 30, height: 2, backgroundColor: "#555", position: "absolute", top: 35, left: 15, borderRadius: "1px", transform: "rotate(5deg)" }}></div> {/* Slight hint of stress line */}
        </div>
        {/* Body */}
        <div style={{ width: 180, height: 220, backgroundColor: "#a0a0a0", position: "absolute", bottom: 0, left: "50%", transform: "translateX(-50%)", borderRadius: "5px" }}></div>
      </div>

      {/* Narrator V.O. */}
      <Sequence from={fps * 2} duration={fps * 8}> {/* Appears from frame 60 to 300 (relative to scene start) */}
        <div style={{ position: "absolute", top: "70%", left: "50%", transform: "translateX(-50%)", color: "#fff", fontSize: 36, fontFamily: "sans-serif", fontWeight: "bold", textAlign: "center", textShadow: "2px 2px 8px rgba(0,0,0,0.5)" }}>
          Searching for a moment of calm, a clear path forward?
        </div>
      </Sequence>
    </AbsoluteFill>
  );
};
