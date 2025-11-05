#!/usr/bin/env python3
"""
Script to link all shops to their respective areas in shops_details.json
based on the area information from plan-data.json inspectionData
"""

import json
import sys

def load_json_file(filename):
    """Load JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        sys.exit(1)

def save_json_file(filename, data):
    """Save JSON file with proper formatting"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Successfully saved {filename}")
    except Exception as e:
        print(f"Error saving {filename}: {e}")
        sys.exit(1)

def link_shops_to_areas():
    """Main function to link shops to areas"""
    
    # Load data files
    print("Loading data files...")
    plan_data = load_json_file('plan-data.json')
    shops_details = load_json_file('shops_details.json')
    
    # Build area mapping: area name -> area id
    area_name_to_id = {}
    if 'areas' in plan_data:
        for area in plan_data['areas']:
            area_name_to_id[area['name']] = area['id']
    
    print(f"Found {len(area_name_to_id)} areas in plan-data.json")
    
    # Build shop to area mapping from inspectionData
    shop_to_area = {}
    if 'inspectionData' in plan_data:
        for inspection in plan_data['inspectionData']:
            area_name = inspection.get('area')
            shops = inspection.get('shops', [])
            
            for shop_name in shops:
                # Store area name for this shop
                if area_name:
                    shop_to_area[shop_name] = area_name
    
    print(f"Found {len(shop_to_area)} shop-to-area mappings in inspectionData")
    
    # Update shops_details.json
    updated_count = 0
    already_linked_count = 0
    not_found_count = 0
    
    for shop_name, shop_info in shops_details.items():
        # Skip invalid entries (like "0", "1", "2")
        if shop_name in ["0", "1", "2"]:
            continue
            
        current_area_id = shop_info.get('areaId')
        
        # If shop already has areaId, skip it
        if current_area_id:
            already_linked_count += 1
            continue
        
        # Try to find area for this shop
        if shop_name in shop_to_area:
            area_name = shop_to_area[shop_name]
            area_id = area_name_to_id.get(area_name)
            
            if area_id:
                # Update shop with area information
                shops_details[shop_name]['area'] = area_name
                shops_details[shop_name]['areaId'] = area_id
                updated_count += 1
                print(f"Linked '{shop_name}' to area '{area_name}' (ID: {area_id})")
            else:
                print(f"Warning: Area '{area_name}' not found in areas list for shop '{shop_name}'")
                not_found_count += 1
        else:
            # Check if shop has address that might indicate area
            address = shop_info.get('address', '')
            if address:
                # Try to match address to area name
                for area_name, area_id in area_name_to_id.items():
                    if area_name in address:
                        shops_details[shop_name]['area'] = area_name
                        shops_details[shop_name]['areaId'] = area_id
                        updated_count += 1
                        print(f"Linked '{shop_name}' to area '{area_name}' based on address")
                        break
                else:
                    not_found_count += 1
                    print(f"Warning: Could not determine area for shop '{shop_name}'")
            else:
                not_found_count += 1
    
    # Save updated shops_details.json
    print("\nSummary:")
    print(f"- Already linked: {already_linked_count}")
    print(f"- Newly linked: {updated_count}")
    print(f"- Could not link: {not_found_count}")
    print(f"- Total shops: {len(shops_details)}")
    
    if updated_count > 0:
        save_json_file('shops_details.json', shops_details)
        print(f"\n✅ Successfully linked {updated_count} shops to their areas")
    else:
        print("\n⚠️ No shops needed to be updated")

if __name__ == '__main__':
    link_shops_to_areas()
