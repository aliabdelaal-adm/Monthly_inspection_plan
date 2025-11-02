#!/usr/bin/env python3
"""
Fix shop area assignments based on inspection data.
This script:
1. Identifies the correct area for each shop based on inspection data
2. Updates existing shops with wrong area assignments
3. Adds missing shops to the master list
"""

import json
import os
from datetime import datetime
from collections import defaultdict

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

def extract_shops_from_inspections(data):
    """
    Extract all unique shops and their areas from inspection data.
    Returns a dict mapping shop name to area.
    For shops appearing in multiple areas, uses the most common area.
    """
    shop_areas = defaultdict(list)
    
    for inspection in data.get('inspectionData', []):
        area = inspection.get('area', 'Unknown')
        for shop in inspection.get('shops', []):
            shop_areas[shop].append(area)
    
    # For each shop, determine the correct area
    # Use the most common area assignment
    shop_to_area = {}
    for shop, areas in shop_areas.items():
        # Count area occurrences
        area_counts = defaultdict(int)
        for area in areas:
            area_counts[area] += 1
        # Pick the most common area
        most_common_area = max(area_counts.items(), key=lambda x: x[1])[0]
        shop_to_area[shop] = most_common_area
    
    return shop_to_area

def main():
    print("="*80)
    print("Shop Area Assignment Fix Script")
    print("="*80)
    
    # Load data
    data = load_plan_data()
    
    # Extract correct shop-to-area mappings from inspection data
    print("\nExtracting shop-area mappings from inspection data...")
    shop_to_area = extract_shops_from_inspections(data)
    print(f"Found {len(shop_to_area)} unique shops in inspection data")
    
    # Get current shops
    current_shops = {shop['name']: shop for shop in data.get('shops', [])}
    print(f"Current master list has {len(current_shops)} shops")
    
    # Track changes
    updated_count = 0
    added_count = 0
    unchanged_count = 0
    
    # Update existing shops and add missing ones
    new_shops_list = []
    
    for shop_name, correct_area in sorted(shop_to_area.items()):
        if shop_name in current_shops:
            shop = current_shops[shop_name].copy()
            current_area = shop.get('area', 'Unknown')
            
            if current_area != correct_area:
                print(f"\nUpdating: {shop_name}")
                print(f"  Old area: {current_area}")
                print(f"  New area: {correct_area}")
                shop['area'] = correct_area
                updated_count += 1
            else:
                unchanged_count += 1
            
            new_shops_list.append(shop)
        else:
            # Add missing shop
            print(f"\nAdding missing shop: {shop_name}")
            print(f"  Area: {correct_area}")
            new_shop = {
                'name': shop_name,
                'area': correct_area,
                'location': 'Unknown'
            }
            new_shops_list.append(new_shop)
            added_count += 1
    
    # Sort shops by name
    new_shops_list.sort(key=lambda x: x['name'])
    
    # Update data
    data['shops'] = new_shops_list
    
    # Print summary
    print("\n" + "="*80)
    print("SUMMARY:")
    print(f"  Shops updated with new areas: {updated_count}")
    print(f"  Shops added to master list: {added_count}")
    print(f"  Shops unchanged: {unchanged_count}")
    print(f"  Total shops in master list: {len(new_shops_list)}")
    print("="*80)
    
    # Show area distribution
    print("\nNew area distribution:")
    area_counts = defaultdict(int)
    for shop in new_shops_list:
        area_counts[shop['area']] += 1
    
    for area, count in sorted(area_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {area}: {count} shops")
    
    # Save the updated data
    print("\nSaving changes...")
    save_plan_data(data)
    print("\n✅ Done!")

if __name__ == '__main__':
    main()
