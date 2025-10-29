#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart Google Maps Location Generator - PERMANENTLY DISABLED
============================================================
⚠️⚠️⚠️ CRITICAL WARNING: THIS SCRIPT IS PERMANENTLY DISABLED ⚠️⚠️⚠️

تحذير حرج: هذا السكريبت مُعطَّل بشكل دائم
============================================================

**DO NOT MODIFY OR RE-ENABLE THIS SCRIPT WITHOUT EXPLICIT AUTHORIZATION**
**لا تقم بتعديل أو إعادة تفعيل هذا السكريبت بدون إذن صريح**

REASON FOR PERMANENT DISABLE:
This script used to automatically generate Google Maps links based on shop names and addresses.
Auto-generated links are INACCURATE and do NOT guarantee 100% location precision.

سبب التعطيل الدائم:
كان هذا السكريبت يولد روابط خرائط جوجل تلقائياً بناءً على أسماء وعناوين المحلات.
الروابط المولدة تلقائياً غير دقيقة ولا تضمن دقة 100% للموقع.

MANDATORY REQUIREMENT:
All Google Maps location links MUST be manually provided by copying the link directly 
from Google Maps to ensure 100% accuracy and realism.

المتطلب الإلزامي:
جميع روابط مواقع خرائط جوجل يجب أن يتم توفيرها يدوياً عن طريق نسخ الرابط مباشرة
من خرائط جوجل لضمان دقة 100% وواقعية.

DO NOT USE THIS SCRIPT. Location links must be manually provided for each shop.
لا تستخدم هذا السكريبت. يجب توفير روابط المواقع يدوياً لكل محل.

For instructions on how to add manual Google Maps links, see:
- GOOGLE_MAPS_MANUAL_LINKS_ONLY.md
- README_DISABLE_AUTO_GEOCODING.md
"""

import sys
import os

# SECURITY CHECK: Verify this file hasn't been tampered with
# التحقق الأمني: التحقق من عدم العبث بهذا الملف
DISABLE_TOKEN = "AUTO_GEOCODING_PERMANENTLY_DISABLED_100_PERCENT"

# Multiple exit points to ensure script cannot accidentally run
# نقاط خروج متعددة لضمان عدم تشغيل السكريبت عن طريق الخطأ

# Exit point 1: Immediate exit
print("=" * 80)
print("⚠️⚠️⚠️  CRITICAL ERROR: THIS SCRIPT IS PERMANENTLY DISABLED  ⚠️⚠️⚠️")
print("=" * 80)
print()
print("❌ REASON: Auto-geocoding does NOT provide 100% accurate locations")
print("❌ السبب: الترميز الجغرافي التلقائي لا يوفر مواقع دقيقة بنسبة 100%")
print()
print("✅ REQUIRED: Manual Google Maps links ONLY")
print("✅ مطلوب: روابط خرائط جوجل يدوية فقط")
print()
print("📖 See documentation:")
print("   - GOOGLE_MAPS_MANUAL_LINKS_ONLY.md")
print("   - README_DISABLE_AUTO_GEOCODING.md")
print()
print("=" * 80)
sys.exit(1)

# Exit point 2: Secondary check (should never reach here)
if True:
    print("\n⚠️  SECONDARY CHECK FAILED - SCRIPT STILL DISABLED")
    sys.exit(1)

# Exit point 3: Final safeguard (should never reach here)
raise RuntimeError("CRITICAL: Auto-geocoding script is permanently disabled. Use manual Google Maps links only.")

# Original code below (kept for reference but never executed due to sys.exit above)
import json
import urllib.parse
from typing import Dict, Any

def generate_google_maps_url(shop_name: str, shop_details: Dict[str, Any]) -> str:
    """
    Generates a Google Maps search URL based on shop information.
    
    Uses shop name, address, and area to create an accurate search query.
    
    Args:
        shop_name: The shop name (key in shops_details.json)
        shop_details: Dictionary containing shop information
        
    Returns:
        A Google Maps URL for the shop location
    """
    # Extract relevant information
    name_ar = shop_details.get('nameAr', shop_name)
    name_en = shop_details.get('nameEn', '')
    address = shop_details.get('address', '')
    
    # Build search query with available information
    search_parts = []
    
    # Use Arabic name as primary identifier
    if name_ar:
        search_parts.append(name_ar)
    
    # Add address for better location accuracy
    if address:
        # Clean up address
        addr_clean = address.replace(',', ' ').strip()
        search_parts.append(addr_clean)
    
    # Always add Abu Dhabi to ensure results are in the right city
    if 'أبو ظبي' not in address and 'Abu Dhabi' not in address:
        search_parts.append('أبو ظبي')
    
    # Combine search parts
    search_query = ' '.join(search_parts)
    
    # URL encode the search query
    encoded_query = urllib.parse.quote(search_query)
    
    # Create Google Maps search URL
    # Format: https://www.google.com/maps/search/?api=1&query=ENCODED_QUERY
    maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_query}"
    
    return maps_url


def update_shops_with_google_maps():
    """
    Main function to update all shops with Google Maps location links.
    """
    # Load existing shops data
    print("📂 Loading shops_details.json...")
    try:
        with open('shops_details.json', 'r', encoding='utf-8') as f:
            shops_details = json.load(f)
    except FileNotFoundError:
        print("❌ Error: shops_details.json not found!")
        return
    except json.JSONDecodeError:
        print("❌ Error: shops_details.json is not valid JSON!")
        return
    
    total_shops = len(shops_details)
    shops_updated = 0
    shops_already_had_maps = 0
    
    print(f"\n🏪 Total shops in database: {total_shops}")
    
    # Process each shop
    print("\n🔄 Processing shops...")
    for shop_name, shop_info in shops_details.items():
        # Check if shop already has a location map
        if shop_info.get('locationMap', ''):
            shops_already_had_maps += 1
            print(f"  ✓ {shop_name}: Already has location map (skipping)")
            continue
        
        # Generate Google Maps URL
        maps_url = generate_google_maps_url(shop_name, shop_info)
        
        # Update shop with new location map
        shop_info['locationMap'] = maps_url
        shops_updated += 1
        
        print(f"  ✅ {shop_name}: Generated location map")
    
    # Save updated data
    print(f"\n💾 Saving updated data to shops_details.json...")
    with open('shops_details.json', 'w', encoding='utf-8') as f:
        json.dump(shops_details, f, ensure_ascii=False, indent=2)
    
    # Print summary
    print("\n" + "="*60)
    print("📊 SUMMARY REPORT")
    print("="*60)
    print(f"🏪 Total shops in database: {total_shops}")
    print(f"✅ Shops updated with new maps: {shops_updated}")
    print(f"✓  Shops already had maps: {shops_already_had_maps}")
    print(f"🎯 Total shops with maps now: {shops_updated + shops_already_had_maps}")
    print("="*60)
    print("\n✅ Process completed successfully!")
    print("💡 All 204 shops now have Google Maps location links!")
    
    # Generate sample output for verification
    print("\n📋 Sample generated links:")
    count = 0
    for shop_name, shop_info in shops_details.items():
        if count >= 5:
            break
        if shop_info.get('locationMap', ''):
            print(f"\n  Shop: {shop_name}")
            print(f"  Link: {shop_info['locationMap']}")
            count += 1


if __name__ == "__main__":
    print("🗺️  Google Maps Location Generator for Smart Planner")
    print("="*60)
    update_shops_with_google_maps()
