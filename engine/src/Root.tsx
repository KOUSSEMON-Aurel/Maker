import React from 'react';
import { Composition } from 'remotion';
import { MainComposition } from './Composition';
import { VideoProps } from './types';

export const defaultProps: VideoProps = {
  theme: 'punchy_creator',
  title: 'Ce gars a vendu la Tour Eiffel...',
  avatarGender: 'male',
  voiceAudioUrl: 'sfx/paper_slide.mp3', // default fallback audio
  musicTrackUrl: 'music/suspense_dark/track_01.mp3',
  totalDurationInFrames: 360, // 12 seconds preview
  fps: 30,
  scenes: [
    {
      sceneId: 1,
      voiceText: 'Ce gars a accidentellement vendu la Tour Eiffel deux fois de suite.',
      avatarVisible: true,
      avatarPose: 'shocked_jawdrop',
      highlightWord: 'vendu',
      sfxTrigger: 'sub_bass_hit',
      startFrame: 0,
      durationInFrames: 120,
    },
    {
      sceneId: 2,
      voiceText: 'En 1925 Victor Lustig apprend que la tour coûte trop cher à repeindre.',
      avatarVisible: false,
      highlightWord: '1925',
      sfxTrigger: 'paper_slide',
      startFrame: 120,
      durationInFrames: 120,
    },
    {
      sceneId: 3,
      voiceText: 'Il a encaissé le chèque et a fui en train. Et voilà comment...',
      avatarVisible: true,
      avatarPose: 'secret_whisper',
      highlightWord: 'chèque',
      sfxTrigger: 'whoosh',
      startFrame: 240,
      durationInFrames: 120,
    },
  ],
  captions: [
    { word: 'Ce', start: 0.1, end: 0.35 },
    { word: 'gars', start: 0.36, end: 0.75 },
    { word: 'a', start: 0.76, end: 0.95 },
    { word: 'vendu', start: 0.96, end: 1.45 },
    { word: 'la', start: 1.46, end: 1.65 },
    { word: 'Tour', start: 1.66, end: 2.1 },
    { word: 'Eiffel', start: 2.11, end: 2.7 },
    { word: 'deux', start: 2.75, end: 3.1 },
    { word: 'fois', start: 3.11, end: 3.5 },
    { word: 'de', start: 3.51, end: 3.7 },
    { word: 'suite', start: 3.71, end: 4.1 },
    { word: 'En', start: 4.2, end: 4.4 },
    { word: '1925', start: 4.41, end: 5.1 },
    { word: 'Victor', start: 5.15, end: 5.6 },
    { word: 'Lustig', start: 5.61, end: 6.2 },
    { word: 'apprend', start: 6.21, end: 6.7 },
    { word: 'que', start: 6.71, end: 6.9 },
    { word: 'la', start: 6.91, end: 7.1 },
    { word: 'tour', start: 7.11, end: 7.5 },
    { word: 'rouille', start: 7.51, end: 8.1 },
    { word: 'Il', start: 8.2, end: 8.4 },
    { word: 'encaisse', start: 8.41, end: 8.9 },
    { word: 'le', start: 8.91, end: 9.1 },
    { word: 'chèque', start: 9.11, end: 9.7 },
    { word: 'et', start: 9.71, end: 9.9 },
    { word: 'fuit', start: 9.91, end: 10.4 },
    { word: 'en', start: 10.41, end: 10.6 },
    { word: 'train', start: 10.61, end: 11.2 },
  ],
};

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition<any, VideoProps>
        id="ShortVideo"
        component={MainComposition}
        durationInFrames={defaultProps.totalDurationInFrames}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultProps}
        calculateMetadata={async ({ props }) => {
          return {
            durationInFrames: props.totalDurationInFrames || defaultProps.totalDurationInFrames,
            fps: props.fps || 30,
            width: 1080,
            height: 1920,
            props,
          };
        }}
      />
    </>
  );
};
