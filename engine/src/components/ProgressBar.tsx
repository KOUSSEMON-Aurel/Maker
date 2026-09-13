import React from 'react';
import { useCurrentFrame, useVideoConfig } from 'remotion';

interface ProgressBarProps {
  accentColor: string;
}

export const ProgressBar: React.FC<ProgressBarProps> = ({ accentColor }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const progressPercent = Math.min(100, (frame / Math.max(1, durationInFrames)) * 100);

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 0,
        left: 0,
        right: 0,
        height: '8px',
        backgroundColor: 'rgba(255, 255, 255, 0.1)',
        zIndex: 60,
      }}
    >
      <div
        style={{
          width: `${progressPercent}%`,
          height: '100%',
          backgroundColor: accentColor,
          boxShadow: `0 0 16px ${accentColor}`,
          transition: 'width 0.05s linear',
        }}
      />
    </div>
  );
};
