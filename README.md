# 🎬 Maker : Autonomous Short Video Factory

Pipeline autonome de création et publication de vidéos courtes (YouTube Shorts, TikTok, Instagram Reels) basé sur **Remotion**, synthèse vocale ultra-naturelle et orchestration agentique.

---

## 🚀 Architecture

```text
Maker/
├── engine/              # Moteur de rendu vidéo en code (React, TypeScript, Remotion)
│   ├── src/
│   │   ├── components/  # Sous-titres dynamiques, Avatar 10 poses, B-roll, Audio ducking
│   │   ├── themes/      # 4 chartes visuelles (Dark Tech, Punchy, Swiss, Vintage)
│   │   ├── Root.tsx
│   │   └── Composition.tsx
│   └── public/          # Poses d'avatars, SFX, musiques par mood
│
├── agent/               # Cerveau de l'automatisation (Python)
│   ├── src/
│   │   ├── voice_engine.py   # Génération vocale naturelle gratuite
│   │   ├── broll_fetcher.py  # Téléchargement médias d'illustration
│   │   └── orchestrator.py   # Script maître (assemble props.json & lance Remotion)
│   └── requirements.txt
│
└── video_automation_guide.md # Guide de référence et spécifications complètes
```

---

## ⚡ Démarrage Rapide

### 1. Prérequis
* Node.js >= 18
* Python >= 3.10
* FFmpeg

### 2. Installation du moteur Remotion
```bash
cd engine
npm install
npm run preview     # Ouvre le Remotion Studio dans le navigateur
```

### 3. Lancer un rendu de test
```bash
npx remotion render Root ShortVideo output.mp4 --props="./sample_props.json"
```
