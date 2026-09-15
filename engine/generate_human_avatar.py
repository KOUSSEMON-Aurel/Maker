import os

AVATAR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "avatars")
os.makedirs(AVATAR_DIR, exist_ok=True)

# Common palette
C_OUTLINE = "#181B20"
C_SKIN = "#FFE2CF"
C_SKIN_SHADOW = "#E8BA9F"
C_BLUSH = "#FF9EAA"
C_HAIR = "#271E18"
C_HAIR_HIGHLIGHT = "#4E3C32"
C_HOODIE = "#2563EB"
C_HOODIE_SHADOW = "#1D4ED8"
C_HOODIE_INNER = "#1E3A8A"
C_WHITE = "#FFFFFF"
C_PUPIL = "#1E293B"
C_IRIS = "#0284C7"
C_SWEAT = "#38BDF8"

def make_svg(pose_name: str, elements: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 550" width="100%" height="100%">
  <defs>
    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.35"/>
    </filter>
    <linearGradient id="skinGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{C_SKIN}"/>
      <stop offset="100%" stop-color="{C_SKIN_SHADOW}"/>
    </linearGradient>
    <linearGradient id="hoodieGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{C_HOODIE}"/>
      <stop offset="100%" stop-color="{C_HOODIE_SHADOW}"/>
    </linearGradient>
  </defs>

  <g filter="url(#softShadow)">
    {elements}
  </g>
</svg>"""

# Base Body (Streetwear Hoodie)
def hoodie_body(shoulder_tilt=0):
    return f"""
    <!-- Shoulders & Torso -->
    <path d="M 120 420 Q 250 395 380 420 L 410 550 L 90 550 Z" 
          fill="url(#hoodieGrad)" stroke="{C_OUTLINE}" stroke-width="4" stroke-linejoin="round"/>
    
    <!-- Chest / Zip folds -->
    <path d="M 250 435 L 250 550" stroke="{C_HOODIE_SHADOW}" stroke-width="4" stroke-linecap="round"/>
    <path d="M 170 480 Q 210 495 240 485" stroke="{C_HOODIE_SHADOW}" stroke-width="3" stroke-linecap="round" fill="none"/>
    <path d="M 330 480 Q 290 495 260 485" stroke="{C_HOODIE_SHADOW}" stroke-width="3" stroke-linecap="round" fill="none"/>

    <!-- Hood Collar Behind Neck -->
    <path d="M 175 350 C 145 380 160 440 250 440 C 340 440 355 380 325 350 Z" 
          fill="{C_HOODIE_INNER}" stroke="{C_OUTLINE}" stroke-width="4"/>

    <!-- White Drawstrings -->
    <path d="M 215 425 Q 210 480 215 505" stroke="{C_WHITE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
    <rect x="212" y="505" width="6" height="12" rx="3" fill="#CBD5E1"/>
    <path d="M 285 425 Q 290 480 285 505" stroke="{C_WHITE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
    <rect x="282" y="505" width="6" height="12" rx="3" fill="#CBD5E1"/>
    """

def head_base():
    return f"""
    <!-- Neck -->
    <path d="M 220 330 L 220 380 Q 250 395 280 380 L 280 330 Z" fill="{C_SKIN_SHADOW}" stroke="{C_OUTLINE}" stroke-width="4"/>

    <!-- Ears -->
    <path d="M 162 255 C 145 255 145 295 165 295 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <path d="M 158 270 Q 152 280 160 285" stroke="{C_SKIN_SHADOW}" stroke-width="3" fill="none"/>
    <path d="M 338 255 C 355 255 355 295 335 295 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <path d="M 342 270 Q 348 280 340 285" stroke="{C_SKIN_SHADOW}" stroke-width="3" fill="none"/>

    <!-- Face Shape (Anime soft jaw) -->
    <path d="M 165 240 C 165 170 335 170 335 240 C 335 310 295 355 250 355 C 205 355 165 310 165 240 Z" 
          fill="url(#skinGrad)" stroke="{C_OUTLINE}" stroke-width="4" stroke-linejoin="round"/>
    
    <!-- Nose -->
    <path d="M 248 270 L 253 277 L 247 280" stroke="{C_OUTLINE}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    """

def hair():
    return f"""
    <!-- Hair Base & Dynamic Tuft Layers -->
    <path d="M 155 240 C 145 150 200 115 250 115 C 310 115 355 150 345 240 C 355 220 358 190 340 165 C 320 140 300 130 250 130 C 190 130 170 150 155 240 Z"
          fill="{C_HAIR}" stroke="{C_OUTLINE}" stroke-width="4" stroke-linejoin="round"/>
    
    <!-- Top Hair Volume & Spikes -->
    <path d="M 160 220 C 150 160 190 110 255 110 C 320 110 355 155 342 215 C 335 170 310 130 260 130 C 200 130 175 165 160 220 Z" 
          fill="{C_HAIR_HIGHLIGHT}"/>

    <!-- Front Strands / Fringe -->
    <path d="M 168 205 Q 185 240 205 220 Q 225 250 250 215 Q 275 250 295 218 Q 320 235 332 205 C 325 160 300 140 250 140 C 195 140 175 165 168 205 Z"
          fill="{C_HAIR}" stroke="{C_OUTLINE}" stroke-width="3.5" stroke-linejoin="round"/>
    
    <!-- Accent Highlight Lock -->
    <path d="M 215 150 Q 240 135 270 145" stroke="{C_HAIR_HIGHLIGHT}" stroke-width="4" stroke-linecap="round" fill="none"/>
    """

# 1. SHOCKED JAW DROP
def pose_shocked():
    eyes = f"""
    <!-- Shocked Wide Eyes -->
    <ellipse cx="205" cy="245" rx="20" ry="24" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <ellipse cx="205" cy="246" rx="9" ry="12" fill="{C_IRIS}"/>
    <circle cx="205" cy="246" r="6" fill="{C_PUPIL}"/>
    <circle cx="202" cy="241" r="3" fill="{C_WHITE}"/>

    <ellipse cx="295" cy="245" rx="20" ry="24" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <ellipse cx="295" cy="246" rx="9" ry="12" fill="{C_IRIS}"/>
    <circle cx="295" cy="246" r="6" fill="{C_PUPIL}"/>
    <circle cx="292" cy="241" r="3" fill="{C_WHITE}"/>

    <!-- High Eyebrows -->
    <path d="M 185 210 Q 205 198 228 210" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
    <path d="M 272 210 Q 295 198 315 210" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>

    <!-- Open 'O' Mouth -->
    <ellipse cx="250" cy="315" rx="14" ry="22" fill="#7F1D1D" stroke="{C_OUTLINE}" stroke-width="4"/>
    <ellipse cx="250" cy="324" rx="8" ry="7" fill="#EF4444"/>

    <!-- Anime Sweat Drop -->
    <path d="M 330 200 C 330 190 342 180 342 170 C 342 180 354 190 354 200 C 354 208 344 214 336 210 C 332 208 330 204 330 200 Z" 
          fill="{C_SWEAT}" stroke="{C_OUTLINE}" stroke-width="2.5"/>

    <!-- Hands on Cheeks -->
    <!-- Left Hand -->
    <g transform="translate(135, 260) rotate(-15)">
      <path d="M 10 50 C 0 30 10 10 25 5 C 32 3 38 12 35 25 L 35 60 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="4"/>
      <path d="M 28 5 C 38 0 48 10 42 28" stroke="{C_OUTLINE}" stroke-width="3.5" fill="none"/>
      <!-- Sleeve cuff -->
      <ellipse cx="22" cy="70" rx="20" ry="12" fill="{C_HOODIE}" stroke="{C_OUTLINE}" stroke-width="3.5"/>
    </g>
    <!-- Right Hand -->
    <g transform="translate(325, 260) rotate(15)">
      <path d="M 30 50 C 40 30 30 10 15 5 C 8 3 2 12 5 25 L 5 60 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="4"/>
      <path d="M 12 5 C 2 0 -8 10 -2 28" stroke="{C_OUTLINE}" stroke-width="3.5" fill="none"/>
      <!-- Sleeve cuff -->
      <ellipse cx="18" cy="70" rx="20" ry="12" fill="{C_HOODIE}" stroke="{C_OUTLINE}" stroke-width="3.5"/>
    </g>
    """
    return make_svg("shocked_jawdrop", hoodie_body() + head_base() + hair() + eyes)

# 2. LAUGHING JOKE
def pose_laughing():
    face = f"""
    <!-- Laughing Eyes (^ ^) -->
    <path d="M 188 248 Q 208 230 226 248" stroke="{C_OUTLINE}" stroke-width="5" stroke-linecap="round" fill="none"/>
    <path d="M 274 248 Q 292 230 312 248" stroke="{C_OUTLINE}" stroke-width="5" stroke-linecap="round" fill="none"/>

    <!-- Eyebrows -->
    <path d="M 185 220 Q 208 212 228 222" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
    <path d="M 272 222 Q 292 212 315 220" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>

    <!-- Cheerful Open Mouth with Tongue & Teeth -->
    <path d="M 220 295 Q 250 290 280 295 C 280 330 220 330 220 295 Z" 
          fill="#881337" stroke="{C_OUTLINE}" stroke-width="4" stroke-linejoin="round"/>
    <!-- Teeth -->
    <path d="M 228 295 Q 250 292 272 295 C 270 302 230 302 228 295 Z" fill="{C_WHITE}"/>
    <!-- Tongue -->
    <path d="M 235 315 Q 250 308 265 315 C 265 325 235 325 235 315 Z" fill="#FB7185"/>

    <!-- Blush Marks -->
    <ellipse cx="185" cy="272" rx="14" ry="7" fill="{C_BLUSH}" opacity="0.6"/>
    <ellipse cx="315" cy="272" rx="14" ry="7" fill="{C_BLUSH}" opacity="0.6"/>

    <!-- Cheerful Hand Wave / Chest -->
    <g transform="translate(260, 360)">
      <path d="M 0 40 Q 30 10 60 40 L 40 80 Z" fill="{C_HOODIE}" stroke="{C_OUTLINE}" stroke-width="4"/>
      <!-- Hand -->
      <ellipse cx="65" cy="35" rx="18" ry="14" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="3.5"/>
    </g>
    """
    return make_svg("laughing_joke", hoodie_body() + head_base() + hair() + face)

# 3. SECRET WHISPER (Wink & Finger to mouth)
def pose_whisper():
    face = f"""
    <!-- One Winking Eye, One Alert Eye -->
    <!-- Left Eye Open -->
    <ellipse cx="205" cy="245" rx="17" ry="19" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <ellipse cx="205" cy="246" rx="8" ry="10" fill="{C_IRIS}"/>
    <circle cx="205" cy="246" r="5" fill="{C_PUPIL}"/>
    <circle cx="202" cy="242" r="2.5" fill="{C_WHITE}"/>
    <path d="M 185 218 Q 205 208 228 218" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>

    <!-- Right Eye Winking 😉 -->
    <path d="M 276 248 Q 295 238 314 248" stroke="{C_OUTLINE}" stroke-width="5.5" stroke-linecap="round" fill="none"/>
    <path d="M 274 220 Q 295 212 314 224" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>

    <!-- Smirk Mouth -->
    <path d="M 235 305 Q 255 305 268 296" stroke="{C_OUTLINE}" stroke-width="4" stroke-linecap="round" fill="none"/>

    <!-- Finger on Lips (Shhh / Secret gesture) -->
    <g transform="translate(245, 275)">
      <!-- Index Finger pointing up to lips -->
      <path d="M 8 30 L 8 5 C 8 0 18 0 18 5 L 18 30 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="3.5" stroke-linejoin="round"/>
      <!-- Folded other fingers -->
      <path d="M 18 15 C 28 15 28 32 18 32 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="3"/>
      <path d="M 18 25 C 26 25 26 40 18 40 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="3"/>
      <!-- Forearm & Blue Sleeve -->
      <path d="M 5 35 L 2 95 L 35 95 L 25 35 Z" fill="{C_HOODIE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    </g>
    """
    return make_svg("secret_whisper", hoodie_body() + head_base() + hair() + face)

# 4. THINKING CHIN
def pose_thinking():
    face = f"""
    <!-- Puzzled Look -->
    <ellipse cx="205" cy="242" rx="16" ry="18" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="208" cy="240" r="7" fill="{C_IRIS}"/>
    <circle cx="208" cy="240" r="4" fill="{C_PUPIL}"/>

    <ellipse cx="295" cy="242" rx="16" ry="18" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="298" cy="240" r="7" fill="{C_IRIS}"/>
    <circle cx="298" cy="240" r="4" fill="{C_PUPIL}"/>

    <!-- One eyebrow raised high, other furrowed -->
    <path d="M 185 225 Q 205 222 225 228" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
    <path d="M 275 212 Q 295 198 318 210" stroke="{C_OUTLINE}" stroke-width="5" stroke-linecap="round" fill="none"/>

    <!-- Thoughtful Wavy Mouth -->
    <path d="M 235 305 Q 248 300 262 305" stroke="{C_OUTLINE}" stroke-width="4" stroke-linecap="round" fill="none"/>

    <!-- Hand under Chin -->
    <g transform="translate(230, 320)">
      <path d="M 0 35 Q 20 15 40 35 L 35 70 L 5 70 Z" fill="{C_HOODIE}" stroke="{C_OUTLINE}" stroke-width="4"/>
      <!-- Hand on chin -->
      <path d="M 15 15 C 5 15 5 35 25 35 C 35 35 35 15 25 15 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="3.5"/>
      <path d="M 20 15 L 20 5 C 20 0 28 0 28 5 L 28 15" stroke="{C_OUTLINE}" stroke-width="3.5" fill="{C_SKIN}"/>
    </g>

    <!-- Floating Thought Bulb / Sparkle -->
    <path d="M 370 170 Q 385 170 385 155 Q 385 170 400 170 Q 385 170 385 185 Q 385 170 370 170 Z" 
          fill="#FBBF24" stroke="{C_OUTLINE}" stroke-width="2.5"/>
    """
    return make_svg("thinking_chin", hoodie_body() + head_base() + hair() + face)

# 5. IDLE NEUTRAL
def pose_idle():
    face = f"""
    <!-- Calm Confident Eyes -->
    <ellipse cx="205" cy="245" rx="16" ry="18" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="206" cy="245" r="7" fill="{C_IRIS}"/>
    <circle cx="206" cy="245" r="4" fill="{C_PUPIL}"/>
    <circle cx="203" cy="242" r="2.5" fill="{C_WHITE}"/>

    <ellipse cx="295" cy="245" rx="16" ry="18" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="294" cy="245" r="7" fill="{C_IRIS}"/>
    <circle cx="294" cy="245" r="4" fill="{C_PUPIL}"/>
    <circle cx="291" cy="242" r="2.5" fill="{C_WHITE}"/>

    <!-- Friendly Eyebrows -->
    <path d="M 188 220 Q 208 214 228 220" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
    <path d="M 272 220 Q 292 214 312 220" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>

    <!-- Subtle Friendly Smile -->
    <path d="M 235 300 Q 250 312 265 300" stroke="{C_OUTLINE}" stroke-width="4" stroke-linecap="round" fill="none"/>
    """
    return make_svg("idle_neutral", hoodie_body() + head_base() + hair() + face)

# 6. EXPLAINING POINT
def pose_explaining():
    face = f"""
    <!-- Attentive Focused Eyes -->
    <ellipse cx="205" cy="245" rx="16" ry="18" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="208" cy="245" r="7" fill="{C_IRIS}"/>
    <circle cx="208" cy="245" r="4" fill="{C_PUPIL}"/>
    <circle cx="205" cy="242" r="2.5" fill="{C_WHITE}"/>

    <ellipse cx="295" cy="245" rx="16" ry="18" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="298" cy="245" r="7" fill="{C_IRIS}"/>
    <circle cx="298" cy="245" r="4" fill="{C_PUPIL}"/>
    <circle cx="295" cy="242" r="2.5" fill="{C_WHITE}"/>

    <path d="M 188 218 Q 208 210 228 216" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
    <path d="M 272 216 Q 292 210 312 218" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>

    <!-- Explaining Mouth -->
    <ellipse cx="250" cy="305" rx="10" ry="8" fill="#881337" stroke="{C_OUTLINE}" stroke-width="3.5"/>
    <path d="M 243 303 Q 250 300 257 303" stroke="{C_WHITE}" stroke-width="2" fill="none"/>

    <!-- Hand Pointing Up -->
    <g transform="translate(100, 240)">
      <path d="M 40 120 L 60 70 L 80 120 Z" fill="{C_HOODIE}" stroke="{C_OUTLINE}" stroke-width="4"/>
      <!-- Pointing Hand -->
      <path d="M 60 65 L 60 15 C 60 8 70 8 70 15 L 70 65 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="3.5"/>
      <ellipse cx="65" cy="65" rx="14" ry="10" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="3"/>
    </g>
    """
    return make_svg("explaining_point", hoodie_body() + head_base() + hair() + face)

# 7. HYPED VICTORY
def pose_hyped():
    face = f"""
    <!-- High Energy Joyful Face -->
    <path d="M 186 245 Q 206 226 226 245" stroke="{C_OUTLINE}" stroke-width="5.5" stroke-linecap="round" fill="none"/>
    <path d="M 274 245 Q 294 226 314 245" stroke="{C_OUTLINE}" stroke-width="5.5" stroke-linecap="round" fill="none"/>

    <path d="M 185 214 Q 206 204 228 214" stroke="{C_OUTLINE}" stroke-width="5" stroke-linecap="round" fill="none"/>
    <path d="M 272 214 Q 294 204 315 214" stroke="{C_OUTLINE}" stroke-width="5" stroke-linecap="round" fill="none"/>

    <path d="M 215 292 Q 250 286 285 292 C 285 340 215 340 215 292 Z" fill="#991B1B" stroke="{C_OUTLINE}" stroke-width="4"/>
    <path d="M 225 293 Q 250 290 275 293" stroke="{C_WHITE}" stroke-width="6" stroke-linecap="round" fill="none"/>
    <ellipse cx="250" cy="326" rx="18" ry="9" fill="#F87171"/>

    <!-- Both Fists Raised in Air -->
    <g transform="translate(70, 200)">
      <path d="M 30 150 L 50 70 L 80 140 Z" fill="{C_HOODIE}" stroke="{C_OUTLINE}" stroke-width="4"/>
      <ellipse cx="50" cy="60" rx="18" ry="16" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="4"/>
    </g>
    <g transform="translate(350, 200)">
      <path d="M 70 150 L 50 70 L 20 140 Z" fill="{C_HOODIE}" stroke="{C_OUTLINE}" stroke-width="4"/>
      <ellipse cx="50" cy="60" rx="18" ry="16" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="4"/>
    </g>
    """
    return make_svg("hyped_victory", hoodie_body() + head_base() + hair() + face)

# 8. SKEPTICAL SIDE EYE
def pose_skeptical():
    face = f"""
    <!-- Side Looking Eyes -->
    <ellipse cx="205" cy="245" rx="16" ry="16" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="196" cy="245" r="7" fill="{C_IRIS}"/>
    <circle cx="196" cy="245" r="4" fill="{C_PUPIL}"/>

    <ellipse cx="295" cy="245" rx="16" ry="16" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="286" cy="245" r="7" fill="{C_IRIS}"/>
    <circle cx="286" cy="245" r="4" fill="{C_PUPIL}"/>

    <!-- One Raised, One Down -->
    <path d="M 185 228 L 225 224" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round"/>
    <path d="M 275 210 Q 295 198 318 214" stroke="{C_OUTLINE}" stroke-width="5" stroke-linecap="round" fill="none"/>

    <!-- Wry Smirk -->
    <path d="M 230 305 Q 245 306 265 298" stroke="{C_OUTLINE}" stroke-width="4" stroke-linecap="round" fill="none"/>
    """
    return make_svg("skeptical_sideeye", hoodie_body() + head_base() + hair() + face)

# 9. ANGRY TRIGGERED
def pose_angry():
    face = f"""
    <!-- Angled Angry Brows -->
    <path d="M 185 215 L 230 230" stroke="{C_OUTLINE}" stroke-width="5.5" stroke-linecap="round"/>
    <path d="M 315 215 L 270 230" stroke="{C_OUTLINE}" stroke-width="5.5" stroke-linecap="round"/>

    <ellipse cx="205" cy="245" rx="15" ry="16" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="208" cy="245" r="6" fill="{C_IRIS}"/>
    <circle cx="208" cy="245" r="3.5" fill="{C_PUPIL}"/>

    <ellipse cx="295" cy="245" rx="15" ry="16" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="4"/>
    <circle cx="292" cy="245" r="6" fill="{C_IRIS}"/>
    <circle cx="292" cy="245" r="3.5" fill="{C_PUPIL}"/>

    <!-- Clenched Teeth Mouth -->
    <rect x="225" y="295" width="50" height="16" rx="6" fill="{C_WHITE}" stroke="{C_OUTLINE}" stroke-width="3.5"/>
    <line x1="225" y1="303" x2="275" y2="303" stroke="{C_OUTLINE}" stroke-width="2"/>
    <line x1="242" y1="295" x2="242" y2="311" stroke="{C_OUTLINE}" stroke-width="2"/>
    <line x1="258" y1="295" x2="258" y2="311" stroke="{C_OUTLINE}" stroke-width="2"/>

    <!-- Anime Anger Mark 💢 -->
    <path d="M 335 160 L 355 160 M 345 150 L 345 170" stroke="#EF4444" stroke-width="4" stroke-linecap="round"/>
    """
    return make_svg("angry_triggered", hoodie_body() + head_base() + hair() + face)

# 10. FACEPALM
def pose_facepalm():
    face = f"""
    <!-- Closed Disappointed Eye on Left -->
    <path d="M 188 245 Q 206 235 224 245" stroke="{C_OUTLINE}" stroke-width="4.5" stroke-linecap="round" fill="none"/>
    <path d="M 185 225 L 225 220" stroke="{C_OUTLINE}" stroke-width="4" stroke-linecap="round"/>

    <!-- Sigh Mouth -->
    <path d="M 235 310 Q 250 305 265 310" stroke="{C_OUTLINE}" stroke-width="4" stroke-linecap="round" fill="none"/>

    <!-- Hand Covering Forehead/Eye on Right -->
    <g transform="translate(250, 180)">
      <path d="M 40 180 L 50 90 L 80 180 Z" fill="{C_HOODIE}" stroke="{C_OUTLINE}" stroke-width="4"/>
      <!-- Palm over eye -->
      <path d="M 20 60 C 20 30 65 30 65 60 L 55 90 L 30 90 Z" fill="{C_SKIN}" stroke="{C_OUTLINE}" stroke-width="4"/>
      <path d="M 30 30 L 30 15 C 30 10 38 10 38 15 L 38 30" stroke="{C_OUTLINE}" stroke-width="3" fill="{C_SKIN}"/>
      <path d="M 40 30 L 40 10 C 40 5 48 5 48 10 L 48 30" stroke="{C_OUTLINE}" stroke-width="3" fill="{C_SKIN}"/>
      <path d="M 50 30 L 50 15 C 50 10 58 10 58 15 L 58 30" stroke="{C_OUTLINE}" stroke-width="3" fill="{C_SKIN}"/>
    </g>
    """
    return make_svg("facepalm", hoodie_body() + head_base() + hair() + face)

POSES = {
    "shocked_jawdrop.svg": pose_shocked(),
    "laughing_joke.svg": pose_laughing(),
    "secret_whisper.svg": pose_whisper(),
    "thinking_chin.svg": pose_thinking(),
    "idle_neutral.svg": pose_idle(),
    "explaining_point.svg": pose_explaining(),
    "hyped_victory.svg": pose_hyped(),
    "skeptical_sideeye.svg": pose_skeptical(),
    "angry_triggered.svg": pose_angry(),
    "facepalm.svg": pose_facepalm(),
}

def generate_all():
    print(f"🎨 Génération de {len(POSES)} poses d'avatars humains soignés dans {AVATAR_DIR}...")
    for filename, svg_content in POSES.items():
        filepath = os.path.join(AVATAR_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content.strip())
        print(f"  ✓ {filename}")
    print("✨ Avatars générés avec succès !")

if __name__ == "__main__":
    generate_all()
