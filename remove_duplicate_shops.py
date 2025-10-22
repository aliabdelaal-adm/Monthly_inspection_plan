#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove duplicate shops from plan-data.json
Keep the first occurrence of each shop name
"""

import json
import time

def main():
    # Load plan-data.json
    print("Loading plan-data.json...")
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    original_count = len(plan_data['shops'])
    print(f"Original shop count: {original_count}")
    
    # Remove duplicates - keep first occurrence
    seen_names = set()
    unique_shops = []
    duplicates_removed = []
    
    for shop in plan_data['shops']:
        if shop['name'] not in seen_names:
            seen_names.add(shop['name'])
            unique_shops.append(shop)
        else:
            duplicates_removed.append(shop['name'])
    
    plan_data['shops'] = unique_shops
    
    # Update lastUpdate timestamp
    plan_data['lastUpdate'] = int(time.time() * 1000)
    
    print(f"\nRemoved {len(duplicates_removed)} duplicate shops:")
    for dup in sorted(set(duplicates_removed)):
        print(f"  - {dup}")
    
    print(f"\nFinal shop count: {len(plan_data['shops'])}")
    
    # Save updated plan-data.json
    print("\nSaving updated plan-data.json...")
    with open('plan-data.json', 'w', encoding='utf-8') as f:
        json.dump(plan_data, f, ensure_ascii=False, indent=2)
    
    print("✅ Done! Duplicates removed successfully.")

if __name__ == '__main__':
    main()
