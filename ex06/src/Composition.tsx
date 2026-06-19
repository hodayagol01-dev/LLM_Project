import React from "react";
import {
  AbsoluteFill,
  Img,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
} from "remotion";

/**
 * Assignment 06 - ShoreStep AI
 * Stable Remotion implementation:
 * Still-image cinematic storyboard with animated overlays.
 * Flow: stress -> imagination -> vacation calm -> product clarity -> confident ending.
 */

const imageStyle: React.CSSProperties = {
  width: "100%",
  height: "100%",
  objectFit: "cover",
  position: "absolute",
};

const titleStyle: React.CSSProperties = {
  fontFamily: "Arial, sans-serif",
  fontSize: 78,
  fontWeight: 900,
  color: "white",
  lineHeight: 1.04,
  letterSpacing: "-2.2px",
  maxWidth: 1100,
};

const subtitleStyle: React.CSSProperties = {
  fontFamily: "Arial, sans-serif",
  fontSize: 32,
  color: "rgba(255,255,255,0.9)",
  marginTop: 24,
  maxWidth: 820,
  lineHeight: 1.35,
};

function BackgroundImage({
  src,
  zoomFrom = 1,
  zoomTo = 1.08,
  panX = 0,
  sceneFrames = 360,
}: {
  src: string;
  zoomFrom?: number;
  zoomTo?: number;
  panX?: number;
  sceneFrames?: number;
}) {
  const frame = useCurrentFrame();

  const scale = interpolate(frame, [0, sceneFrames], [zoomFrom, zoomTo], {
    extrapolateRight: "clamp",
  });

  const x = interpolate(frame, [0, sceneFrames], [0, panX], {
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
  left = 105,
  center = false,
}: {
  title: string;
  subtitle?: string;
  top?: number;
  left?: number;
  center?: boolean;
}) {
  const frame = useCurrentFrame();

  const opacity = interpolate(frame, [0, 25], [0, 1], {
    extrapolateRight: "clamp",
  });

  const y = interpolate(frame, [0, 25], [44, 0], {
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        position: "absolute",
        left: center ? "50%" : left,
        top,
        opacity,
        transform: center ? `translate(-50%, ${y}px)` : `translateY(${y}px)`,
        textAlign: center ? "center" : "left",
      }}
    >
      <div style={titleStyle}>{title}</div>
      {subtitle && <div style={subtitleStyle}>{subtitle}</div>}
    </div>
  );
}

function StressBubble() {
  const frame = useCurrentFrame();
  const bubbleOpacity = interpolate(frame, [20, 42], [0, 1], {
    extrapolateRight: "clamp",
  });

  const words = ["Deadline", "PRD", "TODO", "Too much", "Where do I start?"];

  return (
    <div
      style={{
        position: "absolute",
        right: 120,
        top: 95,
        width: 455,
        minHeight: 260,
        borderRadius: "48px 48px 48px 12px",
        background: "rgba(255,255,255,0.94)",
        color: "#123047",
        padding: "32px 34px",
        boxShadow: "0 24px 70px rgba(0,0,0,0.34)",
        opacity: bubbleOpacity,
        transform: `translateY(${interpolate(bubbleOpacity, [0, 1], [22, 0])}px)`,
        fontFamily: "Arial, sans-serif",
      }}
    >
      <div style={{ fontSize: 30, fontWeight: 900, marginBottom: 20 }}>
        My brain right now:
      </div>

      {words.map((word, index) => {
        const appear = interpolate(frame, [35 + index * 7, 50 + index * 7], [0, 1], {
          extrapolateRight: "clamp",
        });

        return (
          <div
            key={word}
            style={{
              display: "inline-block",
              margin: "6px",
              padding: "10px 14px",
              borderRadius: 999,
              background: index % 2 === 0 ? "#fff1d8" : "#e5f7ff",
              border: "1px solid rgba(18,48,71,0.12)",
              fontSize: 22,
              fontWeight: 800,
              opacity: appear,
              transform: `scale(${interpolate(appear, [0, 1], [0.85, 1])})`,
            }}
          >
            {word}
          </div>
        );
      })}
    </div>
  );
}

function JumpingFish() {
  const frame = useCurrentFrame();
  const fish = [
    { emoji: "𓆝", left: 210, top: 430, delay: 0 },
    { emoji: "𓆟", left: 540, top: 405, delay: 18 },
    { emoji: "𓆞", left: 875, top: 455, delay: 34 },
    { emoji: "𓆝", left: 1120, top: 420, delay: 52 },
  ];

  return (
    <>
      {fish.map((item, index) => {
        const local = (frame - item.delay) % 80;
        const jump = interpolate(local, [0, 28, 56, 80], [0, -82, 0, 0], {
          extrapolateRight: "clamp",
        });
        const opacity = interpolate(local, [0, 8, 54, 70], [0, 1, 1, 0], {
          extrapolateRight: "clamp",
        });
        const rotate = interpolate(local, [0, 28, 56], [-18, 16, -8], {
          extrapolateRight: "clamp",
        });

        return (
          <div
            key={index}
            style={{
              position: "absolute",
              left: item.left,
              top: item.top,
              fontSize: 42,
              opacity: opacity * 0.65,
              color: "rgba(255,255,255,0.9)",
              transform: `translateY(${jump}px) rotate(${rotate}deg)`,
              filter: "drop-shadow(0 8px 12px rgba(0,0,0,0.18))",
            }}
          >
            {item.emoji}
          </div>
        );
      })}
    </>
  );
}

function StudentScene() {
  return (
    <AbsoluteFill>
      <BackgroundImage
        src="assets/images/from-videos/student-thinking.jpg"
        zoomTo={1.12}
        panX={-18}
        sceneFrames={360}
      />

      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "linear-gradient(90deg, rgba(8,14,28,0.78), rgba(8,14,28,0.34), rgba(8,14,28,0.72))",
        }}
      />

      <TextBlock
        title="Too many pieces."
        subtitle="One assignment suddenly feels like a whole ocean."
        top={350}
      />

      <StressBubble />
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
        sceneFrames={540}
      />

      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "linear-gradient(180deg, rgba(0,88,132,0.12), rgba(0,33,60,0.48))",
        }}
      />

      <JumpingFish />

      <TextBlock
        title="Pause. Breathe."
        subtitle="Let the noise become water."
        top={315}
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
        sceneFrames={360}
      />

      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "linear-gradient(180deg, rgba(5,14,30,0.18), rgba(0,56,85,0.42), rgba(5,14,30,0.52))",
        }}
      />

      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(circle at center, rgba(255,255,255,0.10), transparent 46%)",
        }}
      />

      <TextBlock
        title="Close your eyes."
        subtitle="Imagine yourself on vacation. The assignment is still there — but now it has a first step."
        top={210}
        center
      />
    </AbsoluteFill>
  );
}

function PhoneMockup() {
  const frame = useCurrentFrame();
  const chips: string[] = [];

  return (
    <>
      <div
        style={{
          position: "absolute",
          right: 145,
          top: 52,
          width: 350,
          height: 625,
          borderRadius: 44,
          background: "#071827",
          border: "10px solid rgba(255,255,255,0.82)",
          boxShadow: "0 34px 90px rgba(0,0,0,0.38)",
          overflow: "hidden",
        }}
      >
        <div
          style={{
            position: "absolute",
            top: 16,
            left: "50%",
            transform: "translateX(-50%)",
            width: 92,
            height: 18,
            borderRadius: 999,
            background: "#02070d",
            zIndex: 2,
          }}
        />

        <div
          style={{
            position: "absolute",
            inset: 0,
            padding: "58px 26px 26px",
            background:
              "linear-gradient(180deg, #eefaff 0%, #ffffff 54%, #eaf7f2 100%)",
            fontFamily: "Arial, sans-serif",
          }}
        >
          <div style={{ color: "#0b3150", fontSize: 19, fontWeight: 900 }}>
            ShoreStep AI
          </div>
          <div
            style={{
              marginTop: 18,
              fontSize: 35,
              lineHeight: 1.02,
              fontWeight: 900,
              color: "#0b3150",
            }}
          >
            From chaos
            <br />
            to clarity.
          </div>

          {["Read brief", "Generate PRD", "Build plan", "Prepare GitHub"].map(
            (step, index) => {
              const appear = interpolate(
                frame,
                [18 + index * 10, 33 + index * 10],
                [0, 1],
                { extrapolateRight: "clamp" }
              );

              return (
                <div
                  key={step}
                  style={{
                    marginTop: index === 0 ? 28 : 12,
                    padding: "13px 14px",
                    borderRadius: 16,
                    background: "rgba(11,49,80,0.08)",
                    color: "#0b3150",
                    fontSize: 18,
                    fontWeight: 800,
                    opacity: appear,
                    transform: `translateX(${interpolate(appear, [0, 1], [22, 0])}px)`,
                  }}
                >
                  ✓ {step}
                </div>
              );
            }
          )}
        </div>
      </div>

      {chips.map((chip, index) => {
        const appear = interpolate(frame, [index * 7, index * 7 + 16], [0, 1], {
          extrapolateRight: "clamp",
        });

        const positions = [
          { left: 760, top: 120 },
          { left: 710, top: 230 },
          { left: 745, top: 340 },
          { left: 705, top: 455 },
          { left: 1010, top: 230 },
          { left: 990, top: 420 },
        ];

        return (
          <div
            key={chip}
            style={{
              position: "absolute",
              left: positions[index].left,
              top: positions[index].top,
              padding: "12px 18px",
              borderRadius: 999,
              background: "rgba(255,255,255,0.94)",
              color: "#0b3150",
              fontFamily: "Arial, sans-serif",
              fontSize: 21,
              fontWeight: 900,
              opacity: appear,
              transform: `translateY(${interpolate(appear, [0, 1], [24, 0])}px)`,
              boxShadow: "0 10px 24px rgba(0,0,0,0.14)",
            }}
          >
            {chip}
          </div>
        );
      })}
    </>
  );
}

function ProductScene() {
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
            "radial-gradient(circle at 20% 20%, rgba(255,255,255,0.18), transparent 32%)",
        }}
      />

      <div
        style={{
          position: "absolute",
          left: 100,
          top: 115,
          color: "white",
        }}
      >
        <div
          style={{
            fontSize: 42,
            fontWeight: 800,
            marginBottom: 18,
            opacity: 0.92,
          }}
        >
          ShoreStep AI
        </div>

        <div
          style={{
            fontSize: 76,
            fontWeight: 900,
            lineHeight: 1.03,
            maxWidth: 830,
          }}
        >
          Calm the chaos.
          <br />
          Build the plan.
        </div>

        <div
          style={{
            marginTop: 28,
            fontSize: 30,
            lineHeight: 1.35,
            maxWidth: 690,
            color: "rgba(255,255,255,0.9)",
          }}
        >
          A simple workflow for turning assignment stress into clear next steps.
        </div>
      </div>

      <PhoneMockup />
    </AbsoluteFill>
  );
}

function FinalScene() {
  const frame = useCurrentFrame();

  const opacity = interpolate(frame, [0, 24], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        background:
          "linear-gradient(135deg, #061826 0%, #0e7490 56%, #f5d49b 100%)",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: "Arial, sans-serif",
        color: "white",
        textAlign: "center",
      }}
    >
      <div
        style={{
          opacity,
          transform: `translateY(${interpolate(opacity, [0, 1], [28, 0])}px)`,
        }}
      >
        <div style={{ fontSize: 48, fontWeight: 800, marginBottom: 24 }}>
          ShoreStep AI
        </div>

        <div
          style={{
            fontSize: 88,
            fontWeight: 950,
            maxWidth: 1250,
            lineHeight: 1.04,
          }}
        >
          From anxiety
          <br />
          to clarity.
        </div>

        <div
          style={{
            marginTop: 34,
            fontSize: 34,
            fontWeight: 800,
            direction: "rtl",
            unicodeBidi: "plaintext",
          }}
        >
מטלה גדולה מתחילה בצעד קטן
        </div>
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
        <ProductScene />
      </Sequence>

      <Sequence from={55 * 30} durationInFrames={5 * 30}>
        <FinalScene />
      </Sequence>
    </AbsoluteFill>
  );
};
