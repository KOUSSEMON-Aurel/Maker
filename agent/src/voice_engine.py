import asyncio
import os
import re
from typing import List, Dict, Any

DEFAULT_VOICE = "fr-FR-VivienneMultilingualNeural"
MALE_VOICE = "fr-FR-HenriNeural"

async def generate_voice_and_timestamps(
    text: str,
    output_audio_path: str,
    voice: str = DEFAULT_VOICE,
    rate: str = "+5%"
) -> List[Dict[str, Any]]:
    """
    Génère la voix-off via Edge-TTS et extrait les timestamps des phrases et mots.
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

    # Vérifier si on a reçu des WordBoundary ou des SentenceBoundary
    word_events = [b for b in boundaries if b["type"] == "WordBoundary"]

    if word_events:
        for chunk in word_events:
            w = chunk.get("text", "").strip()
            if w:
                start_sec = round(chunk["offset"] / 10_000_000, 3)
                end_sec = round((chunk["offset"] + chunk["duration"]) / 10_000_000, 3)
                captions.append({"word": w, "start": start_sec, "end": end_sec})
    else:
        # Interpolation intelligente des mots dans chaque phrase
        sentence_events = [b for b in boundaries if b["type"] == "SentenceBoundary"]
        for s_chunk in sentence_events:
            sentence_text = s_chunk.get("text", "").strip()
            if not sentence_text:
                continue
            
            s_start = s_chunk["offset"] / 10_000_000
            s_duration = s_chunk["duration"] / 10_000_000
            
            # Découper en mots
            raw_words = re.findall(r"\S+", sentence_text)
            if not raw_words:
                continue
            
            # Poids par longueur de mot (pour un timing réaliste)
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

def synthesize(text: str, output_path: str, voice: str = DEFAULT_VOICE) -> List[Dict[str, Any]]:
    return asyncio.run(generate_voice_and_timestamps(text, output_path, voice))
