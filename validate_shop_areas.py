#!/usr/bin/env python3
"""
Validate that all shops in inspection data exist in master list with correct areas.
"""

import json
from collections import defaultdict

def load_plan_data():
    """Load the plan-data.json file."""
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("="*80)
    print("Shop-Area Validation Report")
    print("="*80)
    
    data = load_plan_data()
    
    # Build master shop lookup
    master_shops = {shop['name']: shop for shop in data.get('shops', [])}
    
    # Collect all shops from inspections
    inspection_shop_areas = defaultdict(set)
    for inspection in data.get('inspectionData', []):
        area = inspection.get('area', 'Unknown')
        for shop in inspection.get('shops', []):
            inspection_shop_areas[shop].add(area)
    
    # Validate
    all_valid = True
    missing_shops = []
    wrong_area_shops = []
    multiple_area_shops = []
    
    for shop_name, inspection_areas in sorted(inspection_shop_areas.items()):
        if shop_name not in master_shops:
            missing_shops.append(shop_name)
            all_valid = False
            continue
        
        master_area = master_shops[shop_name].get('area', 'Unknown')
        
        # Check if shop appears in multiple areas
        if len(inspection_areas) > 1:
            multiple_area_shops.append((shop_name, inspection_areas, master_area))
        
        # Check if master area matches any inspection area
        if master_area not in inspection_areas:
            wrong_area_shops.append((shop_name, master_area, inspection_areas))
            all_valid = False
    
    # Print results
    if all_valid:
        print("\n✅ ALL VALIDATIONS PASSED!")
        print(f"\n  Total shops in master list: {len(master_shops)}")
        print(f"  Total shops in inspections: {len(inspection_shop_areas)}")
        print(f"  All shops have correct area assignments!")
    else:
        print("\n❌ VALIDATION FAILED!")
        
        if missing_shops:
            print(f"\n  Missing shops ({len(missing_shops)}):")
            for shop in missing_shops:
                print(f"    - {shop}")
        
        if wrong_area_shops:
            print(f"\n  Wrong area assignments ({len(wrong_area_shops)}):")
            for shop, master_area, inspection_areas in wrong_area_shops:
                print(f"    - {shop}")
                print(f"      Master area: {master_area}")
                print(f"      Inspection areas: {', '.join(inspection_areas)}")
    
    # Always show shops in multiple areas (informational)
    if multiple_area_shops:
        print(f"\n⚠️  INFO: Shops appearing in multiple areas ({len(multiple_area_shops)}):")
        for shop, areas, master_area in multiple_area_shops:
            print(f"    - {shop}")
            print(f"      Appears in: {', '.join(sorted(areas))}")
            print(f"      Master area: {master_area}")
    
    # Show area distribution
    print("\n" + "="*80)
    print("Area Distribution Summary:")
    print("="*80)
    
    master_area_counts = defaultdict(int)
    for shop in data.get('shops', []):
        master_area_counts[shop['area']] += 1
    
    inspection_area_counts = defaultdict(int)
    for inspection in data.get('inspectionData', []):
        area = inspection.get('area', 'Unknown')
        inspection_area_counts[area] += len(inspection.get('shops', []))
    
    # Print side-by-side comparison
    all_areas = sorted(set(list(master_area_counts.keys()) + list(inspection_area_counts.keys())))
    
    print(f"\n{'Area':<30} {'Master List':<15} {'Inspections':<15} {'Status'}")
    print("-" * 80)
    
    for area in all_areas:
        master_count = master_area_counts.get(area, 0)
        inspection_count = inspection_area_counts.get(area, 0)
        status = "✓" if master_count > 0 else "!"
        print(f"{area:<30} {master_count:<15} {inspection_count:<15} {status}")
    
    print("\n" + "="*80)
    
    return 0 if all_valid else 1

if __name__ == '__main__':
    exit(main())
