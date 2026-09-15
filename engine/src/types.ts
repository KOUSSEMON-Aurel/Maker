export type ThemeName = 'dark_tech' | 'punchy_creator' | 'minimalist_swiss' | 'vintage_archive';

export type AvatarPose =
  | 'idle_neutral'
  | 'shocked_jawdrop'
  | 'explaining_point'
  | 'laughing_joke'
  | 'skeptical_sideeye'
  | 'facepalm'
  | 'secret_whisper'
  | 'angry_triggered'
  | 'hyped_victory'
  | 'thinking_chin';

export interface Scene {
  sceneId: number;
  voiceText: string;
  avatarVisible?: boolean;
  avatarPose?: AvatarPose;
  visualFocus?: 'title_card' | 'center_card' | 'newspaper_zoom' | 'split_broll' | 'fullscreen_broll';
  brollUrl?: string;
  brollQuery?: string;
  highlightWord?: string;
  sfxTrigger?: 'sub_bass_hit' | 'soft_pop' | 'whoosh' | 'paper_slide';
  startFrame: number;
  durationInFrames: number;
}

export interface CaptionWord {
  word: string;
  start: number; // in seconds
  end: number;   // in seconds
}

export type AvatarGender = 'male' | 'female';

export interface VideoProps {
  theme: ThemeName;
  title: string;
  avatarGender?: AvatarGender;
  voiceAudioUrl: string;       // path to voice audio file
  musicTrackUrl?: string;      // path to background music
  totalDurationInFrames: number;
  fps: number;
  scenes: Scene[];
  captions: CaptionWord[];
}
