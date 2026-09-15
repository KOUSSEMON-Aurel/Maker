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

  // Clean captions: merge any punctuation-only word to previous word
  const cleanCaptions = React.useMemo(() => {
    if (!captions || captions.length === 0) return [];
    const list: CaptionWord[] = [];
    const punctRegex = /^[!?.…,:;—–\-()]+$/;
    for (const item of captions) {
      const w = item.word.trim();
      if (!w) continue;
      if (punctRegex.test(w) && list.length > 0) {
        list[list.length - 1].word += (w === '?' || w === '!' || w === ':' || w === ';') ? ` ${w}` : w;
        list[list.length - 1].end = Math.max(list[list.length - 1].end, item.end);
      } else {
        list.push({ ...item, word: w });
      }
    }
    return list;
  }, [captions]);

  if (cleanCaptions.length === 0) return null;

  // Find the active word index
  const activeIndex = cleanCaptions.findIndex(
    (c) => currentTime >= c.start && currentTime <= c.end + 0.12
  );

  const displayIndex =
    activeIndex !== -1
      ? activeIndex
      : cleanCaptions.findIndex((c) => currentTime < c.start);

  if (displayIndex === -1 && currentTime > cleanCaptions[cleanCaptions.length - 1].end + 0.5) {
    return null;
  }

  const targetIndex = displayIndex === -1 ? cleanCaptions.length - 1 : displayIndex;

  // Show 2-word chunk
  const windowSize = 2;
  const startIndex = Math.floor(targetIndex / windowSize) * windowSize;
  const currentChunk = cleanCaptions.slice(startIndex, startIndex + windowSize);

  return (
    <div
      style={{
        position: 'absolute',
        bottom: '420px',
        left: '0',
        right: '0',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 60,
        pointerEvents: 'none',
      }}
    >
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          gap: '28px',
          padding: '12px 28px',
          background: 'rgba(10, 10, 18, 0.55)',
          backdropFilter: 'blur(12px)',
          borderRadius: '24px',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          boxShadow: '0 8px 32px rgba(0, 0, 0, 0.45)',
        }}
      >
        {currentChunk.map((item, idx) => {
          const globalIdx = startIndex + idx;
          const isActive = globalIdx === activeIndex;

          const wordStartFrame = Math.round(item.start * fps);
          const relativeFrame = Math.max(0, frame - wordStartFrame);

          // Gentle spring pop on active word
          const wordScale = isActive
            ? spring({
                frame: relativeFrame,
                fps,
                config: { damping: 14, stiffness: 220, mass: 0.4 },
              }) * 0.06 + 1.0
            : 1.0;

          // Active: clean accent yellow, inactive: crisp bright white
          const textColor = isActive ? accentColor : '#F3F4F6';

          return (
            <span
              key={`${item.word}-${item.start}-${globalIdx}`}
              style={{
                fontSize: '52px',
                fontWeight: 800,
                fontFamily: '"Montserrat", "Inter", -apple-system, sans-serif',
                textTransform: 'uppercase',
                letterSpacing: '1.5px',
                lineHeight: 1.1,
                color: textColor,
                display: 'inline-block',
                transform: `scale(${wordScale})`,
                transformOrigin: 'center center',
                WebkitTextStroke: isActive ? '1px rgba(0, 0, 0, 0.4)' : 'none',
                textShadow: '0 2px 8px rgba(0, 0, 0, 0.8), 0 4px 16px rgba(0, 0, 0, 0.6)',
                transition: 'color 0.1s ease, transform 0.1s ease',
              }}
            >
              {item.word}
            </span>
          );
        })}
      </div>
    </div>
  );
};
