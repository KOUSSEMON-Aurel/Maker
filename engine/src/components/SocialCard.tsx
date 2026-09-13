import React from 'react';
import { interpolate, spring, useVideoConfig } from 'remotion';
import { ThemeConfig } from '../themes';

interface SocialCardProps {
  title: string;
  theme: ThemeConfig;
  sceneFrame: number;
}

export const SocialCard: React.FC<SocialCardProps> = ({ title, theme, sceneFrame }) => {
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: sceneFrame,
    fps,
    config: { damping: 14, stiffness: 140, mass: 0.8 },
  });

  const translateY = interpolate(entrance, [0, 1], [-140, 0]);
  const opacity = interpolate(entrance, [0, 0.4, 1], [0, 1, 1]);

  return (
    <div
      style={{
        position: 'absolute',
        top: '80px',
        left: '50px',
        right: '50px',
        zIndex: 40,
        transform: `translateY(${translateY}px)`,
        opacity,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <div
        style={{
          background: 'rgba(15, 23, 42, 0.88)',
          border: `2px solid ${theme.accentColor}55`,
          borderRadius: '28px',
          padding: '20px 36px',
          boxShadow: `0 20px 50px rgba(0, 0, 0, 0.8), 0 0 30px ${theme.accentColor}25`,
          backdropFilter: 'blur(20px)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: '10px',
          maxWidth: '920px',
        }}
      >
        {/* Viral Badge */}
        <div
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '10px',
            backgroundColor: `${theme.accentColor}20`,
            border: `1px solid ${theme.accentColor}88`,
            padding: '6px 18px',
            borderRadius: '20px',
          }}
        >
          <div
            style={{
              width: '10px',
              height: '10px',
              borderRadius: '50%',
              backgroundColor: theme.accentColor,
              boxShadow: `0 0 14px ${theme.accentColor}`,
            }}
          />
          <span
            style={{
              fontSize: '18px',
              fontWeight: 800,
              textTransform: 'uppercase',
              letterSpacing: '2.5px',
              color: theme.accentColor,
            }}
          >
            HISTOIRE SECRÈTE
          </span>
        </div>

        <h1
          style={{
            margin: 0,
            fontSize: '40px',
            fontWeight: 900,
            textAlign: 'center',
            lineHeight: 1.2,
            color: '#FFFFFF',
            letterSpacing: '-0.5px',
            textShadow: '0 2px 10px rgba(0,0,0,0.8)',
          }}
        >
          {title}
        </h1>
      </div>
    </div>
  );
};
