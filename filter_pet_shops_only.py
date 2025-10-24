#!/usr/bin/env python3
"""
Filter shops_details.json to keep only pet-related shops.
This script identifies shops with pet-related activities and removes all others.
"""

import json
import shutil
from datetime import datetime

def is_pet_related(activity, shop_name=''):
    """Check if an activity or shop name is related to pets/animals"""
    if not activity and not shop_name:
        return False
    
    text_to_check = f"{activity} {shop_name}".lower()
    pet_keywords = [
        'حيوان', 'طير', 'عصافير', 'كلاب', 'قطط', 'أسماك', 'اسماك',
        'حباري', 'صقور', 'طيور', 'زينة', 'اليفة', 'بيطري', 'فندق',
        'pet', 'bird', 'animal', 'fish', 'veterinary', 'avian',
        'صالون', 'salon', 'بت', 'بيت', 'hotel', 'care', 'منتجات',
        'paw', 'وف', 'كلاود'  # Pet-related business names
    ]
    
    return any(keyword in text_to_check for keyword in pet_keywords)

def main():
    print("=" * 80)
    print("FILTERING SHOPS_DETAILS.JSON - KEEPING ONLY PET SHOPS")
    print("=" * 80)
    
    # Load existing shops_details.json
    print("\n[1/5] Loading shops_details.json...")
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    print(f"   ✓ Loaded {len(shops_details)} shops")
    
    # Create backup
    backup_filename = f'shops_details.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    print(f"\n[2/5] Creating backup: {backup_filename}")
    shutil.copy2('shops_details.json', backup_filename)
    print("   ✓ Backup created")
    
    # Filter pet-related shops
    print("\n[3/5] Filtering pet-related shops...")
    pet_shops = {}
    non_pet_shops = {}
    
    for shop_name, shop_data in shops_details.items():
        activity = shop_data.get('activity', '')
        if is_pet_related(activity, shop_name):
            pet_shops[shop_name] = shop_data
        else:
            non_pet_shops[shop_name] = shop_data
    
    print(f"   ✓ Found {len(pet_shops)} pet-related shops")
    print(f"   ✓ Found {len(non_pet_shops)} non-pet shops to remove")
    
    # Display some shops being removed
    if non_pet_shops:
        print("\n   Shops being removed (non-pet related):")
        for i, (name, data) in enumerate(list(non_pet_shops.items())[:10], 1):
            activity = data.get('activity', 'N/A')
            print(f"   {i}. {name} - Activity: {activity}")
        if len(non_pet_shops) > 10:
            print(f"   ... and {len(non_pet_shops) - 10} more")
    
    # Save filtered shops_details.json
    print(f"\n[4/5] Saving filtered shops_details.json...")
    with open('shops_details.json', 'w', encoding='utf-8') as f:
        json.dump(pet_shops, f, ensure_ascii=False, indent=2)
    print(f"   ✓ Saved {len(pet_shops)} pet shops")
    
    # Summary
    print("\n[5/5] SUMMARY")
    print("=" * 80)
    print(f"Total shops before filtering: {len(shops_details)}")
    print(f"Pet shops kept: {len(pet_shops)}")
    print(f"Non-pet shops removed: {len(non_pet_shops)}")
    print(f"Backup file: {backup_filename}")
    print("=" * 80)
    print("\n✅ Filtering complete!")

if __name__ == '__main__':
    main()
