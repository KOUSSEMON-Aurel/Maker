import React from 'react';
import { AbsoluteFill, useCurrentFrame } from 'remotion';
import { AudioManager } from './components/AudioManager';
import { Avatar } from './components/Avatar';
import { BrollLayer } from './components/BrollLayer';
import { Captions } from './components/Captions';
import { ProgressBar } from './components/ProgressBar';
import { THEMES } from './themes';
import { VideoProps } from './types';

export const MainComposition: React.FC<VideoProps> = ({
  theme: themeKey = 'punchy_creator',
  title = 'Titre de la vidéo',
  avatarGender = 'male',
  voiceAudioUrl = '',
  musicTrackUrl = '',
  scenes = [],
  captions = [],
}) => {
  const frame = useCurrentFrame();
  const currentTheme = THEMES[themeKey] || THEMES.punchy_creator;

  // Find the currently active scene
  const activeSceneIndex = scenes.findIndex(
    (s) => frame >= s.startFrame && frame < s.startFrame + s.durationInFrames
  );

  const activeScene =
    activeSceneIndex !== -1
      ? scenes[activeSceneIndex]
      : scenes.length > 0
      ? scenes[scenes.length - 1]
      : undefined;

  const sceneFrame = activeScene ? frame - activeScene.startFrame : 0;
  const sceneDuration = activeScene ? activeScene.durationInFrames : 90;

  // Subtle SVG Noise Texture
  const noiseSvg = `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E")`;

  return (
    <AbsoluteFill
      style={{
        background: currentTheme.bgGradient,
        fontFamily: currentTheme.fontFamily,
        overflow: 'hidden',
      }}
    >
      {/* 1. Subtle Procedural Noise Overlay */}
      <AbsoluteFill
        style={{
          opacity: 0.035,
          backgroundImage: noiseSvg,
          pointerEvents: 'none',
          zIndex: 5,
        }}
      />

      {/* 2. Media / B-Roll Layer with Centerpiece Graphic */}
      <BrollLayer
        sceneId={activeScene?.sceneId}
        brollUrl={activeScene?.brollUrl}
        sceneFrame={sceneFrame}
        sceneDuration={sceneDuration}
        accentColor={currentTheme.accentColor}
      />

      {/* 3. Headline supprimé — rendu immersif documentaire sans bandeau IA */}

      {/* 4. Karaoke Dynamic Subtitles */}
      <Captions
        captions={captions}
        accentColor={currentTheme.accentColor}
        textColor={currentTheme.textColor}
      />

      {/* 5. Expressive 2D Avatar Mascot */}
      <Avatar
        pose={activeScene?.avatarPose}
        gender={avatarGender}
        visible={activeScene?.avatarVisible}
        sceneFrame={sceneFrame}
      />

      {/* 6. Discreet Progress Bar */}
      <ProgressBar accentColor={currentTheme.accentColor} />

      {/* 7. Audio Mixing (Voice, Music Ducking & SFX) */}
      <AudioManager
        voiceAudioUrl={voiceAudioUrl}
        musicTrackUrl={musicTrackUrl}
        scenes={scenes}
      />
    </AbsoluteFill>
  );
};
