import os

os.makedirs('/home/aurel/CODE/Maker/engine/public/illustrations', exist_ok=True)

# 1. Eiffel Tower Blueprint Card
svg1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" width="100%" height="100%">
  <rect x="10" y="10" width="580" height="430" rx="28" fill="#1E293B" stroke="#38BDF8" stroke-width="4" opacity="0.95"/>
  <rect x="25" y="25" width="550" height="400" rx="20" fill="#0F172A" stroke="#1E293B" stroke-width="2"/>
  
  <!-- Stamp / Badge -->
  <rect x="420" y="45" width="130" height="45" rx="10" fill="#EF4444" opacity="0.9"/>
  <text x="485" y="74" fill="#FFFFFF" font-family="sans-serif" font-weight="900" font-size="20" text-anchor="middle">TOP SECRET</text>

  <!-- Eiffel Tower Graphic Silhouette -->
  <path d="M 300 60 L 310 160 L 335 290 L 380 390 L 350 390 L 330 330 Q 300 340 270 330 L 250 390 L 220 390 L 265 290 L 290 160 Z" fill="none" stroke="#FBBF24" stroke-width="6"/>
  <line x1="285" y1="180" x2="315" y2="180" stroke="#FBBF24" stroke-width="5"/>
  <line x1="265" y1="290" x2="335" y2="290" stroke="#FBBF24" stroke-width="5"/>
  <path d="M 270 330 Q 300 345 330 330" stroke="#FBBF24" stroke-width="5" fill="none"/>
  
  <text x="300" y="415" fill="#38BDF8" font-family="sans-serif" font-weight="800" font-size="24" text-anchor="middle" letter-spacing="4">PARIS, 1889 - 7 300 TONNES</text>
</svg>'''

# 2. 1925 Vintage Newspaper
svg2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" width="100%" height="100%">
  <rect x="10" y="10" width="580" height="430" rx="24" fill="#F5F5F0" stroke="#D4D4D8" stroke-width="6" opacity="0.98"/>
  
  <!-- Newspaper Header -->
  <text x="300" y="65" fill="#18181B" font-family="serif" font-weight="900" font-size="44" text-anchor="middle" letter-spacing="2">LE JOURNAL DE PARIS</text>
  <line x1="40" y1="85" x2="560" y2="85" stroke="#18181B" stroke-width="3"/>
  <text x="300" y="105" fill="#52525B" font-family="sans-serif" font-size="16" text-anchor="middle">ÉDITION SPÉCIALE DU 14 MAI 1925 • PRIX : 25 CENTIMES</text>
  <line x1="40" y1="115" x2="560" y2="115" stroke="#18181B" stroke-width="2"/>

  <!-- Headline -->
  <text x="300" y="165" fill="#DC2626" font-family="sans-serif" font-weight="900" font-size="34" text-anchor="middle">LA TOUR EIFFEL EN DÉMOLITION ?</text>
  <text x="300" y="200" fill="#27272A" font-family="serif" font-style="italic" font-size="20" text-anchor="middle">Le coût exorbitant des réparations pousse l'État à la vente.</text>

  <!-- Article Columns Mockup -->
  <line x1="300" y1="220" x2="300" y2="400" stroke="#E4E4E7" stroke-width="2"/>
  <rect x="50" y="230" width="230" height="12" fill="#71717A" rx="3"/>
  <rect x="50" y="255" width="230" height="12" fill="#A1A1AA" rx="3"/>
  <rect x="50" y="280" width="230" height="12" fill="#A1A1AA" rx="3"/>
  <rect x="50" y="305" width="180" height="12" fill="#A1A1AA" rx="3"/>

  <rect x="320" y="230" width="230" height="12" fill="#71717A" rx="3"/>
  <rect x="320" y="255" width="230" height="12" fill="#A1A1AA" rx="3"/>
  <rect x="320" y="280" width="230" height="12" fill="#A1A1AA" rx="3"/>
  <rect x="320" y="305" width="190" height="12" fill="#A1A1AA" rx="3"/>

  <!-- Stamp -->
  <rect x="360" y="340" width="190" height="60" rx="12" fill="none" stroke="#DC2626" stroke-width="4" transform="rotate(-6 450 370)"/>
  <text x="455" y="380" fill="#DC2626" font-family="sans-serif" font-weight="900" font-size="26" text-anchor="middle" transform="rotate(-6 450 370)">FAUSSE ALERTE</text>
</svg>'''

# 3. Scrap Metal & Money Caper
svg3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" width="100%" height="100%">
  <rect x="10" y="10" width="580" height="430" rx="28" fill="#18181B" stroke="#F59E0B" stroke-width="4" opacity="0.95"/>
  
  <circle cx="300" cy="200" r="120" fill="#F59E0B" opacity="0.15"/>

  <!-- Steel Girders Icon -->
  <rect x="180" y="160" width="240" height="30" rx="8" fill="#71717A" stroke="#F4F4F5" stroke-width="2"/>
  <rect x="160" y="210" width="280" height="30" rx="8" fill="#71717A" stroke="#F4F4F5" stroke-width="2"/>
  <rect x="200" y="260" width="200" height="30" rx="8" fill="#71717A" stroke="#F4F4F5" stroke-width="2"/>

  <!-- Bank Check Stamp -->
  <rect x="130" y="80" width="340" height="60" rx="16" fill="#10B981" opacity="0.9"/>
  <text x="300" y="120" fill="#FFFFFF" font-family="sans-serif" font-weight="900" font-size="28" text-anchor="middle">CHÈQUE ENCAISSÉ : 250 000 F</text>

  <text x="300" y="350" fill="#F59E0B" font-family="sans-serif" font-weight="900" font-size="32" text-anchor="middle">L'ARNAQUE DU SIÈCLE</text>
  <text x="300" y="390" fill="#A1A1AA" font-family="sans-serif" font-size="18" text-anchor="middle">Victor Lustig vend du vent à des industriels crédules</text>
</svg>'''

# 4. Paris-Vienna Train Ticket
svg4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" width="100%" height="100%">
  <rect x="10" y="10" width="580" height="430" rx="28" fill="#1E1B4B" stroke="#A855F7" stroke-width="4" opacity="0.95"/>

  <!-- Ticket Shape -->
  <rect x="50" y="70" width="500" height="280" rx="20" fill="#312E81" stroke="#818CF8" stroke-width="3"/>
  <circle cx="50" cy="210" r="25" fill="#1E1B4B"/>
  <circle cx="550" cy="210" r="25" fill="#1E1B4B"/>
  <line x1="200" y1="70" x2="200" y2="350" stroke="#818CF8" stroke-width="3" stroke-dasharray="10 8"/>

  <!-- Left Ticket Stub -->
  <text x="125" y="150" fill="#FBBF24" font-family="sans-serif" font-weight="900" font-size="36" text-anchor="middle">1ÈRE</text>
  <text x="125" y="190" fill="#FFFFFF" font-family="sans-serif" font-size="18" text-anchor="middle">CLASSE</text>
  <text x="125" y="270" fill="#A5B4FC" font-family="monospace" font-size="16" text-anchor="middle">#VL-1925</text>

  <!-- Right Ticket Info -->
  <text x="240" y="140" fill="#93C5FD" font-family="sans-serif" font-size="18">DÉPART :</text>
  <text x="240" y="175" fill="#FFFFFF" font-family="sans-serif" font-weight="900" font-size="28">PARIS GARE DE L'EST</text>

  <text x="240" y="230" fill="#93C5FD" font-family="sans-serif" font-size="18">DESTINATION :</text>
  <text x="240" y="265" fill="#34D399" font-family="sans-serif" font-weight="900" font-size="28">VIENNE (AUTRICHE)</text>

  <text x="300" y="400" fill="#FBBF24" font-family="sans-serif" font-weight="900" font-size="28" text-anchor="middle">ET IL A REBOUCLÉ LE CRIME...</text>
</svg>'''

files = [
    ('illustration_scene_1.svg', svg1),
    ('illustration_scene_2.svg', svg2),
    ('illustration_scene_3.svg', svg3),
    ('illustration_scene_4.svg', svg4),
]

for name, content in files:
    path = f"/home/aurel/CODE/Maker/engine/public/illustrations/{name}"
    with open(path, "w") as f:
        f.write(content)
    print(f"Created {path}")
