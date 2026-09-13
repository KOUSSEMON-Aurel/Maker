import os

os.makedirs('/home/aurel/CODE/Maker/engine/public/avatars', exist_ok=True)

# Human Character Palette
SKIN = "#FDDFB2"          # Warm natural human skin
SKIN_SHADOW = "#F3C594"   # Soft shadow on skin
HAIR = "#261C14"          # Modern dark brown haircut
HAIR_HIGHLIGHT = "#4A3B32"# Hair shine
HOODIE = "#3B82F6"        # Electric blue stylish hoodie
HOODIE_DARK = "#1D4ED8"   # Hoodie folds
HOODIE_STRINGS = "#FFFFFF"# White drawstrings
INNER_SHIRT = "#111827"   # Dark inner tee
EYE_COLOR = "#0284C7"     # Vibrant blue eyes

def render_human(face_features, arms_features):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 580" width="100%" height="100%">
  <defs>
    <radialGradient id="skinGrad" cx="45%" cy="40%" r="60%">
      <stop offset="0%" stop-color="{SKIN}" />
      <stop offset="100%" stop-color="{SKIN_SHADOW}" />
    </radialGradient>
    <linearGradient id="hoodieGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{HOODIE}" />
      <stop offset="100%" stop-color="{HOODIE_DARK}" />
    </linearGradient>
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-opacity="0.25"/>
    </filter>
  </defs>

  <!-- Torso & Hoodie Base -->
  <path d="M 140 370 C 100 440, 80 520, 80 580 L 420 580 C 420 520, 400 440, 360 370 Z" fill="url(#hoodieGrad)" />
  
  <!-- Inner T-shirt Collar -->
  <path d="M 215 370 Q 250 410 285 370 Z" fill="{INNER_SHIRT}" />
  
  <!-- Hoodie Drawstrings -->
  <line x1="225" y1="375" x2="220" y2="460" stroke="{HOODIE_STRINGS}" stroke-width="5" stroke-linecap="round"/>
  <line x1="275" y1="375" x2="280" y2="460" stroke="{HOODIE_STRINGS}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="220" cy="463" r="5" fill="#E2E8F0"/>
  <circle cx="280" cy="463" r="5" fill="#E2E8F0"/>

  <!-- Neck -->
  <rect x="220" y="300" width="60" height="85" rx="15" fill="{SKIN_SHADOW}" />

  <!-- Head Base (Human jaw and cheeks) -->
  <path d="M 160 210 C 160 130, 340 130, 340 210 C 340 285, 305 340, 250 345 C 195 340, 160 285, 160 210 Z" fill="url(#skinGrad)" filter="url(#softShadow)"/>

  <!-- Ears -->
  <ellipse cx="156" cy="225" rx="14" ry="22" fill="{SKIN_SHADOW}" />
  <ellipse cx="344" cy="225" rx="14" ry="22" fill="{SKIN_SHADOW}" />
  <ellipse cx="156" cy="225" rx="7" ry="12" fill="#E7AB79" />
  <ellipse cx="344" cy="225" rx="7" ry="12" fill="#E7AB79" />

  <!-- Arms / Gestures (Layered above torso) -->
  {arms_features}

  <!-- Facial Features (Eyes, Mouth, Eyebrows, Nose, Cheeks) -->
  {face_features}

  <!-- Stylish Human Hair (Messy voluminous top + side fringe) -->
  <path d="M 140 190 C 130 90, 240 60, 290 70 C 340 80, 370 120, 360 190 C 345 150, 310 130, 280 135 C 230 145, 190 120, 150 170 Z" fill="{HAIR}" />
  <path d="M 180 130 C 230 110, 280 110, 330 130" stroke="{HAIR_HIGHLIGHT}" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.6"/>
  <!-- Front locks falling over forehead -->
  <path d="M 190 135 Q 210 175 230 150" fill="{HAIR}"/>
  <path d="M 270 135 Q 260 170 290 155" fill="{HAIR}"/>
</svg>'''

# 10 Human Expressive Poses
poses = {
    "idle_neutral": (
        # Natural eyes with reflection + friendly smile
        '''<ellipse cx="205" cy="225" rx="16" ry="18" fill="#FFFFFF"/>
           <ellipse cx="295" cy="225" rx="16" ry="18" fill="#FFFFFF"/>
           <circle cx="205" cy="225" r="11" fill="{eye}"/>
           <circle cx="295" cy="225" r="11" fill="{eye}"/>
           <circle cx="202" cy="220" r="4" fill="#FFFFFF"/>
           <circle cx="292" cy="220" r="4" fill="#FFFFFF"/>
           <circle cx="208" cy="228" r="2" fill="#FFFFFF"/>
           <circle cx="298" cy="228" r="2" fill="#FFFFFF"/>
           <!-- Eyebrows -->
           <path d="M 185 200 Q 205 194 225 198" stroke="{hair}" stroke-width="5" stroke-linecap="round" fill="none"/>
           <path d="M 275 198 Q 295 194 315 200" stroke="{hair}" stroke-width="5" stroke-linecap="round" fill="none"/>
           <!-- Nose -->
           <path d="M 248 240 Q 254 252 246 256" stroke="#DCA273" stroke-width="3" stroke-linecap="round" fill="none"/>
           <!-- Smile -->
           <path d="M 225 280 Q 250 300 275 280" stroke="#8A4A28" stroke-width="4" stroke-linecap="round" fill="none"/>
           <!-- Subtle blush -->
           <ellipse cx="185" cy="255" rx="14" ry="7" fill="#F87171" opacity="0.35"/>
           <ellipse cx="315" cy="255" rx="14" ry="7" fill="#F87171" opacity="0.35"/>''',
        # Arms in hoodie front pocket
        '''<path d="M 130 400 Q 180 470 250 470 Q 320 470 370 400" stroke="{hoodie_dark}" stroke-width="44" stroke-linecap="round" fill="none"/>'''
    ),
    "shocked_jawdrop": (
        # Wide open eyes + O-shaped dropped mouth + sweat drop
        '''<ellipse cx="198" cy="220" rx="22" ry="24" fill="#FFFFFF"/>
           <ellipse cx="302" cy="220" rx="22" ry="24" fill="#FFFFFF"/>
           <circle cx="198" cy="220" r="13" fill="{eye}"/>
           <circle cx="302" cy="220" r="13" fill="{eye}"/>
           <circle cx="194" cy="215" r="5" fill="#FFFFFF"/>
           <circle cx="298" cy="215" r="5" fill="#FFFFFF"/>
           <!-- High raised arched eyebrows -->
           <path d="M 175 185 Q 200 170 222 185" stroke="{hair}" stroke-width="5" stroke-linecap="round" fill="none"/>
           <path d="M 278 185 Q 300 170 325 185" stroke="{hair}" stroke-width="5" stroke-linecap="round" fill="none"/>
           <!-- Dropped open mouth -->
           <ellipse cx="250" cy="292" rx="18" ry="24" fill="#4A1515"/>
           <ellipse cx="250" cy="302" rx="12" ry="10" fill="#E11D48"/>
           <!-- Anime sweat drop -->
           <path d="M 335 180 C 335 170, 350 170, 350 180 C 350 190, 335 195, 335 180 Z" fill="#38BDF8" opacity="0.9"/>''',
        # Hands on cheeks in disbelief
        '''<path d="M 110 440 Q 120 280 155 255" stroke="{hoodie}" stroke-width="40" stroke-linecap="round" fill="none"/>
           <circle cx="155" cy="255" r="22" fill="{skin}"/>
           <path d="M 390 440 Q 380 280 345 255" stroke="{hoodie}" stroke-width="40" stroke-linecap="round" fill="none"/>
           <circle cx="345" cy="255" r="22" fill="{skin}"/>'''
    ),
    "explaining_point": (
        # Confident speaking expression + index finger up
        '''<ellipse cx="205" cy="225" rx="16" ry="17" fill="#FFFFFF"/>
           <ellipse cx="295" cy="225" rx="16" ry="17" fill="#FFFFFF"/>
           <circle cx="205" cy="225" r="10" fill="{eye}"/>
           <circle cx="295" cy="225" r="10" fill="{eye}"/>
           <circle cx="202" cy="221" r="3" fill="#FFFFFF"/>
           <circle cx="292" cy="221" r="3" fill="#FFFFFF"/>
           <!-- Confident eyebrows -->
           <path d="M 185 198 L 220 203" stroke="{hair}" stroke-width="5" stroke-linecap="round"/>
           <path d="M 280 203 L 315 198" stroke="{hair}" stroke-width="5" stroke-linecap="round"/>
           <!-- Talking mouth -->
           <path d="M 230 280 Q 250 295 270 280 Z" fill="#6B2810"/>''',
        # Left hand down, right arm raised pointing with finger
        '''<path d="M 120 420 Q 110 500 130 550" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <path d="M 370 420 Q 430 330 395 210" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <!-- Hand & pointing finger -->
           <circle cx="390" cy="200" r="20" fill="{skin}"/>
           <rect x="384" y="160" width="12" height="42" rx="6" fill="{skin}"/>'''
    ),
    "laughing_joke": (
        # Squinted XD laughing eyes + wide happy open mouth
        '''<path d="M 185 225 L 205 215 L 225 225" stroke="{hair}" stroke-width="6" stroke-linecap="round" fill="none"/>
           <path d="M 275 225 L 295 215 L 315 225" stroke="{hair}" stroke-width="6" stroke-linecap="round" fill="none"/>
           <!-- Laughing curved eyebrows -->
           <path d="M 180 190 Q 205 180 225 192" stroke="{hair}" stroke-width="5" stroke-linecap="round" fill="none"/>
           <path d="M 275 192 Q 295 180 320 190" stroke="{hair}" stroke-width="5" stroke-linecap="round" fill="none"/>
           <!-- Big laughing mouth with teeth & tongue -->
           <path d="M 220 270 Q 250 325 280 270 Z" fill="#6B1A1A"/>
           <path d="M 226 270 Q 250 280 274 270 Z" fill="#FFFFFF"/>
           <path d="M 235 300 Q 250 290 265 300 Q 250 320 235 300 Z" fill="#F43F5E"/>
           <!-- Big blush -->
           <ellipse cx="180" cy="245" rx="16" ry="8" fill="#F43F5E" opacity="0.4"/>
           <ellipse cx="320" cy="245" rx="16" ry="8" fill="#F43F5E" opacity="0.4"/>''',
        # Holding stomach laughing
        '''<path d="M 120 420 Q 180 490 230 460" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="230" cy="460" r="20" fill="{skin}"/>
           <path d="M 380 420 Q 320 490 270 460" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="270" cy="460" r="20" fill="{skin}"/>'''
    ),
    "skeptical_sideeye": (
        # One high eyebrow, pupils looking sideways, flat smirk
        '''<ellipse cx="205" cy="225" rx="15" ry="16" fill="#FFFFFF"/>
           <ellipse cx="295" cy="225" rx="15" ry="16" fill="#FFFFFF"/>
           <circle cx="213" cy="225" r="9" fill="{eye}"/>
           <circle cx="303" cy="225" r="9" fill="{eye}"/>
           <!-- Raised left eyebrow, flat right eyebrow -->
           <path d="M 180 185 Q 200 172 225 180" stroke="{hair}" stroke-width="5" stroke-linecap="round" fill="none"/>
           <path d="M 275 205 L 315 205" stroke="{hair}" stroke-width="5" stroke-linecap="round"/>
           <!-- Smug smirk to side -->
           <path d="M 230 285 Q 260 280 275 272" stroke="#8A4A28" stroke-width="4" stroke-linecap="round" fill="none"/>''',
        # Crossed arms
        '''<path d="M 120 440 Q 250 510 380 440" stroke="{hoodie}" stroke-width="42" stroke-linecap="round" fill="none"/>'''
    ),
    "facepalm": (
        # Closed eyes, hand covering face with embarrassment sweat
        '''<line x1="185" y1="225" x2="225" y2="225" stroke="{hair}" stroke-width="5" stroke-linecap="round"/>
           <!-- Drooped mouth -->
           <path d="M 235 290 Q 250 280 265 290" stroke="#8A4A28" stroke-width="4" stroke-linecap="round" fill="none"/>
           <ellipse cx="185" cy="255" rx="14" ry="7" fill="#F87171" opacity="0.5"/>''',
        # Right hand pressed over face
        '''<path d="M 120 420 Q 110 500 130 550" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <path d="M 380 440 Q 360 260 280 220" stroke="{hoodie}" stroke-width="40" stroke-linecap="round" fill="none"/>
           <circle cx="270" cy="215" r="26" fill="{skin}"/>'''
    ),
    "secret_whisper": (
        # Winking eye + leaning forward with hand near mouth
        '''<path d="M 185 225 Q 205 212 225 225" stroke="{hair}" stroke-width="6" stroke-linecap="round" fill="none"/>
           <ellipse cx="295" cy="225" rx="16" ry="18" fill="#FFFFFF"/>
           <circle cx="295" cy="225" r="10" fill="{eye}"/>
           <!-- Smirk -->
           <path d="M 235 280 Q 255 290 275 276" stroke="#8A4A28" stroke-width="4" stroke-linecap="round" fill="none"/>''',
        # Hand shielding mouth
        '''<path d="M 120 420 Q 110 500 130 550" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <path d="M 380 440 Q 340 330 295 285" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="295" cy="280" r="24" fill="{skin}"/>'''
    ),
    "angry_triggered": (
        # Sharp anime angry eyebrows + clenched gritted teeth
        '''<path d="M 180 200 L 225 215" stroke="{hair}" stroke-width="6" stroke-linecap="round"/>
           <path d="M 320 200 L 275 215" stroke="{hair}" stroke-width="6" stroke-linecap="round"/>
           <ellipse cx="205" cy="230" rx="14" ry="16" fill="#FFFFFF"/>
           <ellipse cx="295" cy="230" rx="14" ry="16" fill="#FFFFFF"/>
           <circle cx="205" cy="230" r="8" fill="#DC2626"/>
           <circle cx="295" cy="230" r="8" fill="#DC2626"/>
           <!-- Gritted teeth mouth -->
           <rect x="225" y="275" width="50" height="20" rx="6" fill="#FFFFFF" stroke="#8A4A28" stroke-width="3"/>
           <line x1="225" y1="285" x2="275" y2="285" stroke="#8A4A28" stroke-width="2"/>
           <!-- Angry anime vein symbol -->
           <path d="M 325 155 L 345 155 M 335 145 L 335 165" stroke="#EF4444" stroke-width="5" stroke-linecap="round"/>''',
        # Raised clenched fists
        '''<path d="M 120 440 Q 90 320 120 280" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="120" cy="270" r="22" fill="{skin}"/>
           <path d="M 380 440 Q 410 320 380 280" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="380" cy="270" r="22" fill="{skin}"/>'''
    ),
    "hyped_victory": (
        # Happy eyes + huge smile + V signs
        '''<path d="M 185 225 Q 205 210 225 225" stroke="{hair}" stroke-width="6" stroke-linecap="round" fill="none"/>
           <path d="M 275 225 Q 295 210 315 225" stroke="{hair}" stroke-width="6" stroke-linecap="round" fill="none"/>
           <path d="M 220 270 Q 250 320 280 270 Z" fill="#6B1A1A"/>
           <path d="M 226 270 Q 250 280 274 270 Z" fill="#FFFFFF"/>
           <!-- Blush -->
           <ellipse cx="180" cy="245" rx="14" ry="7" fill="#F43F5E" opacity="0.4"/>
           <ellipse cx="320" cy="245" rx="14" ry="7" fill="#F43F5E" opacity="0.4"/>''',
        # Both arms raised high
        '''<path d="M 120 420 Q 80 280 95 190" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="95" cy="180" r="22" fill="{skin}"/>
           <path d="M 380 420 Q 420 280 405 190" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="405" cy="180" r="22" fill="{skin}"/>'''
    ),
    "thinking_chin": (
        # Looking up curiously + hand on chin
        '''<ellipse cx="205" cy="218" rx="15" ry="16" fill="#FFFFFF"/>
           <ellipse cx="295" cy="218" rx="15" ry="16" fill="#FFFFFF"/>
           <circle cx="205" cy="214" r="9" fill="{eye}"/>
           <circle cx="295" cy="214" r="9" fill="{eye}"/>
           <!-- Inquisitive eyebrows -->
           <path d="M 185 190 Q 205 180 225 190" stroke="{hair}" stroke-width="5" stroke-linecap="round" fill="none"/>
           <path d="M 275 195 Q 295 185 315 195" stroke="{hair}" stroke-width="5" stroke-linecap="round" fill="none"/>
           <!-- Pouty curious mouth -->
           <circle cx="250" cy="285" r="7" fill="#8A4A28"/>''',
        # Hand on chin
        '''<path d="M 120 420 Q 110 500 130 550" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <path d="M 380 440 Q 340 350 280 310" stroke="{hoodie}" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="270" cy="310" r="24" fill="{skin}"/>'''
    ),
}

for name, (face, arms) in poses.items():
    formatted_face = face.format(eye=EYE_COLOR, hair=HAIR, skin=SKIN)
    formatted_arms = arms.format(hoodie=HOODIE, hoodie_dark=HOODIE_DARK, skin=SKIN)
    svg_data = render_human(formatted_face, formatted_arms)
    file_path = f"/home/aurel/CODE/Maker/engine/public/avatars/{name}.svg"
    with open(file_path, "w") as f:
        f.write(svg_data)

print("10 Human Character Avatars successfully generated!")
