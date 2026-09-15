import asyncio
import os
import re
import subprocess
from typing import List, Dict, Any

VOICE_PRESETS = {
    "male_creator": "fr-FR-HenriNeural",             # Énergique, percutant, créateur YouTube/TikTok
    "male_narrator": "fr-FR-RemyMultilingualNeural",   # Posé, chaleureux, conteur
    "female_modern": "fr-FR-VivienneMultilingualNeural", # Moderne, claire
    "female_calm": "fr-FR-DeniseNeural",             # Calme, journalistique
}

DEFAULT_VOICE = VOICE_PRESETS["male_creator"]

async def generate_single_audio(
    text: str,
    output_audio_path: str,
    voice: str = DEFAULT_VOICE,
    rate: str = "+4%"
) -> List[Dict[str, Any]]:
    """
    Génère l'audio d'une phrase/scène via Edge-TTS et extrait les timestamps des mots.
    """
    import edge_tts

    dir_name = os.path.dirname(output_audio_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    communicate = edge_tts.Communicate(text, voice=voice, rate=rate)
    boundaries = []

    with open(output_audio_path, "wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] in ("SentenceBoundary", "WordBoundary"):
                boundaries.append(chunk)

    captions: List[Dict[str, Any]] = []
    word_events = [b for b in boundaries if b["type"] == "WordBoundary"]

    if word_events:
        for chunk in word_events:
            w = chunk.get("text", "").strip()
            if w:
                start_sec = round(chunk["offset"] / 10_000_000, 3)
                end_sec = round((chunk["offset"] + chunk["duration"]) / 10_000_000, 3)
                captions.append({"word": w, "start": start_sec, "end": end_sec})
    else:
        sentence_events = [b for b in boundaries if b["type"] == "SentenceBoundary"]
        for s_chunk in sentence_events:
            sentence_text = s_chunk.get("text", "").strip()
            if not sentence_text:
                continue
            s_start = s_chunk["offset"] / 10_000_000
            s_duration = s_chunk["duration"] / 10_000_000

            raw_words = re.findall(r"\S+", sentence_text)
            if not raw_words:
                continue

            weights = [max(1, len(w)) for w in raw_words]
            total_weight = sum(weights)

            cur_time = s_start
            for w, weight in zip(raw_words, weights):
                w_dur = (weight / total_weight) * s_duration
                captions.append({
                    "word": w,
                    "start": round(cur_time, 3),
                    "end": round(cur_time + w_dur, 3)
                })
                cur_time += w_dur

    return captions

def get_audio_duration(file_path: str) -> float:
    """Retourne la durée exacte en secondes d'un fichier audio via ffprobe."""
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(res.stdout.strip())
    except Exception:
        return 4.0

def synthesize_multivoice_scenes(
    scenes: List[Dict[str, Any]],
    output_audio_path: str,
    temp_dir: str
) -> Dict[str, Any]:
    """
    Synthétise chaque scène avec sa voix attitrée, concatène les audios,
    calcule les timestamps absolus et met à jour les durées exactes par scène.
    """
    os.makedirs(temp_dir, exist_ok=True)
    scene_audio_files = []
    all_captions: List[Dict[str, Any]] = []
    
    current_time_offset = 0.0
    updated_scenes = []

    for i, scene in enumerate(scenes):
        voice_key = scene.get("voice", "male_creator")
        voice = VOICE_PRESETS.get(voice_key, voice_key)
        voice_text = scene.get("voiceText", "")
        
        scene_audio_filename = f"scene_{i+1}.mp3"
        scene_audio_path = os.path.join(temp_dir, scene_audio_filename)
        
        # Synthèse
        caps = asyncio.run(generate_single_audio(voice_text, scene_audio_path, voice=voice))
        actual_duration = get_audio_duration(scene_audio_path)
        
        # Ajuster timestamps avec l'offset actuel
        for c in caps:
            all_captions.append({
                "word": c["word"],
                "start": round(c["start"] + current_time_offset, 3),
                "end": round(c["end"] + current_time_offset, 3)
            })

        # Pause respiratoire de 0.35s entre scènes pour un rythme naturel
        pause_duration = 0.35 if i < len(scenes) - 1 else 0.5
        scene_total_duration = actual_duration + pause_duration
        
        scene_copy = dict(scene)
        scene_copy["audioDurationSeconds"] = round(scene_total_duration, 3)
        updated_scenes.append(scene_copy)
        
        scene_audio_files.append((scene_audio_path, pause_duration))
        current_time_offset += scene_total_duration

    # Concaténation propre avec FFmpeg en ajoutant de légers silences entre répliques
    filter_complex = ""
    inputs = []
    for idx, (aud_path, pause) in enumerate(scene_audio_files):
        inputs.extend(["-i", aud_path])
        filter_complex += f"[{idx}:a]apad=pad_dur={pause}[a{idx}];"
    
    concat_inputs = "".join(f"[a{i}]" for i in range(len(scene_audio_files)))
    filter_complex += f"{concat_inputs}concat=n={len(scene_audio_files)}:v=0:a=1[outa]"
    
    concat_cmd = ["ffmpeg", "-y"] + inputs + [
        "-filter_complex", filter_complex,
        "-map", "[outa]",
        "-ac", "2",
        output_audio_path
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    total_duration = get_audio_duration(output_audio_path)

    return {
        "captions": all_captions,
        "scenes": updated_scenes,
        "totalAudioSeconds": total_duration
    }

def synthesize(text: str, output_path: str, voice: str = DEFAULT_VOICE) -> List[Dict[str, Any]]:
    return asyncio.run(generate_single_audio(text, output_path, voice))
