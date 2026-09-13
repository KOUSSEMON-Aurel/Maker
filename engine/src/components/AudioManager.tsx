import React from 'react';
import { Audio, Sequence, interpolate, staticFile, useCurrentFrame } from 'remotion';
import { Scene } from '../types';

interface AudioManagerProps {
  voiceAudioUrl: string;
  musicTrackUrl?: string;
  scenes: Scene[];
}

export const AudioManager: React.FC<AudioManagerProps> = ({
  voiceAudioUrl,
  musicTrackUrl,
  scenes,
}) => {
  const frame = useCurrentFrame();

  // Determine if voice is speaking during the current frame
  // (In our pipeline, scenes represent the voice active segments)
  const isSpeaking = scenes.some(
    (scene) => frame >= scene.startFrame && frame <= scene.startFrame + scene.durationInFrames
  );

  // Smooth ducking transition using interpolate
  const targetVolume = isSpeaking ? 0.08 : 0.22;
  const musicVolume = interpolate(
    isSpeaking ? 1 : 0,
    [0, 1],
    [0.22, 0.08],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  return (
    <>
      {/* 1. Primary Voiceover Track */}
      {voiceAudioUrl && (
        <Audio
          src={voiceAudioUrl.startsWith('http') || voiceAudioUrl.startsWith('/') ? voiceAudioUrl : staticFile(voiceAudioUrl)}
          volume={1.0}
        />
      )}

      {/* 2. Background Music with Smooth Ducking */}
      {musicTrackUrl && (
        <Audio
          src={musicTrackUrl.startsWith('http') || musicTrackUrl.startsWith('/') ? musicTrackUrl : staticFile(musicTrackUrl)}
          volume={musicVolume}
          loop
        />
      )}

      {/* 3. Dynamic Sound Effects (SFX) per Scene */}
      {scenes.map((scene) => {
        if (!scene.sfxTrigger) return null;
        const sfxPath = staticFile(`sfx/${scene.sfxTrigger}.mp3`);

        return (
          <Sequence
            key={`sfx-${scene.sceneId}-${scene.startFrame}`}
            from={scene.startFrame}
            durationInFrames={30}
          >
            <Audio src={sfxPath} volume={0.5} />
          </Sequence>
        );
      })}
    </>
  );
};
