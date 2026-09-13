import urllib.request
import os

os.makedirs('/home/aurel/CODE/Maker/engine/public/broll', exist_ok=True)

# Authentic, 100% Real Historical Public Domain Assets
real_assets = {
    "broll_eiffel.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Eiffel_Tower%2C_full-view_looking_toward_the_Trocadero%2C_Exposition_Universal%2C_1900%2C_Paris%2C_France.jpg/800px-Eiffel_Tower%2C_full-view_looking_toward_the_Trocadero%2C_Exposition_Universal%2C_1900%2C_Paris%2C_France.jpg",
    "broll_lustig.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Victor_Lustig_DOJ_BOI_%28FBI%29_identification%2C_1931.jpg/800px-Victor_Lustig_DOJ_BOI_%28FBI%29_identification%2C_1931.jpg",
    "broll_francs.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/French_franc_last_series_banknotes.png/800px-French_franc_last_series_banknotes.png",
    "broll_train.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Parovoz_YI_%282%29.jpg/800px-Parovoz_YI_%282%29.jpg"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) MakerBot/1.0'}

for filename, url in real_assets.items():
    dest = f"/home/aurel/CODE/Maker/engine/public/broll/{filename}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded real photo: {filename} ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
