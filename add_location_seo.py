#!/usr/bin/env python3
"""
Add SEO-optimized intro section to location pages after hero.
Focus on dryer vent keywords, avoid air duct confusion.
"""

import os
import re
from pathlib import Path

LOCATIONS = {
    "cold-springs-nevada-dryer-vent-cleaning": {
        "name": "Cold Springs",
        "neighborhoods": "Estates at Cold Springs, Sierra Reflections, and Bordertown",
        "nearby": "Cold Springs and North Valleys"
    },
    "hidden-valley-nevada-dryer-vent-cleaning": {
        "name": "Hidden Valley",
        "neighborhoods": "Hidden Valley, Lakeridge, and South Reno",
        "nearby": "Hidden Valley and surrounding South Reno neighborhoods"
    },
    "incline-village-nevada-dryer-vent-cleaning": {
        "name": "Incline Village",
        "neighborhoods": "Crystal Bay, Lakeshore, and North Lake Tahoe",
        "nearby": "Incline Village and Lake Tahoe's North Shore"
    },
    "lockwood-nv-dryer-vent-cleaning": {
        "name": "Lockwood",
        "neighborhoods": "Lockwood, Mustang, and the Truckee Canyon",
        "nearby": "Lockwood and Eastern Washoe County"
    },
    "minden-nevada-dryer-vent-cleaning": {
        "name": "Minden",
        "neighborhoods": "Gardnerville, Johnson Lane, and Genoa",
        "nearby": "Minden, Gardnerville, and the entire Carson Valley"
    },
    "reno-nv-dryer-vent-services": {
        "name": "Reno",
        "neighborhoods": "Midtown, South Reno, Somersett, and Damonte Ranch",
        "nearby": "Reno and all of Washoe County"
    },
    "sparks-nevada-dryer-vent-cleaning": {
        "name": "Sparks",
        "neighborhoods": "Spanish Springs, Wingfield Springs, and D'Andrea",
        "nearby": "Sparks and the Spanish Springs Valley"
    },
    "sun-valley-nv-dryer-vent-cleaning": {
        "name": "Sun Valley",
        "neighborhoods": "Sun Valley, Lemmon Valley, and Golden Valley",
        "nearby": "Sun Valley and North Reno"
    },
    "washoe-valley-nv-dryer-vent-cleaning": {
        "name": "Washoe Valley",
        "neighborhoods": "New Washoe City, Pleasant Valley, and Bower's Mansion",
        "nearby": "Washoe Valley and the area between Reno and Carson City"
    },
}

def get_seo_section(name, neighborhoods, nearby):
    return f'''
    <!-- LOCAL SEO SECTION -->
    <section class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-200">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
            <div class="space-y-6">
                <h2 class="text-3xl md:text-4xl font-black text-blue-900 tracking-tighter uppercase">{name} Dryer Vent Cleaning Experts</h2>
                <p class="text-lg text-slate-600 leading-relaxed">All Star provides professional <strong class="text-slate-900">dryer vent cleaning in {name}</strong>, NV and surrounding areas including {neighborhoods}. Our {name} dryer vent cleaning service includes complete lint removal, airflow testing, and thorough safety inspection.</p>
                <div class="grid grid-cols-2 gap-4">
                    <div class="flex items-start gap-3">
                        <span class="text-2xl">✓</span>
                        <div>
                            <h3 class="font-black text-blue-900 text-sm uppercase">Dryer Vent Cleaning</h3>
                            <p class="text-xs text-slate-600">Complete lint extraction</p>
                        </div>
                    </div>
                    <div class="flex items-start gap-3">
                        <span class="text-2xl">✓</span>
                        <div>
                            <h3 class="font-black text-blue-900 text-sm uppercase">Dryer Duct Repair</h3>
                            <p class="text-xs text-slate-600">Damaged vent restoration</p>
                        </div>
                    </div>
                    <div class="flex items-start gap-3">
                        <span class="text-2xl">✓</span>
                        <div>
                            <h3 class="font-black text-blue-900 text-sm uppercase">Dryer Vent Install</h3>
                            <p class="text-xs text-slate-600">Code-compliant systems</p>
                        </div>
                    </div>
                    <div class="flex items-start gap-3">
                        <span class="text-2xl">✓</span>
                        <div>
                            <h3 class="font-black text-blue-900 text-sm uppercase">Safety Inspection</h3>
                            <p class="text-xs text-slate-600">12-point fire prevention</p>
                        </div>
                    </div>
                </div>
                <p class="text-slate-600">Serving {nearby} with same-day appointments available. <strong>Call 775-224-4136</strong> for your free estimate.</p>
            </div>
            <div class="relative">
                <img src="../../images/dryer-vent-cover-clean-install-reno.jpg" alt="Dryer vent cleaning {name} NV - professional lint removal service" class="rounded-2xl shadow-xl w-full">
            </div>
        </div>
    </section>
'''

def update_location(folder, config):
    filepath = Path(f"locations/{folder}/index.html")
    if not filepath.exists():
        print(f"  ❌ Not found: {filepath}")
        return False
    
    content = filepath.read_text()
    
    # Check if already added
    if '<!-- LOCAL SEO SECTION -->' in content:
        print(f"  ⏭️  Already has SEO section: {config['name']}")
        return False
    
    # Find the SERVICES SECTION and insert before it
    seo_section = get_seo_section(config['name'], config['neighborhoods'], config['nearby'])
    
    if '<!-- SERVICES SECTION -->' in content:
        content = content.replace(
            '<!-- SERVICES SECTION -->',
            seo_section + '\n    <!-- SERVICES SECTION -->'
        )
        filepath.write_text(content)
        print(f"  ✅ Added SEO section: {config['name']}")
        return True
    else:
        print(f"  ⚠️  No SERVICES SECTION marker: {config['name']}")
        return False

def main():
    os.chdir("/root/.openclaw/workspace/clients/allstardryervent_clone")
    print("🍝 Adding Local SEO Sections to Location Pages")
    print("=" * 50)
    
    updated = 0
    for folder, config in LOCATIONS.items():
        if update_location(folder, config):
            updated += 1
    
    print(f"\n{'=' * 50}")
    print(f"✨ Updated {updated}/{len(LOCATIONS)} pages")

if __name__ == "__main__":
    main()
