#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Maps Links Standardization Script - PERMANENTLY DISABLED
================================================================
⚠️⚠️⚠️ CRITICAL WARNING: THIS SCRIPT IS PERMANENTLY DISABLED ⚠️⚠️⚠️

تحذير حرج: هذا السكريبت مُعطَّل بشكل دائم
================================================================

**DO NOT MODIFY OR RE-ENABLE THIS SCRIPT WITHOUT EXPLICIT AUTHORIZATION**
**لا تقم بتعديل أو إعادة تفعيل هذا السكريبت بدون إذن صريح**

REASON FOR PERMANENT DISABLE:
This script used to standardize and auto-generate Google Maps links from shop data.
Auto-generated or auto-standardized links do NOT guarantee 100% location accuracy.

سبب التعطيل الدائم:
كان هذا السكريبت يوحد ويولد روابط خرائط جوجل تلقائياً من بيانات المحلات.
الروابط المولدة أو الموحدة تلقائياً لا تضمن دقة 100% للموقع.

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
print("❌ REASON: Auto-standardization does NOT provide 100% accurate locations")
print("❌ السبب: التوحيد التلقائي لا يوفر مواقع دقيقة بنسبة 100%")
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
raise RuntimeError("CRITICAL: Auto-standardization script is permanently disabled. Use manual Google Maps links only.")

# Original code below (kept for reference but never executed due to sys.exit above)
import json
import urllib.parse
import re
from typing import Dict, Any

def extract_coordinates_from_url(url: str) -> tuple:
    """
    Extract coordinates from various Google Maps URL formats.
    
    Args:
        url: Google Maps URL
        
    Returns:
        Tuple of (latitude, longitude) or (None, None) if not found
    """
    # Pattern 1: @lat,lng format
    match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', url)
    if match:
        return float(match.group(1)), float(match.group(2))
    
    # Pattern 2: ?q=lat,lng format
    match = re.search(r'\?q=(-?\d+\.\d+)%2C(-?\d+\.\d+)', url)
    if match:
        return float(match.group(1)), float(match.group(2))
    
    # Pattern 3: ?q=lat,lng without encoding
    match = re.search(r'\?q=(-?\d+\.\d+),(-?\d+\.\d+)', url)
    if match:
        return float(match.group(1)), float(match.group(2))
    
    return None, None

def generate_standard_maps_url(shop_name: str, shop_details: Dict[str, Any], existing_url: str = '') -> str:
    """
    Generates a standardized Google Maps search URL.
    
    If the existing URL contains coordinates, use them for better accuracy.
    Otherwise, use shop information to create a search query.
    
    Args:
        shop_name: The shop name (key in shops_details.json)
        shop_details: Dictionary containing shop information
        existing_url: The existing Google Maps URL (if any)
        
    Returns:
        A standardized Google Maps URL
    """
    # Try to extract coordinates from existing URL
    lat, lng = extract_coordinates_from_url(existing_url) if existing_url else (None, None)
    
    if lat and lng:
        # Use coordinate-based search for accuracy
        search_query = f"{lat},{lng}"
    else:
        # Build search query from shop information
        name_ar = shop_details.get('nameAr', shop_name)
        name_en = shop_details.get('nameEn', '')
        address = shop_details.get('address', '')
        
        search_parts = []
        
        # Use Arabic name as primary identifier
        if name_ar:
            search_parts.append(name_ar)
        
        # Add address for better location accuracy
        if address:
            # Clean up address
            addr_clean = address.replace(',', ' ').strip()
            # Only add first part of address to keep query concise
            addr_parts = addr_clean.split('-')
            if addr_parts:
                search_parts.append(addr_parts[0].strip())
        
        # Always add Abu Dhabi to ensure results are in the right city
        if 'أبو ظبي' not in ' '.join(search_parts) and 'Abu Dhabi' not in ' '.join(search_parts):
            search_parts.append('أبو ظبي')
        
        # Combine search parts
        search_query = ' '.join(search_parts)
    
    # URL encode the search query
    encoded_query = urllib.parse.quote(search_query)
    
    # Create standardized Google Maps search URL using Search API
    maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_query}"
    
    return maps_url

def standardize_all_links():
    """
    Main function to standardize all Google Maps links in shops_details.json
    """
    print("🗺️  Google Maps Links Standardization Tool")
    print("=" * 70)
    
    # Load existing shops data
    print("\n📂 Loading shops_details.json...")
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
    print(f"✅ Loaded {total_shops} shops")
    
    # Categorize links
    stats = {
        'already_standard': 0,
        'updated': 0,
        'kept_coordinates': 0,
        'generated_new': 0,
        'no_link': 0
    }
    
    print("\n🔄 Processing shops...")
    
    for shop_name, shop_info in shops_details.items():
        existing_link = shop_info.get('locationMap', '')
        
        if not existing_link:
            stats['no_link'] += 1
            # Generate new link for shops without one
            new_link = generate_standard_maps_url(shop_name, shop_info)
            shop_info['locationMap'] = new_link
            stats['generated_new'] += 1
            print(f"  ➕ {shop_name}: Generated new link")
        elif 'www.google.com/maps/search/?api=1' in existing_link:
            stats['already_standard'] += 1
            # Already in standard format, keep it
            continue
        else:
            # Need to standardize
            lat, lng = extract_coordinates_from_url(existing_link)
            new_link = generate_standard_maps_url(shop_name, shop_info, existing_link)
            shop_info['locationMap'] = new_link
            stats['updated'] += 1
            
            if lat and lng:
                stats['kept_coordinates'] += 1
                print(f"  ✅ {shop_name}: Standardized (kept coordinates)")
            else:
                print(f"  🔄 {shop_name}: Standardized (used shop info)")
    
    # Save updated data
    print(f"\n💾 Saving updated data to shops_details.json...")
    with open('shops_details.json', 'w', encoding='utf-8') as f:
        json.dump(shops_details, f, ensure_ascii=False, indent=2)
    
    # Print summary
    print("\n" + "=" * 70)
    print("📊 STANDARDIZATION SUMMARY")
    print("=" * 70)
    print(f"🏪 Total shops processed: {total_shops}")
    print(f"✅ Already in standard format: {stats['already_standard']}")
    print(f"🔄 Updated to standard format: {stats['updated']}")
    print(f"   - Preserved coordinates: {stats['kept_coordinates']}")
    print(f"   - Used shop info: {stats['updated'] - stats['kept_coordinates']}")
    print(f"➕ New links generated: {stats['generated_new']}")
    print("=" * 70)
    
    if stats['updated'] + stats['generated_new'] > 0:
        print(f"\n✅ Successfully standardized {stats['updated'] + stats['generated_new']} shop links!")
    else:
        print(f"\n✅ All shop links are already in standard format!")
    
    print("\n💡 All shops now use consistent Google Maps Search API format!")
    
    # Show examples
    print("\n📋 Sample standardized links:")
    count = 0
    for shop_name, shop_info in shops_details.items():
        if count >= 3:
            break
        if shop_info.get('locationMap', ''):
            print(f"\n  Shop: {shop_name}")
            print(f"  Link: {shop_info['locationMap'][:80]}...")
            count += 1

if __name__ == "__main__":
    standardize_all_links()
