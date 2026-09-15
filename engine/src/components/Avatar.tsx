import React from 'react';
import { Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { AvatarGender, AvatarPose } from '../types';

interface AvatarProps {
  pose?: AvatarPose;
  gender?: AvatarGender;
  visible?: boolean;
  sceneFrame: number;
}

// Map poses to filename base
const POSE_FILES: Record<string, string> = {
  shocked_jawdrop: 'shocked_jawdrop.png',
  laughing_joke: 'laughing_joke.png',
  secret_whisper: 'secret_whisper.png',
  idle_neutral: 'idle_neutral.png',
  explaining_point: 'explaining_point.png',
  thinking_chin: 'thinking_chin.png',
  hyped_victory: 'hyped_victory.png',
  skeptical_sideeye: 'skeptical_sideeye.png',
  angry_triggered: 'angry_triggered.png',
  facepalm: 'facepalm.png',
};

export const Avatar: React.FC<AvatarProps> = ({
  pose = 'idle_neutral',
  gender = 'male',
  visible = true,
  sceneFrame,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Snappy pop-in spring
  const enterProgress = spring({
    frame: sceneFrame,
    fps,
    config: { damping: 11, stiffness: 200, mass: 0.5 },
  });

  // Subtle idle float (gentler for chibi portrait)
  const floatOffset = Math.sin(frame / 14) * 8;

  const translateY = visible
    ? interpolate(enterProgress, [0, 1], [300, 0]) + floatOffset
    : 400;

  const opacity = visible ? interpolate(enterProgress, [0, 0.25, 1], [0, 1, 1]) : 0;
  const scale = visible
    ? (interpolate(enterProgress, [0, 1], [0.7, 1]) + Math.sin(frame / 22) * 0.012)
    : 0.7;

  const fileName = POSE_FILES[pose] ?? POSE_FILES.idle_neutral;
  const avatarSrc = staticFile(`avatars/${gender}/${fileName}`);

  return (
    <div
      style={{
        position: 'absolute',
        bottom: '30px',
        right: '-10px',
        width: '380px',
        height: '380px',
        zIndex: 50,
        pointerEvents: 'none',
        transform: `translateY(${translateY}px) scale(${scale})`,
        opacity,
        // Clean drop shadow only, no glow (chibi style doesn't need glow)
        filter: 'drop-shadow(0 20px 30px rgba(0, 0, 0, 0.85))',
      }}
    >
      <Img
        src={avatarSrc}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'contain',
        }}
      />
    </div>
  );
};
