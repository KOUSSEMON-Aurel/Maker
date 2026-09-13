
# Guide Complet : Automatisation de Vidéos Réseaux Sociaux (Shorts, TikTok, Reels) avec Remotion & Agents IA

Ce document rassemble l'analyse stratégique, le comparatif technique, l'architecture logicielle et les retours d'expérience du web pour concevoir un pipeline de création et de publication de vidéos automatisé, déterministe et de qualité professionnelle.

---

## 1. Philosophie : Pourquoi "Code-as-Video" plutôt que l'IA Générative (Sora, Veo, Runway) ?

L'IA générative de vidéo (text-to-video) souffre de limitations critiques pour l'automatisation de masse :

* **Imprévisibilité & Hallucinations** : Déformations physiques, texte illisible ou déformé, impossibilité de garantir un placement précis au pixel près.
* **Désynchronisation temporelle** : Incapacité d'aligner une animation sur un mot spécifique d'une voix-off.
* **Coût prohibitif** : Plusieurs dizaines de centimes ou dollars par seconde de vidéo générée.
* **Vitesse de rendu** : Plusieurs minutes d'attente par séquence de 5 secondes.

L'approche **Code-as-Video** (programmatique) inverse le paradigme :

1. **Contrôle absolu** : Rendu vectoriel 4K/60fps, typographie nette, respect strict d'une charte graphique.
2. **Synchronisation à la frame près** : Sous-titres dynamiques et transitions calés sur les timestamps exacts de l'audio.
3. **Coût marginal proche de zéro** : Rendu local ou sur serveur CPU standard (quelques centimes d'électricité ou de compute).
4. **Déterminisme** : Le code s'exécute de façon reproductible sans bugs visuels inattendus.

---

## 2. Comparatif des Technologies & Choix Stratégique

Pour une chaîne aux **thématiques ultra-diversifiées** (actualités, tech, culture générale, pop-culture, faits insolites, histoire, storytelling), voici l'évaluation des trois technologies envisagées :

| Critère                              | Remotion (React/TypeScript)                                     | Manim (Python)                                  | Hyperframes                             |
| :------------------------------------ | :-------------------------------------------------------------- | :---------------------------------------------- | :-------------------------------------- |
| **Cible principale**            | Réseaux sociaux, SaaS, créateurs                              | Mathématiques, physique, science               | Animations web déclaratives            |
| **Maturité & Écosystème**    | **Excellente** (communauté massive, plugins officiels)   | Très bonne (communauté académique)           | Faible (projet récent et confidentiel) |
| **Polyvalence des formats**     | **Totale** (CSS, Tailwind, Lottie, SVG, Three.js, Canvas) | Restreinte (graphes, courbes, formules LaTeX)   | Moyenne                                 |
| **Gestion Audio & Sous-titres** | Native (`@remotion/captions`, pitch, audio ducking)           | Complexe (nécessite MoviePy ou FFmpeg externe) | Manuelle                                |
| **Prévisualisation en direct** | **Oui** (`@remotion/player` dans le navigateur)         | Non (rendu frame par frame)                     | Partielle                               |

> **Choix validé : REMOTION.**
> Remotion s'appuie sur l'écosystème web standard. Tout ce qui est réalisable sur une page web moderne peut être converti en vidéo HD/4K à 60 images par seconde.

---

## 3. Retours d'Expérience du Web & Projets Réels en Production

L'analyse de projets open-source et de créateurs tournant en production révèle des précédents concrets :

* **DevByte Engine V2** : Scrape Hacker News, GitHub Releases et blogs tech, filtre via un éditeur IA, génère la voix-off et compile des Shorts verticaux au style "SaaS premium" avec Remotion.
* **Hermes Video Pipeline** : Pipeline automatisé pour la chaîne éducative *Tertiary Courses*, piloté par un agent autonome avec rendu vectoriel et vérification QA par ledger d'audit.
* **Auto-Shorts** : Générateur quotidien basé sur Remotion, AssemblyAI et l'API NASA APOD, avec téléversement automatique sur YouTube.
* **MoneyPrinterTurbo / ShortGPT** : Projets généralistes majeurs démontrant l'intérêt massif pour ces architectures.

---

## 4. Les 5 Pièges Majeurs et Leurs Solutions "100 % Qualité"

| Défaut constaté chez les amateurs                  | Conséquence                                                    | Solution d'ingénierie appliquée                                                                                                                                            |
| :--------------------------------------------------- | :-------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Contenu générique ("Slop" / Brainrot)** | Shadowban, 0 vue, refus de monétisation pour "Reused Content". | Charte visuelle distinctive (layouts originaux, animations spring, typographies premium type*Cabinet Grotesk* ou *Inter*).                                               |
| **2. Drift temporel (Désynchronisation)**     | Sous-titres en retard ou en avance sur la parole.               | **L'audio pilote la vidéo** : extraction des timestamps mot-à-mot via Whisper/ElevenLabs avant de calculer la durée exacte en frames (`fps * audioDuration`).     |
| **3. Hallucination de code par l'IA**          | Crashs fréquents de rendu (erreurs de syntaxe JSX/CSS).        | **Découplage strict Code / Données** : le code React est figé et modulaire. L'agent IA ne génère qu'un objet JSON validé par un schéma strict (Pydantic / Zod). |
| **4. Mauvais mixage sonore**                   | Voix étouffée par la musique ou saturée.                     | *Audio Ducking* automatique (baisse de -18 dB de la musique sous la voix) et normalisation sonore à -14 LUFS (norme YouTube).                                             |
| **5. Dépassement des quotas d'API**           | Blocage des uploads (YouTube limite à ~6 uploads/jour/projet). | Rythme maîtrisé (1 à 2 vidéos/jour), système de ledger d'audit (`publication-ledger.json`) pour éviter tout doublon en cas de reprise sur incident.                  |

---

## 5. Architecture Complète du Pipeline Agentique (De A à Z)

Le système se compose de 6 étapes séquentielles indépendantes :

```
[1. Veille & Idéation]
         │ (Topic validé)
         ▼
[2. Scénariste & Storyboarder (LLM)]
         │ (JSON strict : hook, scènes, métadonnées, layout)
         ▼
[3. Audio & Alignement Temporel]
         │ (Fichier voix.mp3 + Timestamps mot-à-mot)
         ▼
[4. Moteur Visuel Remotion]
         │ (Injection des props JSON -> Rendu MP4 1080x1920)
         ▼
[5. Contrôle Qualité (QA)]
         │ (Vérification durée, LUFS, intégrité du fichier)
         ▼
[6. Publication & Suivi]
         │ (YouTube Data API v3 / TikTok API)
         ▼
   [Base / Ledger]
```

### Le Contrat de Données (`props.json`)

L'agent IA produit un JSON structuré qui alimente directement Remotion :

```json
{
  "videoId": "short_2026_09_13_001",
  "title": "La découverte qui réécrit l'histoire",
  "layoutType": "social_card",
  "musicMood": "dark_suspense",
  "scenes": [
    {
      "id": 1,
      "text": "Cette cité engloutie sous la Méditerranée n'aurait jamais dû exister.",
      "highlightWords": ["engloutie", "Méditerranée"],
      "brollQuery": "ancient underwater ruins",
      "visualFocus": "center_card"
    },
    {
      "id": 2,
      "text": "Les archéologues y ont trouvé un mécanisme en bronze vieux de 2000 ans.",
      "highlightWords": ["mécanisme", "2000 ans"],
      "brollQuery": "ancient mechanism bronze artifact",
      "visualFocus": "split_screen"
    }
  ],
  "captions": [
    {"word": "Cette", "start": 0.05, "end": 0.28},
    {"word": "cité", "start": 0.29, "end": 0.62},
    {"word": "engloutie", "start": 0.65, "end": 1.15}
  ]
}
```

---

## 6. Stratégie Voix IA & Sous-Titres : Le Combo 100 % Gratuit & Indétectable

Pour obtenir une voix humaine sans défaut (respirations, intonations dynamiques, zéro voix robotique) sans payer d'abonnement, l'architecture s'appuie sur le découplage entre la **synthèse vocale** et l'**alignement temporel**.

### A. Synthèse Vocale (TTS) : Options 100 % Gratuites

| Solution                              | Type                                         | Vitesse & Poids             | Réalisme (Français)                         | Utilisation recommandée                                                                               |
| :------------------------------------ | :------------------------------------------- | :-------------------------- | :-------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| **Kokoro-82M (Local)**          | Open Source (CPU/GPU)                        | ~300 Mo / < 1s sur CPU      | **8.5/10** (Moderne, expressif)         | **Recommandé par défaut.** Zéro dépendance externe, pas de quota.                            |
| **Kokoro-82M (Cloud API)**      | Hugging Face Spaces (`hexgrad/Kokoro-TTS`) | API Cloud sans calcul local | **8.5/10** (Identique au local)         | Idéal si l'on ne souhaite installer aucun paquet lourd sur la machine.                                |
| **Edge-TTS (Microsoft)**        | API directe gratuite illimitée              | Instantané / 0 Mo          | **7/10** (Voix média / présentateur)  | **Secours automatique.** Fiabilité 100 %, sans clé API (`fr-FR-VivienneMultilingualNeural`). |
| **ElevenLabs (Palier Gratuit)** | Cloud officiel                               | 1s par requête             | **10/10** (Indétectable, respirations) | 10 000 car/mois offerts =**10 à 12 Shorts 100 % parfaits par mois**.                            |

#### Code Python type : Génération vocale avec Kokoro

```python
from kokoro import KPipeline
import soundfile as sf

# Initialisation du pipeline français
pipeline = KPipeline(lang_code='f')
generator = pipeline("Cette cité engloutie n'aurait jamais dû exister.", voice='ff_siwis', speed=1.0)

for i, (gs, ps, audio) in enumerate(generator):
    sf.write(f"voice_scene_{i}.wav", audio, 24000)
```

---

### B. Sous-Titres & Timestamps Mot-à-Mot : Groq Whisper API (Gratuit)

Pour caler les sous-titres au mot près dans Remotion sans surcharger le processeur de la machine :

* **Groq Cloud API** met à disposition le modèle **Whisper-Large-v3** avec un palier gratuit généreux (plusieurs milliers de requêtes par jour).
* **Vitesse d'inférence** : Un audio de 45 secondes est transcrit en **~0,3 seconde**, avec le timestamp de début et de fin de chaque mot (`word_timestamps=True`).

#### Format de sortie injecté directement dans `props.json` :

```json
"captions": [
  {"word": "Cette", "start": 0.04, "end": 0.26},
  {"word": "cité", "start": 0.28, "end": 0.61},
  {"word": "engloutie", "start": 0.63, "end": 1.12}
]
```

Dans Remotion, le composant `<Captions />` lit ce tableau et allume dynamiquement chaque mot en synchronisation absolue avec l'onde sonore.

---

## 7. Stratégie Audio : Musique de Fond & Effets Sonores (SFX) 100 % Légaux et Dynamiques

Pour maximiser la rétention sur TikTok et YouTube Shorts sans tomber dans le piège de l'audio "agressif, répétitif ou amateur" qui fait fuir l'audience après 5 secondes, l'environnement sonore doit être riche, varié et maîtrisé au décibel près.

---

### A. La Musique de Fond : La "Music Vault" Hybride (Combinaison Risque Zéro)

Pour combiner l'immunité juridique totale sur YouTube et la liberté commerciale sur TikTok/Reels, le système s'appuie sur une **bibliothèque locale de morceaux pré-validés**, organisée par atmosphères narratives (*Moods*) :

1. **Source 1 : YouTube Audio Library (Filtre "Attribution non requise")** :
   * Immunité absolue contre le Content ID sur YouTube. Zéro risque de démonétisation ou de réclamation.
2. **Source 2 : Creative Commons 0 (CC0) / Domaine Public (Free Music Archive, Incompetech CC0, Musopen)** :
   * Fichiers libres de tout droit patrimonial mondial, utilisables sans restriction sur TikTok, Instagram et YouTube.

#### Architecture de la Music Vault locale (`engine/public/music/`) :
```text
music/
├── suspense_dark/   # 3 à 4 boucles de 60s (ambiance mystère, tension)
├── tech_future/     # 3 à 4 boucles (synthwave subtile, data, IA)
├── epic_cinematic/  # 3 à 4 boucles (histoire, grandes découvertes)
├── lofi_curious/    # 3 à 4 boucles (faits insolites, culture générale)
└── upbeat_pulse/    # 3 à 4 boucles (actualités rapides, business)
```

> **Anti-répétition** : L'agent IA indique le mood dans son JSON (`"musicMood": "suspense_dark"`). Le moteur vidéo tire au sort l'un des morceaux du dossier pour ne jamais réutiliser la même musique deux vidéos d'affilée.

---

### B. Les Effets Sonores (SFX) : Le Système Anti-Redondance & Psychoacoustique

L'erreur numéro 1 des chaînes automatisées est d'utiliser le **même "whoosh" agressif et le même "pop" suraigu** toutes les 2 secondes. Le spectateur ressent une fatigue auditive immédiate et scrolle.

Pour un rendu professionnel digne d'un monteur chevronné :

#### 1. Le principe des "Audio Pools" (Variations aléatoires)
Chaque événement visuel est associé à un panier de 3 à 5 variations légères. Remotion pioche aléatoirement dans le panier :
* `sfx/whoosh/soft_01.mp3`, `soft_02.mp3`, `air_03.mp3`
* `sfx/pop/wooden_pop_01.mp3`, `bubble_soft_02.mp3`, `tap_03.mp3`

#### 2. SFX Contextuels et Signifiants (Pas de bruitage gratuit)
Le son doit souligner le sens de ce qui est montré à l'écran :

| Famille visuelle | Type de son appliqué | Fréquence / Caractéristique |
| :--- | :--- | :--- |
| **Hook / Enjeu dramatique** | *Sub-bass hit* ou *Riser* étouffé | Fréquence basse (< 100 Hz), non agressive mais percutante. |
| **Apparition de mots-clés / Badges** | *Soft Pop* ou *Tactile Tap* | Son feutré (bois ou verre dépoli), très court (< 150 ms). |
| **Changement de scène / Slide** | *Air Swoop* ou *Paper Slide* | Balayage d'air organique sans distorsion dans les aigus. |
| **Données chiffrées / Infographie** | *Counter Tick* ou *Digital Click* | Micro-bruitage mécanique discret pour rythmer la montée du chiffre. |

#### 3. Règle du Silence et du Pacing
* **Ne jamais bruiter chaque mot ni chaque seconde**.
* On applique un **seuil d'espacement minimal** : au moins 3 à 4 secondes entre deux SFX. Les moments d'explication verbale doivent rester épurés pour que les SFX clés conservent leur impact.

#### 4. Sources SFX 100 % Domaine Public (CC0)
* **Kenney.nl (UI Audio & Impact Packs)** : Des centaines de sons d'interface, pops et taps en **CC0 pur (domaine public)**, zéro attribution nécessaire.
* **Sonniss GDC Audio Archives** : Bibliothèque massive d'effets sonores professionnels sous licence commerciale gratuite.
* **Freesound.org** : Sons uniques avec filtre strict `license:"Creative Commons 0"`.

---

### C. Le Mixage Sonore : Audio Ducking Fluide dans Remotion

Pour que la musique sublime la voix sans jamais l'étouffer, on utilise la fonction `interpolate()` de Remotion pour adoucir les transitions sonores (pas de coupure brute) :

```tsx
import { Audio, interpolate, staticFile, useCurrentFrame } from 'remotion';

export const AudioManager = ({ 
  musicTrack, 
  voiceSpeakingTimestamps 
}: { 
  musicTrack: string; 
  voiceSpeakingTimestamps: { startFrame: number; endFrame: number }[] 
}) => {
  const frame = useCurrentFrame();

  // Détection si la voix parle sur la frame actuelle
  const isSpeaking = voiceSpeakingTimestamps.some(
    (span) => frame >= span.startFrame && frame <= span.endFrame
  );

  // Transition douce du volume (sur 8 frames) : 7% quand la voix parle, 22% pendant les silences
  const musicVolume = interpolate(
    isSpeaking ? 1 : 0,
    [0, 1],
    [0.22, 0.07],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  return (
    <>
      <Audio src={staticFile(`music/${musicTrack}`)} volume={musicVolume} loop />
    </>
  );
};
```

---

### D. Mastering Final : Normalisation à -14 LUFS (Norme YouTube / TikTok)

Avant l'upload, l'audio de la vidéo est passé dans le filtre de normalisation psychoacoustique de FFmpeg :
```bash
ffmpeg -i input.mp4 -af loudnorm=I=-14:LRA=7:TP=-1.5 -c:v copy output_mastered.mp4
```
* **I=-14 LUFS** : Volume perçu cible officiel des plateformes sociales.
* **TP=-1.5 dB** : Marge de crête pour éviter toute distorsion ou grésillement lors de la recompression par YouTube/TikTok.

---

## 8. L'Avatar 2D Dynamique : Système à 10 Poses & Gestion de Présence

Pour donner une âme reconnaissable à la chaîne sans alourdir le rendu, un système de mascotte 2D vectorielle transparente (style *Trash* ou *Kurzgesagt*) est intégré.

### A. Bibliothèque des 10 Poses Expressives (PNG/SVG transparents)
1. `idle_neutral` : Bras croisés ou le long du corps, regard neutre attentif.
2. `shocked_jawdrop` : Bouche bée, yeux écarquillés (pour les révélations folles).
3. `explaining_point` : Doigt levé vers le texte ou les éléments à l'écran.
4. `laughing_joke` : Rire franc, yeux plissés (pour souligner une vanne ou une ironie).
5. `skeptical_sideeye` : Sourcil haussé, regard de biais (pour les doutes et absurdités).
6. `facepalm` : Main sur le visage (pour les erreurs humaines historiques grotesques).
7. `secret_whisper` : Main près de la bouche (pour révéler un secret ou une théorie taboue).
8. `angry_triggered` : Poing levé, sourcils froncés (pour les arnaques ou injustices).
9. `hyped_victory` : Bras en l'air, grand sourire (pour les accomplissements épiques).
10. `thinking_chin` : Main sous le menton, regard vers le haut (pour poser une énigme).

### B. Gestion Dynamique de la Présence à l'Écran
L'avatar ne doit **jamais être une statue figée**. Dans chaque scène, l'agent contrôle son apparition :
* **`avatarVisible: false` (~60 % du temps)** : Plein écran réservé au B-roll vidéo HD, aux graphiques ou aux cartes d'actu.
* **`avatarVisible: true` (~40 % du temps)** :
  * L'avatar entre avec une animation `spring()` élastique (slide-in depuis le coin inférieur).
  * Il anime une micro-respiration (léger balancement vertical périodique).
  * Il quitte l'écran dès que la scène suivante nécessite une attention visuelle totale sur les médias.

---

## 9. Le Design System Multi-Thèmes (4 Chartes Graphiques)

Pour garantir une identité forte adaptée à des sujets variés sans répétition visuelle :

| Thème | Typographies (Titre / Corps) | Palette de couleurs | Cas d'usage idéal |
| :--- | :--- | :--- | :--- |
| **Dark Tech** | **Clash Display** + **Space Mono** | Fond `#0A0B0E`, Cyan néon `#00F5FF`, Vert `#00FF66` | IA, cybersécurité, science du futur, innovations. |
| **Punchy Creator** | **Montserrat ExtraBold** + **Inter** | Fond `#121212`, Jaune néon `#FFDD00`, Violet `#8B5CF6` | Storytelling insolite, faits divers, anecdotes pop. |
| **Minimalist Swiss** | **Cabinet Grotesk** + **Satoshi** | Fond `#F4F4F0` (clair) ou `#18181B`, Rouge vif `#EF4444` | Business, géopolitique, économie, enquêtes. |
| **Vintage Archive** | **Playfair Display** + **Cinzel** | Fond sépia sombre `#1A1612`, Or vieilli `#F59E0B` | Histoire ancienne, archéologie, guerres, mystères. |

---

## 10. L'Agent Scénariste : Prompt Système Maître & Rétention

Le prompt système force le LLM à respecter une cadence de parole de **130 à 150 mots/minute**, à insérer de l'humour percutant et à verrouiller la **Boucle Infinie (Seamless Loop)** :

```markdown
Tu es le directeur d'écriture d'une chaîne de vulgarisation courte et percutante (style Trash / Kurzgesagt / MrBeast).
Ton objectif est d'écrire un script de Short/TikTok viral de 45 à 55 secondes (130 à 150 mots maximum) sur le sujet suivant :
Sujet : {TOPIC}
Ambiance demandée : {THEME}

RÈGLES D'OR D'ÉCRITURE :
1. LE HOOK (Scène 1) : Démarre immédiatement dans le vif du sujet. BANNIR formellement "Bonjour", "Aujourd'hui on va voir", ou "Saviez-vous que...". Phrase choc, contre-intuitive ou absurde.
2. HUMOUR & RYTHME : Insère au moins une micro-vanne, comparaison imagée ou remarque d'autodérision brisant le 4ème mur. Le ton est vivant et spontané.
3. SEAMLESS LOOP (Boucle Infinie) : La dernière phrase de la dernière scène doit s'achever sur une amorce syntaxique qui s'enchaîne naturellement avec le tout premier mot du Hook de la Scène 1.
4. AVATAR DYNAMIQUE : L'avatar ne doit apparaître (avatarVisible: true avec une pose expressive) que pour ponctuer le hook, une vanne ou une réaction d'étonnement. Pour les explications descriptives, passe avatarVisible à false.
5. FORMAT DE SORTIE STRICT : Réponds UNIQUEMENT avec un JSON valide respectant ce schéma :

{
  "theme": "punchy_creator",
  "musicMood": "suspense_dark",
  "hookOpeningWord": "Ce gars",
  "scenes": [
    {
      "sceneId": 1,
      "voiceText": "Ce gars a accidentellement vendu la Tour Eiffel... deux fois de suite.",
      "avatarVisible": true,
      "avatarPose": "shocked_jawdrop",
      "visualFocus": "title_card",
      "brollQuery": "eiffel tower aerial paris vintage",
      "highlightWord": "vendu",
      "sfxTrigger": "sub_bass_hit"
    },
    {
      "sceneId": 2,
      "voiceText": "En 1925, Victor Lustig lit dans le journal que la tour rouille et coûte une blinde à réparer.",
      "avatarVisible": false,
      "visualFocus": "newspaper_zoom",
      "brollQuery": "old newspaper 1920s reading",
      "highlightWord": "rouille",
      "sfxTrigger": "paper_slide"
    },
    {
      "sceneId": 3,
      "voiceText": "Il s'est dit : et si je la vendais à des ferrailleurs ? Oui, le type n'avait aucun respect.",
      "avatarVisible": true,
      "avatarPose": "laughing_joke",
      "visualFocus": "split_broll",
      "brollQuery": "scrap metal junk yard",
      "highlightWord": "aucun respect",
      "sfxTrigger": "soft_pop"
    },
    {
      "sceneId": 4,
      "voiceText": "Il a encaissé le chèque, fui à Vienne, puis est revenu recommencer. Et voilà comment...",
      "avatarVisible": true,
      "avatarPose": "secret_whisper",
      "visualFocus": "center_card",
      "brollQuery": "steam train 1920s vintage travel",
      "highlightWord": "recommencer",
      "sfxTrigger": "whoosh"
    }
  ]
}
```

---

## 11. Médias d'Arrière-Plan (B-Roll) : Pipeline Multi-Sources 100 % Légal

Pour illustrer chaque scène avec des vidéos et images gratuites, exploitables commercialement et sans droits d'auteur :

1. **Vidéos HD/4K : Pexels Video API (N°1)**
   * Vidéos verticales ou horizontales de haute qualité.
   * Licence Pexels : 100 % gratuite, utilisation commerciale autorisée, aucune attribution obligatoire.
   * L'agent effectue une recherche avec le mot-clé `brollQuery` (ex: `"vintage train"`) et télécharge un extrait optimisé.
2. **Photos & Vecteurs : Pixabay API**
   * Catalogue massif de textures, illustrations transparentes et photos.
3. **Histoire, Science & Célébrités : Wikimedia Commons API**
   * Essentiel pour les tableaux, personnalités historiques réelles (Napoléon, Marie Curie) et événements du 20ème siècle tombés dans le **Domaine Public**.
4. **Secours Procédural (Zéro Écran Noir)** :
   * Si aucune vidéo ne correspond au mot-clé ou en cas de coupure API, Remotion active un fond procédural animé (grille néon en perspective, mesh gradients ou texture de bruit avec particules).

---

## 12. Structure Recommandée du Répertoire Projet

```text
video-automation-engine/
├── agent/                       # Cerveau de l'automatisation (Node.js ou Python)
│   ├── src/
│   │   ├── ideation/           # Scrapers (Trends, Reddit, RSS)
│   │   ├── writer/             # Prompts LLM & validation du schéma JSON
│   │   ├── voice/              # Générateur Kokoro/Edge-TTS & Groq Whisper
│   │   ├── media/              # Fetcher B-Roll (API Pexels / Pixabay / Wikimedia)
│   │   ├── qa/                 # Vérification intégrité, LUFS & boucle infinie
│   │   └── publisher/          # Scripts d'upload (YouTube Data API v3, TikTok)
│   ├── config.json             # Paramètres et clés d'API (Groq, Pexels, etc.)
│   └── orchestrator.py         # Script maître qui enchaîne les étapes
│
├── engine/                      # Moteur de rendu Remotion (React / TypeScript)
│   ├── src/
│   │   ├── components/
│   │   │   ├── Captions.tsx    # Sous-titres dynamiques mot-à-mot (style karaoke)
│   │   │   ├── Avatar.tsx      # Composant Avatar (10 poses, animations spring)
│   │   │   ├── ProgressBar.tsx # Barre de progression discrète en bas d'écran
│   │   │   ├── SocialCard.tsx  # Carte flottante élégante avec ombre douce
│   │   │   ├── AudioManager.tsx# Gestionnaire musique de fond + ducking + SFX
│   │   │   └── BrollLayer.tsx  # Arrière-plan vidéo avec effet Ken Burns & flou
│   │   ├── themes/             # Thèmes graphiques (DarkTech, Punchy, Swiss, Vintage)
│   │   ├── Root.tsx            # Déclaration des compositions Remotion
│   │   └── Composition.tsx     # Composition principale réceptive aux props
│   ├── public/
│   │   ├── avatars/            # 10 poses PNG transparentes de la mascotte
│   │   ├── fonts/              # Typographies locales (Inter, Cabinet Grotesk, Clash Display)
│   │   ├── sfx/                # Banques SFX en Audio Pools (whooshes, pops, taps, hits)
│   │   └── music/              # Music Vault classée par mood (suspense, epic, tech...)
│   ├── package.json
│   └── remotion.config.ts
│
├── storage/
│   ├── temp/                   # Fichiers audio temporaires et frames QA
│   ├── outputs/                # Vidéos MP4 finales prêtes à diffuser
│   └── publication_ledger.json # Historique et traçabilité des vidéos publiées
└── README.md
```

---

## 13. Plan d'Action pour le Déploiement

1. **Phase 1 : Socle Visuel Remotion & Audio Pools**
   * Initialiser le dossier `engine/` avec Remotion.
   * Constituer la *Music Vault* (YouTube Audio Library + CC0) et les dossiers SFX (Kenney CC0).
   * Intégrer les 10 poses de l'Avatar et coder le composant `Avatar.tsx`.
   * Coder le composant `AudioManager.tsx` avec interpolation de ducking fluide.
   * Coder les sous-titres animés (`Captions.tsx`) et le premier layout multi-thèmes.
2. **Phase 2 : Pipeline Voix & Timestamps (100 % Gratuit)**
   * Configurer Kokoro-82M (local ou Hugging Face) avec repli automatique sur Edge-TTS.
   * Connecter Groq Whisper API pour l'extraction instantanée des timestamps mot-à-mot.
   * Connecter la durée de la composition à la durée exacte de l'audio.
3. **Phase 3 : Scénarisation IA Structurée & B-Roll Fetcher**
   * Concevoir le script d'appel LLM avec le prompt maître (Seamless Loop + Humour).
   * Développer le module de téléchargement B-Roll via l'API Pexels.
4. **Phase 4 : Rendu Bout-en-Bout, Mastering LUFS & Publication**
   * Automatiser l'appel `npx remotion render --props=...`.
   * Normaliser l'audio avec le filtre FFmpeg `loudnorm`.
   * Configurer le téléversement via l'API YouTube Data v3.

