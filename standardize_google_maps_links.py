#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Maps Links Standardization Script - DISABLED
====================================================
⚠️ WARNING: This script is DISABLED ⚠️

تحذير: هذا السكريبت مُعطَّل
====================================================

This script used to standardize and auto-generate Google Maps links from shop data.
It has been DISABLED per requirement to ensure that all Google Maps locations are manually 
provided via direct Google Maps links only.

كان هذا السكريبت يوحد ويولد روابط خرائط جوجل تلقائياً من بيانات المحلات.
تم تعطيله حسب المتطلبات لضمان أن جميع مواقع خرائط جوجل يتم توفيرها يدوياً فقط 
عبر روابط مباشرة من خرائط جوجل.

DO NOT USE THIS SCRIPT. Location links must be manually provided for each shop.
لا تستخدم هذا السكريبت. يجب توفير روابط المواقع يدوياً لكل محل.
"""

import sys

# Exit immediately with error message
print("=" * 80)
print("⚠️  ERROR: This script is DISABLED")
print("=" * 80)
print()
print("This script used to standardize and auto-generate Google Maps links.")
print("It has been disabled to ensure all locations use manual Google Maps links only.")
print()
print("هذا السكريبت كان يوحد ويولد روابط خرائط جوجل تلقائياً.")
print("تم تعطيله لضمان أن جميع المواقع تستخدم روابط خرائط جوجل اليدوية فقط.")
print()
print("Please provide Google Maps links manually for each shop in shops_details.json")
print("يرجى توفير روابط خرائط جوجل يدوياً لكل محل في shops_details.json")
print("=" * 80)
sys.exit(1)

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
