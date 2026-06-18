import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";

export const OverwhelmedScene = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 30], [0, 1]);

  return (
    <AbsoluteFill style={{ 
      backgroundColor: "#f7fafc", 
      color: "#2d3748", 
      display: "flex", 
      justifyContent: "center", 
      alignItems: "center",
      textAlign: "center",
      padding: 40
    }}>
      <div style={{ opacity }}>
        <h1 style={{ fontSize: "56px", fontWeight: "800", marginBottom: "20px" }}>Assignment Chaos</h1>
        <p style={{ fontSize: "28px", color: "#4a5568" }}>So many requirements. So little time.</p>
      </div>
    </AbsoluteFill>
  );
};
