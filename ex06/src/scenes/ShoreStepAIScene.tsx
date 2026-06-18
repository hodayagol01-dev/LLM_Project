import React from "react";
import { AbsoluteFill, useCurrentFrame, interpolate, useVideoConfig } from "remotion";

const ShoreStepAIInterface: React.FC<{ frame: number }> = ({ frame }) => {
  const { fps } = useVideoConfig();

  // Animations: UI fade, scaling elements
  const uiOpacity = interpolate(frame, [0, 30], [0, 1], { extrapolateRight: "clamp" });
  const uiScale = interpolate(frame, [0, 30], [0.95, 1], { extrapolateRight: "clamp" });
  const outputOpacity = interpolate(frame, [90, 150], [0, 1], { extrapolateRight: "clamp" });

  return (
    <div
      style={{
        width: "85%",
        height: "80%",
        background: "linear-gradient(135deg, #ffffff, #f0f4f8)",
        borderRadius: "24px",
        position: "absolute",
        top: "10%",
        left: "50%",
        transform: `translateX(-50%) scale(${uiScale})`,
        opacity: uiOpacity,
        boxShadow: "0 20px 40px rgba(0,0,0,0.1)",
        padding: 40,
        display: "flex",
        flexDirection: "column",
        gap: 20,
      }}
    >
      <div style={{ fontSize: 32, fontWeight: "700", color: "#2e4053" }}>ShoreStep AI</div>
      
      <div style={{ flex: 1, backgroundColor: "#e2e8f0", borderRadius: "12px", padding: 20 }}>
        <p style={{ color: "#4a5568", fontSize: 20 }}>Assignment: Build a polished product video...</p>
      </div>

      <div style={{ opacity: outputOpacity, display: "flex", flexWrap: "wrap", gap: 12 }}>
        {["PRD.md", "PLAN.md", "TODO.md", "PROMPTS.md", "JSON", "GitHub"].map((item, i) => (
          <div key={i} style={{ padding: "12px 20px", backgroundColor: "#3182ce", color: "white", borderRadius: "8px", fontWeight: "600" }}>
            {item}
          </div>
        ))}
        {/* Hebrew RTL requirement */}
        <div
          style={{
            padding: "12px 20px",
            backgroundColor: "#2b6cb0",
            color: "white",
            borderRadius: "8px",
            fontWeight: "600",
            direction: "rtl",
            textAlign: "right",
          }}
        >
          מטלה גדולה מתחילה בצעד קטן
        </div>
      </div>
    </div>
  );
};

export const ShoreStepAIScene: React.FC = () => {
  const { fps } = useVideoConfig();
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill style={{ backgroundColor: "#FFFFFF" }}>
      <ShoreStepAIInterface frame={frame} />
    </AbsoluteFill>
  );
};
