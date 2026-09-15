import json
import os
import subprocess
import sys
from typing import Dict, Any

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from voice_engine import synthesize_multivoice_scenes
from broll_fetcher import fetch_broll_clip
from script_generator import generate_sample_script

MAKER_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
ENGINE_DIR = os.path.join(MAKER_ROOT, "engine")
OUTPUT_DIR = os.path.join(MAKER_ROOT, "outputs")

def run_pipeline(script_data: Dict[str, Any] = None, output_filename: str = "final_short.mp4"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if script_data is None:
        script_data = generate_sample_script()

    print("🚀 [1/5] Préparation du script & configuration...")
    title = script_data.get("title", "Vidéo Maker")
    theme = script_data.get("theme", "punchy_creator")
    music_mood = script_data.get("musicMood", "suspense_dark")
    scenes = script_data.get("scenes", [])
    fps = 30

    voice_audio_filename = "generated_voice.mp3"
    voice_audio_path = os.path.join(ENGINE_DIR, "public", voice_audio_filename)
    temp_voice_dir = os.path.join(MAKER_ROOT, "outputs", "temp_voice")

    print(f"🎙️ [2/5] Synthèse multi-voix par scène (Henri & Remy) & calcul des timestamps...")
    voice_result = synthesize_multivoice_scenes(scenes, voice_audio_path, temp_voice_dir)
    captions = voice_result["captions"]
    updated_scenes = voice_result["scenes"]
    total_audio_seconds = voice_result["totalAudioSeconds"]

    print(f"🎬 [3/5] Synchronisation précise des scènes & intégration des B-rolls...")
    processed_scenes = []
    current_frame = 0

    for i, sc in enumerate(updated_scenes):
        broll_url = sc.get("brollUrl", "")
        if not broll_url:
            query = sc.get("brollQuery", "")
            broll_url = fetch_broll_clip(query) if query else ""
        
        audio_dur = sc.get("audioDurationSeconds", 4.0)
        scene_frames = max(30, int(round(audio_dur * fps)))
        
        processed_scenes.append({
            "sceneId": sc.get("sceneId", i + 1),
            "voiceText": sc.get("voiceText", ""),
            "avatarVisible": sc.get("avatarVisible", True),
            "avatarPose": sc.get("avatarPose", "idle_neutral"),
            "brollUrl": broll_url,
            "highlightWord": sc.get("highlightWord", ""),
            "sfxTrigger": sc.get("sfxTrigger", "soft_pop"),
            "startFrame": current_frame,
            "durationInFrames": scene_frames
        })
        current_frame += scene_frames

    total_frames = current_frame

    music_track = f"music/{music_mood}/track_01.mp3"

    props = {
        "theme": theme,
        "title": title,
        "avatarGender": script_data.get("avatarGender", "male"),
        "voiceAudioUrl": voice_audio_filename,
        "musicTrackUrl": music_track,
        "totalDurationInFrames": total_frames,
        "fps": fps,
        "scenes": processed_scenes,
        "captions": captions
    }

    props_path = os.path.join(ENGINE_DIR, "props.json")
    with open(props_path, "w", encoding="utf-8") as f:
        json.dump(props, f, indent=2, ensure_ascii=False)
    print(f"📝 Props générées ({total_frames} frames, {len(captions)} mots horodatés)")

    raw_output_path = os.path.join(OUTPUT_DIR, f"raw_{output_filename}")
    final_output_path = os.path.join(OUTPUT_DIR, output_filename)

    print(f"🎥 [4/5] Rendu Remotion 1080x1920 @ 30fps ({total_frames} frames)...")
    cmd = [
        "npx", "remotion", "render", "ShortVideo", raw_output_path,
        f"--props={props_path}"
    ]
    subprocess.run(cmd, cwd=ENGINE_DIR, check=True)

    print(f"🎚️ [5/5] Normalisation sonore finale à -14 LUFS (EBU R128)...")
    master_cmd = [
        "ffmpeg", "-y", "-i", raw_output_path,
        "-af", "loudnorm=I=-14:LRA=7:TP=-1.5",
        "-c:v", "copy",
        final_output_path
    ]
    subprocess.run(master_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(raw_output_path):
        os.remove(raw_output_path)

    print(f"\n✅ Vidéo terminée avec succès : {final_output_path}")
    return final_output_path

if __name__ == "__main__":
    run_pipeline()
