import json
import os
import subprocess
import sys
from typing import Dict, Any

# Ensure agent/src is in path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from voice_engine import synthesize
from broll_fetcher import fetch_broll_clip
from script_generator import generate_sample_script

MAKER_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
ENGINE_DIR = os.path.join(MAKER_ROOT, "engine")
OUTPUT_DIR = os.path.join(MAKER_ROOT, "outputs")

def run_pipeline(script_data: Dict[str, Any] = None, output_filename: str = "final_short.mp4"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if script_data is None:
        script_data = generate_sample_script()

    print("🚀 [1/5] Préparation du script...")
    title = script_data.get("title", "Vidéo Maker")
    theme = script_data.get("theme", "punchy_creator")
    music_mood = script_data.get("musicMood", "suspense_dark")
    scenes = script_data.get("scenes", [])

    full_text = " ".join(s["voiceText"] for s in scenes)
    voice_audio_filename = "generated_voice.mp3"
    voice_audio_path = os.path.join(ENGINE_DIR, "public", voice_audio_filename)

    print(f"🎙️ [2/5] Synthèse vocale naturelle & calcul des timestamps...")
    try:
        captions = synthesize(full_text, voice_audio_path)
    except Exception as e:
        print(f"⚠️ Erreur edge-tts ({e})")
        captions = []

    fps = 30
    if captions:
        total_audio_seconds = captions[-1]["end"] + 0.8
    else:
        total_audio_seconds = 18.0
    total_frames = max(180, int(total_audio_seconds * fps))

    print(f"🎬 [3/5] Traitement des scènes & intégration des médias authentiques...")
    processed_scenes = []
    current_frame = 0
    frames_per_scene = total_frames // max(1, len(scenes))

    for i, sc in enumerate(scenes):
        broll_url = sc.get("brollUrl", "")
        if not broll_url:
            query = sc.get("brollQuery", "")
            broll_url = fetch_broll_clip(query) if query else ""
        
        duration = frames_per_scene if i < len(scenes) - 1 else (total_frames - current_frame)
        
        processed_scenes.append({
            "sceneId": sc.get("sceneId", i + 1),
            "voiceText": sc.get("voiceText", ""),
            "avatarVisible": sc.get("avatarVisible", True),
            "avatarPose": sc.get("avatarPose", "idle_neutral"),
            "brollUrl": broll_url,
            "highlightWord": sc.get("highlightWord", ""),
            "sfxTrigger": sc.get("sfxTrigger", "soft_pop"),
            "startFrame": current_frame,
            "durationInFrames": duration
        })
        current_frame += duration

    music_track = f"music/{music_mood}/track_01.mp3"

    props = {
        "theme": theme,
        "title": title,
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
    print(f"📝 Props générées dans {props_path} ({len(captions)} mots horodatés)")

    raw_output_path = os.path.join(OUTPUT_DIR, f"raw_{output_filename}")
    final_output_path = os.path.join(OUTPUT_DIR, output_filename)

    print(f"🎥 [4/5] Rendu Remotion en cours ({total_frames} frames)...")
    cmd = [
        "npx", "remotion", "render", "ShortVideo", raw_output_path,
        f"--props={props_path}"
    ]
    subprocess.run(cmd, cwd=ENGINE_DIR, check=True)

    print(f"🎚️ [5/5] Normalisation sonore finale à -14 LUFS...")
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
