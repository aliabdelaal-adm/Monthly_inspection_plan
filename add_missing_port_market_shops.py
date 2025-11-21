#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add missing Port Market (سوق الميناء) shops from shops_details.json to plan-data.json
"""

import json
import sys
import io
import time

# Ensure UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PORT_MARKET_NAME = "سوق الميناء"
PORT_MARKET_AREA_ID = "area_1758839345230"

def generate_shop_id():
    """Generate a unique shop ID using timestamp"""
    return f"shop_{int(time.time() * 1000)}"

def main():
    print("=" * 70)
    print("Adding Missing Port Market Shops to plan-data.json")
    print("=" * 70)
    print()
    
    # Load shops_details.json
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    # Load plan-data.json
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    # Get Port Market shops from both files
    port_market_details = {
        name: data for name, data in shops_details.items() 
        if data.get('area') == PORT_MARKET_NAME
    }
    
    port_market_plan = {
        shop.get('name'): shop for shop in plan_data.get('shops', []) 
        if shop.get('area') == PORT_MARKET_NAME
    }
    
    print(f"Port Market shops in shops_details.json: {len(port_market_details)}")
    print(f"Port Market shops in plan-data.json: {len(port_market_plan)}")
    print()
    
    # Find missing shops
    missing_shops = []
    for name, data in port_market_details.items():
        if name not in port_market_plan:
            missing_shops.append((name, data))
    
    print(f"Missing shops to add: {len(missing_shops)}")
    
    if not missing_shops:
        print("✓ No missing shops found. All shops are already in plan-data.json")
        return
    
    print()
    print("Adding missing shops...")
    print()
    
    # Get all existing shop IDs to avoid duplicates
    existing_ids = {shop['id'] for shop in plan_data.get('shops', [])}
    
    # Add missing shops
    added_count = 0
    for name, data in missing_shops:
        # Generate unique shop ID
        shop_id = generate_shop_id()
        while shop_id in existing_ids:
            time.sleep(0.001)  # Wait a bit to get a different timestamp
            shop_id = generate_shop_id()
        existing_ids.add(shop_id)
        
        # Create shop object matching the plan-data.json structure
        new_shop = {
            'id': shop_id,
            'name': name,
            'englishName': data.get('nameEn', ''),
            'admCode': data.get('admCode', ''),
            'license': data.get('licenseNo', ''),
            'phone': data.get('contact', ''),
            'email': data.get('email', ''),
            'activity': data.get('activity', ''),
            'area': PORT_MARKET_NAME,
            'areaId': PORT_MARKET_AREA_ID,
            'googleMapsUrl': data.get('locationMap', ''),
            'address': data.get('address', '')
        }
        
        # Add to plan-data
        plan_data['shops'].append(new_shop)
        added_count += 1
        
        print(f"  ✓ Added: {name}")
        if data.get('admCode'):
            print(f"    ADM Code: {data.get('admCode')}")
    
    # Save updated plan-data.json
    with open('plan-data.json', 'w', encoding='utf-8') as f:
        json.dump(plan_data, f, ensure_ascii=False, indent=2)
    
    print()
    print("=" * 70)
    print(f"✓ Successfully added {added_count} shops to plan-data.json")
    print(f"✓ Total shops in plan-data.json: {len(plan_data['shops'])}")
    print(f"✓ Total Port Market shops: {len([s for s in plan_data['shops'] if s.get('area') == PORT_MARKET_NAME])}")
    print("=" * 70)

if __name__ == '__main__':
    main()
