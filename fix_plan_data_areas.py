#!/usr/bin/env python3
"""
Fix plan-data.json by adding missing 'area' field to all shops.
Maps areaId to area name from the areas list.
"""

import json
import shutil
from datetime import datetime

def fix_plan_data_areas():
    """Add area field to all shops in plan-data.json"""
    
    # Backup first
    backup_file = f'plan-data.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    shutil.copy('plan-data.json', backup_file)
    print(f"✅ Created backup: {backup_file}")
    
    # Load plan-data.json
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    # Create area mapping (areaId -> area name)
    area_map = {area['id']: area['name'] for area in plan_data.get('areas', [])}
    print(f"\n📍 Found {len(area_map)} areas in plan-data.json")
    
    # Fix shops
    shops = plan_data.get('shops', [])
    print(f"🏪 Processing {len(shops)} shops...")
    
    fixed_count = 0
    for shop in shops:
        area_id = shop.get('areaId')
        if area_id and area_id in area_map:
            # Add or update the area field
            area_name = area_map[area_id]
            if 'area' not in shop or shop['area'] != area_name:
                shop['area'] = area_name
                fixed_count += 1
                print(f"  ✓ Fixed '{shop.get('name', 'Unknown')}': area = '{area_name}'")
        elif area_id:
            print(f"  ⚠️  Warning: Shop '{shop.get('name', 'Unknown')}' has unknown areaId: {area_id}")
        else:
            print(f"  ⚠️  Warning: Shop '{shop.get('name', 'Unknown')}' has no areaId")
    
    # Save updated plan-data.json
    with open('plan-data.json', 'w', encoding='utf-8') as f:
        json.dump(plan_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Fixed {fixed_count} shops")
    print(f"✅ Saved updated plan-data.json")
    
    # Verify
    print("\n🔍 Verification:")
    shops_with_area = sum(1 for shop in shops if 'area' in shop and shop['area'])
    print(f"  Shops with area field: {shops_with_area}/{len(shops)}")
    
    return fixed_count

if __name__ == '__main__':
    print("="*60)
    print("Fix plan-data.json - Add missing area fields")
    print("="*60)
    fixed = fix_plan_data_areas()
    print("\n" + "="*60)
    print(f"✅ DONE! Fixed {fixed} shops")
    print("="*60)
