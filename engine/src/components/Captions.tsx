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

  if (!captions || captions.length === 0) return null;

  // Find the active word index
  const activeIndex = captions.findIndex(
    (c) => currentTime >= c.start && currentTime <= c.end + 0.12
  );

  const displayIndex =
    activeIndex !== -1
      ? activeIndex
      : captions.findIndex((c) => currentTime < c.start);

  if (displayIndex === -1 && currentTime > captions[captions.length - 1].end + 0.5) {
    return null;
  }

  const targetIndex = displayIndex === -1 ? captions.length - 1 : displayIndex;

  // Show 2-word chunk
  const windowSize = 2;
  const startIndex = Math.floor(targetIndex / windowSize) * windowSize;
  const currentChunk = captions.slice(startIndex, startIndex + windowSize);

  return (
    <div
      style={{
        position: 'absolute',
        // Place captions in the lower-middle zone, above avatar area
        bottom: '420px',
        left: '32px',
        right: '32px',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '14px',
        zIndex: 60,
        pointerEvents: 'none',
      }}
    >
      {currentChunk.map((item, idx) => {
        const globalIdx = startIndex + idx;
        const isActive = globalIdx === activeIndex;

        const wordStartFrame = Math.round(item.start * fps);
        const relativeFrame = Math.max(0, frame - wordStartFrame);

        // Bounce scale only on the active word, subtle
        const wordScale = isActive
          ? spring({
              frame: relativeFrame,
              fps,
              config: { damping: 10, stiffness: 280, mass: 0.35 },
            }) * 0.12 + 1.0
          : 1.0;

        // Active: bright accent color text, inactive: white
        const textColor = isActive ? accentColor : '#FFFFFF';

        // Multi-layer text stroke for maximum readability on any background
        const textShadow = [
          '3px 3px 0 #000',
          '-3px -3px 0 #000',
          '3px -3px 0 #000',
          '-3px 3px 0 #000',
          '4px 0 0 #000',
          '-4px 0 0 #000',
          '0 4px 0 #000',
          '0 -4px 0 #000',
          '0 8px 20px rgba(0,0,0,0.9)',
        ].join(', ');

        return (
          <span
            key={`${item.word}-${item.start}-${globalIdx}`}
            style={{
              fontSize: '82px',
              fontWeight: 900,
              fontFamily: '"Montserrat", "Inter", "Arial Black", sans-serif',
              textTransform: 'uppercase',
              letterSpacing: '-2px',
              lineHeight: 1.0,
              color: textColor,
              // No background box — color pop only on text itself
              padding: '0 6px',
              display: 'inline-block',
              transform: `scale(${wordScale})`,
              transformOrigin: 'center bottom',
              textShadow,
              // Subtle glow on active word only
              filter: isActive
                ? `drop-shadow(0 0 18px ${accentColor}CC)`
                : 'none',
              transition: 'color 0.08s ease',
            }}
          >
            {item.word}
          </span>
        );
      })}
    </div>
  );
};
