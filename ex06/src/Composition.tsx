import React from "react";
import {
  AbsoluteFill,
  Img,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

/**
 * Assignment 06 - ShoreStep AI
 * Stable Remotion implementation:
 * Video playback assets were replaced with extracted still frames because
 * local MP4/WebM playback caused browser media errors in Remotion Preview.
 * The cinematic feeling is preserved using Ken Burns zoom/pan motion,
 * gradients, animated text, and product UI cards.
 */

const imageStyle: React.CSSProperties = {
  width: "100%",
  height: "100%",
  objectFit: "cover",
  position: "absolute",
};

const overlay: React.CSSProperties = {
  position: "absolute",
  inset: 0,
  background:
    "linear-gradient(90deg, rgba(5,14,30,0.72), rgba(5,14,30,0.32), rgba(5,14,30,0.65))",
};

const titleStyle: React.CSSProperties = {
  fontFamily: "Arial, sans-serif",
  fontSize: 74,
  fontWeight: 800,
  color: "white",
  lineHeight: 1.05,
  letterSpacing: "-2px",
  maxWidth: 980,
};

const subtitleStyle: React.CSSProperties = {
  fontFamily: "Arial, sans-serif",
  fontSize: 30,
  color: "rgba(255,255,255,0.88)",
  marginTop: 24,
  maxWidth: 780,
  lineHeight: 1.35,
};

function BackgroundImage({
  src,
  zoomFrom = 1,
  zoomTo = 1.08,
  panX = 0,
}: {
  src: string;
  zoomFrom?: number;
  zoomTo?: number;
  panX?: number;
}) {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const scale = interpolate(frame, [0, durationInFrames], [zoomFrom, zoomTo], {
    extrapolateRight: "clamp",
  });

  const x = interpolate(frame, [0, durationInFrames], [0, panX], {
    extrapolateRight: "clamp",
  });

  return (
    <Img
      src={staticFile(src)}
      style={{
        ...imageStyle,
        transform: `scale(${scale}) translateX(${x}px)`,
      }}
    />
  );
}

function TextBlock({
  title,
  subtitle,
  top = 250,
}: {
  title: string;
  subtitle?: string;
  top?: number;
}) {
  const frame = useCurrentFrame();

  const opacity = interpolate(frame, [0, 25], [0, 1], {
    extrapolateRight: "clamp",
  });

  const y = interpolate(frame, [0, 25], [40, 0], {
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        position: "absolute",
        left: 105,
        top,
        opacity,
        transform: `translateY(${y}px)`,
      }}
    >
      <div style={titleStyle}>{title}</div>
      {subtitle && <div style={subtitleStyle}>{subtitle}</div>}
    </div>
  );
}

function StudentScene() {
  return (
    <AbsoluteFill>
      <BackgroundImage src="assets/images/from-videos/student-thinking.jpg" zoomTo={1.12} />
      <div style={overlay} />
      <TextBlock
        title="Too many requirements."
        subtitle="Too little clarity."
        top={315}
      />
    </AbsoluteFill>
  );
}

function BeachScene() {
  return (
    <AbsoluteFill>
      <BackgroundImage
        src="assets/images/from-videos/beach-dream.jpg"
        zoomFrom={1.04}
        zoomTo={1.14}
        panX={-25}
      />
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "linear-gradient(180deg, rgba(0,68,102,0.20), rgba(0,33,60,0.52))",
        }}
      />
      <TextBlock
        title="Pause. Breathe."
        subtitle="Find the first step."
        top={330}
      />
    </AbsoluteFill>
  );
}

function SurfScene() {
  return (
    <AbsoluteFill>
      <BackgroundImage
        src="assets/images/from-videos/surfing-dream.jpg"
        zoomFrom={1.02}
        zoomTo={1.11}
        panX={30}
      />
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "linear-gradient(90deg, rgba(5,14,30,0.72), rgba(0,90,130,0.24))",
        }}
      />
      <TextBlock
        title="Big tasks become possible"
        subtitle="when they become small steps."
        top={305}
      />
    </AbsoluteFill>
  );
}

function ProductCards() {
  const frame = useCurrentFrame();
  const cards = ["PRD", "PLAN", "TODO", "PROMPTS", "JSON", "GitHub"];

  return (
    <AbsoluteFill
      style={{
        background:
          "linear-gradient(135deg, #08233d 0%, #0f5f7a 48%, #f3d6a1 100%)",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(circle at 20% 20%, rgba(255,255,255,0.16), transparent 32%)",
        }}
      />

      <div
        style={{
          position: "absolute",
          left: 100,
          top: 95,
          color: "white",
        }}
      >
        <div
          style={{
            fontSize: 46,
            fontWeight: 800,
            marginBottom: 14,
          }}
        >
          ShoreStep AI
        </div>
        <div
          style={{
            fontSize: 72,
            fontWeight: 900,
            lineHeight: 1.04,
            maxWidth: 950,
          }}
        >
          Assignment chaos becomes a clear plan.
        </div>
      </div>

      <div
        style={{
          position: "absolute",
          right: 90,
          top: 110,
          width: 560,
          borderRadius: 34,
          padding: 32,
          background: "rgba(255,255,255,0.92)",
          boxShadow: "0 24px 80px rgba(0,0,0,0.28)",
        }}
      >
        <div
          style={{
            color: "#0b3150",
            fontSize: 26,
            fontWeight: 800,
            marginBottom: 22,
          }}
        >
          Generated workflow
        </div>

        {cards.map((card, index) => {
          const appear = interpolate(
            frame,
            [index * 8, index * 8 + 14],
            [0, 1],
            { extrapolateRight: "clamp" }
          );

          return (
            <div
              key={card}
              style={{
                opacity: appear,
                transform: `translateY(${interpolate(appear, [0, 1], [20, 0])}px)`,
                background: "#f4fbff",
                border: "1px solid rgba(9,71,112,0.14)",
                borderRadius: 18,
                padding: "18px 22px",
                marginBottom: 14,
                fontSize: 28,
                fontWeight: 800,
                color: "#0b3150",
              }}
            >
              ✓ {card}
            </div>
          );
        })}

        <div
          style={{
            marginTop: 20,
            padding: 18,
            borderRadius: 18,
            background: "#e7f7f4",
            color: "#0b3150",
            fontSize: 26,
            fontWeight: 800,
            direction: "rtl",
            textAlign: "right",
          }}
        >
          מטלה גדולה מתחילה בצעד קטן
        </div>
      </div>
    </AbsoluteFill>
  );
}

function FinalScene() {
  return (
    <AbsoluteFill
      style={{
        background:
          "linear-gradient(135deg, #061826 0%, #0e7490 55%, #f5d49b 100%)",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: "Arial, sans-serif",
        color: "white",
        textAlign: "center",
      }}
    >
      <div style={{ fontSize: 48, fontWeight: 700, marginBottom: 22 }}>
        ShoreStep AI
      </div>
      <div
        style={{
          fontSize: 78,
          fontWeight: 900,
          maxWidth: 1250,
          lineHeight: 1.06,
        }}
      >
        Start calm. Build smart.
        <br />
        Submit with confidence.
      </div>
    </AbsoluteFill>
  );
}

export const MyComposition = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#071827" }}>
      <Sequence from={0} durationInFrames={12 * 30}>
        <StudentScene />
      </Sequence>

      <Sequence from={12 * 30} durationInFrames={18 * 30}>
        <BeachScene />
      </Sequence>

      <Sequence from={30 * 30} durationInFrames={12 * 30}>
        <SurfScene />
      </Sequence>

      <Sequence from={42 * 30} durationInFrames={13 * 30}>
        <ProductCards />
      </Sequence>

      <Sequence from={55 * 30} durationInFrames={5 * 30}>
        <FinalScene />
      </Sequence>
    </AbsoluteFill>
  );
};
