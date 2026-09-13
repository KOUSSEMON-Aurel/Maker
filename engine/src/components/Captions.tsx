import React from 'react';
import { spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { CaptionWord } from '../types';

interface CaptionsProps {
  captions: CaptionWord[];
  accentColor: string;
  textColor: string;
}

export const Captions: React.FC<CaptionsProps> = ({ captions, accentColor }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;

  if (!captions || captions.length === 0) {
    return null;
  }

  // Find active word
  const activeIndex = captions.findIndex(
    (c) => currentTime >= c.start && currentTime <= c.end + 0.1
  );

  const displayIndex =
    activeIndex !== -1
      ? activeIndex
      : captions.findIndex((c) => currentTime < c.start);

  if (displayIndex === -1 && currentTime > captions[captions.length - 1].end + 0.5) {
    return null;
  }

  const targetIndex = displayIndex === -1 ? captions.length - 1 : displayIndex;

  // Window of 2 words for rapid TikTok/Shorts pacing
  const windowSize = 2;
  const startIndex = Math.floor(targetIndex / windowSize) * windowSize;
  const currentChunk = captions.slice(startIndex, startIndex + windowSize);

  return (
    <div
      style={{
        position: 'absolute',
        top: '61%',
        left: '40px',
        right: '40px',
        transform: 'translateY(-50%)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '20px',
        zIndex: 60,
        pointerEvents: 'none',
      }}
    >
      {currentChunk.map((item, idx) => {
        const globalIdx = startIndex + idx;
        const isCurrentWord = globalIdx === activeIndex;

        const wordStartFrame = Math.round(item.start * fps);
        const relativeFrame = Math.max(0, frame - wordStartFrame);

        const wordScale = isCurrentWord
          ? spring({
              frame: relativeFrame,
              fps,
              config: { damping: 9, stiffness: 240, mass: 0.4 },
            }) * 0.18 + 1.05
          : 1.0;

        return (
          <span
            key={`${item.word}-${item.start}-${globalIdx}`}
            style={{
              fontSize: '78px',
              fontWeight: 900,
              fontFamily: '"Montserrat", "Inter", sans-serif',
              textTransform: 'uppercase',
              letterSpacing: '-1.5px',
              color: isCurrentWord ? '#000000' : '#FFFFFF',
              backgroundColor: isCurrentWord ? accentColor : 'transparent',
              padding: isCurrentWord ? '12px 28px' : '12px 8px',
              borderRadius: isCurrentWord ? '24px' : '0',
              transform: `scale(${wordScale})`,
              boxShadow: isCurrentWord ? `0 0 50px ${accentColor}FF, 0 14px 32px rgba(0,0,0,0.9)` : 'none',
              textShadow: isCurrentWord
                ? 'none'
                : '0 6px 20px rgba(0, 0, 0, 1), 0 0 12px rgba(0, 0, 0, 1), 3px 3px 0 #000, -3px -3px 0 #000, 3px -3px 0 #000, -3px 3px 0 #000',
              display: 'inline-block',
              transition: 'transform 0.05s ease',
            }}
          >
            {item.word}
          </span>
        );
      })}
    </div>
  );
};
