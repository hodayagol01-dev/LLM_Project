import { Composition } from "remotion";
import { MyComposition } from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="ShoreStepVideo"
        component={MyComposition}
        durationInFrames={60 * 30} // 60 seconds * 30fps
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
