import json
import os
from typing import Dict, Any

def generate_sample_script(topic: str = "Victor Lustig") -> Dict[str, Any]:
    """
    Script de démonstration prêt à l'emploi avec boucle infinie,
    humour percutant et vraies photographies historiques d'archives.
    """
    return {
        "theme": "punchy_creator",
        "title": "Ce gars a vendu la Tour Eiffel...",
        "musicMood": "suspense_dark",
        "scenes": [
            {
                "sceneId": 1,
                "voiceText": "Ce gars a accidentellement vendu la Tour Eiffel deux fois de suite.",
                "avatarVisible": True,
                "avatarPose": "shocked_jawdrop",
                "brollUrl": "broll/broll_eiffel.jpg",
                "highlightWord": "vendu",
                "sfxTrigger": "sub_bass_hit"
            },
            {
                "sceneId": 2,
                "voiceText": "En 1925, Victor Lustig lit dans le journal que la tour rouille et coûte une fortune à réparer.",
                "avatarVisible": False,
                "avatarPose": "idle_neutral",
                "brollUrl": "broll/broll_lustig.jpg",
                "highlightWord": "1925",
                "sfxTrigger": "paper_slide"
            },
            {
                "sceneId": 3,
                "voiceText": "Il s'est dit : et si je la vendais à des ferrailleurs ? Oui, le type n'avait aucun respect.",
                "avatarVisible": True,
                "avatarPose": "laughing_joke",
                "brollUrl": "broll/broll_francs.png",
                "highlightWord": "aucun respect",
                "sfxTrigger": "soft_pop"
            },
            {
                "sceneId": 4,
                "voiceText": "Il a encaissé le gros chèque, fui à Vienne, puis est revenu recommencer. Et voilà comment...",
                "avatarVisible": True,
                "avatarPose": "secret_whisper",
                "brollUrl": "broll/broll_train.jpg",
                "highlightWord": "chèque",
                "sfxTrigger": "whoosh"
            }
        ]
    }
