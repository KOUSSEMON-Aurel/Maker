import React from 'react';
import { Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { AvatarPose } from '../types';

interface AvatarProps {
  pose?: AvatarPose;
  visible?: boolean;
  sceneFrame: number;
}

export const Avatar: React.FC<AvatarProps> = ({
  pose = 'idle_neutral',
  visible = true,
  sceneFrame,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Snappy entrance spring
  const enterProgress = spring({
    frame: sceneFrame,
    fps,
    config: { damping: 12, stiffness: 160, mass: 0.7 },
  });

  // Idle floating animation
  const floatOffset = Math.sin(frame / 12) * 12;
  const slightTilt = Math.sin(frame / 18) * 2.5;

  const translateY = visible
    ? interpolate(enterProgress, [0, 1], [400, 0]) + floatOffset
    : 500;

  const opacity = visible ? interpolate(enterProgress, [0, 0.3, 1], [0, 1, 1]) : 0;
  const scale = visible ? interpolate(enterProgress, [0, 1], [0.75, 1]) : 0.75;

  const avatarSrc = staticFile(`avatars/${pose}.svg`);

  return (
    <div
      style={{
        position: 'absolute',
        bottom: '40px',
        right: '20px',
        width: '460px',
        height: '510px',
        zIndex: 50,
        pointerEvents: 'none',
        transform: `translateY(${translateY}px) scale(${scale}) rotate(${slightTilt}deg)`,
        opacity,
        filter: 'drop-shadow(0 25px 35px rgba(0, 0, 0, 0.9)) drop-shadow(0 0 25px rgba(0, 245, 255, 0.25))',
        transition: 'opacity 0.15s ease, transform 0.15s ease',
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
