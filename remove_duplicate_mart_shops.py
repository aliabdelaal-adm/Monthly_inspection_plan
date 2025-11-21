#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to remove duplicate Port Market shops that were added
Keep the original shops and remove the newly added duplicates
"""

import json
import sys
import io

# Ensure UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PORT_MARKET_NAME = "سوق الميناء"

# Original shop IDs that should be kept (from before the sync)
# Using set for O(1) lookup performance
ORIGINAL_PORT_MARKET_IDS = {
    "shop_1762462290355",  # جرين لندز
    "shop_1762462290356",  # معرض الطيور الاليفه
    "shop_1762462290357",  # عصافير الخليج
    "shop_1762462290358",  # جزيرة الاحلام لطيور الزينة
    "shop_1762462290359",  # جراح  للطيور
    "shop_1762462290360",  # أبو سولع  للتجارة
    "shop_1762462290375",  # حباري للحيوانات الأليفة
    "shop_1762462290376",  # بيت الطيور  للأدوية البيطرية
    "shop_1762462290377",  # ابوظبي  للطيور
    "shop_1762462290378",  # الياقوت لطيور الزينة
    "shop_1762462290379",  # العندليب  للأسماك
    "shop_1762462290380",  # زون تايم لطيور الزينة
    "shop_1762462290381",  # الجود للأدوية البيطرية
    "shop_1762465496058",  # محل بيتش فيليج (not in shops_details, likely correct)
}

def main():
    print("=" * 70)
    print("Removing Duplicate Port Market Shops")
    print("=" * 70)
    print()
    
    # Load plan-data.json
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    # Get Port Market shops
    port_market_shops = [shop for shop in plan_data['shops'] if shop.get('area') == PORT_MARKET_NAME]
    
    print(f"Total Port Market shops before cleanup: {len(port_market_shops)}")
    print()
    
    # Find duplicates by license number
    from collections import defaultdict
    shops_by_license = defaultdict(list)
    
    for shop in port_market_shops:
        license = shop.get('license', '')
        if license:
            shops_by_license[license].append(shop)
    
    # Find and remove duplicates
    duplicates_to_remove = []
    kept_shops = []
    
    for license, shops in shops_by_license.items():
        if len(shops) > 1:
            print(f"Found {len(shops)} shops with license {license}:")
            # Sort to prefer original IDs
            shops_sorted = sorted(shops, key=lambda s: s['id'] in ORIGINAL_PORT_MARKET_IDS, reverse=True)
            
            keep_shop = shops_sorted[0]
            kept_shops.append(keep_shop['id'])
            print(f"  ✓ Keeping: {keep_shop['name']} (ID: {keep_shop['id']})")
            
            for shop in shops_sorted[1:]:
                duplicates_to_remove.append(shop['id'])
                print(f"  ✗ Removing: {shop['name']} (ID: {shop['id']})")
            print()
    
    # Remove duplicates from plan-data
    if duplicates_to_remove:
        original_count = len(plan_data['shops'])
        plan_data['shops'] = [shop for shop in plan_data['shops'] if shop['id'] not in duplicates_to_remove]
        removed_count = original_count - len(plan_data['shops'])
        
        # Save updated plan-data.json
        with open('plan-data.json', 'w', encoding='utf-8') as f:
            json.dump(plan_data, f, ensure_ascii=False, indent=2)
        
        print()
        print("=" * 70)
        print(f"✓ Successfully removed {removed_count} duplicate shops")
        print(f"✓ Total shops in plan-data.json: {len(plan_data['shops'])}")
        
        port_market_count = len([s for s in plan_data['shops'] if s.get('area') == PORT_MARKET_NAME])
        print(f"✓ Total Port Market shops: {port_market_count}")
        print("=" * 70)
    else:
        print("✓ No duplicates found to remove")

if __name__ == '__main__':
    main()
