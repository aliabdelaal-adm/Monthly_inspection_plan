#!/usr/bin/env python3
"""
Fix areaId fields for shops to match the canonical areas list.
"""

import json
from datetime import datetime

def load_plan_data():
    """Load the plan-data.json file."""
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_plan_data(data):
    """Save the plan-data.json file with backup."""
    # Create backup
    backup_name = f'plan-data.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    with open(backup_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Backup created: {backup_name}")
    
    # Save updated data
    with open('plan-data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Updated plan-data.json saved")

def main():
    print("="*80)
    print("Fix Shop areaId Fields")
    print("="*80)
    
    # Load data
    data = load_plan_data()
    
    # Build canonical area name to ID mapping
    area_name_to_id = {}
    for area in data.get('areas', []):
        area_name = area.get('name')
        area_id = area.get('id')
        if area_name and area_id:
            area_name_to_id[area_name] = area_id
    
    print(f"\nFound {len(area_name_to_id)} areas in canonical list")
    
    # Update shops with correct areaId
    updated_count = 0
    no_area_id_count = 0
    
    for shop in data.get('shops', []):
        area_name = shop.get('area')
        current_area_id = shop.get('areaId')
        
        if area_name in area_name_to_id:
            correct_area_id = area_name_to_id[area_name]
            
            if current_area_id != correct_area_id:
                print(f"\nUpdating areaId for: {shop['name']}")
                print(f"  Area: {area_name}")
                print(f"  Old areaId: {current_area_id}")
                print(f"  New areaId: {correct_area_id}")
                shop['areaId'] = correct_area_id
                updated_count += 1
        else:
            # Area not in canonical list - need to add it
            print(f"\n⚠️  Area '{area_name}' not found in canonical areas list")
            print(f"   Shop: {shop['name']}")
            if not shop.get('areaId'):
                no_area_id_count += 1
    
    # Print summary
    print("\n" + "="*80)
    print("SUMMARY:")
    print(f"  Shops with updated areaId: {updated_count}")
    print(f"  Shops with no areaId in canonical list: {no_area_id_count}")
    print("="*80)
    
    if updated_count > 0:
        # Save the updated data
        print("\nSaving changes...")
        save_plan_data(data)
        print("\n✅ Done!")
    else:
        print("\nNo changes needed - all areaIds are correct!")

if __name__ == '__main__':
    main()
