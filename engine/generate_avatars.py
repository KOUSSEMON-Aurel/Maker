import os

os.makedirs('/home/aurel/CODE/Maker/engine/public/avatars', exist_ok=True)

# Mascot Colors: Modern Cyber-Storyteller (Neon Cyan & Gold highlights on Deep Obsidian Jacket)
HOODIE = "#1E293B"       # Deep slate hoodie jacket
HOODIE_DARK = "#0F172A"  # Inner hood / shadow
FACE_SKIN = "#1E1E2E"    # Dark tech visor / face
NEON_CYAN = "#00F5FF"    # Glowing cyan eyes & lines
GOLD = "#FBBF24"         # Gold trims
WHITE = "#FFFFFF"

def render_mascot(face_expression, arms_markup):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 550" width="100%" height="100%">
  <defs>
    <radialGradient id="auraGlow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="{NEON_CYAN}" stop-opacity="0.35" />
      <stop offset="100%" stop-color="{NEON_CYAN}" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="hoodieGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <filter id="neonBlur" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Ambient Backlight Aura -->
  <circle cx="250" cy="240" r="210" fill="url(#auraGlow)" />

  <!-- Headphones Arc -->
  <path d="M 120 200 A 130 130 0 0 1 380 200" stroke="{GOLD}" stroke-width="18" fill="none" stroke-linecap="round"/>
  <!-- Headphone earcups -->
  <rect x="100" y="190" width="30" height="70" rx="15" fill="#3B82F6" filter="url(#neonBlur)"/>
  <rect x="370" y="190" width="30" height="70" rx="15" fill="#3B82F6" filter="url(#neonBlur)"/>

  <!-- Outer Hood / Cape -->
  <path d="M 120 260 C 120 100, 380 100, 380 260 C 380 340, 340 370, 250 370 C 160 370, 120 340, 120 260 Z" fill="url(#hoodieGrad)" stroke="#475569" stroke-width="6"/>

  <!-- Inner Hood Void -->
  <ellipse cx="250" cy="245" rx="115" ry="110" fill="{HOODIE_DARK}" />

  <!-- Visor / Face Screen -->
  <rect x="155" y="170" width="190" height="135" rx="55" fill="{FACE_SKIN}" stroke="{NEON_CYAN}" stroke-width="4" filter="url(#neonBlur)"/>

  <!-- Torso / Jacket -->
  <path d="M 160 365 L 120 540 L 380 540 L 340 365 Q 250 400 160 365 Z" fill="url(#hoodieGrad)" stroke="#334155" stroke-width="5"/>
  <!-- Jacket Zipper / Tech Seam -->
  <line x1="250" y1="375" x2="250" y2="540" stroke="{GOLD}" stroke-width="5" stroke-dasharray="10 6"/>

  <!-- Arms / Hands Layer -->
  {arms_markup}

  <!-- Eyes & Face Expressions (Rendered in Visor) -->
  <g transform="translate(0, 0)">
    {face_expression}
  </g>
</svg>'''

# Poses specifications
poses = {
    "idle_neutral": (
        # Calm, confident eyes + subtle smile
        '''<ellipse cx="205" cy="235" rx="16" ry="20" fill="{cyan}" filter="url(#neonBlur)"/>
           <circle cx="210" cy="228" r="6" fill="#FFFFFF"/>
           <ellipse cx="295" cy="235" rx="16" ry="20" fill="{cyan}" filter="url(#neonBlur)"/>
           <circle cx="300" cy="228" r="6" fill="#FFFFFF"/>
           <path d="M 230 268 Q 250 280 270 268" stroke="{cyan}" stroke-width="5" stroke-linecap="round" fill="none"/>''',
        # Arms resting casually
        '''<path d="M 140 380 Q 90 440 120 520" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>
           <path d="M 360 380 Q 410 440 380 520" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>'''
    ),
    "shocked_jawdrop": (
        # Giant glowing eyes + open mouth
        '''<ellipse cx="195" cy="225" rx="24" ry="30" fill="{cyan}" filter="url(#neonBlur)"/>
           <ellipse cx="305" cy="225" rx="24" ry="30" fill="{cyan}" filter="url(#neonBlur)"/>
           <ellipse cx="250" cy="275" rx="20" ry="24" fill="{cyan}" filter="url(#neonBlur)"/>''',
        # Hands grasping head/hood
        '''<path d="M 120 400 Q 80 240 150 200" stroke="#334155" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="150" cy="200" r="26" fill="{gold}"/>
           <path d="M 380 400 Q 420 240 350 200" stroke="#334155" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="350" cy="200" r="26" fill="{gold}"/>'''
    ),
    "explaining_point": (
        # Confident eyes + right hand pointing up
        '''<ellipse cx="205" cy="230" rx="17" ry="21" fill="{cyan}" filter="url(#neonBlur)"/>
           <ellipse cx="295" cy="230" rx="17" ry="21" fill="{cyan}" filter="url(#neonBlur)"/>
           <path d="M 235 268 Q 250 282 265 268" stroke="{cyan}" stroke-width="6" stroke-linecap="round" fill="none"/>''',
        # Left arm relaxed, right arm raised pointing with glowing fingertip
        '''<path d="M 140 390 Q 90 450 120 520" stroke="#334155" stroke-width="34" stroke-linecap="round" fill="none"/>
           <path d="M 360 400 Q 420 320 400 180" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>
           <circle cx="400" cy="170" r="24" fill="{gold}"/>
           <circle cx="400" cy="150" r="12" fill="{cyan}" filter="url(#neonBlur)"/>'''
    ),
    "laughing_joke": (
        # Crescent laughing eyes (XD) + big grin
        '''<path d="M 185 235 Q 205 210 225 235" stroke="{cyan}" stroke-width="8" stroke-linecap="round" fill="none" filter="url(#neonBlur)"/>
           <path d="M 275 235 Q 295 210 315 235" stroke="{cyan}" stroke-width="8" stroke-linecap="round" fill="none" filter="url(#neonBlur)"/>
           <path d="M 215 260 Q 250 300 285 260 Z" fill="{cyan}" filter="url(#neonBlur)"/>''',
        # Hands holding ribs/stomach
        '''<path d="M 130 400 Q 180 470 230 450" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>
           <path d="M 370 400 Q 320 470 270 450" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>'''
    ),
    "skeptical_sideeye": (
        # One high eyebrow, pupils looking sideways
        '''<path d="M 180 205 Q 205 190 225 205" stroke="{gold}" stroke-width="6" stroke-linecap="round" fill="none"/>
           <ellipse cx="215" cy="235" rx="14" ry="18" fill="{cyan}" filter="url(#neonBlur)"/>
           <ellipse cx="305" cy="235" rx="14" ry="18" fill="{cyan}" filter="url(#neonBlur)"/>
           <line x1="225" y1="270" x2="275" y2="265" stroke="{cyan}" stroke-width="5" stroke-linecap="round"/>''',
        # Folded arms across chest
        '''<path d="M 120 420 Q 250 490 380 420" stroke="#334155" stroke-width="40" stroke-linecap="round" fill="none"/>'''
    ),
    "facepalm": (
        # Hand over face with forehead sweat mark
        '''<ellipse cx="195" cy="235" rx="14" ry="14" fill="{cyan}" opacity="0.4"/>
           <line x1="230" y1="270" x2="265" y2="270" stroke="{cyan}" stroke-width="5" stroke-linecap="round"/>''',
        # Right hand pressed directly against forehead
        '''<path d="M 140 400 Q 100 470 120 520" stroke="#334155" stroke-width="34" stroke-linecap="round" fill="none"/>
           <path d="M 370 420 Q 340 220 270 210" stroke="#334155" stroke-width="38" stroke-linecap="round" fill="none"/>
           <circle cx="260" cy="205" r="30" fill="{gold}"/>'''
    ),
    "secret_whisper": (
        # Winking eye + smirk
        '''<path d="M 185 235 Q 205 220 225 235" stroke="{cyan}" stroke-width="7" stroke-linecap="round" fill="none"/>
           <ellipse cx="295" cy="230" rx="16" ry="20" fill="{cyan}" filter="url(#neonBlur)"/>
           <path d="M 235 270 Q 255 278 275 266" stroke="{cyan}" stroke-width="5" stroke-linecap="round" fill="none"/>''',
        # Hand cupping mouth
        '''<path d="M 140 400 Q 100 460 120 520" stroke="#334155" stroke-width="34" stroke-linecap="round" fill="none"/>
           <path d="M 370 420 Q 320 310 290 290" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>
           <circle cx="295" cy="285" r="25" fill="{gold}"/>'''
    ),
    "angry_triggered": (
        # Angular red eyes + teeth grit
        '''<path d="M 185 210 L 225 225" stroke="#EF4444" stroke-width="7" stroke-linecap="round"/>
           <path d="M 315 210 L 275 225" stroke="#EF4444" stroke-width="7" stroke-linecap="round"/>
           <ellipse cx="205" cy="240" rx="14" ry="16" fill="#EF4444" filter="url(#neonBlur)"/>
           <ellipse cx="295" cy="240" rx="14" ry="16" fill="#EF4444" filter="url(#neonBlur)"/>
           <path d="M 225 275 Q 250 262 275 275" stroke="#EF4444" stroke-width="6" stroke-linecap="round" fill="none"/>''',
        # Clenched fists raised
        '''<path d="M 140 420 Q 90 280 120 250" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>
           <circle cx="120" cy="240" r="26" fill="{gold}"/>
           <path d="M 360 420 Q 410 280 380 250" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>
           <circle cx="380" cy="240" r="26" fill="{gold}"/>'''
    ),
    "hyped_victory": (
        # Star eyes + open joyful mouth
        '''<polygon points="205,215 209,227 222,227 212,235 216,247 205,239 194,247 198,235 188,227 201,227" fill="{gold}" filter="url(#neonBlur)"/>
           <polygon points="295,215 299,227 312,227 302,235 306,247 295,239 284,247 288,235 278,227 291,227" fill="{gold}" filter="url(#neonBlur)"/>
           <ellipse cx="250" cy="275" rx="20" ry="22" fill="{cyan}" filter="url(#neonBlur)"/>''',
        # Both arms high in victory
        '''<path d="M 140 400 Q 60 250 80 160" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>
           <circle cx="80" cy="150" r="26" fill="{gold}"/>
           <path d="M 360 400 Q 440 250 420 160" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>
           <circle cx="420" cy="150" r="26" fill="{gold}"/>'''
    ),
    "thinking_chin": (
        # Eyes looking up curiously + hand on chin
        '''<ellipse cx="205" cy="225" rx="14" ry="18" fill="{cyan}" filter="url(#neonBlur)"/>
           <ellipse cx="295" cy="225" rx="14" ry="18" fill="{cyan}" filter="url(#neonBlur)"/>
           <circle cx="250" cy="272" r="6" fill="{cyan}"/>''',
        # Hand resting under visor chin
        '''<path d="M 140 400 Q 100 460 120 520" stroke="#334155" stroke-width="34" stroke-linecap="round" fill="none"/>
           <path d="M 370 420 Q 340 330 280 300" stroke="#334155" stroke-width="36" stroke-linecap="round" fill="none"/>
           <circle cx="270" cy="300" r="28" fill="{gold}"/>'''
    ),
}

for name, (face, arms) in poses.items():
    formatted_face = face.format(cyan=NEON_CYAN, gold=GOLD)
    formatted_arms = arms.format(cyan=NEON_CYAN, gold=GOLD)
    svg_data = render_mascot(formatted_face, formatted_arms)
    file_path = f"/home/aurel/CODE/Maker/engine/public/avatars/{name}.svg"
    with open(file_path, "w") as f:
        f.write(svg_data)

print("10 Redesigned High-Quality Mascots generated!")
