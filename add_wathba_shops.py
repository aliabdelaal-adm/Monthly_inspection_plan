#!/usr/bin/env python3
"""
Script to add missing shops from shops_details.json to plan-data.json for الوثبة جنوب area.
"""
import json
import random

def load_json(filename):
    """Load JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filename, data):
    """Save JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    # Load both files
    print("Loading plan-data.json...")
    plan_data = load_json('plan-data.json')
    
    print("Loading shops_details.json...")
    shops_details = load_json('shops_details.json')
    
    # Get the area ID for الوثبة جنوب
    area_name = "الوثبة جنوب"
    area_id = None
    
    if 'areas' in plan_data:
        for area in plan_data['areas']:
            if area['name'] == area_name:
                area_id = area['id']
                break
    
    if not area_id:
        print(f"ERROR: Could not find area '{area_name}' in plan-data.json")
        return
    
    print(f"Found area ID: {area_id}")
    
    # Get existing shop names in plan-data.json
    existing_shop_names = set()
    if 'shops' in plan_data:
        existing_shop_names = {shop['name'] for shop in plan_data['shops']}
    
    print(f"Existing shops in plan-data.json: {len(existing_shop_names)}")
    
    # Get shops from shops_details.json that are in الوثبة جنوب
    wathba_shops_in_details = {
        name: details 
        for name, details in shops_details.items() 
        if details.get('area') == area_name
    }
    
    print(f"Shops in {area_name} in shops_details.json: {len(wathba_shops_in_details)}")
    
    # Find shops that are missing in plan-data.json
    missing_shops = []
    for shop_name in wathba_shops_in_details.keys():
        if shop_name not in existing_shop_names:
            missing_shops.append(shop_name)
    
    print(f"\nMissing shops to add: {len(missing_shops)}")
    
    if not missing_shops:
        print("All shops from shops_details.json are already in plan-data.json!")
        return
    
    # Add missing shops to plan-data.json
    for shop_name in missing_shops:
        # Generate a unique shop ID
        shop_id = f"shop_{random.randint(1700000000000, 1800000000000)}"
        
        new_shop = {
            "id": shop_id,
            "name": shop_name,
            "areaId": area_id,
            "area": area_name
        }
        
        plan_data['shops'].append(new_shop)
        print(f"  + Added: {shop_name}")
    
    # Save updated plan-data.json
    print(f"\nSaving updated plan-data.json...")
    save_json('plan-data.json', plan_data)
    
    # Verify
    wathba_shops_after = [s for s in plan_data['shops'] if s.get('area') == area_name]
    print(f"\n✅ SUCCESS!")
    print(f"Shops in {area_name} after update: {len(wathba_shops_after)}")
    print(f"Total shops in plan-data.json: {len(plan_data['shops'])}")

if __name__ == '__main__':
    main()
