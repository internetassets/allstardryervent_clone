#!/usr/bin/env python3
"""
Fix All Star Dryer Vent location pages:
1. Remove SEO Anchors section (links at bottom)
2. Fix meta descriptions (remove HTML tags)
3. Fix canonical URLs per location
4. Replace generic "Reno" references with location-specific names
5. Optimize for local SEO keywords
"""

import os
import re
from pathlib import Path

# Location config: folder name -> (display name, slug for canonical, neighborhoods)
LOCATIONS = {
    "cold-springs-nevada-dryer-vent-cleaning": {
        "name": "Cold Springs",
        "canonical": "cold-springs-nevada-dryer-vent-cleaning",
        "neighborhoods": ["Estates at Cold Springs", "Sierra Reflections", "Countryside Estates", "Mountain View", "Cold Springs Valley", "Bordertown"],
        "nearby": "near Reno"
    },
    "hidden-valley-nevada-dryer-vent-cleaning": {
        "name": "Hidden Valley",
        "canonical": "hidden-valley-nevada-dryer-vent-cleaning",
        "neighborhoods": ["Hidden Valley Ranch", "Hidden Valley Highlands", "Rolling Hills", "Lakeridge", "South Reno"],
        "nearby": "near Reno"
    },
    "incline-village-nevada-dryer-vent-cleaning": {
        "name": "Incline Village",
        "canonical": "incline-village-nevada-dryer-vent-cleaning",
        "neighborhoods": ["Crystal Bay", "Lakeshore", "Mill Creek", "Tyner", "Ponderosa", "Ski Way"],
        "nearby": "at Lake Tahoe"
    },
    "lockwood-nv-dryer-vent-cleaning": {
        "name": "Lockwood",
        "canonical": "lockwood-nv-dryer-vent-cleaning",
        "neighborhoods": ["Lockwood Valley", "Patrick", "Mustang", "Vista", "Tracy Clark"],
        "nearby": "near Reno"
    },
    "minden-nevada-dryer-vent-cleaning": {
        "name": "Minden",
        "canonical": "minden-nevada-dryer-vent-cleaning",
        "neighborhoods": ["Gardnerville", "Gardnerville Ranchos", "Johnson Lane", "Genoa", "Carson Valley", "Topaz Lake"],
        "nearby": "in Carson Valley"
    },
    "reno-nv-dryer-vent-services": {
        "name": "Reno",
        "canonical": "reno-nv-dryer-vent-services",
        "neighborhoods": ["Midtown", "Downtown", "South Reno", "Northwest Reno", "Somersett", "Damonte Ranch", "Double Diamond", "Caughlin Ranch", "University District", "Old Southwest", "Galena Forest", "Arrowcreek"],
        "nearby": ""
    },
    "sparks-nevada-dryer-vent-cleaning": {
        "name": "Sparks",
        "canonical": "sparks-nevada-dryer-vent-cleaning",
        "neighborhoods": ["Spanish Springs", "Wingfield Springs", "D'Andrea", "Victorian Square", "Sparks Marina", "Wedekind", "Los Altos"],
        "nearby": "near Reno"
    },
    "sun-valley-nv-dryer-vent-cleaning": {
        "name": "Sun Valley",
        "canonical": "sun-valley-nv-dryer-vent-cleaning",
        "neighborhoods": ["Sun Valley General Improvement District", "El Rancho", "Golden Valley", "Lemmon Valley", "Stead"],
        "nearby": "near Reno"
    },
    "washoe-valley-nv-dryer-vent-cleaning": {
        "name": "Washoe Valley",
        "canonical": "washoe-valley-nv-dryer-vent-cleaning",
        "neighborhoods": ["New Washoe City", "Washoe City", "Pleasant Valley", "Bower's Mansion", "Davis Creek"],
        "nearby": "between Reno and Carson City"
    },
}

def fix_location_page(folder_name, config):
    """Fix a single location page."""
    filepath = Path(f"locations/{folder_name}/index.html")
    if not filepath.exists():
        print(f"  ❌ File not found: {filepath}")
        return False
    
    content = filepath.read_text(encoding='utf-8')
    original = content
    location = config["name"]
    canonical_slug = config["canonical"]
    neighborhoods = config["neighborhoods"]
    
    # 1. Fix meta description - remove HTML tags, make it clean
    meta_pattern = r'<meta name="description" content="[^"]*">'
    new_meta = f'<meta name="description" content="Professional dryer vent cleaning, repair & restoration in {location}, NV. Prevent house fires, reduce energy bills, and extend dryer life. CSIA certified. Locally owned since 2013. Call 775-224-4136.">'
    content = re.sub(meta_pattern, new_meta, content)
    
    # 2. Fix canonical URL
    canonical_pattern = r'<link rel="canonical" href="[^"]*" />'
    new_canonical = f'<link rel="canonical" href="https://allstardryervent.com/locations/{canonical_slug}/" />'
    content = re.sub(canonical_pattern, new_canonical, content)
    
    # 3. Remove SEO Anchors section
    seo_anchors_pattern = r'<!-- SEO ANCHORS -->\s*<section class="max-w-7xl mx-auto px-6 py-12 border-t border-slate-100 text-center font-black">.*?</section>'
    content = re.sub(seo_anchors_pattern, '', content, flags=re.DOTALL)
    
    # 4. Fix title to include repair/restoration keywords
    title_pattern = r'<title>[^<]*Dryer Vent Cleaning[^<]*</title>'
    new_title = f'<title>{location} Dryer Vent Cleaning, Repair & Restoration | All Star NV</title>'
    content = re.sub(title_pattern, new_title, content)
    
    # 5. Update neighborhoods section if exists (for Sparks and others)
    if location != "Reno":
        # Replace Reno neighborhoods section with location-specific
        old_neighborhoods_section = r'<h2 class="text-3xl md:text-4xl font-black text-blue-900 tracking-tighter uppercase">Reno Neighborhoods.*?</section>'
        
        neighborhood_divs = '\n            '.join([
            f'<div class="bg-slate-100 p-4 rounded-xl font-bold text-slate-700">{n}</div>'
            for n in neighborhoods[:12]  # Limit to 12
        ])
        
        new_neighborhoods = f'''<h2 class="text-3xl md:text-4xl font-black text-blue-900 tracking-tighter uppercase">{location} Areas <br class="md:hidden">We Serve</h2>
            <p class="text-slate-600 mt-4">Professional dryer vent cleaning, repair & restoration throughout {location}, NV</p>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4 text-center">
            {neighborhood_divs}
        </div>
    </section>'''
        content = re.sub(old_neighborhoods_section, new_neighborhoods, content, flags=re.DOTALL)
    
    # 6. Fix H1 to include repair/restoration
    h1_pattern = rf'<h1[^>]*>\s*{re.escape(location)} Dryer Vent Cleaning\s*</h1>'
    new_h1 = f'''<h1 class="text-5xl md:text-6xl lg:text-7xl font-black text-slate-900 leading-[0.95] tracking-tighter uppercase font-black">
                    {location} Dryer Vent Cleaning & Repair
                </h1>'''
    content = re.sub(h1_pattern, new_h1, content, flags=re.IGNORECASE)
    
    # 7. Replace "Reno" with location name in body content (careful not to break links)
    # Only replace in text content, not in URLs or location menu
    if location != "Reno":
        # Replace "Reno's" with location's
        content = re.sub(r"Reno's Best Choice", f"{location}'s Best Choice", content)
        content = re.sub(r"Reno's trusted", f"{location}'s trusted", content)
        content = re.sub(r"Reno's dry climate", f"Northern Nevada's dry climate", content)
        
        # Replace "Reno homeowners" etc
        content = re.sub(r"Reno homeowners", f"{location} homeowners", content)
        content = re.sub(r"Reno residents", f"{location} residents", content)
        content = re.sub(r"Reno homes", f"{location} homes", content)
        content = re.sub(r"Reno property", f"{location} property", content)
        content = re.sub(r"Reno pet owners", f"{location} pet owners", content)
        
        # Replace in service card descriptions
        content = re.sub(r"older Reno systems", f"older {location} systems", content)
        content = re.sub(r"Reno's climate", f"Northern Nevada's climate", content)
        content = re.sub(r"new Reno construction", f"new {location} construction", content)
        content = re.sub(r"Reno real estate", f"{location} real estate", content)
        
        # Replace "in Reno" (but not URLs)
        content = re.sub(r"in Reno(?![/-])", f"in {location}", content)
        content = re.sub(r"for Reno(?![/-])", f"for {location}", content)
        
        # Section headers
        content = re.sub(r"Premium Reno Care", f"Premium {location} Care", content)
        content = re.sub(r"Why Reno Homeowners", f"Why {location} Homeowners", content)
        
        # NV Energy reference - keep as generic
        content = re.sub(r"NV Energy bills", "energy bills", content)
        
    # Write back
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        print(f"  ✅ Fixed: {location}")
        return True
    else:
        print(f"  ⚠️  No changes needed: {location}")
        return False

def main():
    os.chdir("/root/.openclaw/workspace/clients/allstardryervent_clone")
    
    print("🍝 Al Dente's Location Page Optimizer")
    print("=" * 50)
    
    fixed = 0
    for folder, config in LOCATIONS.items():
        print(f"\n📍 {config['name']}...")
        if fix_location_page(folder, config):
            fixed += 1
    
    print(f"\n{'=' * 50}")
    print(f"✨ Fixed {fixed}/{len(LOCATIONS)} location pages")
    print("\nChanges made:")
    print("  • Removed SEO anchors section (bottom links)")
    print("  • Fixed meta descriptions (removed HTML)")
    print("  • Fixed canonical URLs per location")
    print("  • Added repair/restoration to titles & H1s")
    print("  • Replaced generic 'Reno' with location names")

if __name__ == "__main__":
    main()
