import os
import requests

PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY", "")

def fetch_broll_clip(query: str, output_dir: str = "/home/aurel/CODE/Maker/engine/public/broll") -> str:
    """
    Recherche et télécharge un extrait vidéo HD vertical sur Pexels.
    Retourne le chemin relatif pour Remotion (ex: 'broll/clip_xxx.mp4')
    ou une chaîne vide en cas de repli procédural.
    """
    if not PEXELS_API_KEY or not query:
        return ""

    os.makedirs(output_dir, exist_ok=True)
    clean_name = "".join(c for c in query.lower() if c.isalnum() or c == "_")[:20]
    out_file = f"broll_{clean_name}.mp4"
    dest_path = os.path.join(output_dir, out_file)

    if os.path.exists(dest_path):
        return f"broll/{out_file}"

    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/videos/search?query={requests.utils.quote(query)}&orientation=portrait&per_page=1"

    try:
        resp = requests.get(url, headers=headers, timeout=8)
        if resp.status_code == 200:
            data = resp.json()
            videos = data.get("videos", [])
            if videos:
                files = videos[0].get("video_files", [])
                # Préférer un fichier HD vertical
                chosen = next((f for f in files if f.get("width", 0) <= 1080 and f.get("quality") == "hd"), files[0])
                video_url = chosen.get("link")
                if video_url:
                    v_data = requests.get(video_url, timeout=15).content
                    with open(dest_path, "wb") as f:
                        f.write(v_data)
                    return f"broll/{out_file}"
    except Exception as e:
        print(f"[broll_fetcher] Erreur lors de la récupération Pexels ({query}): {e}")

    return ""
