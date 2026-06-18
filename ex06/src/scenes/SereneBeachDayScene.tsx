import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";

export const SereneBeachDayScene = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 30], [0, 1]);

  return (
    <AbsoluteFill style={{ 
      background: "linear-gradient(180deg, #e0f2f1 0%, #b2dfdb 100%)", 
      color: "#004d40", 
      display: "flex", 
      justifyContent: "center", 
      alignItems: "center",
      textAlign: "center",
      padding: 60
    }}>
      <div style={{ opacity }}>
        <h1 style={{ fontSize: "64px", fontWeight: "700", marginBottom: "30px" }}>Pause. Breathe.</h1>
        <p style={{ fontSize: "32px" }}>Find the first step.</p>
      </div>
    </AbsoluteFill>
  );
};
