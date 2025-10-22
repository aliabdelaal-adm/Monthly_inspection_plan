#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix missing shops issue:
1. Load all shops from shops_details.json
2. Merge them into plan-data.json
3. Identify and categorize mobile salons
4. Ensure "صالون متنقل" area exists and contains all mobile salons
"""

import json
import uuid
import time

def generate_shop_id():
    """Generate unique shop ID"""
    return f"shop_{int(time.time() * 1000)}"

def generate_area_id():
    """Generate unique area ID"""
    return f"area_{int(time.time() * 1000)}"

def is_mobile_salon(shop_name):
    """Check if a shop is a mobile salon"""
    name_lower = shop_name.lower()
    mobile_keywords = ['متنقل', 'متحرك', 'موبايل', 'mobile']
    salon_keywords = ['صالون', 'salon', 'grooming', 'spa']
    
    # Check if it's explicitly mobile
    if any(keyword in name_lower for keyword in mobile_keywords):
        return True
    
    # Some salons might be mobile without explicit mention
    # We'll be conservative and only mark those with explicit keywords
    return False

def main():
    # Load plan-data.json
    print("Loading plan-data.json...")
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    # Load shops_details.json
    print("Loading shops_details.json...")
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    print(f"Total shops in shops_details.json: {len(shops_details)}")
    print(f"Current shops in plan-data.json: {len(plan_data.get('shops', []))}")
    print(f"Current areas in plan-data.json: {len(plan_data.get('areas', []))}")
    
    # Ensure areas and shops arrays exist
    if 'areas' not in plan_data:
        plan_data['areas'] = []
    if 'shops' not in plan_data:
        plan_data['shops'] = []
    
    # Find or create "صالون متنقل" area
    mobile_salon_area = None
    for area in plan_data['areas']:
        if 'متنقل' in area['name']:
            mobile_salon_area = area
            break
    
    if not mobile_salon_area:
        print("Creating 'صالون متنقل' area...")
        mobile_salon_area = {
            'id': generate_area_id(),
            'name': 'صالون متنقل'
        }
        plan_data['areas'].append(mobile_salon_area)
    else:
        print(f"Found existing mobile salon area: {mobile_salon_area['name']}")
    
    # Create a map of existing shops by name
    existing_shops = {shop['name']: shop for shop in plan_data['shops']}
    
    # Create a map of areas by name for quick lookup
    area_map = {area['name']: area for area in plan_data['areas']}
    
    # Track statistics
    added_shops = 0
    updated_shops = 0
    mobile_salons_found = []
    
    # Process each shop from shops_details.json
    for shop_name, shop_info in shops_details.items():
        # Use Arabic name if available, otherwise use the key
        shop_display_name = shop_info.get('nameAr', shop_name)
        
        # Determine if this is a mobile salon
        is_mobile = is_mobile_salon(shop_display_name)
        
        # Get or determine the area for this shop
        shop_area_id = None
        
        if is_mobile:
            # Assign to mobile salon area
            shop_area_id = mobile_salon_area['id']
            mobile_salons_found.append(shop_display_name)
        else:
            # Try to determine area from address or existing data
            address = shop_info.get('address', '')
            
            # Try to match area from address
            for area_name, area_obj in area_map.items():
                if area_name in address:
                    shop_area_id = area_obj['id']
                    break
            
            # If no area matched and shop has existing entry, keep its area
            if not shop_area_id and shop_display_name in existing_shops:
                shop_area_id = existing_shops[shop_display_name].get('areaId')
            
            # Default to first non-mobile area if still no match
            if not shop_area_id:
                # Find a default area (not mobile salon)
                for area in plan_data['areas']:
                    if 'متنقل' not in area['name']:
                        shop_area_id = area['id']
                        break
        
        # Check if shop already exists
        if shop_display_name in existing_shops:
            # Update existing shop
            existing_shop = existing_shops[shop_display_name]
            
            # Update area if it's a mobile salon
            if is_mobile and existing_shop['areaId'] != mobile_salon_area['id']:
                existing_shop['areaId'] = mobile_salon_area['id']
                updated_shops += 1
                print(f"  ✓ Updated: {shop_display_name} -> صالون متنقل")
        else:
            # Add new shop
            new_shop = {
                'id': generate_shop_id(),
                'name': shop_display_name,
                'areaId': shop_area_id or plan_data['areas'][0]['id'] if plan_data['areas'] else 'unknown'
            }
            plan_data['shops'].append(new_shop)
            added_shops += 1
            
            if is_mobile:
                print(f"  ✓ Added mobile salon: {shop_display_name}")
    
    # Update statistics
    print("\n" + "="*60)
    print("Summary:")
    print(f"  • Total shops now: {len(plan_data['shops'])}")
    print(f"  • New shops added: {added_shops}")
    print(f"  • Shops updated: {updated_shops}")
    print(f"  • Mobile salons identified: {len(mobile_salons_found)}")
    print(f"  • Total areas: {len(plan_data['areas'])}")
    
    print("\nMobile salons:")
    for salon in sorted(mobile_salons_found):
        print(f"  - {salon}")
    
    # Update lastUpdate timestamp
    plan_data['lastUpdate'] = int(time.time() * 1000)
    
    # Save updated plan-data.json
    print("\nSaving updated plan-data.json...")
    with open('plan-data.json', 'w', encoding='utf-8') as f:
        json.dump(plan_data, f, ensure_ascii=False, indent=2)
    
    print("✅ Done! All shops have been merged successfully.")
    
    # Verify the result
    print("\nVerification:")
    print(f"  • Shops in plan-data.json: {len(plan_data['shops'])}")
    print(f"  • Shops in shops_details.json: {len(shops_details)}")
    print(f"  • Mobile salon area has {len([s for s in plan_data['shops'] if s['areaId'] == mobile_salon_area['id']])} shops")

if __name__ == '__main__':
    main()
