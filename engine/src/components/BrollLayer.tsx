import React from 'react';
import { Img, Video, interpolate, staticFile } from 'remotion';

interface BrollLayerProps {
  brollUrl?: string;
  sceneFrame: number;
  sceneDuration: number;
  accentColor: string;
}

export const BrollLayer: React.FC<BrollLayerProps> = ({
  brollUrl,
  sceneFrame,
  sceneDuration,
  accentColor,
}) => {
  const progress = Math.min(1, sceneFrame / Math.max(1, sceneDuration));
  
  // Smooth Ken Burns zoom effect
  const zoomScale = interpolate(progress, [0, 1], [1.0, 1.09]);
  const bgZoom = interpolate(progress, [0, 1], [1.1, 1.2]);

  const hasMedia = Boolean(brollUrl && brollUrl.trim().length > 0);
  const isVideo = hasMedia && (brollUrl!.endsWith('.mp4') || brollUrl!.endsWith('.webm'));

  const resolvedUrl = hasMedia
    ? brollUrl!.startsWith('http') || brollUrl!.startsWith('/')
      ? brollUrl!
      : staticFile(brollUrl!)
    : '';

  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        overflow: 'hidden',
        zIndex: 10,
        backgroundColor: '#0A0B10',
      }}
    >
      {/* 1. Full-bleed Blurred Background Layer (Cinematic Ambient Wash) */}
      {hasMedia ? (
        <div
          style={{
            position: 'absolute',
            inset: -40,
            overflow: 'hidden',
            filter: 'blur(30px) brightness(0.35) saturate(1.4)',
            transform: `scale(${bgZoom})`,
            transformOrigin: 'center center',
          }}
        >
          {isVideo ? (
            <Video
              src={resolvedUrl}
              style={{ width: '100%', height: '100%', objectFit: 'cover' }}
              muted
            />
          ) : (
            <Img
              src={resolvedUrl}
              style={{ width: '100%', height: '100%', objectFit: 'cover' }}
            />
          )}
        </div>
      ) : (
        /* Rich dark nebula fallback if no media */
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background: `radial-gradient(circle at 50% 35%, #1E1B4B 0%, #0F172A 60%, #030712 100%)`,
          }}
        />
      )}

      {/* 2. Focused Sharp Centerpiece Photograph / Video (Documentary Framing) */}
      {hasMedia && (
        <div
          style={{
            position: 'absolute',
            top: '15%',
            left: '50%',
            transform: 'translateX(-50%)',
            width: '920px',
            height: '620px',
            borderRadius: '28px',
            overflow: 'hidden',
            border: '2px solid rgba(255, 255, 255, 0.18)',
            boxShadow: '0 30px 60px rgba(0, 0, 0, 0.9), 0 0 40px rgba(0, 0, 0, 0.5)',
            zIndex: 15,
            backgroundColor: '#000000',
          }}
        >
          <div
            style={{
              width: '100%',
              height: '100%',
              transform: `scale(${zoomScale})`,
              transformOrigin: 'center center',
            }}
          >
            {isVideo ? (
              <Video
                src={resolvedUrl}
                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                muted
              />
            ) : (
              <Img
                src={resolvedUrl}
                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
              />
            )}
          </div>

          {/* Inner subtle photo vignette */}
          <div
            style={{
              position: 'absolute',
              inset: 0,
              background: 'radial-gradient(circle at center, transparent 65%, rgba(0,0,0,0.5) 100%)',
              pointerEvents: 'none',
            }}
          />
        </div>
      )}

      {/* 3. Global Darkening Gradients for Legibility (Top for Header, Bottom for Captions & Avatar) */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: '240px',
          background: 'linear-gradient(to bottom, rgba(0,0,0,0.85) 0%, transparent 100%)',
          pointerEvents: 'none',
          zIndex: 20,
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: '420px',
          background: 'linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 60%, transparent 100%)',
          pointerEvents: 'none',
          zIndex: 20,
        }}
      />
    </div>
  );
};
