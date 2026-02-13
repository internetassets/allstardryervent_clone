#!/usr/bin/env python3
"""
Update All Star Dryer Vent location pages:
- Replace hero section with homepage-style (rolling text + contact form)
- Add image strip below hero
"""

import os
import re
from pathlib import Path

# Location config
LOCATIONS = {
    "cold-springs-nevada-dryer-vent-cleaning": {
        "name": "Cold Springs",
        "tagline": "Cold Springs",
        "description": "Cold Springs and the surrounding high-desert communities"
    },
    "hidden-valley-nevada-dryer-vent-cleaning": {
        "name": "Hidden Valley", 
        "tagline": "Hidden Valley",
        "description": "Hidden Valley, South Reno, and surrounding neighborhoods"
    },
    "incline-village-nevada-dryer-vent-cleaning": {
        "name": "Incline Village",
        "tagline": "Incline Village", 
        "description": "Incline Village, Crystal Bay, and Lake Tahoe's North Shore"
    },
    "lockwood-nv-dryer-vent-cleaning": {
        "name": "Lockwood",
        "tagline": "Lockwood",
        "description": "Lockwood, Mustang, and the Truckee Canyon area"
    },
    "minden-nevada-dryer-vent-cleaning": {
        "name": "Minden",
        "tagline": "Carson Valley",
        "description": "Minden, Gardnerville, and the entire Carson Valley"
    },
    "reno-nv-dryer-vent-services": {
        "name": "Reno",
        "tagline": "Reno",
        "description": "Reno, Sparks, and the surrounding high-desert communities"
    },
    "sparks-nevada-dryer-vent-cleaning": {
        "name": "Sparks",
        "tagline": "Sparks",
        "description": "Sparks, Spanish Springs, and Northern Nevada"
    },
    "sun-valley-nv-dryer-vent-cleaning": {
        "name": "Sun Valley",
        "tagline": "Sun Valley",
        "description": "Sun Valley, Lemmon Valley, and North Reno"
    },
    "washoe-valley-nv-dryer-vent-cleaning": {
        "name": "Washoe Valley",
        "tagline": "Washoe Valley",
        "description": "Washoe Valley, New Washoe City, and Pleasant Valley"
    },
}

# CSS additions needed for rolling text
ROLLING_CSS = '''        @keyframes roll {
            0% { opacity: 0; transform: translateY(20px); }
            10% { opacity: 1; transform: translateY(0); }
            30% { opacity: 1; transform: translateY(0); }
            40% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 0; transform: translateY(-20px); }
        }
        .rolling-text span {
            position: absolute;
            opacity: 0;
            animation: roll 6s infinite;
        }
        .rolling-text span:nth-child(1) { color: #0f172a; }
        .rolling-text span:nth-child(2) { animation-delay: 2s; color: #2563eb; }
        .rolling-text span:nth-child(3) { animation-delay: 4s; color: #dc2626; }
        .before-after-img {
            transition: all 0.3s ease;
        }
        .before-after-img:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }'''

def get_new_hero(location_name, tagline, description):
    """Generate new hero section HTML."""
    return f'''<!-- HERO SECTION -->
    <section class="hero-gradient relative overflow-hidden pt-8 pb-12 md:pt-16 md:pb-24">
        <div class="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-16 items-start relative z-10">
            <div class="space-y-8">
                <div class="inline-block bg-white/80 backdrop-blur px-4 py-1 rounded-full border border-blue-100 shadow-sm">
                    <span class="text-blue-600 font-bold text-xs uppercase tracking-widest font-black">🏆 Locally Owned & Operated</span>
                </div>
                <div class="space-y-2">
                    <h1 class="text-5xl md:text-7xl font-black text-slate-900 leading-[0.95] tracking-tighter uppercase">
                        Dryer Vent <br>
                        <div class="rolling-text relative h-[1.1em] overflow-hidden">
                            <span>Restoration</span>
                            <span>Cleaning</span>
                            <span>Repairs</span>
                        </div>
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-900 to-red-600 block pt-2">{tagline}</span>
                    </h1>
                </div>
                <p class="text-xl text-slate-600 leading-relaxed max-w-xl font-medium">
                    Northern Nevada's elite choice for <span class="font-bold text-slate-900">dryer vent cleaning and restoration.</span> Since 2013, we've specialized in professional lint removal and reviving safety across {description}.
                </p>
                <div class="flex flex-col sm:flex-row gap-4">
                    <a href="https://book.housecallpro.com/book/All-Star-Dryer-Vent/1a8d0e15a2844e429147c1c8050bde35?v2=true" class="bg-blue-600 text-white rounded-2xl px-10 py-5 text-xl font-black uppercase tracking-wider shadow-2xl hover:bg-black transition-all hover:-translate-y-1 active:scale-95 inline-block text-center">Book Online Now</a>
                    <a href="tel:7752244136" class="bg-white text-blue-900 border-2 border-blue-900 rounded-2xl px-10 py-5 text-xl font-black uppercase tracking-wider shadow-xl hover:bg-blue-50 transition-all text-center">775-224-4136</a>
                </div>
            </div>
            <div class="relative group">
                <div class="absolute -inset-1 bg-gradient-to-r from-blue-600 to-red-600 rounded-[2.5rem] blur opacity-25 group-hover:opacity-50 transition duration-1000 group-hover:duration-200"></div>
                <div class="relative bg-white p-10 rounded-[2rem] shadow-2xl border border-slate-100">
                    <div class="mb-8 space-y-2">
                        <h2 class="text-3xl font-black text-slate-900 uppercase tracking-tight italic">Service Call Request</h2>
                        <p class="text-slate-500 font-medium text-sm">Send All Star Dryer Vent a message here.</p>
                    </div>
                    <form action="https://api.web3forms.com/submit" method="POST" class="space-y-5">
                        <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
                        <input type="hidden" name="location" value="{location_name}">
                        <input type="checkbox" name="botcheck" class="hidden" style="display: none;">
                        <input type="text" name="name" placeholder="Full Name*" required class="w-full bg-slate-50 border-2 border-slate-100 p-4 rounded-xl focus:border-blue-600 outline-none transition font-semibold">
                        <input type="tel" name="phone" placeholder="Phone Number*" required class="w-full bg-slate-50 border-2 border-slate-100 p-4 rounded-xl focus:border-blue-600 outline-none transition font-semibold">
                        <input type="email" name="email" placeholder="Email Address*" required class="w-full bg-slate-50 border-2 border-slate-100 p-4 rounded-xl focus:border-blue-600 outline-none transition font-semibold">
                        <input type="text" name="postal_code" placeholder="Service Zip Code*" required class="w-full bg-slate-50 border-2 border-slate-100 p-4 rounded-xl focus:border-blue-600 outline-none transition font-semibold">
                        <button type="submit" class="w-full bg-red-600 hover:bg-black text-white font-black text-xl py-5 rounded-2xl shadow-xl uppercase tracking-[0.2em] transition duration-300">Submit Request</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- IMAGE STRIP -->
    <section class="lint-bg border-y border-slate-700 py-10">
        <div class="max-w-[100vw] overflow-hidden">
            <div class="flex flex-wrap justify-center gap-4 px-4">
                <div class="rounded-2xl overflow-hidden shadow-2xl border-2 border-white/20 aspect-square w-24 md:w-52 flex-shrink-0">
                    <img src="../../images/dryer-vent-cover-clean-install-reno.jpg" alt="Professional dryer vent cover installation {location_name} NV" title="New Dryer Vent Cover Installation {location_name}" loading="lazy" width="208" height="208" class="before-after-img w-full h-full object-cover">
                </div>
                <div class="rounded-2xl overflow-hidden shadow-2xl border-2 border-white/20 aspect-square w-24 md:w-52 flex-shrink-0">
                    <img src="../../images/dryer-vent-damaged-before-repair.jpg" alt="Damaged dryer vent before repair {location_name} NV" title="Dryer Vent Damage Assessment {location_name}" loading="lazy" width="208" height="208" class="before-after-img w-full h-full object-cover">
                </div>
                <div class="rounded-2xl overflow-hidden shadow-2xl border-2 border-white/20 aspect-square w-24 md:w-52 flex-shrink-0">
                    <img src="../../images/dryer-duct-inspection-dirty.jpg" alt="Dirty dryer duct inspection {location_name} NV" title="In-Duct Lint Buildup Inspection {location_name}" loading="lazy" width="208" height="208" class="before-after-img w-full h-full object-cover">
                </div>
                <div class="rounded-2xl overflow-hidden shadow-2xl border-2 border-white/20 aspect-square w-24 md:w-52 flex-shrink-0">
                    <img src="../../images/dryer-vent-roof-lint-clog.jpg" alt="Roof dryer vent lint clog removal {location_name} NV" title="Roof Exit Dryer Vent Lint Accumulation {location_name}" loading="lazy" width="208" height="208" class="before-after-img w-full h-full object-cover">
                </div>
                <div class="rounded-2xl overflow-hidden shadow-2xl border-2 border-white/20 aspect-square w-24 md:w-52 flex-shrink-0">
                    <img src="../../images/dryer-vent-exterior-damaged.jpg" alt="Damaged exterior dryer vent cover {location_name} NV" title="Exterior Dryer Vent Cover Damage {location_name}" loading="lazy" width="208" height="208" class="before-after-img w-full h-full object-cover">
                </div>
                <div class="rounded-2xl overflow-hidden shadow-2xl border-2 border-white/20 aspect-square w-24 md:w-52 flex-shrink-0">
                    <img src="../../images/dryer-duct-after-cleaning-sparks.jpg" alt="Clean dryer duct after professional cleaning {location_name} NV" title="Dryer Duct Interior After Professional Cleaning {location_name}" loading="lazy" width="208" height="208" class="before-after-img w-full h-full object-cover">
                </div>
            </div>
        </div>
    </section>'''

def update_location_page(folder_name, config):
    """Update a single location page."""
    filepath = Path(f"locations/{folder_name}/index.html")
    if not filepath.exists():
        print(f"  ❌ File not found: {filepath}")
        return False
    
    content = filepath.read_text(encoding='utf-8')
    original = content
    
    location_name = config["name"]
    tagline = config["tagline"]
    description = config["description"]
    
    # 1. Add rolling-text CSS if not present
    if '.rolling-text' not in content:
        # Insert before </style>
        content = content.replace('</style>', ROLLING_CSS + '\n    </style>')
    
    # 2. Replace hero section
    # Pattern to match old hero section (from <!-- HERO SECTION --> to next section)
    hero_pattern = r'<!-- HERO SECTION -->.*?(?=\n    <!-- SERVICES SECTION -->|\n    <!-- [A-Z]+ SECTION -->)'
    new_hero = get_new_hero(location_name, tagline, description)
    
    if re.search(hero_pattern, content, flags=re.DOTALL):
        content = re.sub(hero_pattern, new_hero + '\n\n', content, flags=re.DOTALL)
    else:
        # Try alternate pattern
        hero_pattern2 = r'<section class="hero-gradient.*?</section>\s*(?=<section)'
        if re.search(hero_pattern2, content, flags=re.DOTALL):
            content = re.sub(hero_pattern2, new_hero + '\n\n    ', content, count=1, flags=re.DOTALL)
    
    # Write back
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        print(f"  ✅ Updated: {location_name}")
        return True
    else:
        print(f"  ⚠️  No changes: {location_name}")
        return False

def main():
    os.chdir("/root/.openclaw/workspace/clients/allstardryervent_clone")
    
    print("🍝 Al Dente's Hero Section Updater")
    print("=" * 50)
    
    updated = 0
    for folder, config in LOCATIONS.items():
        print(f"\n📍 {config['name']}...")
        if update_location_page(folder, config):
            updated += 1
    
    print(f"\n{'=' * 50}")
    print(f"✨ Updated {updated}/{len(LOCATIONS)} location pages")
    print("\nChanges made:")
    print("  • New hero with rolling text animation")
    print("  • Contact form instead of image")
    print("  • Image strip below hero")
    print("  • Location-specific taglines")

if __name__ == "__main__":
    main()
